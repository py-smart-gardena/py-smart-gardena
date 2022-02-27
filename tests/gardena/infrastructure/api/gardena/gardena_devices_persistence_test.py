import json
from unittest.mock import Mock

import pytest
from gardena.domain.entities.device_type import DeviceType
from gardena.domain.entities.location import Location
from gardena.infrastructure.api.gardena.gardena_devices_persistence import (
    GardenaDevicesPersistence,
)


class TestGardenaDeevicesPersistence:
    @pytest.mark.usefixtures("mower_fixture")
    def test_get_devices_should_return_a_list_of_devices(self, mower_fixture):
        # Given
        gardena_api_mock = Mock()
        gardena_api_mock.call_smart_system_get.return_value = json.load(
            open("tests/gardena/infrastructure/api/gardena/ressources/get_devices.json")
        )

        gardena_persistence: GardenaDevicesPersistence = GardenaDevicesPersistence(
            gardena_api_mock
        )

        # When
        returned_devices = gardena_persistence.get_devices(Location())

        # Then
        assert len(returned_devices.mowers) == 1
        assert returned_devices.mowers[0].id == "4ad7d828-b19f-47d5-b7d2-15eea0fb8516"
        assert returned_devices.mowers[0].type == DeviceType.MOWER
        assert returned_devices.mowers[0].activity == "PARKED_PARK_SELECTED"
        assert returned_devices.mowers[0].operating_hours == 341
        assert returned_devices.mowers[0].state == "OK"
        assert returned_devices.mowers[0].last_error_code == "N/A"
        assert returned_devices.mowers[0].battery_level == 100
        assert returned_devices.mowers[0].battery_state == "N/A"
        assert returned_devices.mowers[0].name == "SILENO"
        assert returned_devices.mowers[0].rf_link_level == 100
        assert returned_devices.mowers[0].rf_link_state == "ONLINE"
        assert returned_devices.mowers[0].serial == "123456789"
        assert returned_devices.mowers[0].model_type == "GARDENA smart Mower"
        assert returned_devices.mowers[0].callbacks == []
