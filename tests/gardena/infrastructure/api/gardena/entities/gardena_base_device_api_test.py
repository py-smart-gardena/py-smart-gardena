import pytest
from gardena.infrastructure.api.gardena.entities.gardena_base_device_api import (
    GardenaBaseDeviceApi,
)


class TestGardenaBaseDeviceApi:
    @pytest.mark.usefixtures("mower_fixture")
    def test_setup_values_from_device_map_should_set_the_value_from_map(
        self, mower_fixture
    ):
        # Given
        gardena_base_device_api = GardenaBaseDeviceApi()
        device_map = {"message_list": [mower_fixture["COMMON"][0]]}
        # When
        gardena_base_device_api.setup_values_from_device_map(device_map)
        # Then
        assert gardena_base_device_api.id is None
        assert gardena_base_device_api.type == "N/A"
        assert gardena_base_device_api.battery_level == 100
        assert gardena_base_device_api.battery_state == "OK"
        assert gardena_base_device_api.name == "SILENO"
        assert gardena_base_device_api.rf_link_level == 50
        assert gardena_base_device_api.rf_link_state == "ONLINE"
        assert gardena_base_device_api.serial == "00003676"
