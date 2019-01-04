from gardena.base_gardena_device_class import BaseGardenaDeviceClass


class Sensor(BaseGardenaDeviceClass):
    """Class to communicate with a sensor"""

    sensor_ambient_temperature = None
    sensor_frost_warning = None
    sensor_soil_temperature = None
    sensor_soil_humidity = None
    sensor_light = None
    firmware_status = None

    """Used to map data between 'mower' ability fields and class fields"""
    ambient_temperature_ability_fields = {
        "temperature": "sensor_ambient_temperature",
        "frost_warning": "sensor_frost_warning",
    }

    soil_temperature_sensor_ability_fields = {"temperature": "sensor_soil_temperature"}

    soil_humidity_sensor_ability_fields = {"humidity": "sensor_soil_humidity"}

    light_sensor_ability_fields = {"light": "sensor_light"}

    firmware_ability_fields = {"firmware_status": "firmware_status"}

    def update_information(self, information):
        super(Sensor, self).update_information(information)
        if "abilities" in information:
            self.handle_abilities(information["abilities"])

    def update_specific_device_info(self, device_specific_information):
        if device_specific_information["type"] == "ambient_temperature_sensor":
            self.set_ability_field(
                device_specific_information, self.ambient_temperature_ability_fields
            )
        elif device_specific_information["type"] == "soil_temperature_sensor":
            self.set_ability_field(
                device_specific_information, self.soil_temperature_sensor_ability_fields
            )
        elif device_specific_information["type"] == "soil_humidity_sensor":
            self.set_ability_field(
                device_specific_information, self.soil_humidity_sensor_ability_fields
            )
        elif device_specific_information["type"] == "light_sensor":
            self.set_ability_field(
                device_specific_information, self.light_sensor_ability_fields
            )
        elif device_specific_information["type"] == "firmware":
            self.set_ability_field(
                device_specific_information, self.firmware_ability_fields
            )
