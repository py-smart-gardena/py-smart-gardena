from gardena.domain.entities.location import Location
from gardena.infrastructure.api.gardena.gardena_api_client import GardenaApiClient
from gardena.infrastructure.api.gardena.mappers.gardena_location_api_mapper import (
    GardenaLocationApiMapper,
)
from gardena.use_cases.persistence.locations_persistence import LocationsPersistence


class GardenaLocationsPersistence(LocationsPersistence):
    def __init__(self, gardena_api: GardenaApiClient):
        self.gardena_api = gardena_api
        self.gardena_api.authenticate()

    def get_locations(self) -> [Location]:
        response_data = self.gardena_api.call_smart_system_get("/v1/locations")
        if response_data is not None:
            if "data" in response_data and len(response_data["data"]) >= 1:
                return list(
                    map(
                        lambda x: GardenaLocationApiMapper.to_location(x),
                        response_data["data"],
                    )
                )
        return list()
