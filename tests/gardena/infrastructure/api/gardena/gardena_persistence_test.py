from unittest.mock import Mock

from gardena.infrastructure.api.gardena.entities.gardena_location_api import (
    GardenaLocationApi,
)
from gardena.infrastructure.api.gardena.gardena_persistence import GardenaPersistence


class TestGardenaPersistence:
    def test_get_locations_should_return_a_list_of_locations(self):
        # Given
        first_location = GardenaLocationApi()
        first_location.id = "id-1"
        first_location.name = "my first garden"

        second_location = GardenaLocationApi()
        second_location.id = "id-2"
        second_location.name = "my second garden"

        gardena_api_mock = Mock()
        gardena_api_mock.get_locations.return_value = [first_location, second_location]

        gardena_persistence: GardenaPersistence = GardenaPersistence(gardena_api_mock)

        # When
        returned_locations = gardena_persistence.get_locations()

        # Then
        assert len(returned_locations) == 2
        assert returned_locations[0].id == "id-1"
        assert returned_locations[0].name == "my first garden"
        assert returned_locations[0].devices == {}
        assert returned_locations[1].id == "id-2"
        assert returned_locations[1].name == "my second garden"
        assert returned_locations[1].devices == {}
