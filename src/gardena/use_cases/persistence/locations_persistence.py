from gardena.domain.entities.location import Location


class LocationsPersistence:
    """Interface for Location API"""

    def get_locations(self) -> [Location]:
        pass
