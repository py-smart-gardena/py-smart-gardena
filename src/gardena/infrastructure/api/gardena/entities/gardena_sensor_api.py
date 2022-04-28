from gardena.domain.entities.sensor import Sensor
from gardena.infrastructure.api.gardena.entities.gardena_base_device_api import (
    GardenaBaseDeviceApi,
)


class GardenaSensorApi(GardenaBaseDeviceApi):
    def __init__(self, device_map):
        GardenaBaseDeviceApi.__init__(self)
        self.device_map = device_map
        self.ambient_temperature = "N/A"
        self.light_intensity = "N/A"
        self.soil_humidity = "N/A"
        self.soil_temperature = "N/A"
        self.battery_level = "N/A"
        self.battery_state = "N/A"
        self.setup_values_from_device_map(device_map)

    def update_device_specific_data(self, device_map):
        if device_map["type"] == "SENSOR":
            # Sensor has only one item
            self.set_attribute_value(
                "ambient_temperature", device_map, "ambientTemperature"
            )
            self.set_attribute_value("light_intensity", device_map, "lightIntensity")
            self.set_attribute_value("soil_humidity", device_map, "soilHumidity")
            self.set_attribute_value("soil_temperature", device_map, "soilTemperature")

    def toDomainObject(self):
        return Sensor(
            id=self.id,
            name=self.name,
            rf_link_level=self.rf_link_level,
            rf_link_state=self.rf_link_state,
            serial=self.serial,
            model_type=self.model_type,
            battery_level=self.battery_level,
            battery_state=self.battery_state,
            callbacks=[],
            ambient_temperature=self.ambient_temperature,
            light_intensity=self.light_intensity,
            soil_humidity=self.soil_humidity,
            soil_temperature=self.soil_temperature,
        )
