import pytest
import unittest
from gardena.smart_system import SmartSystem
from gardena.location import Location


class LocationTestCase(unittest.TestCase):

    smart_system_test_info = SmartSystem(email="test@test.com", password="password")

    location_test_info = {
        "id": "1c8b301f-22c8-423d-1b4d-ec25315d1377",
        "name": "My Garden",
        "devices": [
            "75cfc1f8-a20c-51d6-c5ea-1b5ecdde80c1",
            "e3c1b615-7351-25fc-a551-1908254a2b3e",
        ],
    }

    def test_init(self):
        location = Location(
            smart_system=self.smart_system_test_info,
            api_information=self.location_test_info,
        )
        assert location.smart_system == self.smart_system_test_info
        assert location.api_information == self.location_test_info

    def test_init_exception_without_smart_system(self):
        with pytest.raises(ValueError):
            Location(api_information=self.location_test_info)

    def test_init_exception_without_device_info(self):
        with pytest.raises(ValueError):
            Location(smart_system=self.smart_system_test_info)

    def test_locations_infos(self):
        location = Location(
            smart_system=self.smart_system_test_info,
            api_information=self.location_test_info,
        )
        assert location.get_id() == self.location_test_info["id"]
        assert location.get_name() == self.location_test_info["name"]
