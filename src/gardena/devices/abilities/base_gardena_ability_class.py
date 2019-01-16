from gardena.base_gardena_class import BaseGardenaClass


class BaseGardenaAbilityClass(BaseGardenaClass):
    """Base class for Gardena devices"""

    abilities = {}

    def __init__(self, smart_system=None, location=None):
        """Constructor, create instance of a gardena location"""
        super(BaseGardenaAbilityClass, self).__init__(smart_system)
        if location is None:
            raise ValueError("Argument 'location' is missing")
        self.location = location
        self.description = None
        self.category = None
        self.device_state = None
        self.is_configuration_synchronized = False

    def handle_abilities(self, abilities):
        for ability in abilities:
            if ability["type"] in self.abilities:
                self.set_ability_field(ability, self.abilities[ability["type"]])

    def register_abilities(self, abilities):
        for ability, ability_description in abilities.items():
            self.abilities[ability] = ability_description

    def set_ability_field(self, hashmap, fields_hashmap):
        for prop in hashmap["properties"]:
            if prop["name"] in fields_hashmap:
                setattr(self, fields_hashmap[prop["name"]], prop["value"])

    def update_information(self, information):
        super(BaseGardenaAbilityClass, self).update_information(information)
        self.set_field_if_exists(information, "description", "description")
        self.set_field_if_exists(information, "category", "category")
        self.set_field_if_exists(information, "device_state", "device_state")
        self.set_field_if_exists(
            information, "configuration_synchronized", "is_configuration_synchronized"
        )
        if "abilities" in information:
            self.handle_abilities(information["abilities"])

    def call_ability_command(self, command, data):
        url = (
            "https://smart.gardena.com/sg-1/devices/"
            + self.id
            + "/abilities/"
            + command
            + "/command?locationId="
            + self.location.id
        )
        self.smart_system.call_smart_system(url=url, request_type="post", data=data)

    def call_property_command(self, command, property_command, data):
        url = (
            "https://smart.gardena.com/sg-1/devices/"
            + self.id
            + "/abilities/"
            + command
            + "/properties/"
            + property_command
            + "?locationId="
            + self.location.id
        )
        self.smart_system.call_smart_system(url=url, request_type="put", data=data)

    def get_all_info(self):
        values = {
            "description": self.description,
            "category": self.category,
            "is_configuration_synchronized": self.is_configuration_synchronized,
            "device_state": self.device_state,
        }
        return {**super(BaseGardenaAbilityClass, self).get_all_info(), **values}
