import requests
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
    def __init__(self, smart_system=None):
        self.smart_system = smart_system

    def on_message(self, message):
        self.smart_system.on_message(message)

    def on_error(self, error):
        print("error", error)
        pprint.pprint(error)

    def on_close(self):
        self.live = False
        print("### closed ###")
        sys.exit(0)

    def on_open(self):
        print("### connected ###")

        self.live = True

        def run(*args):
            while self.live:
                time.sleep(1)

        Thread(target=run).start()


class SmartSystem:
    """Base class to communicate with gardena and handle network calls"""

    def __init__(self, email=None, password=None, client_id=None, level=logging.WARN):
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
        self.oauth_session = OAuth2Session(
            client=LegacyApplicationClient(client_id=self.client_id)
        )
        self.supported_services = ["COMMON", "VALVE"]

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

    def call_smart_system(self, url=None, params=None, request_type="GET", data=None):
        req = requests.Request(
            request_type,
            url,
            headers=self.create_header(),
            params=params,
            data=json.dumps(data, ensure_ascii=False),
        )
        prepared = req.prepare()
        self.pretty_print(prepared)
        response = self.oauth_session.send(prepared)
        response.raise_for_status()
        return response

    def start_ws(self):
        url = f"{self.SMART_HOST}/v1/locations"
        response = self.oauth_session.get(url, headers=self.create_header())
        response.raise_for_status()
        response_data = json.loads(response.content.decode("utf-8"))
        if len(response_data["data"]) < 1:
            print("No location found. Exiting ...")
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
        client = Client(self)
        ws = websocket.WebSocketApp(
            ws_url,
            on_message=client.on_message,
            on_error=client.on_error,
            on_close=client.on_close,
        )
        ws.on_open = client.on_open
        ws.run_forever(ping_interval=150, ping_timeout=1)

    def on_message(self, message):
        print("------- Beginning of message ---------")
        data = json.loads(message)
        pprint.pprint(data)
        if data["type"] == "LOCATION":
            print(">>>>>>>>>>>>> Found LOCATION")
            self.treat_location(data)
        elif data["type"] == "DEVICE":
            print(">>>>>>>>>>>>> Found DEVICE")
            self.treat_device(data)
        elif data["type"] in self.supported_services:
            self.treat_service(data)
        else:
            print(">>>>>>>>>>>>> Unkonwn Message")
        print("------- End of message ---------")

    def treat_location(self, location):
        if location["id"] not in self.locations:
            self.locations[location["id"]] = Location()
        self.locations[location["id"]].update_data(location)

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
            print(self.locations[self.devices_locations[device_id]].devices[device_id])

    # def update_all_devices(self):
    #     for location in self.locations.values():
    #         location.update_devices()
    #
    # def get_all_devices_from_type(self, device_type):
    #     devices = {}
    #     for location in self.locations.values():
    #         for device in getattr(location, device_type).values():
    #             devices[device.id] = device
    #     return devices
    #
    # def get_all_gateways(self):
    #     return self.get_all_devices_from_type("gateways")
    #
    # def get_all_mowers(self):
    #     return self.get_all_devices_from_type("mowers")
    #
    # def get_all_sensors(self):
    #     return self.get_all_devices_from_type("sensors")
    #
    # def get_all_water_controls(self):
    #     return self.get_all_devices_from_type("water_controls")
    #
    # def get_all_powers(self):
    #     return self.get_all_devices_from_type("powers")
