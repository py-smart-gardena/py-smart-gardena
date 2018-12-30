import requests
import json


class Gateway:
    """Class to communicate with smart gateway and handle network calls"""

    def __init__(self, email=None, password=None, debug=False):
        """Constructor, create instance of gateway"""
        if email is None or password is None:
            raise ValueError("Arguments 'email' and 'passwords' are required")
        self.debug = debug
        self.email = email
        self.password = password
        self.token = None
        self.refresh_token = None
        self.user_id = None
        self.etag = None
        self.locations = None
        self.request_session = requests.session()

    def authenticate(self):
        """
        Authenticate and get tokens.
        This function needs to be called first.
        """
        url = 'https://smart.gardena.com/sg-1/sessions'
        credentials = {
            "email": self.email,
            "password": self.password
        }
        response = self.request_session.post(
            url,
            headers=self.__create_header(),
            data=json.dumps(credentials, ensure_ascii=False)
        )
        response.raise_for_status()
        response_data = json.loads(response.content.decode('utf-8'))
        self.token = response_data['sessions']['token']
        self.refresh_token = response_data['sessions']['refresh_token']
        self.user_id = response_data['sessions']['user_id']

    def update_locations(self):
        """Update locations (gardens, ..) """
        url = "https://smart.gardena.com/sg-1/locations/"
        params = (
            ('user_id', self.user_id),
        )
        response = self.request_session.get(
            url,
            headers=self.__create_header(),
            params=params
        )
        response_data = json.loads(response.content.decode('utf-8'))
        self.locations = [(i['id'], i['name']) for i in
                          response_data['locations']]

    def __create_header(self):
        headers = {
            'Content-Type': 'application/json',
        }
        if self.token is not None:
            headers['X-Session'] = self.token
        if self.etag is not None:
            headers['If-None-Match'] = ETag
        return headers
