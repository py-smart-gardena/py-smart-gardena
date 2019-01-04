from gardena.base_gardena_device_class import BaseGardenaDeviceClass


class Mower(BaseGardenaDeviceClass):
    """Class to communicate with a mower"""

    """Used to map data between 'mower' ability fields and class fields"""
    mower_ability_fields = {}

    def update_information(self, information):
        super(Mower, self).update_information(information)
        self.set_field_if_exists(
            information, "configuration_synchronized", "is_configuration_synchronized"
        )
        self.set_field_if_exists(information, "device_state", "device_state")
        if "abilities" in information:
            self.handle_abilities(information["abilities"])

    def update_specific_device_info(self, device_specific_information):
        if device_specific_information["type"] == "robotic_mower":
            self.set_ability_field(
                device_specific_information, self.mower_ability_fields
            )
