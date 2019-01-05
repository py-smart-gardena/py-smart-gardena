from gardena.devices.base_gardena_device_class import BaseGardenaDeviceClass


class Gateway(BaseGardenaDeviceClass):
    """Class to hold informations about gateways"""

    ip_address = None
    timezone = None

    """Used to map data between 'gateway' ability fields and class fields"""
    gateway_ability_fields = {"ip_address": "ip_address", "time_zone": "timezone"}

    gateway_ability_type_maps = {"gateway": gateway_ability_fields}

    def get_device_specific_ability_type_maps(self):
        return self.gateway_ability_type_maps
