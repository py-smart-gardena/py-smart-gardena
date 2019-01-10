from gardena.devices.abilities.base_gardena_ability_class import BaseGardenaAbilityClass


class RechargeableBatteryAbility(BaseGardenaAbilityClass):

    # Battery specific fields
    rechargeable_abilities = {
        "battery_power": {
            "level": "battery_level",
            "rechargable_battery_status": "battery_status",
            "charging": "battery_charging",
        }
    }

    def __init__(self, smart_system=None, location=None):
        super(RechargeableBatteryAbility, self).__init__(
            smart_system=smart_system, location=location
        )
        self.register_abilities(self.rechargeable_abilities)
        self.battery_level = None
        self.battery_status = None
        self.battery_charging = False

    def get_all_info(self):
        values = {
            "battery_level": self.battery_level,
            "battery_status": self.battery_status,
            "battery_charging": self.battery_charging,
        }
        return {**super(RechargeableBatteryAbility, self).get_all_info(), **values}
