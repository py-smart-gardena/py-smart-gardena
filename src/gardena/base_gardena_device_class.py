from gardena.base_gardena_class import BaseGardenaClass


class BaseGardenaDeviceClass(BaseGardenaClass):
    """Base class for Gardena devices"""

    description = None
    category = None
    is_configuration_synchronized = False

    """Used to map data between 'device_info' ability fields and class fields"""
    device_info_ability_fields = {
        "serial_number": "serial_number",
        "version": "version",
        "last_time_online": "last_time_online",
    }

    def handle_abilities(self, abilities):
        for ability in abilities:
            if ability["type"] == "device_info":
                self.set_ability_field(ability, self.device_info_ability_fields)
            else:
                self.update_specific_device_info(ability)

    def update_specific_device_info(self, device_specific_information):
        pass

    def set_ability_field(self, hashmap, fields_hashmap):
        for prop in hashmap["properties"]:
            if prop["name"] in fields_hashmap:
                setattr(self, fields_hashmap[prop["name"]], prop["value"])

    def update_information(self, information):
        super(BaseGardenaDeviceClass, self).update_information(information)
        self.set_field_if_exists(information, "description", "description")
        self.set_field_if_exists(information, "category", "category")
        self.set_field_if_exists(
            information, "configuration_synchronized", "is_configuration_synchronized"
        )
