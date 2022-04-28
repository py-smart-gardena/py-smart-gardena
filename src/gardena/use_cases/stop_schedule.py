from gardena.domain.entities.mower import Mower
from gardena.use_cases.persistence.mowers_persistence import MowersPersistence


class StopSchedule:
    def __init__(self, mowers_persistence: MowersPersistence):
        self.mowers_persistence = mowers_persistence

    def execute(self, mower: Mower):
        return self.mowers_persistence.park_until_further_notice(mower_id=mower.id)
