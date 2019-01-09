import pytest
import unittest
import requests
import requests_mock

from requests import HTTPError
from gardena.smart_system import SmartSystem
from tests.gardena_api_return.authentication_return import authentication_return
from tests.mocks.gardena_api_mock import GardenaApiMock, init_failed_mock
from tests.gardena_api_return.locations_return import (
    location_return,
    location_return_two,
)


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
        adapter = requests_mock.Adapter()
        adapter.register_uri(
            "POST",
            "https://smart.gardena.com/sg-1/sessions",
            json=authentication_return,
            status_code=200,
        )
        smart_system.request_session.mount("https://smart.gardena.com/", adapter)
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
        print("Taille test : " + str(len(smart_system.locations)))
        api_mock = GardenaApiMock()
        m_sessions = api_mock.register_sessions()
        m_locations = api_mock.register_locations()
        api_mock.mount(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        assert len(smart_system.locations) == 1
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].id
            == location_return["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].name
            == location_return["name"]
        )
        assert m_sessions.call_count == 1
        assert m_locations.call_count == 1

    def test_call_update_locations_multiple_times(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        api_mock = GardenaApiMock()
        m_sessions = api_mock.register_sessions()
        m_locations = api_mock.register_locations()
        api_mock.mount(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        assert len(smart_system.locations) == 1
        smart_system.update_locations()
        assert len(smart_system.locations) == 1
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].id
            == location_return["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].name
            == location_return["name"]
        )
        assert m_sessions.call_count == 1
        assert m_locations.call_count == 2

    def test_update_locations_with_two_locations(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        api_mock = GardenaApiMock()
        m_sessions = api_mock.register_sessions()
        m_locations = api_mock.register_two_locations()
        api_mock.mount(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        assert len(smart_system.locations) == 2
        smart_system.update_locations()
        assert len(smart_system.locations) == 2
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].id
            == location_return["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].name
            == location_return["name"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1378"].id
            == location_return_two["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1378"].name
            == location_return_two["name"]
        )
        assert m_sessions.call_count == 1
        assert m_locations.call_count == 2

    def test_update_locations_failed(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_failed_mock(smart_system)
        smart_system.authenticate()
        with pytest.raises(HTTPError):
            smart_system.update_locations()

    def test_get_session(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        assert isinstance(smart_system.get_session(), requests.sessions.Session)

    def test_get_all_gateways(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        api_mock = GardenaApiMock()
        api_mock.register_sessions()
        api_mock.register_two_locations()
        m_devices = api_mock.register_devices()
        m_devices_2 = api_mock.register_second_location_devices()
        api_mock.mount(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        smart_system.update_all_devices()
        assert len(smart_system.get_all_gateways()) == 2
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].id
            == location_return["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
            .gateways["75cfc1f8-a20c-51d6-c5ea-1b5ecdde80c1"]
            .name
            == "Gardena Zentrale"
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1378"].id
            == location_return_two["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1378"]
            .gateways["75cfc1f8-a20c-51d6-c5ea-1b5ecdde80c2"]
            .name
            == "Gardena Zentrale 2"
        )
        assert m_devices.call_count == 1
        assert m_devices_2.call_count == 1

    def test_get_all_mowers(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        api_mock = GardenaApiMock()
        api_mock.register_sessions()
        api_mock.register_two_locations()
        m_devices = api_mock.register_devices()
        m_devices_2 = api_mock.register_second_location_devices()
        api_mock.mount(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        smart_system.update_all_devices()
        assert len(smart_system.get_all_mowers()) == 2
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].id
            == location_return["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
            .mowers["e3c1b615-7351-25fc-a551-1908254a2b3e"]
            .name
            == "Rosi"
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1378"].id
            == location_return_two["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1378"]
            .mowers["e3c1b615-7351-25fc-a551-1908254a2b3f"]
            .name
            == "Rosi 2"
        )
        assert m_devices.call_count == 1
        assert m_devices_2.call_count == 1

    def test_get_all_sensors(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        api_mock = GardenaApiMock()
        api_mock.register_sessions()
        api_mock.register_two_locations()
        m_devices = api_mock.register_devices()
        m_devices_2 = api_mock.register_second_location_devices()
        api_mock.mount(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        smart_system.update_all_devices()
        assert len(smart_system.get_all_sensors()) == 2
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].id
            == location_return["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
            .sensors["a130596e-6627-4030-aea5-b6d2f24d0e03"]
            .name
            == "Sensor"
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1378"].id
            == location_return_two["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1378"]
            .sensors["a130596e-6627-4030-aea5-b6d2f24d0e04"]
            .name
            == "Sensor 2"
        )
        assert m_devices.call_count == 1
        assert m_devices_2.call_count == 1

    def test_get_all_water_controls(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        api_mock = GardenaApiMock()
        api_mock.register_sessions()
        api_mock.register_two_locations()
        m_devices = api_mock.register_devices()
        m_devices_2 = api_mock.register_second_location_devices()
        api_mock.mount(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        smart_system.update_all_devices()
        assert len(smart_system.get_all_water_controls()) == 2
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"].id
            == location_return["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
            .water_controls["d6259669-3241-488c-a88e-bcf3a07a58bf"]
            .name
            == "Water Control"
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1378"].id
            == location_return_two["id"]
        )
        assert (
            smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1378"]
            .water_controls["d6259669-3241-488c-a88e-bcf3a07a58c0"]
            .name
            == "Water Control 2"
        )
        assert m_devices.call_count == 1
        assert m_devices_2.call_count == 1
