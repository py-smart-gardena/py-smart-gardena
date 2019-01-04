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
        assert location.latitude == self.location_test_info["geo_position"]["latitude"]
        assert (
            location.longitude == self.location_test_info["geo_position"]["longitude"]
        )
        assert location.address == self.location_test_info["geo_position"]["address"]
        assert location.city == self.location_test_info["geo_position"]["city"]
        assert location.sunrise == self.location_test_info["geo_position"]["sunrise"]
        assert location.sunset == self.location_test_info["geo_position"]["sunset"]
        assert (
            location.time_zone == self.location_test_info["geo_position"]["time_zone"]
        )
        assert (
            location.time_zone_offset
            == self.location_test_info["geo_position"]["time_zone_offset"]
        )

    def test_update_devices(self):
        location = Location(smart_system=self.smart_system_test_info)
        location.update_information(self.location_test_info)
        location.update_devices()
        assert len(location.gateways) == 1
        assert len(location.mowers) == 1

    def test_update_devices_unknown_category(self):
        location = Location(smart_system=self.smart_system_test_info)
        location.update_information(self.location_test_info)
        location.update_devices()
        assert len(location.gateways) == 1
        assert len(location.mowers) == 1
        with pytest.raises(ValueError):
            location.add_or_update_device(
                device={
                    "id": "75cfc1f8-a20c-51d6-c5ea-1b5eccce80c1",
                    "name": "Unknown device",
                    "description": "Unknown device",
                    "category": "unknown_category",
                }
            )
        assert len(location.gateways) == 1
        assert len(location.mowers) == 1

    def test_update_devices_exception_with_none_device(self):
        location = Location(smart_system=self.smart_system_test_info)
        location.update_information(self.location_test_info)
        location.update_devices()
        assert len(location.gateways) == 1
        assert len(location.mowers) == 1
        with pytest.raises(ValueError):
            location.add_or_update_device()
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
