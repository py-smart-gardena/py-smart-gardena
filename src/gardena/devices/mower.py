from .base_device import BaseDevice
import uuid


class Mower(BaseDevice):

    def __init__(self, location, device_map):
        """Constructor for the mower device."""
        BaseDevice.__init__(self, location, device_map["COMMON"][0]["id"])
        self.type = "MOWER"
        self.activity = "N/A"
        self.operating_hours = "N/A"
        self.state = "N/A"
        self.last_error_code = "N/A"
        self.mower_id = None
        self.setup_values_from_device_map(device_map)

    def update_device_specific_data(self, device_map):
        # Mower has only one item
        if device_map["type"] == "MOWER":
            self.mower_id = device_map["id"]
            self.set_attribute_value("activity", device_map, "activity")
            self.set_attribute_value("operating_hours", device_map, "operatingHours")
            self.set_attribute_value("state", device_map, "state")
            self.set_attribute_value("last_error_code", device_map, "lastErrorCode")

    def start_seconds_to_override(self, duration):
        if self.mower_id is not None:
            data = {
                "id": str(uuid.uuid1()),
                "type": "MOWER_CONTROL",
                "attributes": {"command": "START_SECONDS_TO_OVERRIDE", "seconds": duration},
            }
            self.location.smart_system.call_smart_system_service(self.mower_id, data)
        else:
            self.location.smart_system.logger.error("The mower id is not defined")

    def start_dont_override(self, duration):
        if self.mower_id is not None:
            data = {
                "id": str(uuid.uuid1()),
                "type": "MOWER_CONTROL",
                "attributes": {"command": "START_DONT_OVERRIDE", "seconds": duration},
            }
            self.location.smart_system.call_smart_system_service(self.mower_id, data)
        else:
            self.location.smart_system.logger.error("The mower id is not defined")

    def park_until_next_task(self):
        if self.mower_id is not None:
            data = {
                "id": str(uuid.uuid1()),
                "type": "MOWER_CONTROL",
                "attributes": {"command": "PARK_UNTIL_NEXT_TASK"},
            }
            self.location.smart_system.call_smart_system_service(self.mower_id, data)
        else:
            self.location.smart_system.logger.error("The mower id is not defined")

    def park_until_further_notice(self):
        if self.mower_id is not None:
            data = {
                "id": str(uuid.uuid1()),
                "type": "MOWER_CONTROL",
                "attributes": {"command": "PARK_UNTIL_FURTHER_NOTICE"},
            }
            self.location.smart_system.call_smart_system_service(self.mower_id, data)
        else:
            self.location.smart_system.logger.error("The mower id is not defined")
