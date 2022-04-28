from gardena.domain.entities.mower import Mower
from gardena.use_cases.persistence.mowers_persistence import MowersPersistence


class StartMowing:
    def __init__(self, mowers_persistence: MowersPersistence):
        self.mowers_persistence = mowers_persistence

    def execute(self, mower: Mower, duration: int):
        return self.mowers_persistence.start_and_override_schedule(
            mower_id=mower.id, duration=duration
        )
