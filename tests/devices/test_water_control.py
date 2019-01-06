import unittest

from gardena.devices.water_control import WaterControl
from tests.gardena_api_return.devices_return import device_water_control_return
from tests.fixtures import SmartSystemFixture, LocationFixture


class WaterControlTestCase(unittest.TestCase):
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
        assert not water_control.watering_valve_open
        assert water_control.watering_manual_override == "inactive"
