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
        if "VALVE_SET" in device_map:
            # SmartIrrigationControl has only one item
            self.valve_set_id = device_map["VALVE_SET"][0]["id"]
            self.set_attribute_value(
                "valve_set_state", device_map["VALVE_SET"][0], "state"
            )
            self.set_attribute_value(
                "valve_set_last_error_code", device_map["VALVE_SET"][0], "lastErrorCode"
            )
        if "VALVE" in device_map:
            for valve in device_map["VALVE"]:
                self.valves[valve["id"]] = {
                    "id": valve["id"],
                    "activity": valve["attributes"]["activity"]["value"],
                    "last_error_code": valve["attributes"]["lastErrorCode"]["value"],
                    "name": valve["attributes"]["name"]["value"],
                    "state": valve["attributes"]["state"]["value"],
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
