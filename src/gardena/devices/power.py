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
                    "ability": "bdd9a0cf-b596-3afa-b838-1c2f0ece7c3d",
                }
            },
        )
        # bdd9a0cf-b596-3afa-b838-1c2f0ece7c3d
        # cba0b804-da73-3aa4-a198-203631d7ca7d

    def power_on(self, duration=None):
        value = duration if duration is not None else "on"
        self.call_power_property(value)

    def power_off(self):
        self.call_power_property("off")

    def refresh_link_status(self):
        # https://sg-api.dss.husqvarnagroup.net/sg-1/devices/c6e981e9-8ec6-438f-b400-c720d7f313c8/abilities/radio/command?locationId=753aecac-4c46-440e-aa96-d92436a11e77
        #     * {"name":"measure_rf_link","parameters":{}}
        self.call_ability_command(
            "radio", {"name": "measure_rf_link", "parameters": {}}
        )

    def get_all_info(self):
        values = {"power_timer": self.power_timer, "power_error": self.power_error}
        return {**values, **super(Power, self).get_all_info()}
