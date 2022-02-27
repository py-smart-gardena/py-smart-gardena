import uuid

from gardena.infrastructure.api.gardena.mappers.gardena_location_api_mapper import (
    GardenaLocationApiMapper,
)


class TestGardenaApiConfiguration:
    def test_to_location_devrait_renvoyer_une_locations(self):
        # Given
        location_id = uuid.uuid4()
        garden_name = "My garden"
        data = {"id": location_id, "attributes": {"name": garden_name}}
        gardena_location_api_mapper = GardenaLocationApiMapper()

        # When
        returned_location = gardena_location_api_mapper.to_location(data)

        # Then
        assert returned_location.id == location_id
        assert returned_location.name == garden_name
        assert returned_location.devices == {}
