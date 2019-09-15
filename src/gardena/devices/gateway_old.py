from gardena.devices.abilities.device_info import DeviceInfoAbility
from gardena.devices.abilities.radio import RadioAbility


class Gateway(RadioAbility, DeviceInfoAbility):
    """Class to hold informations about gateways"""

    gateway_abilities = {
        "gateway": {"ip_address": "ip_address", "time_zone": "timezone"}
    }

    def __init__(self, smart_system=None, location=None):
        super(Gateway, self).__init__(smart_system=smart_system, location=location)
        self.register_abilities(self.gateway_abilities)
        self.ip_address = None
        self.timezone = None

    def get_all_info(self):
        values = {"ip_address": self.ip_address, "timezone": self.timezone}
        return {**values, **super(Gateway, self).get_all_info()}
