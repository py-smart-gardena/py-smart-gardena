import json
import logging
from contextlib import contextmanager
from json.decoder import JSONDecodeError

from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

import websocket
from threading import Thread

from gardena.exceptions.authentication_exception import AuthenticationException
from gardena.location import Location
from gardena.devices.device_factory import DeviceFactory


class Client:
    def __init__(self, smart_system=None, level=logging.WARN, location=None):
        self.smart_system = smart_system
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)
        self.live = False
        self.location = location
        self.should_stop = False

    def on_message(self, ws, message):
        self.smart_system.on_message(message)

    def on_error(self, ws, error):
        self.logger.error(f"error : {error}")
        self.smart_system.set_ws_status(False)

    def is_connected(self):
        return self.live

    def on_close(self, ws, close_status_code, close_msg):
        self.live = False
        self.logger.info("Connection close to gardena API")
        self.smart_system.set_ws_status(False)
        if not self.should_stop:
            self.logger.info("Restarting websocket")
            self.smart_system.start_ws(self.location)

    def on_open(self, ws):
        self.logger.info("Connected to Gardena API")
        self.live = True
        self.smart_system.set_ws_status(True)

        # def run(*args):
        #     while self.live:
        #         time.sleep(1)
        #
        # Thread(target=run).start()


class SmartSystem:
    """Base class to communicate with gardena and handle network calls"""

    def __init__(self, email=None, password=None, client_id=None, level=logging.INFO):
        """Constructor, create instance of gateway"""
        if email is None or password is None or client_id is None:
            raise ValueError(
                "Arguments 'email', 'passwords' and 'client_id' are required"
            )
        logging.basicConfig(
            level=level,
            format='%(asctime)s %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.AUTHENTICATION_HOST = "https://api.authentication.husqvarnagroup.dev"
        self.SMART_HOST = "https://api.smart.gardena.dev"
        self.email = email
        self.password = password
        self.client_id = client_id
        self.locations = {}
        self.level = level
        self.client = None
        self.oauth_session = None
        self.ws = None
        self.is_ws_connected = False
        self.ws_status_callback = None
        self.supported_services = [
            "COMMON",
            "VALVE",
            "VALVE_SET",
            "SENSOR",
            "MOWER",
            "POWER_SOCKET",
            "DEVICE",
        ]
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

    def create_header(self, include_json=False):
        headers = {"Authorization-Provider": "husqvarna", "X-Api-Key": self.client_id}
        if include_json:
            headers["Content-Type"] = "application/vnd.api+json"
        return headers

    def authenticate(self):
        """
        Authenticate and get tokens.
        This function needs to be called first.
        """
        url = self.AUTHENTICATION_HOST + "/v1/oauth2/token"
        extra = {"client_id": self.client_id}
        self.oauth_session = OAuth2Session(
            client=LegacyApplicationClient(client_id=self.client_id),
            auto_refresh_url=url,
            auto_refresh_kwargs=extra,
            token_updater=self.token_saver,
        )
        self.token = self.oauth_session.fetch_token(
            token_url=url,
            username=self.email,
            password=self.password,
            client_id=self.client_id,
        )

    def quit(self):
        if self.client:
            self.client.should_stop = True
        if self.ws:
            self.ws.close()
        if self.oauth_session:
            self.oauth_session.delete(
                f'{self.AUTHENTICATION_HOST}/v1/token/{self.token["refresh_token"]}',
                headers={"X-Api-Key": self.client_id},
            )
            self.oauth_session.delete(
                f'{self.AUTHENTICATION_HOST}/v1/token/{self.token["access_token"]}',
                headers={"X-Api-Key": self.client_id},
            )

    def set_ws_status(self, status):
        self.is_ws_connected = status
        if self.ws_status_callback:
            self.ws_status_callback(status)

    def token_saver(self, token):
        self.token = token

    def call_smart_system_service(self, service_id, data):
        args = {"data": data}
        headers = self.create_header(True)

        r = self.oauth_session.put(
            f"{self.SMART_HOST}/v1/command/{service_id}",
            headers=headers,
            data=json.dumps(args, ensure_ascii=False),
        )
        if r.status_code != 202:
            response = r.json()

            raise Exception(f"{r.status_code} : {response['errors'][0]['title']}")

    def __response_has_errors(self, response):
        if response.status_code not in (200, 202):
            try:
                r = response.json()
                if 'errors' in r:
                    msg = "{r['errors'][0]['title']} - {r['errors'][0]['detail']}"
                elif 'message' in r:
                    msg = f"{r['message']}"

                    if response.status_code == 403:
                        msg = f"{msg} (hint: did you 'Connect an API' in your Application?)"
                else:
                    msg = f"{r}"

            except JSONDecodeError:
                msg = response.content

            self.logger.error(f"{response.status_code} : {msg}")

            if response.status_code in (403, 429):
                raise Exception(msg)
            elif response.status_code == 401:
                raise AuthenticationException(msg)

            return True
        return False

    def __call_smart_system_get(self, url):
        response = self.oauth_session.get(url, headers=self.create_header())
        if self.__response_has_errors(response):
            return None
        return json.loads(response.content.decode("utf-8"))

    @contextmanager
    def __set_retry_on_session(
            self,
            backoff_factor=0.3,
            status_forcelist=(500, 502, 504),
    ):
        try:
            retry = Retry(
                total=None,
                read=None,
                connect=None,
                status=None,
                method_whitelist=False,
                backoff_factor=backoff_factor,
                status_forcelist=status_forcelist,
            )
            adapter = HTTPAdapter(max_retries=retry)
            self.oauth_session.mount('http://', adapter)
            self.oauth_session.mount('https://', adapter)
            yield self.oauth_session
        finally:
            self.oauth_session.mount('http://', HTTPAdapter())
            self.oauth_session.mount('https://', HTTPAdapter())

    def update_locations(self):
        response_data = self.__call_smart_system_get(f"{self.SMART_HOST}/v1/locations")
        if response_data is not None:
            if 'data' not in response_data or len(response_data["data"]) < 1:
                self.logger.error("No locations found....")
            else:
                self.locations = {}
                for location in response_data["data"]:
                    new_location = Location(self, location)
                    new_location.update_location_data(location)
                    self.locations[new_location.id] = new_location

    def update_devices(self, location):
        response_data = self.__call_smart_system_get(
            f"{self.SMART_HOST}/v1/locations/{location.id}"
        )
        if response_data is not None:
            #  TODO : test if key exists
            if len(response_data["data"]["relationships"]["devices"]["data"]) < 1:
                self.logger.error("No device found....")
            else:
                devices_smart_system = {}
                self.logger.debug(f'Received devices in  message')
                self.logger.debug("------- Beginning of message ---------")
                self.logger.debug(response_data["included"])
                for device in response_data["included"]:
                    real_id = device["id"].split(":")[0]
                    if real_id not in devices_smart_system:
                        devices_smart_system[real_id] = {}
                    if device["type"] in self.supported_services:
                        if device["type"] not in devices_smart_system[real_id]:
                            devices_smart_system[real_id][device["type"]] = []
                        devices_smart_system[real_id][device["type"]].append(device)
                for parsed_device in devices_smart_system.values():
                    device_obj = DeviceFactory.build(location, parsed_device)
                    if device_obj is not None:
                        location.add_device(device_obj)

    def start_ws(self, location):
        args = {
            "data": {
                "type": "WEBSOCKET",
                "attributes": {"locationId": location.id},
                "id": "does-not-matter",
            }
        }
        with self.__set_retry_on_session() as session:
            r = session.post(
                f"{self.SMART_HOST}/v1/websocket",
                headers=self.create_header(True),
                data=json.dumps(args, ensure_ascii=False),
            )
            r.raise_for_status()
            response = r.json()
            ws_url = response["data"]["attributes"]["url"]
            if self.client is None:
                self.client = Client(self, level=self.level, location=location)
            if self.level == logging.DEBUG:
                websocket.enableTrace(True)
            self.ws = websocket.WebSocketApp(
                ws_url,
                on_message=self.client.on_message,
                on_error=self.client.on_error,
                on_close=self.client.on_close,
                on_open=self.client.on_open,
            )
            wst = Thread(
                target=self.ws.run_forever, kwargs={"ping_interval": 60, "ping_timeout": 5}
            )
            wst.daemon = True
            wst.start()

    def on_message(self, message):
        data = json.loads(message)
        self.logger.debug(f'Received {data["type"]} message')
        self.logger.debug("------- Beginning of message ---------")
        self.logger.debug(message)
        if data["type"] == "LOCATION":
            self.logger.debug(">>>>>>>>>>>>> Found LOCATION")
            self.parse_location(data)
        elif data["type"] in self.supported_services:
            self.parse_device(data)
        else:
            self.logger.debug(">>>>>>>>>>>>> Unkonwn Message")
        self.logger.debug("------- End of message ---------")

    def parse_location(self, location):
        if location["id"] not in self.locations:
            self.logger.debug(f"Location not found : {location['attributes']['name']}")
        self.locations[location["id"]].update_location_data(location)

    def parse_device(self, device):
        device_id = device["id"].split(":")[0]
        for location in self.locations.values():
            if device_id in location.devices:
                location.devices[device_id].update_data(device)
                break

    def add_ws_status_callback(self, callback):
        self.ws_status_callback = callback