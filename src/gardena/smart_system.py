import requests
import json
import logging

from gardena.location import Location


class SmartSystem:
    """Base class to communicate with gardena and handle network calls"""

    def __init__(self, email=None, password=None, level=logging.WARN):
        """Constructor, create instance of gateway"""
        if email is None or password is None:
            raise ValueError("Arguments 'email' and 'passwords' are required")
        logging.basicConfig(level=level)
        self.email = email
        self.password = password
        self.locations = {}
        self.token = None
        self.refresh_token = None
        self.user_id = None
        self.request_session = requests.session()

    def create_header(self):
        headers = {"Content-Type": "application/json"}
        if self.token is not None:
            headers["X-Session"] = self.token
        return headers

    def authenticate(self):
        """
        Authenticate and get tokens.
        This function needs to be called first.
        """
        url = "https://smart.gardena.com/sg-1/sessions"
        credentials = {"sessions": {"email": self.email, "password": self.password}}
        response = self.request_session.post(
            url,
            headers=self.create_header(),
            data=json.dumps(credentials, ensure_ascii=False),
        )
        response.raise_for_status()
        response_data = json.loads(response.content.decode("utf-8"))
        if (
            "sessions" not in response_data
            or "token" not in response_data["sessions"]
            or "user_id" not in response_data["sessions"]
        ):
            raise RuntimeError("Could not authenticate to gateway")
        self.token = response_data["sessions"]["token"]
        self.user_id = response_data["sessions"]["user_id"]

    def get_session(self):
        return self.request_session

    def pretty_print_POST(self, req):
        """
        At this point it is completely built and ready
        to be fired; it is "prepared".

        However pay attention at the formatting used in
        this function because it is programmed to be pretty
        printed and may differ from the actual request.
        """
        logging.debug(
            "{}\n{}\n{}\n\n{}".format(
                "-----------START-----------",
                req.method + " " + req.url,
                "\n".join("{}: {}".format(k, v) for k, v in req.headers.items()),
                req.body,
            )
        )

    def call_smart_system(self, url=None, params=None, request_type="GET", data={}):
        req = requests.Request(
            request_type,
            url,
            headers=self.create_header(),
            params=params,
            data=json.dumps(data, ensure_ascii=False),
        )
        prepared = req.prepare()
        self.pretty_print_POST(prepared)
        response = self.request_session.send(prepared)
        response.raise_for_status()
        return response

    def update_locations(self):
        """Update locations (gardens, ..) """
        url = "https://smart.gardena.com/sg-1/locations/"
        params = (("user_id", self.user_id),)
        response = self.request_session.get(
            url, headers=self.create_header(), params=params
        )
        response.raise_for_status()
        response_data = json.loads(response.content.decode("utf-8"))
        for location in response_data["locations"]:
            if location["id"] not in self.locations:
                self.locations[location["id"]] = Location(smart_system=self)
            self.locations[location["id"]].update_information(location)

    def update_all_devices(self):
        for location in self.locations.values():
            location.update_devices()

    def get_all_devices_from_type(self, device_type):
        devices = {}
        for location in self.locations.values():
            for device in getattr(location, device_type).values():
                devices[device.id] = device
        return devices

    def get_all_gateways(self):
        return self.get_all_devices_from_type("gateways")

    def get_all_mowers(self):
        return self.get_all_devices_from_type("mowers")

    def get_all_sensors(self):
        return self.get_all_devices_from_type("sensors")

    def get_all_water_controls(self):
        return self.get_all_devices_from_type("water_controls")

    def get_all_powers(self):
        return self.get_all_devices_from_type("powers")
