import unittest

from gardena.devices.mower import Mower
from tests.gardena_api_return.devices_return import device_mower_return
from tests.fixtures import SmartSystemFixture, LocationFixture


class MowerTestCase(unittest.TestCase):
    def test_mower_information(self):
        mower = Mower(
            smart_system=SmartSystemFixture.get_smart_system_fixture(),
            location=LocationFixture.get_location_fixture(),
        )
        mower.update_information(information=device_mower_return)
        assert mower.id == device_mower_return["id"]
        assert mower.name == device_mower_return["name"]
        # XXX : no description for mower ?
        # assert mower.description == device_mower_return["description"]
        assert mower.category == device_mower_return["category"]
        assert (
            mower.is_configuration_synchronized
            == device_mower_return["configuration_synchronized"]
        )
        assert mower.serial_number == "12345678"
        assert mower.version == "3-2.4.7-1.2.0-4380-MODIFIED-ICD1.16_1.2.0"
        assert mower.last_time_online == "2016-07-21T13:28:48Z"
        assert mower.battery_level == 100
        assert mower.battery_status == "ok"
        assert not mower.battery_charging
        assert mower.radio_quality == 50
        assert mower.radio_connection_status == "status_device_unreachable"
        assert mower.radio_state == "good"
        assert mower.internal_temperature == 32
        assert mower.mower_status == "off_disabled"
        assert not mower.mower_manual_operation
        assert mower.mower_timestamp_next_start == "2016-07-22T08:00:00.000000001Z"
