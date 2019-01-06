from gardena.devices.abilities.device_info import DeviceInfoAbility
from gardena.devices.abilities.radio import RadioAbility


class Gateway(RadioAbility, DeviceInfoAbility):
    """Class to hold informations about gateways"""

    ip_address = None
    timezone = None

    gateway_abilities = {
        "gateway": {"ip_address": "ip_address", "time_zone": "timezone"}
    }

    def __init__(self, smart_system=None, location=None):
        super(Gateway, self).__init__(smart_system=smart_system, location=location)
        self.register_abilities(self.gateway_abilities)
