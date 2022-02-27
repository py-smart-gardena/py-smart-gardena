from unittest.mock import Mock

from gardena.domain.entities.location import Location
from gardena.domain.entities.mower import Mower
from gardena.use_cases.list_locations import ListLocations
from gardena.use_cases.list_mowers import ListMowers


class TestListLocations:
    def test_execute_should_return_a_list_of_locations(self):
        # Given
        locations = [
            Location(),
            Location(),
        ]
        location_persistence_mock = Mock()
        location_persistence_mock.get_locations.return_value = locations

        list_locations = ListLocations(location_persistence=location_persistence_mock)
        # When
        returned_locations = list_locations.execute()

        # Then
        assert len(returned_locations) == 2
        assert returned_locations[0].id == "N/A"
        assert returned_locations[0].name == "N/A"
        assert returned_locations[0].devices == {}
        assert returned_locations[1].id == "N/A"
        assert returned_locations[1].name == "N/A"
        assert returned_locations[1].devices == {}
