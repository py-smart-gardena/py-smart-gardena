import unittest

from gardena.devices.water_control import WaterControl
from tests.gardena_api_return.devices_return import device_water_control_return
from tests.fixtures import SmartSystemFixture, LocationFixture
from tests.devices.base_device_test_class import BaseDeviceTestClass


class WaterControlTestCase(unittest.TestCase, BaseDeviceTestClass):
    def test_water_control_information(self):
        water_control = WaterControl(
            smart_system=SmartSystemFixture.get_smart_system_fixture(),
            location=LocationFixture.get_location_fixture(),
        )
        water_control.update_information(device_water_control_return)
        assert water_control.id == device_water_control_return["id"]
        assert water_control.name == device_water_control_return["name"]
        # XXX : no description for water_control ?
        # assert water_control.description == device_water_control_return["description"]
        assert water_control.category == device_water_control_return["category"]
        assert (
            water_control.is_configuration_synchronized
            == device_water_control_return["configuration_synchronized"]
        )
        assert water_control.serial_number == "12345678"
        assert water_control.version == "0.3.5-2.5.2-1.2.5-ICD1.17_1.0.20"
        assert water_control.last_time_online == "2019-01-03T23:25:56.050Z"
        assert water_control.device_state == "ok"
        assert water_control.battery_level == 97
        assert water_control.battery_status == "ok"
        assert water_control.radio_quality == 100
        assert water_control.radio_connection_status == "unknown"
        assert water_control.radio_state == "good"
        assert water_control.ambient_temperature == 22
        assert water_control.frost_warning == "no_frost"
        assert water_control.firmware_status == "up_to_date"
        assert water_control.firmware_upload_progress == 0
        assert water_control.firmware_update_start
        assert not water_control.watering_valve_open
        assert water_control.watering_manual_override == "inactive"

    def test_open_valve(self):
        smart_system = SmartSystemFixture.get_smart_system_fixture()
        mock = self.create_mock(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        location = smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
        m_result = mock.register_device_water_control_open__close_valve_command(
            "d6259669-3241-488c-a88e-bcf3a07a58bf",
            "1c8b301f-22c8-423d-1b4d-ec25315d1377",
        )
        water_control = WaterControl(smart_system=smart_system, location=location)
        water_control.update_information(device_water_control_return)
        water_control.open_valve()
        assert m_result.call_count == 1

    def test_close_valve(self):
        smart_system = SmartSystemFixture.get_smart_system_fixture()
        mock = self.create_mock(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        location = smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
        m_result = mock.register_device_water_control_open__close_valve_command(
            "d6259669-3241-488c-a88e-bcf3a07a58bf",
            "1c8b301f-22c8-423d-1b4d-ec25315d1377",
        )
        water_control = WaterControl(smart_system=smart_system, location=location)
        water_control.update_information(device_water_control_return)
        water_control.close_valve()
        assert m_result.call_count == 1
