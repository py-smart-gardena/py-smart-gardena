from gardena.devices.abilities.base_gardena_ability_class import BaseGardenaAbilityClass


class RechargeableBatteryAbility(BaseGardenaAbilityClass):

    # Battery specific fields
    battery_level = None
    battery_status = None
    battery_charging = False
    battery_status = None
    rechargeable_abilities = {
        "battery_power": {
            "level": "battery_level",
            "disposable_battery_status": "battery_status",
            "rechargable_battery_status": "battery_status",
            "charging": "battery_charging",
        }
    }

    def __init__(self, smart_system=None, location=None):
        super(RechargeableBatteryAbility, self).__init__(
            smart_system=smart_system, location=location
        )
        self.register_abilities(self.rechargeable_abilities)
