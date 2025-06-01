import asyncio
import json
import logging
import ssl
import functools

import backoff
from httpx import HTTPStatusError
from websockets.asyncio.client import connect
from websockets.exceptions import ConnectionClosed
from authlib.integrations.httpx_client import AsyncOAuth2Client
from json.decoder import JSONDecodeError
from authlib.integrations.base_client.errors import (
    OAuthError,
    InvalidTokenError
)
from gardena.devices.device_factory import DeviceFactory
from gardena.exceptions.authentication_exception import AuthenticationException
from gardena.location import Location
from gardena.token_manager import TokenManager

MAX_BACKOFF_VALUE = 900

@functools.lru_cache(maxsize=1)
def get_ssl_context():
    """Create and cache SSL context outside of event loop."""
    context = ssl.create_default_context()
    return context

class SmartSystem:
    """Base class to communicate with gardena and handle network calls"""

    def __init__(self, client_id=None, client_secret=None, level=logging.INFO, ssl_context=None):
        """Constructor, create instance of gateway"""
        if client_id is None or client_secret is None:
            raise ValueError(
                "Arguments 'email', 'client_secret' and 'client_id' are required"
            )
        logging.basicConfig(
            level=level,
            format="%(asctime)s %(levelname)-8s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)
        self.AUTHENTICATION_HOST = "https://api.authentication.husqvarnagroup.dev"
        self.SMART_HOST = "https://api.smart.gardena.dev"
        self.client_id = client_id
        self.client_secret = client_secret
        self.locations = {}
        self.level = level
        self.client: AsyncOAuth2Client = None
        self.token_manager = TokenManager(logger=self.logger)
        self.ws = None
        self.is_ws_connected = False
        self.ws_status_callback = None
        self.should_stop = False
        self.supported_services = [
            "COMMON",
            "VALVE",
            "VALVE_SET",
            "SENSOR",
            "MOWER",
            "POWER_SOCKET",
            "DEVICE",
        ]
        # Use provided SSL context or get cached one
        self._ssl_context = ssl_context or get_ssl_context()

    def create_header(self, include_json=False):
        headers = {"Authorization-Provider": "husqvarna", "X-Api-Key": self.client_id}
        if include_json:
            headers["Content-Type"] = "application/vnd.api+json"
        return headers

    async def authenticate(self):
        """
        Authenticate and get tokens.
        This function needs to be called first.
        """
        url = self.AUTHENTICATION_HOST + "/v1/oauth2/token"
        extra = {"client_id": self.client_id}
        self.client = AsyncOAuth2Client(
            self.client_id,
            self.client_secret,
            update_token=self.token_saver,
            grant_type="client_credentials",
            token_endpoint=url,
            verify=self._ssl_context  # Pass SSL context to httpx client
        )
        self.token_manager.load_from_oauth2_token(await self.client.fetch_token(
            url, grant_type="client_credentials"
        ))

    async def quit(self):
        self.should_stop = True
        if self.client:
            if self.token_manager.access_token:
                await self.client.delete(
                    f"{self.AUTHENTICATION_HOST}/v1/token/{self.token_manager.access_token}",
                    headers={"X-Api-Key": self.client_id},
                )

    async def token_saver(self, token, refresh_token=None, access_token=None):
        self.token_manager.load_from_oauth2_token(token)

    async def call_smart_system_service(self, service_id, data):
        args = {"data": data}
        headers = self.create_header(True)

        r = await self.client.put(
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
                if "errors" in r:
                    msg = "{r['errors'][0]['title']} - {r['errors'][0]['detail']}"
                elif "message" in r:
                    msg = f"{r['message']}"

                    if response.status_code == 403:
                        msg = f"{msg} (hint: did you 'Connect an API' in your Application?)"
                else:
                    msg = f"{r}"

            except JSONDecodeError:
                msg = response.content

            self.logger.error(f"{response.status_code} : {msg}")

            if response.status_code == 401:
                raise AuthenticationException(msg)
            response.raise_for_status()
            return True
        return False

    @backoff.on_exception(backoff.expo,
                          HTTPStatusError,
                          max_value=MAX_BACKOFF_VALUE,
                          logger=logging.getLogger(__name__))
    async def __call_smart_system_get(self, url):
        response = await self.client.get(url, headers=self.create_header())
        if self.__response_has_errors(response):
            return None
        return json.loads(response.content.decode("utf-8"))

    async def update_locations(self):
        response_data = await self.__call_smart_system_get(
            f"{self.SMART_HOST}/v1/locations"
        )
        if response_data is not None:
            if "data" not in response_data or len(response_data["data"]) < 1:
                self.logger.error("No locations found....")
            else:
                self.locations = {}
                for location in response_data["data"]:
                    new_location = Location(self, location)
                    new_location.update_location_data(location)
                    self.locations[new_location.id] = new_location

    async def update_devices(self, location):
        response_data = await self.__call_smart_system_get(
            f"{self.SMART_HOST}/v1/locations/{location.id}"
        )
        if response_data is not None:
            #  TODO : test if key exists
            if len(response_data["data"]["relationships"]["devices"]["data"]) < 1:
                self.logger.error("No device found....")
            else:
                devices_smart_system = {}
                self.logger.debug(f"Received devices in  message")
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

    async def start_ws(self, location):
        while not self.should_stop:
            self.logger.debug("Trying to connect to gardena API....")
            try:
                ws_url = await self.__get_ws_url(location)
                await self.__launch_websocket_loop(ws_url)
            except (ConnectionClosed, InvalidTokenError, OAuthError) as error:
                self.logger.debug(error, exc_info=True)
                continue
            finally:
                self.set_ws_status(False)
                if not self.should_stop:
                    self.logger.debug("Sleeping 10 seconds ..")
                    await asyncio.sleep(10)

    @backoff.on_exception(backoff.expo,
                          HTTPStatusError,
                          max_value=MAX_BACKOFF_VALUE,
                          logger=logging.getLogger(__name__))
    async def __get_ws_url(self, location):
        args = {
            "data": {
                "type": "WEBSOCKET",
                "attributes": {"locationId": location.id},
                "id": "does-not-matter",
            }
        }
        self.logger.debug("Trying to get Websocket url")
        r = await self.client.post(
            f"{self.SMART_HOST}/v1/websocket",
            headers=self.create_header(True),
            data=json.dumps(args, ensure_ascii=False),
        )
        self.logger.debug("Websocket url: got response")
        r.raise_for_status()
        response = r.json()
        ws_url = response["data"]["attributes"]["url"]
        self.logger.debug("Websocket url retrieved successfully")
        return ws_url

    async def __launch_websocket_loop(self, url):
        self.logger.debug("Connecting to websocket ..")
        websocket = await connect(url, ping_interval=150, ssl=self._ssl_context)
        self.set_ws_status(True)
        self.logger.debug("Connected !")
        while not self.should_stop:
            self.logger.debug("Waiting for message ..")
            message = await websocket.recv()
            self.logger.debug("Message received ..")
            self.on_message(message)

    def on_message(self, message):
        data = json.loads(message)
        self.logger.debug(f'Received {data["type"]} message')
        self.logger.debug("------- Beginning of message ---------")
        self.logger.debug(message)
        if data["type"] == "LOCATION":
            self.logger.debug(">>>>>>>>>>>>> Found LOCATION")
            self.parse_location(data)
        elif data["type"] in self.supported_services:
            self.logger.debug(">>>>>>>>>>>>> Found DEVICE")
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

    def set_ws_status(self, status):
        self.is_ws_connected = status
        if self.ws_status_callback:
            self.ws_status_callback(status)
