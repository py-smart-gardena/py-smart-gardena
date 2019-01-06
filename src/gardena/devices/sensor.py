from gardena.devices.base_gardena_device_class import BaseGardenaDeviceClass


class Sensor(BaseGardenaDeviceClass):
    """Class to communicate with a sensor"""

    sensor_soil_temperature = None
    sensor_soil_humidity = None
    sensor_light = None

    """Used to map data between 'sensor' ability fields and class fields"""
    soil_temperature_sensor_ability_fields = {"temperature": "sensor_soil_temperature"}

    soil_humidity_sensor_ability_fields = {"humidity": "sensor_soil_humidity"}

    light_sensor_ability_fields = {"light": "sensor_light"}

    sensor_ability_type_maps = {
        "soil_temperature_sensor": soil_temperature_sensor_ability_fields,
        "soil_humidity_sensor": soil_humidity_sensor_ability_fields,
        "light_sensor": light_sensor_ability_fields,
    }

    def get_device_specific_ability_type_maps(self):
        return self.sensor_ability_type_maps

    def refresh_ambient_temperature(self):
        data = {"name": "measure_ambient_temperature", "parameters": {}}
        self.smart_system.call_smart_system(
            url=self.get_ability_command_url("ambient_temperature"),
            request_type="post",
            data=data,
        )

    def refresh_light_intensity(self):
        data = {"name": "measure_light", "parameters": {}}
        self.smart_system.call_smart_system(
            url=self.get_ability_command_url("light"), request_type="post", data=data
        )

    def refresh_soil_moisture(self):
        data = {"name": "measure_soil_humidity", "parameters": {}}
        self.smart_system.call_smart_system(
            url=self.get_ability_command_url("humidity"), request_type="post", data=data
        )
