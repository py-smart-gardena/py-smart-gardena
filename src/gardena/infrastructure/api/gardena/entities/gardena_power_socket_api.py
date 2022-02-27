from gardena.domain.entities.power_socket import PowerSocket
from gardena.infrastructure.api.gardena.entities.gardena_base_device_api import (
    GardenaBaseDeviceApi,
)


class GardenaPowerSocketApi(GardenaBaseDeviceApi):
    def __init__(self, device_map):
        GardenaBaseDeviceApi.__init__(self)
        self.device_map = device_map
        self.activity = "N/A"
        self.state = "N/A"
        self.last_error_code = "N/A"
        self.setup_values_from_device_map(device_map)

    def update_device_specific_data(self, device_map):
        # Mower has only one item
        if device_map["type"] == "POWER_SOCKET":
            self.id = device_map["id"]
            self.set_attribute_value("activity", device_map, "activity")
            self.set_attribute_value("state", device_map, "state")
            self.set_attribute_value("last_error_code", device_map, "lastErrorCode")

    def toDomainObject(self):
        return PowerSocket(
            id=self.id,
            name=self.name,
            rf_link_level=self.rf_link_level,
            rf_link_state=self.rf_link_state,
            serial=self.serial,
            model_type=self.model_type,
            activity=self.activity,
            state=self.state,
            last_error_code=self.last_error_code,
        )
