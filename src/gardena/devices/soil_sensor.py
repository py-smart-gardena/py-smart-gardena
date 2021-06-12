from .base_device import BaseDevice


class SoilSensor(BaseDevice):

    def __init__(self, location, device_map):
        """Constructor for the sensor device."""
        BaseDevice.__init__(self, location, device_map["COMMON"][0]["id"])
        self.type = "SOIL_SENSOR"
        self.soil_humidity = "N/A"
        self.soil_temperature = "N/A"
        self.setup_values_from_device_map(device_map)

    def update_device_specific_data(self, device_map):
        if device_map["type"] == "SENSOR":
            # Sensor has only one item
            self.set_attribute_value("soil_humidity", device_map, "soilHumidity")
            self.set_attribute_value("soil_temperature", device_map, "soilTemperature")
