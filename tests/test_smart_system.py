import pytest
import unittest
import requests
import requests_mock
from requests import HTTPError
from gardena.smart_system import SmartSystem
from tests.gardena_api_mock import init_mock, init_failed_mock


class SmartSystemTestCase(unittest.TestCase):
    def test_init(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        assert smart_system.email == "test@test.com"
        assert smart_system.password == "password"

    def test_init_exception_without_email(self):
        with pytest.raises(ValueError):
            SmartSystem(password="password")

    def test_init_exception_without_password(self):
        with pytest.raises(ValueError):
            SmartSystem(email="test@test.com")

    def test_authenticate(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_mock(smart_system)
        smart_system.authenticate()
        assert smart_system.token == "7867e26c-05eb-4a60-bf30-7c3a1b4480aa"
        assert smart_system.user_id == "196ab891-a521-872c-ab1d-1685d1e77afc"

    def test_authenticate_failed(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        adapter = requests_mock.Adapter()
        adapter.register_uri(
            "POST", "https://smart.gardena.com/sg-1/sessions", json={}, status_code=400
        )
        smart_system.request_session.mount("https://smart.gardena.com/", adapter)
        with pytest.raises(HTTPError):
            smart_system.authenticate()

    def test_authenticate_failed_without_session(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        adapter = requests_mock.Adapter()
        adapter.register_uri(
            "POST", "https://smart.gardena.com/sg-1/sessions", json={}, status_code=200
        )
        smart_system.request_session.mount("https://smart.gardena.com/", adapter)
        with pytest.raises(RuntimeError):
            smart_system.authenticate()

    def test_authenticate_failed_without_token(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        adapter = requests_mock.Adapter()
        adapter.register_uri(
            "POST",
            "https://smart.gardena.com/sg-1/sessions",
            json={"sessions": {"user_id": "196ab891-a521-872c-ab1d-1685d1e77afc"}},
            status_code=200,
        )
        smart_system.request_session.mount("https://smart.gardena.com/", adapter)
        with pytest.raises(RuntimeError):
            smart_system.authenticate()

    def test_authenticate_failed_without_user_id(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        adapter = requests_mock.Adapter()
        adapter.register_uri(
            "POST",
            "https://smart.gardena.com/sg-1/sessions",
            json={"sessions": {"token": "7867e26c-05eb-4a60-bf30-7c3a1b4480aa"}},
            status_code=200,
        )
        smart_system.request_session.mount("https://smart.gardena.com/", adapter)
        with pytest.raises(RuntimeError):
            smart_system.authenticate()

    def test_update_locations(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_mock(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        test_location = {
            "id": "1c8b301f-22c8-423d-1b4d-ec25315d1377",
            "name": "My Garden",
            "devices": [
                "75cfc1f8-a20c-51d6-c5ea-1b5ecdde80c1",
                "e3c1b615-7351-25fc-a551-1908254a2b3e",
            ],
        }
        assert len(smart_system.locations) == 1
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].id
            == test_location["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].name
            == test_location["name"]
        )

    def test_update_locations_update(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_mock(smart_system)
        smart_system.authenticate()
        test_location = {
            "id": "1c8b301f-22c8-423d-1b4d-ec25315d1377",
            "name": "My Garden",
            "devices": [
                "75cfc1f8-a20c-51d6-c5ea-1b5ecdde80c1",
                "e3c1b615-7351-25fc-a551-1908254a2b3e",
            ],
            "geo_position": {
                "latitude": 48.8738,
                "longitude": 2.295,
                "address": "Place Charles de Gaulle 75008 Paris, France",
                "city": "Paris",
                "id": "b30e4f46-f96d-4808-ccb8-ecacec57249d",
                "sunrise": "08:46",
                "sunset": "17:09",
                "time_zone": "Europe/Paris",
                "time_zone_offset": 3600000,
            },
        }
        smart_system.update_locations()
        smart_system.update_locations()
        assert len(smart_system.locations) == 1
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].id
            == test_location["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].name
            == test_location["name"]
        )

    def test_update_locations_failed(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_failed_mock(smart_system)
        smart_system.authenticate()
        with pytest.raises(HTTPError):
            smart_system.update_locations()

    def test_get_session(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_mock(smart_system)
        assert isinstance(smart_system.get_session(), requests.sessions.Session)
