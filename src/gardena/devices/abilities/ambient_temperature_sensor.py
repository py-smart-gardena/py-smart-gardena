from gardena.devices.abilities.base_gardena_ability_class import BaseGardenaAbilityClass


class AmbientTemperatureSensorAbility(BaseGardenaAbilityClass):

    # Ambient temperature
    ambient_temperatures_abilities = {
        "ambient_temperature_sensor": {
            "temperature": "ambient_temperature",
            "frost_warning": "frost_warning",
        }
    }

    def __init__(self, smart_system=None, location=None):
        super(AmbientTemperatureSensorAbility, self).__init__(
            smart_system=smart_system, location=location
        )
        self.register_abilities(self.ambient_temperatures_abilities)
        self.ambient_temperature = None
        self.frost_warning = None

    def get_all_info(self):
        values = {
            "ambient_temperature": self.ambient_temperature,
            "radio_connection_status": self.radio_connection_status,
            "frost_warning": self.frost_warning,
        }
        return {**super(AmbientTemperatureSensorAbility, self).get_all_info(), **values}
