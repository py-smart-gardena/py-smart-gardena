class MowersPersistence:
    """Interface for mower API"""

    def start_and_override_schedule(self, mower_id: str, duration: int):
        pass

    def start_and_dont_override_schedule(self, mower_id: str, duration: int):
        pass

    def park_until_next_task(self, mower_id: str):
        pass

    def park_until_further_notice(self, mower_id: str):
        pass
