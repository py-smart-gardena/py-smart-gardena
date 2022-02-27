from gardena.domain.entities.mower import Mower


class MowerPersistence:
    """Interface for mower API"""

    def get_mowers(self) -> [Mower]:
        pass
