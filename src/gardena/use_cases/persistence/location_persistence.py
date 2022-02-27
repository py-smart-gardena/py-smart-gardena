from gardena.domain.entities.location import Location


class LocationPersistence:
    """Interface for Location API"""

    def get_locations(self) -> [Location]:
        pass
