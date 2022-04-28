import uuid

from gardena.infrastructure.api.gardena.gardena_api_client import GardenaApiClient
from gardena.use_cases.persistence.mowers_persistence import MowersPersistence


class GardenaMowersPersistence(MowersPersistence):
    def __init__(self, gardena_api: GardenaApiClient):
        self.gardena_api = gardena_api
        self.gardena_api.authenticate()

    def start_and_override_schedule(self, mower_id: str, duration: int):
        if mower_id is not None:
            data = {
                "id": str(uuid.uuid1()),
                "type": "MOWER_CONTROL",
                "attributes": {
                    "command": "START_SECONDS_TO_OVERRIDE",
                    "seconds": duration,
                },
            }
            self.gardena_api.call_command(mower_id, data)
        else:
            print("The mower id is not defined")

    def start_and_dont_override_schedule(self, mower_id: str, duration: int):
        if mower_id is not None:
            data = {
                "id": str(uuid.uuid1()),
                "type": "MOWER_CONTROL",
                "attributes": {"command": "START_DONT_OVERRIDE", "seconds": duration},
            }
            self.gardena_api.call_command(mower_id, data)
        else:
            print("The mower id is not defined")

    def park_until_next_task(self, mower_id: str):
        if mower_id is not None:
            data = {
                "id": str(uuid.uuid1()),
                "type": "MOWER_CONTROL",
                "attributes": {"command": "PARK_UNTIL_NEXT_TASK"},
            }
            self.gardena_api.call_command(mower_id, data)
        else:
            print("The mower id is not defined")

    def park_until_further_notice(self, mower_id: str):
        if mower_id is not None:
            data = {
                "id": str(uuid.uuid1()),
                "type": "MOWER_CONTROL",
                "attributes": {"command": "PARK_UNTIL_FURTHER_NOTICE"},
            }
            self.gardena_api.call_command(mower_id, data)
        else:
            print("The mower id is not defined")
