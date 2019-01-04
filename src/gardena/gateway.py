from gardena.base_gardena_device_class import BaseGardenaDeviceClass


class Gateway(BaseGardenaDeviceClass):
    """Class to hold informations about gateways"""

    is_configuration_synchronized = None
    ip_address = None
    timezone = None
    serial_number = None
    version = None
    last_time_online = None
    device_state = None

    """Used to map data between 'gateway' ability fields and class fields"""
    gateway_ability_fields = {"ip_address": "ip_address", "time_zone": "timezone"}

    def update_information(self, information):
        super(Gateway, self).update_information(information)
        self.set_field_if_exists(
            information, "configuration_synchronized", "is_configuration_synchronized"
        )
        self.set_field_if_exists(information, "device_state", "device_state")
        if "abilities" in information:
            self.handle_abilities(information["abilities"])

    def update_specific_device_info(self, device_specific_information):
        if device_specific_information["type"] == "gateway":
            self.set_ability_field(
                device_specific_information, self.gateway_ability_fields
            )
