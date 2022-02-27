from gardena.domain.entities.mower import Mower
from gardena.use_cases.persistence.mower_persistence import MowerPersistence


class ListMowers:
    def __init__(self, mower_persistence: MowerPersistence):
        self.mower_persistence = mower_persistence

    def execute(self) -> [Mower]:
        return self.mower_persistence.get_mowers()
