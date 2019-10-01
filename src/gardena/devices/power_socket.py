from .base_device import BaseDevice
import uuid


class PowerSocket(BaseDevice):

    activity = "N/A"
    operating_hours = "N/A"
    state = "N/A"

    def __init__(self, smart_system, device_map):
        BaseDevice.__init__(self, smart_system, device_map)
        self.type = "POWER_SOCKET"

    def start_seconds_to_override(self, duration):
        data = {
            "id": str(uuid.uuid1()),
            "type": "POWER_SOCKET_CONTROL",
            "attributes": {"command": "START_SECONDS_TO_OVERRIDE", "seconds": duration},
        }
        self.smart_system.call_smart_system_service(self.id, data)

    def start_override(self):
        data = {
            "id": str(uuid.uuid1()),
            "type": "POWER_SOCKET_CONTROL",
            "attributes": {"command": "START_OVERRIDE"},
        }
        self.smart_system.call_smart_system_service(self.id, data)

    def stop_until_next_task(self):
        data = {
            "id": str(uuid.uuid1()),
            "type": "POWER_SOCKET_CONTROL",
            "attributes": {"command": "STOP_UNTIL_NEXT_TASK"},
        }
        self.smart_system.call_smart_system_service(self.id, data)

    def pause(self):
        data = {
            "id": str(uuid.uuid1()),
            "type": "POWER_SOCKET_CONTROL",
            "attributes": {"command": "PAUSE"},
        }
        self.smart_system.call_smart_system_service(self.id, data)

    def unpause(self):
        data = {
            "id": str(uuid.uuid1()),
            "type": "POWER_SOCKET_CONTROL",
            "attributes": {"command": "UNPAUSE"},
        }
        self.smart_system.call_smart_system_service(self.id, data)
