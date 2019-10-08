from .base_device import BaseDevice


class Sensor(BaseDevice):

    ambient_temperature = "N/A"
    light_intensity = "N/A"
    soil_humidity = "N/A"
    soil_temperature = "N/A"

    def __init__(self, smart_system, device_map):
        BaseDevice.__init__(self, smart_system, device_map)
        self.type = "SENSOR"

    def update_device_specific_data(self, device_map):
        if device_map["type"] == "SENSOR":
            # Sensor has only one item
            self.set_attribute_value(
                "ambient_temperature", device_map, "ambientTemperature"
            )
            self.set_attribute_value("light_intensity", device_map, "lightIntensity")
            self.set_attribute_value("soil_humidity", device_map, "soilHumidity")
            self.set_attribute_value("soil_temperature", device_map, "soilTemperature")
