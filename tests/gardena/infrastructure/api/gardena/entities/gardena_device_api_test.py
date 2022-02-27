import pytest
from gardena.infrastructure.api.gardena.entities.gardena_device_api import (
    GardenaDeviceApi,
)


class TestGardenaDeviceApi:
    @pytest.mark.usefixtures("mower_fixture")
    def test_init_should_set_the_values_if_the_type_is_supported(self, mower_fixture):
        # Given

        # When
        gardena_device_api = GardenaDeviceApi(mower_fixture["COMMON"][0])
        # Then
        assert gardena_device_api.id == "7859acbd-b23e-dabf-bec6-62c1453fc44c"
        assert gardena_device_api.type == "COMMON"
        assert gardena_device_api.gardena_device == mower_fixture["COMMON"][0]

    @pytest.mark.usefixtures("mower_fixture")
    def test_init_should_not_set_the_values_if_the_type_is_not_supported(
        self, mower_fixture
    ):
        # Given
        unsupported_device_type = mower_fixture["COMMON"][0]
        unsupported_device_type["type"] = "UNSUPPOERTED_TYPE"
        # When
        gardena_device_api = GardenaDeviceApi(unsupported_device_type)
        # Then
        assert gardena_device_api.id is None
        assert gardena_device_api.type is None
        assert gardena_device_api.gardena_device is None
