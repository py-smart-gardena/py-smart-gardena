from gardena.base_gardena_device_class import BaseGardenaDeviceClass


class Mower(BaseGardenaDeviceClass):
    """Class to communicate with a mower"""

    internal_temperature = None

    """Used to map data between 'mower' ability fields and class fields"""
    mower_ability_fields = {}

    temperature_ability_fields = {"temperature": "internal_temperature"}

    def update_information(self, information):
        super(Mower, self).update_information(information)
        if "abilities" in information:
            self.handle_abilities(information["abilities"])

    def update_specific_device_info(self, device_specific_information):
        if device_specific_information["type"] == "robotic_mower":
            self.set_ability_field(
                device_specific_information, self.mower_ability_fields
            )
        elif device_specific_information["type"] == "internal_temperature_sensor":
            self.set_ability_field(
                device_specific_information, self.temperature_ability_fields
            )
