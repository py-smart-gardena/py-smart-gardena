from gardena.infrastructure.api.gardena.entities.gardena_location_api import (
    GardenaLocationApi,
)
from gardena.infrastructure.api.gardena.gardena_persistence_configuration import (
    GardenaPersistenceConfiguration,
)


class GardenaApi:
    def __init__(
        self, gardena_persistence_configuration: GardenaPersistenceConfiguration
    ):
        self.gardena_persistence_configuration = gardena_persistence_configuration

    def get_locations(self) -> [GardenaLocationApi]:
        pass
