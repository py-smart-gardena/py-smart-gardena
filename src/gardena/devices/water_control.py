from .base_device import BaseDevice
import uuid


class WaterControl(BaseDevice):
    def __init__(self, location, device_map):
        """Constructor for the water control device."""
        BaseDevice.__init__(self, location, device_map["COMMON"][0]["id"])
        self.type = "WATER_CONTROL"
        self.valve_set_id = "N/A"
        self.valve_id = "N/A"
        self.valve_activity = "N/A"
        self.valve_name = "N/A"
        self.valve_state = "N/A"
        self.setup_values_from_device_map(device_map)

    def update_device_specific_data(self, device_map):
        if device_map["type"] == "VALVE_SET":
            self.valve_set_id = device_map["id"]
        if device_map["type"] == "VALVE":
            self.valve_id = device_map["id"]
            self.set_attribute_value("valve_activity", device_map, "activity")
            self.set_attribute_value("valve_name", device_map, "name")
            self.set_attribute_value("valve_state", device_map, "state")

    async def start_seconds_to_override(self, duration):
        data = {
            "id": str(uuid.uuid1()),
            "type": "VALVE_CONTROL",
            "attributes": {"command": "START_SECONDS_TO_OVERRIDE", "seconds": duration},
        }
        await self.location.smart_system.call_smart_system_service(self.valve_id, data)

    async def stop_until_next_task(self):
        data = {
            "id": str(uuid.uuid1()),
            "type": "VALVE_CONTROL",
            "attributes": {"command": "STOP_UNTIL_NEXT_TASK"},
        }
        await self.location.smart_system.call_smart_system_service(self.valve_id, data)

    async def pause(self):
        data = {
            "id": str(uuid.uuid1()),
            "type": "VALVE_CONTROL",
            "attributes": {"command": "PAUSE"},
        }
        await self.location.smart_system.call_smart_system_service(self.valve_id, data)

    async def unpause(self):
        data = {
            "id": str(uuid.uuid1()),
            "type": "VALVE_CONTROL",
            "attributes": {"command": "UNPAUSE"},
        }
        await self.location.smart_system.call_smart_system_service(self.valve_id, data)
