from .base_device import BaseDevice
import uuid


class PowerSocket(BaseDevice):

    def __init__(self, location, device_map):
        """Constructor for the Power socket device."""
        BaseDevice.__init__(self, location, device_map["COMMON"][0]["id"])
        self.type = "POWER_SOCKET"
        self.activity = "N/A"
        self.state = "N/A"
        self.last_error_code = "N/A"
        self.setup_values_from_device_map(device_map)

    def update_device_specific_data(self, device_map):
        if device_map["type"] == "POWER_SOCKET":
            # Sensor has only one item
            self.set_attribute_value("activity", device_map, "activity")
            self.set_attribute_value("state", device_map, "state")
            self.set_attribute_value("last_error_code", device_map, "lastErrorCode")

    def start_seconds_to_override(self, duration):
        data = {
            "id": str(uuid.uuid1()),
            "type": "POWER_SOCKET_CONTROL",
            "attributes": {"command": "START_SECONDS_TO_OVERRIDE", "seconds": duration},
        }
        self.location.smart_system.call_smart_system_service(self.id, data)

    def start_override(self):
        data = {
            "id": str(uuid.uuid1()),
            "type": "POWER_SOCKET_CONTROL",
            "attributes": {"command": "START_OVERRIDE"},
        }
        self.location.smart_system.call_smart_system_service(self.id, data)

    def stop_until_next_task(self):
        data = {
            "id": str(uuid.uuid1()),
            "type": "POWER_SOCKET_CONTROL",
            "attributes": {"command": "STOP_UNTIL_NEXT_TASK"},
        }
        self.location.smart_system.call_smart_system_service(self.id, data)

    def pause(self):
        data = {
            "id": str(uuid.uuid1()),
            "type": "POWER_SOCKET_CONTROL",
            "attributes": {"command": "PAUSE"},
        }
        self.location.smart_system.call_smart_system_service(self.id, data)

    def unpause(self):
        data = {
            "id": str(uuid.uuid1()),
            "type": "POWER_SOCKET_CONTROL",
            "attributes": {"command": "UNPAUSE"},
        }
        self.location.smart_system.call_smart_system_service(self.id, data)
