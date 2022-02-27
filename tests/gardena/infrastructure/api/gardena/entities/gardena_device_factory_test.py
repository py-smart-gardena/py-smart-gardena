from unittest.mock import patch, MagicMock

from gardena.infrastructure.api.gardena.entities.gardena_device_factory import (
    GardenaDeviceFactory,
)
from gardena.infrastructure.api.gardena.entities.gardena_mower_api import (
    GardenaMowerApi,
)
from gardena.infrastructure.api.gardena.entities.gardena_power_socket_api import (
    GardenaPowerSocketApi,
)


class TestGardenaDeviceFactory:
    @patch(
        "gardena.infrastructure.api.gardena.entities.gardena_mower_api.GardenaMowerApi",
        create=True,
        new=MagicMock(),
    )
    def test_builds_hould_return_a_mower(self):
        # Given

        # When
        device = GardenaDeviceFactory.build({"MOWER": {}})

        # Then
        assert isinstance(device, GardenaMowerApi)

    @patch(
        "gardena.infrastructure.api.gardena.entities.gardena_power_socket_api.GardenaPowerSocketApi",
        create=True,
        new=MagicMock(),
    )
    def test_build_should_return_a_power_socket(self):
        # Given

        # When
        device = GardenaDeviceFactory.build({"POWER_SOCKET": {}})

        # Then
        assert isinstance(device, GardenaPowerSocketApi)
