from gardena.devices.abilities.base_gardena_ability_class import BaseGardenaAbilityClass


class DisposableBatteryAbility(BaseGardenaAbilityClass):

    # Battery specific fields
    disposable_battery_abilities = {
        "battery_power": {
            "level": "battery_level",
            "disposable_battery_status": "battery_status",
        }
    }

    def __init__(self, smart_system=None, location=None):
        super(DisposableBatteryAbility, self).__init__(
            smart_system=smart_system, location=location
        )
        self.register_abilities(self.disposable_battery_abilities)
        self.battery_level = None
        self.battery_status = None
