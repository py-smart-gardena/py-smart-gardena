from gardena.gateway import Gateway
import pytest
import unittest
from unittest import mock


# This method will be used by the mock to replace requests.get
def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'https://smart.gardena.com/sg-1/sessions':
        return MockResponse({
            "sessions": {
                "token": "7867e26c-05eb-4a60-bf30-7c3a1b4480aa",
                "user_id": "196ab891-a521-872c-ab1d-1685d1e77afc"
            }
        }, 200)
    elif args[0] == 'https://smart.gardena.com/sg-1/locations/':
        return MockResponse({"key2": "value2"}, 200)
    elif args[0] == 'https://smart.gardena.com/sg-1/devices':
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse(None, 404)


class GatewayTestCase(unittest.TestCase):
    def test_init(self):
        gw = Gateway(email='test@test.com', password='password')
        assert gw.email == 'test@test.com'
        assert gw.password == 'password'

    def test_init_exception_without_email(self):
        with pytest.raises(ValueError):
            gw = Gateway(password='password')

    def test_init_exception_without_password(self):
        with pytest.raises(ValueError):
            gw = Gateway(email='test@test.com')

    @mock.patch('gardena.gateway.requests.post',
                side_effect=mocked_requests_post)
    def test_authenticate(self, mock_post):
        gw = Gateway(email='test@test.com', password='password')
        gw.authenticate()
        assert gw.token == "7867e26c-05eb-4a60-bf30-7c3a1b4480aa"
        assert gw.user_id == "196ab891-a521-872c-ab1d-1685d1e77afc"
