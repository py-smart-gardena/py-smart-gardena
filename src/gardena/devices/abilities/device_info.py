from gardena.devices.base_gardena_device_class import BaseGardenaDeviceClass


class DeviceInfoAbility(BaseGardenaDeviceClass):

    # Ambient temperature
    serial_number = None
    version = None
    last_time_online = None

    def __init__(self, smart_system=None, location=None):
        super(DeviceInfoAbility, self).__init__(
            smart_system=smart_system, location=location
        )
        self.register_abilities(
            {
                "device_info": {
                    "serial_number": "serial_number",
                    "version": "version",
                    "last_time_online": "last_time_online",
                }
            }
        )
