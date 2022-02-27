from unittest.mock import Mock

from gardena.domain.entities.device_type import DeviceType
from gardena.domain.entities.location import Location
from gardena.domain.entities.mower import Mower
from gardena.use_cases.list_devices import ListDevice


class TestListDevices:
    def test_execute_should_return_a_list_of_devices(self):
        # Given
        location = Location()
        devices = [
            Mower(),
            Mower(),
        ]
        devices_persistence_mock = Mock()
        devices_persistence_mock.get_devices.return_value = devices

        list_devices = ListDevice(devices_persistence=devices_persistence_mock)
        # When
        returned_devices = list_devices.execute(location)

        # Then
        assert len(returned_devices) == 2
        assert returned_devices[0].type == DeviceType.MOWER
        assert returned_devices[0].id is None
        assert returned_devices[0].battery_level == "N/A"
        assert returned_devices[0].battery_state == "N/A"
        assert returned_devices[0].name == "N/A"
        assert returned_devices[0].rf_link_level == "N/A"
        assert returned_devices[0].rf_link_state == "N/A"
        assert returned_devices[0].serial == "N/A"
        assert returned_devices[0].model_type == "N/A"
        assert returned_devices[0].callbacks == []
        assert returned_devices[0].activity == "N/A"
        assert returned_devices[0].operating_hours == "N/A"
        assert returned_devices[0].state == "N/A"
        assert returned_devices[0].last_error_code == "N/A"
        assert returned_devices[0].type == DeviceType.MOWER
        assert returned_devices[1].id is None
        assert returned_devices[1].battery_level == "N/A"
        assert returned_devices[1].battery_state == "N/A"
        assert returned_devices[1].name == "N/A"
        assert returned_devices[1].rf_link_level == "N/A"
        assert returned_devices[1].rf_link_state == "N/A"
        assert returned_devices[1].serial == "N/A"
        assert returned_devices[1].model_type == "N/A"
        assert returned_devices[1].callbacks == []
        assert returned_devices[1].activity == "N/A"
        assert returned_devices[1].operating_hours == "N/A"
        assert returned_devices[1].state == "N/A"
        assert returned_devices[1].last_error_code == "N/A"
