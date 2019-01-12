from gardena.devices.abilities.base_gardena_ability_class import BaseGardenaAbilityClass


class DeviceInfoAbility(BaseGardenaAbilityClass):

    # Ambient temperature
    device_info_abilities = {
        "device_info": {
            "serial_number": "serial_number",
            "version": "version",
            "last_time_online": "last_time_online",
            "sgtin": "sgtin",
            "manufacturer": "manufacturer",
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
        self.sgtin = None
        self.manufacturer = None

    def get_all_info(self):
        values = {
            "serial_number": self.serial_number,
            "version": self.version,
            "last_time_online": self.last_time_online,
            "sgtin": self.sgtin,
            "manufacturer": self.manufacturer,
        }
        return {**super(DeviceInfoAbility, self).get_all_info(), **values}
