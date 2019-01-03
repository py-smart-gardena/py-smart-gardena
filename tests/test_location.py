import pytest
import unittest

from requests import HTTPError

from gardena.smart_system import SmartSystem
from gardena.location import Location
from tests.gardena_api_mock import init_mock, init_failed_mock


class LocationTestCase(unittest.TestCase):

    smart_system_test_info = None

    location_test_info = {
        "id": "1c8b301f-22c8-423d-1b4d-ec25315d1377",
        "name": "My Garden",
        "devices": [
            "75cfc1f8-a20c-51d6-c5ea-1b5ecdde80c1",
            "e3c1b615-7351-25fc-a551-1908254a2b3e",
        ],
    }

    def setup_method(self, method):
        self.smart_system_test_info = SmartSystem(
            email="test@test.com", password="password"
        )
        init_mock(self.smart_system_test_info)
        self.smart_system_test_info.authenticate()

    def test_init(self):
        location = Location(smart_system=self.smart_system_test_info)
        assert location.smart_system == self.smart_system_test_info

    def test_init_exception_without_smart_system(self):
        with pytest.raises(ValueError):
            Location()

    def test_location_information(self):
        location = Location(smart_system=self.smart_system_test_info)
        location.update_information(self.location_test_info)
        assert location.id == self.location_test_info["id"]
        assert location.name == self.location_test_info["name"]

    def test_get_devices(self):
        location = Location(smart_system=self.smart_system_test_info)
        location.update_information(self.location_test_info)
        location.update_devices()
        assert len(location.gateways) == 1
        assert len(location.mowers) == 1

    def test_get_devices_failed(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_failed_mock(smart_system)
        smart_system.authenticate()
        location = Location(smart_system=smart_system)
        location.update_information(self.location_test_info)
        with pytest.raises(HTTPError):
            location.update_devices()

    def test_device_informations(self):
        location = Location(smart_system=self.smart_system_test_info)
        location.update_information(self.location_test_info)
        location.update_devices()
        assert len(location.gateways) == 1
        assert len(location.mowers) == 1
        assert "75cfc1f8-a20c-51d6-c5ea-1b5ecdde80c1" in location.gateways.keys()
        assert "e3c1b615-7351-25fc-a551-1908254a2b3e" in location.mowers.keys()
