import uuid

from gardena.domain.entities.base_device import BaseDevice
from gardena.domain.entities.device_type import DeviceType


class SmartIrrigationControl(BaseDevice):
    def __init__(
        self,
        id: str = "None",
        name: str = "N/A",
        rf_link_level: str = "N/A",
        rf_link_state: str = "N/A",
        serial: str = "N/A",
        model_type: str = "N/A",
        callbacks=[],
        valve_set_id: str = "N/A",
        valve_set_state: str = "N/A",
        valve_set_last_error_code: str = "N/A",
        valves: {} = {},
    ):
        """Constructor for the smart irrigation control device."""
        BaseDevice.__init__(
            self,
            id=id,
            name=name,
            rf_link_level=rf_link_level,
            rf_link_state=rf_link_state,
            serial=serial,
            model_type=model_type,
            callbacks=callbacks,
        )
        self.type = DeviceType.SMART_IRRIGATION_CONTROL
        self.valve_set_id = valve_set_id
        self.valve_set_state = valve_set_state
        self.valve_set_last_error_code = valve_set_last_error_code
        self.valves = valves

    def _set_valves_map_value(
        self, target_map, source_map, value_name_in_source, value_name_in_target=None
    ):
        if not value_name_in_target:
            value_name_in_target = value_name_in_source
        if value_name_in_source in source_map:
            target_map[value_name_in_target] = source_map[value_name_in_source]["value"]
        else:
            target_map[value_name_in_target] = "N/A"

    def update_device_specific_data(self, device_map):
        if device_map["type"] == "VALVE_SET":
            # SmartIrrigationControl has only one item
            self.valve_set_id = device_map["id"]
            self.set_attribute_value("valve_set_state", device_map, "state")
            self.set_attribute_value(
                "valve_set_last_error_code", device_map, "lastErrorCode"
            )
        if device_map["type"] == "VALVE":
            self.valves[device_map["id"]] = {"id": device_map["id"]}
            self._set_valves_map_value(
                self.valves[device_map["id"]], device_map["attributes"], "activity"
            )
            self._set_valves_map_value(
                self.valves[device_map["id"]],
                device_map["attributes"],
                "lastErrorCode",
                "last_error_code",
            )
            self._set_valves_map_value(
                self.valves[device_map["id"]], device_map["attributes"], "name"
            )
            self._set_valves_map_value(
                self.valves[device_map["id"]], device_map["attributes"], "state"
            )

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
