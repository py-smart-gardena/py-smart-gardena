from gardena.devices.abilities.base_gardena_ability_class import BaseGardenaAbilityClass


class DeviceInfoAbility(BaseGardenaAbilityClass):

    # Ambient temperature
    device_info_abilities = {
        "device_info": {
            "serial_number": "serial_number",
            "version": "version",
            "last_time_online": "last_time_online",
        }
    }

    def __init__(self, smart_system=None, location=None):
        super(DeviceInfoAbility, self).__init__(
            smart_system=smart_system, location=location
        )
        self.register_abilities(self.device_info_abilities)
        self.serial_number = None
        self.version = None
        self.last_time_online = None
