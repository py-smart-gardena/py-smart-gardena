import unittest

from gardena.devices.power import Power
from tests.gardena_api_return.devices_return import device_power_return
from tests.fixtures import SmartSystemFixture, LocationFixture
from tests.devices.base_device_test_class import BaseDeviceTestClass


class PowerTestCase(unittest.TestCase, BaseDeviceTestClass):
    def test_power_information(self):
        smart_system_fixture = SmartSystemFixture.get_smart_system_fixture()
        power = Power(
            smart_system=smart_system_fixture,
            location=LocationFixture.get_location_fixture(),
        )
        power.update_information(device_power_return)
        assert power.id == device_power_return["id"]
        assert power.name == device_power_return["name"]
        assert power.category == device_power_return["category"]
        assert (
            power.is_configuration_synchronized
            == device_power_return["configuration_synchronized"]
        )
        assert power.serial_number == "87654321"
        assert power.version == "0.0.1-2.5.2-1.2.6-ICD1.17_1.0.1"
        assert power.last_time_online == "2019-01-15T23:49:04.331Z"
        assert power.device_state == "ok"
        assert power.sgtin == "3034F8EE902273C000000A52"
        assert power.manufacturer == "Gardena"
        assert power.power_timer == "off"
        assert power.power_error == "ok"

    def test_power_get_all_info(self):
        smart_system_fixture = SmartSystemFixture.get_smart_system_fixture()
        power = Power(
            smart_system=smart_system_fixture,
            location=LocationFixture.get_location_fixture(),
        )
        power.update_information(device_power_return)
        info = power.get_all_info()
        assert info["id"] == device_power_return["id"]
        assert info["name"] == device_power_return["name"]
        assert info["category"] == device_power_return["category"]
        assert (
            info["is_configuration_synchronized"]
            == device_power_return["configuration_synchronized"]
        )
        assert info["serial_number"] == "87654321"
        assert info["version"] == "0.0.1-2.5.2-1.2.6-ICD1.17_1.0.1"
        assert info["last_time_online"] == "2019-01-15T23:49:04.331Z"
        assert info["device_state"] == "ok"
        assert info["sgtin"] == "3034F8EE902273C000000A52"
        assert info["manufacturer"] == "Gardena"
        assert info["power_timer"] == "off"
        assert info["power_error"] == "ok"

    def test_power_on(self):
        smart_system = SmartSystemFixture.get_smart_system_fixture()
        mock = self.create_mock(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        location = smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
        m_result = mock.register_power_command(
            "c6e981e9-8ec6-438f-b400-c720d7f313c8",
            "1c8b301f-22c8-423d-1b4d-ec25315d1377",
        )
        power = Power(smart_system=smart_system, location=location)
        power.update_information(device_power_return)
        power.power_on()
        assert m_result.call_count == 1

    def test_power_on_with_duration(self):
        smart_system = SmartSystemFixture.get_smart_system_fixture()
        mock = self.create_mock(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        location = smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
        m_result = mock.register_power_command(
            "c6e981e9-8ec6-438f-b400-c720d7f313c8",
            "1c8b301f-22c8-423d-1b4d-ec25315d1377",
        )
        power = Power(smart_system=smart_system, location=location)
        power.update_information(device_power_return)
        power.power_on(duration=300)
        assert m_result.call_count == 1

    def test_power_off(self):
        smart_system = SmartSystemFixture.get_smart_system_fixture()
        mock = self.create_mock(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        location = smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
        m_result = mock.register_power_command(
            "c6e981e9-8ec6-438f-b400-c720d7f313c8",
            "1c8b301f-22c8-423d-1b4d-ec25315d1377",
        )
        power = Power(smart_system=smart_system, location=location)
        power.update_information(device_power_return)
        power.power_off()
        assert m_result.call_count == 1

    def test_power_refresh_link_status(self):
        smart_system = SmartSystemFixture.get_smart_system_fixture()
        mock = self.create_mock(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        location = smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
        m_result = mock.register_refresh_link_command(
            "c6e981e9-8ec6-438f-b400-c720d7f313c8",
            "1c8b301f-22c8-423d-1b4d-ec25315d1377",
        )
        power = Power(smart_system=smart_system, location=location)
        power.update_information(device_power_return)
        power.refresh_link_status()
        assert m_result.call_count == 1
