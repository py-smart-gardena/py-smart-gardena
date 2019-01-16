from gardena.devices.abilities.ambient_temperature_sensor import (
    AmbientTemperatureSensorAbility,
)
from gardena.devices.abilities.device_info import DeviceInfoAbility
from gardena.devices.abilities.disposable_battery import DisposableBatteryAbility
from gardena.devices.abilities.firmware import FirmwareAbility
from gardena.devices.abilities.radio import RadioAbility


class Sensor(
    AmbientTemperatureSensorAbility,
    DisposableBatteryAbility,
    RadioAbility,
    DeviceInfoAbility,
    FirmwareAbility,
):
    """Class to communicate with a sensor"""

    """Used to map data between 'sensor' ability fields and class fields"""
    soil_temperature_sensor_ability_fields = {"temperature": "sensor_soil_temperature"}

    soil_humidity_sensor_ability_fields = {"humidity": "sensor_soil_humidity"}

    light_sensor_ability_fields = {"light": "sensor_light"}

    def __init__(self, smart_system=None, location=None):
        super(Sensor, self).__init__(smart_system=smart_system, location=location)
        self.register_abilities(
            {
                "soil_temperature_sensor": self.soil_temperature_sensor_ability_fields,
                "soil_humidity_sensor": self.soil_humidity_sensor_ability_fields,
                "light_sensor": self.light_sensor_ability_fields,
            }
        )
        self.sensor_soil_temperature = None
        self.sensor_soil_humidity = None
        self.sensor_light = None

    def refresh_ambient_temperature(self):
        self.call_ability_command(
            "ambient_temperature",
            {"name": "measure_ambient_temperature", "parameters": {}},
        )

    def refresh_light_intensity(self):
        self.call_ability_command("light", {"name": "measure_light", "parameters": {}})

    def refresh_soil_moisture(self):
        self.call_ability_command(
            "humidity", {"name": "measure_soil_humidity", "parameters": {}}
        )

    def get_all_info(self):
        values = {
            "sensor_soil_temperature": self.sensor_soil_temperature,
            "sensor_soil_humidity": self.sensor_soil_humidity,
            "sensor_light": self.sensor_light,
        }
        return {**values, **super(Sensor, self).get_all_info()}
