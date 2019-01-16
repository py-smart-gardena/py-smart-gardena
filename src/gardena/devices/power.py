import datetime

from gardena.devices.abilities.device_info import DeviceInfoAbility
from gardena.devices.abilities.firmware import FirmwareAbility
from gardena.devices.abilities.radio import RadioAbility


class Power(DeviceInfoAbility, RadioAbility, FirmwareAbility):
    """Class to communicate with a water control device"""

    power_abilities = {
        "power_power": {"power_timer": "power_timer", "error": "power_error"}
    }

    def __init__(self, smart_system=None, location=None):
        super(Power, self).__init__(smart_system=smart_system, location=location)
        self.register_abilities(self.power_abilities)
        self.power_timer = None
        self.power_error = None

    def call_power_property(self, value):
        d = datetime.datetime.now(datetime.timezone.utc)
        self.call_property_command(
            "power",
            "power_timer",
            {
                "properties": {
                    "name": "power_timer",
                    "value": value,
                    "timestamp": d.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    "at_bound": None,
                    "unit": None,
                    "writeable": True,
                    "supported_values": [],
                    "ability": "cba0b804-da73-3aa4-a198-203631d7ca7d",
                }
            },
        )
        # bdd9a0cf-b596-3afa-b838-1c2f0ece7c3d

    def power_on(self, duration=None):
        value = duration if duration is not None else "on"
        self.call_power_property(value)

    def power_off(self):
        self.call_power_property("off")

    def get_all_info(self):
        values = {"power_timer": self.power_timer, "power_error": self.power_error}
        return {**values, **super(Power, self).get_all_info()}
