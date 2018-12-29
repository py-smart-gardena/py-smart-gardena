import requests


class Gateway:
    """Class to communicate with smart gateway and handle network calls"""

    def __init__(self, email=None, password=None, debug=False):
        if email is None or password is None:
            raise ValueError("Arguments 'email' and 'passwords' are required")
        self.debug = debug
        self.email = email
        self.password = password
        self.request_session = requests.session()