from gardena.domain.entities.location import Location
from gardena.use_cases.persistence.locations_persistence import LocationsPersistence


class ListLocations:
    def __init__(self, location_persistence: LocationsPersistence):
        self.location_persistence = location_persistence

    def execute(self) -> [Location]:
        return self.location_persistence.get_locations()
