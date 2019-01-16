from gardena.devices.abilities.ambient_temperature_sensor import (
    AmbientTemperatureSensorAbility,
)
from gardena.devices.abilities.device_info import DeviceInfoAbility
from gardena.devices.abilities.disposable_battery import DisposableBatteryAbility
from gardena.devices.abilities.firmware import FirmwareAbility
from gardena.devices.abilities.radio import RadioAbility


class WaterControl(
    AmbientTemperatureSensorAbility,
    DisposableBatteryAbility,
    RadioAbility,
    DeviceInfoAbility,
    FirmwareAbility,
):
    """Class to communicate with a water control device"""

    watering_abilities = {
        "watering_outlet": {
            "valve_open": "watering_valve_open",
            "manual_override": "watering_manual_override",
        }
    }

    def __init__(self, smart_system=None, location=None):
        super(WaterControl, self).__init__(smart_system=smart_system, location=location)
        self.register_abilities(self.watering_abilities)
        self.watering_valve_open = None
        self.watering_manual_override = None

    def open_valve(self, duration=30):
        self.call_ability_command(
            "outlet",
            {
                "name": "manual_override",
                "parameters": {"manual_override": "open", "duration": duration},
            },
        )

    def close_valve(self):
        self.call_ability_command(
            "outlet", {"name": "cancel_override", "parameters": {}}
        )

    def get_all_info(self):
        values = {
            "watering_valve_open": self.watering_valve_open,
            "watering_manual_override": self.watering_manual_override,
        }
        return {**values, **super(WaterControl, self).get_all_info()}
