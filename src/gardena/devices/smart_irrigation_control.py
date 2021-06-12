from .base_device import BaseDevice
import uuid


class SmartIrrigationControl(BaseDevice):

    def __init__(self, location, device_map):
        """Constructor for the smart irrigation control device."""
        BaseDevice.__init__(self, location, device_map["COMMON"][0]["id"])
        self.type = "SMART_IRRIGATION_CONTROL"
        self.valve_set_id = "N/A"
        self.valve_set_state = "N/A"
        self.valve_set_last_error_code = "N/A"
        self.valves = {}
        self.setup_values_from_device_map(device_map)

    def _set_valves_map_value(self, target_map, source_map, value_name_in_source, value_name_in_target=None):
        if not value_name_in_target:
            value_name_in_target = value_name_in_source
        if value_name_in_source in source_map:
            target_map[value_name_in_target] = source_map[value_name_in_source]["value"]
        else:
            target_map[value_name_in_target] = 'N/A'

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
                "id": device_map["id"]
            }
            self._set_valves_map_value(self.valves[device_map["id"]], device_map["attributes"], 'activity')
            self._set_valves_map_value(self.valves[device_map["id"]], device_map["attributes"], 'lastErrorCode', 'last_error_code')
            self._set_valves_map_value(self.valves[device_map["id"]], device_map["attributes"], 'name')
            self._set_valves_map_value(self.valves[device_map["id"]], device_map["attributes"], 'state')

    def start_seconds_to_override(self, duration, valve_id):
        data = {
            "id": str(uuid.uuid1()),
            "type": "VALVE_CONTROL",
            "attributes": {"command": "START_SECONDS_TO_OVERRIDE", "seconds": duration},
        }
        self.location.smart_system.call_smart_system_service(valve_id, data)

    def stop_until_next_task(self, valve_id):
        data = {
            "id": str(uuid.uuid1()),
            "type": "VALVE_CONTROL",
            "attributes": {"command": "STOP_UNTIL_NEXT_TASK"},
        }
        self.location.smart_system.call_smart_system_service(valve_id, data)

    def pause(self, valve_id):
        data = {
            "id": str(uuid.uuid1()),
            "type": "VALVE_CONTROL",
            "attributes": {"command": "PAUSE"},
        }
        self.location.smart_system.call_smart_system_service(valve_id, data)

    def unpause(self, valve_id):
        data = {
            "id": str(uuid.uuid1()),
            "type": "VALVE_CONTROL",
            "attributes": {"command": "UNPAUSE"},
        }
        self.location.smart_system.call_smart_system_service(valve_id, data)
