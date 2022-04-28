from gardena.domain.entities.mower import Mower
from gardena.infrastructure.api.gardena.entities.gardena_base_device_api import (
    GardenaBaseDeviceApi,
)


class GardenaMowerApi(GardenaBaseDeviceApi):
    def __init__(self, device_map):
        GardenaBaseDeviceApi.__init__(self)
        self.device_map = device_map
        self.activity = "N/A"
        self.operating_hours = "N/A"
        self.state = "N/A"
        self.last_error_code = "N/A"
        self.battery_level = "N/A"
        self.battery_state = "N/A"
        self.setup_values_from_device_map(device_map)

    def update_device_specific_data(self, device_map):
        # Mower has only one item
        if device_map["type"] == "MOWER":
            self.id = device_map["id"]
            self.set_attribute_value("activity", device_map, "activity")
            self.set_attribute_value("operating_hours", device_map, "operatingHours")
            self.set_attribute_value("state", device_map, "state")
            self.set_attribute_value("last_error_code", device_map, "lastErrorCode")

    def toDomainObject(self):
        return Mower(
            id=self.id,
            battery_level=self.battery_level,
            battery_state=self.battery_state,
            name=self.name,
            rf_link_level=self.rf_link_level,
            rf_link_state=self.rf_link_state,
            serial=self.serial,
            model_type=self.model_type,
            activity=self.activity,
            operating_hours=self.operating_hours,
            state=self.state,
            last_error_code=self.last_error_code,
        )
