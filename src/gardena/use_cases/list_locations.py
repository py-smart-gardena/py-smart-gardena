from gardena.domain.entities.mower import Mower
from gardena.use_cases.persistence.location_persistence import LocationPersistence


class ListLocations:
    def __init__(self, location_persistence: LocationPersistence):
        self.location_persistence = location_persistence

    def execute(self) -> [Mower]:
        return self.location_persistence.get_locations()
