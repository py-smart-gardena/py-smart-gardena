from gardena.devices.base_gardena_device_class import BaseGardenaDeviceClass


class DisposableBatteryAbility(BaseGardenaDeviceClass):

    # Battery specific fields
    battery_level = None
    battery_status = None

    def __init__(self, smart_system=None, location=None):
        super(DisposableBatteryAbility, self).__init__(
            smart_system=smart_system, location=location
        )
        self.register_abilities(
            {
                "battery_power": {
                    "level": "battery_level",
                    "disposable_battery_status": "battery_status",
                }
            }
        )
