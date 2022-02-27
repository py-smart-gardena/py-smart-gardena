from unittest.mock import Mock

from gardena.domain.entities.location import Location
from gardena.infrastructure.api.gardena.gardena_location_persistence import (
    GardenaLocationsPersistence,
)


class TestGardenaLocationsPersistence:
    def test_get_locations_should_return_a_list_of_locations(self):
        # Given
        first_location = Location(id="id-1", name="my first garden")
        second_location = Location(id="id-2", name="my second garden")

        gardena_api_mock = Mock()
        gardena_api_mock.call_smart_system_get.return_value = {
            "data": [
                {"id": first_location.id, "attributes": {"name": first_location.name}},
                {
                    "id": second_location.id,
                    "attributes": {"name": second_location.name},
                },
            ]
        }

        gardena_persistence: GardenaLocationsPersistence = GardenaLocationsPersistence(
            gardena_api_mock
        )

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
