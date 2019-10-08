from .base_device import BaseDevice
import uuid


class SmartIrrigationControl(BaseDevice):

    valve_set_id = "N/A"
    valve_set_state = "N/A"
    valve_set_last_error_code = "N/A"
    valves = {}

    def __init__(self, smart_system, device_map):
        BaseDevice.__init__(self, smart_system, device_map)
        self.type = "SMART_IRRIGATION_CONTROL"

    def update_device_specific_data(self, device_map):
        if device_map["type"] == "VALVE_SET":
            # SmartIrrigationControl has only one item
            self.valve_set_id = device_map["id"]
            self.set_attribute_value("valve_set_state", device_map, "state")
            self.set_attribute_value(
                "valve_set_last_error_code", device_map, "lastErrorCode"
            )
        if device_map["type"] == "VALVE":
            self.valves[device_map["id"]] = {
                "id": device_map["id"],
                "activity": device_map["attributes"]["activity"]["value"],
                "last_error_code": device_map["attributes"]["lastErrorCode"]["value"],
                "name": device_map["attributes"]["name"]["value"],
                "state": device_map["attributes"]["state"]["value"],
            }

    def start_seconds_to_override(self, duration, valve_id):
        data = {
            "id": str(uuid.uuid1()),
            "type": "VALVE_CONTROL",
            "attributes": {"command": "START_SECONDS_TO_OVERRIDE", "seconds": duration},
        }
        self.smart_system.call_smart_system_service(valve_id, data)

    def stop_until_next_task(self, valve_id):
        data = {
            "id": str(uuid.uuid1()),
            "type": "VALVE_CONTROL",
            "attributes": {"command": "STOP_UNTIL_NEXT_TASK"},
        }
        self.smart_system.call_smart_system_service(valve_id, data)

    def pause(self, valve_id):
        data = {
            "id": str(uuid.uuid1()),
            "type": "VALVE_CONTROL",
            "attributes": {"command": "PAUSE"},
        }
        self.smart_system.call_smart_system_service(valve_id, data)

    def unpause(self, valve_id):
        data = {
            "id": str(uuid.uuid1()),
            "type": "VALVE_CONTROL",
            "attributes": {"command": "UNPAUSE"},
        }
        self.smart_system.call_smart_system_service(valve_id, data)
