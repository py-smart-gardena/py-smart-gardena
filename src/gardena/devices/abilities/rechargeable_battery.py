from gardena.devices.base_gardena_device_class import BaseGardenaDeviceClass


class RechargeableBatteryAbility(BaseGardenaDeviceClass):

    # Battery specific fields
    battery_level = None
    battery_status = None
    battery_charging = False
    battery_status = None

    def __init__(self, smart_system=None, location=None):
        super(RechargeableBatteryAbility, self).__init__(
            smart_system=smart_system, location=location
        )
        self.register_abilities(
            {
                "battery_power": {
                    "level": "battery_level",
                    "disposable_battery_status": "battery_status",
                    "rechargable_battery_status": "battery_status",
                    "charging": "battery_charging",
                }
            }
        )
