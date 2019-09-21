import json
import logging
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

import websocket
from threading import Thread
import time
import sys

from gardena.location import Location

import pprint


class Client:
    def __init__(self, smart_system=None, level=logging.WARN):
        self.smart_system = smart_system
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)
        self.live = False

    def on_message(self, message):
        self.smart_system.on_message(message)

    def on_error(self, error):
        self.logger.error(f"error : {error}")

    def is_connected(self):
        return self.live

    def on_close(self):
        self.live = False
        self.logger.info("Connection close to gardena API")
        sys.exit(0)

    def on_open(self):
        self.logger.info("Connected to Gardena API")

        self.live = True

        def run(*args):
            while self.live:
                time.sleep(1)

        Thread(target=run).start()


class SmartSystem:
    """Base class to communicate with gardena and handle network calls"""

    def __init__(self, email=None, password=None, client_id=None, level=logging.INFO):
        """Constructor, create instance of gateway"""
        if email is None or password is None or client_id is None:
            raise ValueError(
                "Arguments 'email', 'passwords' and 'client_id' are required"
            )
        logging.basicConfig(level=level)
        self.AUTHENTICATION_HOST = "https://api.authentication.husqvarnagroup.dev"
        self.SMART_HOST = "https://api.smart.gardena.dev"
        self.email = email
        self.password = password
        self.client_id = client_id
        self.locations = {}
        self.devices_locations = {}
        self.level = level
        self.client = None
        self.oauth_session = OAuth2Session(
            client=LegacyApplicationClient(client_id=self.client_id)
        )
        self.supported_services = [
            "COMMON",
            "VALVE",
            "VALVE_SET",
            "SENSOR",
            "MOWER",
            "POWER_SOCKET",
        ]
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)
        self.location_message_arrived = False
        self.awaited_number_of_devices = 0

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
        self.token = self.oauth_session.fetch_token(
            token_url=url,
            username=self.email,
            password=self.password,
            client_id=self.client_id,
        )

    def logout(self):
        self.oauth_session.delete(
            f'{self.AUTHENTICATION_HOST}/v1/token/{self.token["refresh_token"]}',
            headers={"X-Api-Key": self.client_id},
        )
        self.oauth_session.delete(
            f'{self.AUTHENTICATION_HOST}/v1/token/{self.token["access_token"]}',
            headers={"X-Api-Key": self.client_id},
        )

    def call_smart_system_service(self, service_id, data):
        args = {"data": data}
        r = self.oauth_session.put(
            f"{self.SMART_HOST}/command/{service_id}",
            headers=self.create_header(True),
            data=json.dumps(args, ensure_ascii=False),
        )
        if r.status_code != 202:
            response = r.json()
            raise Exception(
                f"{r.status_code} : {response['errors'][0]['title']} - {response['errors'][0]['detail']}"
            )

    def start_ws(self):
        url = f"{self.SMART_HOST}/v1/locations"
        response = self.oauth_session.get(url, headers=self.create_header())
        response.raise_for_status()
        response_data = json.loads(response.content.decode("utf-8"))
        if len(response_data["data"]) < 1:
            self.logger.error("No location found. Exiting ...")
            sys.exit(1)
        location = response_data["data"][0]
        args = {
            "data": {
                "type": "WEBSOCKET",
                "attributes": {"locationId": location["id"]},
                "id": "does-not-matter",
            }
        }
        r = self.oauth_session.post(
            f"{self.SMART_HOST}/v1/websocket",
            headers=self.create_header(True),
            data=json.dumps(args, ensure_ascii=False),
        )
        r.raise_for_status()
        response = r.json()
        ws_url = response["data"]["attributes"]["url"]
        self.client = Client(self, level=self.level)
        ws = websocket.WebSocketApp(
            ws_url,
            on_message=self.client.on_message,
            on_error=self.client.on_error,
            on_close=self.client.on_close,
        )
        ws.on_open = self.client.on_open
        ws.run_forever(ping_interval=150, ping_timeout=1)

    def wait_for_ws_start(self):
        import time

        # Wait for locations
        while not self.location_message_arrived:
            time.sleep(1)
        while len(self.get_all_devices_of_type("ALL")) < self.awaited_number_of_devices:
            time.sleep(1)

    def on_message(self, message):
        self.logger.debug("------- Beginning of message ---------")
        self.logger.debug(message)
        data = json.loads(message)
        self.logger.info(f'Received {data["type"]} message')
        if logging.DEBUG >= self.logger.level:
            pprint.pprint(data)
        if data["type"] == "LOCATION":
            self.logger.debug(">>>>>>>>>>>>> Found LOCATION")
            self.treat_location(data)
        elif data["type"] == "DEVICE":
            self.logger.debug(">>>>>>>>>>>>> Found DEVICE")
            self.treat_device(data)
        elif data["type"] in self.supported_services:
            self.treat_service(data)
        else:
            self.logger.debug(">>>>>>>>>>>>> Unkonwn Message")
        self.logger.debug("------- End of message ---------")

    def treat_location(self, location):
        if location["id"] not in self.locations:
            self.locations[location["id"]] = Location(self)
        self.locations[location["id"]].update_data(location)
        self.awaited_number_of_devices += len(
            location["relationships"]["devices"]["data"]
        )
        self.location_message_arrived = True

    def treat_device(self, device):
        location_id = device["relationships"]["location"]["data"]["id"]
        if location_id in self.locations:
            self.locations[location_id].update_device(device)
        self.devices_locations[device["id"]] = location_id

    def treat_service(self, service):
        device_id = service["relationships"]["device"]["data"]["id"]
        if device_id in self.devices_locations:
            self.locations[self.devices_locations[device_id]].devices[
                device_id
            ].update_service(service)

    def get_all_devices_of_type(self, device_type):
        devices = {}
        for location in self.locations:
            for device in location.devices:
                if device["type"] == device_type or device_type == "ALL":
                    devices[device.data["id"]] = device
        return devices
