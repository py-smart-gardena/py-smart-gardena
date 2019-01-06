import pytest
import unittest

from gardena.devices.abilities.base_gardena_ability_class import BaseGardenaAbilityClass
from tests.mocks.gardena_api_mock import GardenaApiMock
from tests.fixtures import SmartSystemFixture, LocationFixture


class BaseGardenaDeviceClassTestCase(unittest.TestCase):
    smart_system_test_info = None
    location_test_info = None

    def setup_method(self, method):
        self.smart_system_test_info = SmartSystemFixture.get_smart_system_fixture()
        api_mock = GardenaApiMock()
        api_mock.register_sessions()
        api_mock.register_locations()
        api_mock.mount(self.smart_system_test_info)
        self.smart_system_test_info.authenticate()
        self.location_test_info = LocationFixture.get_location_fixture()

    def test_init(self):
        base_device_class = BaseGardenaAbilityClass(
            smart_system=self.smart_system_test_info, location=self.location_test_info
        )
        assert base_device_class.smart_system == self.smart_system_test_info
        assert base_device_class.location == self.location_test_info

    def test_init_exception_without_smart_system(self):
        with pytest.raises(ValueError):
            BaseGardenaAbilityClass(location=self.location_test_info)

    def test_init_exception_without_location(self):
        with pytest.raises(ValueError):
            BaseGardenaAbilityClass(smart_system=self.smart_system_test_info)
