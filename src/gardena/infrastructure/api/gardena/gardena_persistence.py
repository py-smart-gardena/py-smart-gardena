from gardena.domain.entities.location import Location
from gardena.infrastructure.api.gardena.gardena_api import GardenaApi
from gardena.use_cases.persistence.location_persistence import LocationPersistence
from gardena.use_cases.persistence.mower_persistence import MowerPersistence


class GardenaPersistence(MowerPersistence, LocationPersistence):
    def __init__(self, gardena_api: GardenaApi):
        self.gardena_api = gardena_api

    def get_locations(self) -> [Location]:
        return list(map(lambda x: x.to_location(), self.gardena_api.get_locations()))
