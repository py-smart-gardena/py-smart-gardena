from gardena.devices.base_gardena_device_class import BaseGardenaDeviceClass


class AmbientTemperatureSensorAbility(BaseGardenaDeviceClass):

    # Ambient temperature
    ambient_temperature = None
    frost_warning = None

    def __init__(self, smart_system=None, location=None):
        super(AmbientTemperatureSensorAbility, self).__init__(
            smart_system=smart_system, location=location
        )
        self.register_abilities(
            {
                "ambient_temperature_sensor": {
                    "temperature": "ambient_temperature",
                    "frost_warning": "frost_warning",
                }
            }
        )
