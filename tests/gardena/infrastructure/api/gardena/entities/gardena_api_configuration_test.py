import uuid

from gardena.infrastructure.api.gardena.entities.gardena_location_api import (
    GardenaLocationApi,
)


class TestGardenaApiConfiguration:
    def test_to_location_devrait_renvoyer_une_locations(self):
        # Given
        location_id = uuid.uuid4()
        garden_name = "My garden"
        gardena_location_api = GardenaLocationApi()
        gardena_location_api.id = location_id
        gardena_location_api.devices = []
        gardena_location_api.name = garden_name

        # When
        returned_location = gardena_location_api.to_location()

        # Then
        assert returned_location.id == location_id
        assert returned_location.name == garden_name
        assert returned_location.devices == []
