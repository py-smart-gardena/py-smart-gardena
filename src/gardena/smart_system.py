import requests
import json

from gardena.location import Location


class SmartSystem:
    """Base class to communicate with gardena and handle network calls"""

    debug = False
    email = None
    password = None
    token = None
    refresh_token = None
    user_id = None
    locations = {}
    request_session = requests.session()

    def __init__(self, email=None, password=None, debug=False):
        """Constructor, create instance of gateway"""
        if email is None or password is None:
            raise ValueError("Arguments 'email' and 'passwords' are required")
        self.debug = debug
        self.email = email
        self.password = password

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

    def get_session(self):
        return self.request_session
