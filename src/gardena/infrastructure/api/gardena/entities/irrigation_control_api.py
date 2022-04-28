from gardena.domain.entities.smart_irrigation_control import IrrigationControl
from gardena.infrastructure.api.gardena.entities.gardena_base_device_api import (
    GardenaBaseDeviceApi,
)


class SmartIrrigationControlApi(GardenaBaseDeviceApi):
    def __init__(self, device_map):
        GardenaBaseDeviceApi.__init__(self)
        self.device_map = device_map
        self.valve_set_id = "N/A"
        self.valve_set_state = "N/A"
        self.valve_set_last_error_code = "N/A"
        self.valves = {}
        self.setup_values_from_device_map(device_map)

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

    def toDomainObject(self):
        return IrrigationControl(
            id=self.id,
            name=self.name,
            rf_link_level=self.rf_link_level,
            rf_link_state=self.rf_link_state,
            serial=self.serial,
            model_type=self.model_type,
            valve_set_id=self.valve_set_id,
            valve_set_state=self.valve_set_state,
            valve_set_last_error_code=self.valve_set_last_error_code,
            valves=self.valves,
        )
