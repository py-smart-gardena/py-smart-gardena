class BaseGardenaClass:
    """Base class for information retrieved by gardena"""

    id = None
    name = None

    """Used to map data between 'device_info' ability fields and class fields"""
    device_info_ability_fields = {
        "serial_number": "serial_number",
        "version": "version",
        "last_time_online": "last_time_online",
    }

    def __init__(self, smart_system=None):
        """Constructor, create instance of a gardena device"""
        if smart_system is None:
            raise ValueError("Argument 'smart_system' is missing")
        self.smart_system = smart_system

    def set_field_if_exists(self, hashmap, hashmap_key, field_name):
        if hashmap_key in hashmap:
            setattr(self, field_name, hashmap[hashmap_key])

    def update_information(self, information):
        self.set_field_if_exists(information, "id", "id")
        self.set_field_if_exists(information, "name", "name")

    def update_specific_device_info(self, device_specific_information):
        pass

    def handle_abilities(self, abilities):
        for ability in abilities:
            if ability["type"] == "device_info":
                self.set_ability_field(ability, self.device_info_ability_fields)
            else:
                self.update_specific_device_info(ability)

    def set_ability_field(self, hashmap, fields_hashmap):
        for prop in hashmap["properties"]:
            if prop["name"] in fields_hashmap:
                setattr(self, fields_hashmap[prop["name"]], prop["value"])
