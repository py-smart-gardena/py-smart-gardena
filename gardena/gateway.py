import requests


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
        self.etag = None
        self.request_session = requests.session()

    def authenticate(self):
        """Authenticate and get tokens """
        credentials = {
            "email": self.email,
            "password": self.password
        }

    def __create_header(self):
        headers = {
            'Content-Type': 'application/json',
        }
        if self.token is not None:
            headers['X-Session'] = self.token
        if self.etag is not None:
            headers['If-None-Match'] = ETag
        return headers
