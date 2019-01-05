from gardena.base_gardena_class import BaseGardenaClass


class BaseGardenaDeviceClass(BaseGardenaClass):
    """Base class for Gardena devices"""

    # Common fields
    description = None
    category = None
    is_configuration_synchronized = False
    serial_number = None
    version = None
    last_time_online = None
    # Battery specific fields
    battery_level = None
    battery_status = None
    battery_charging = False
    # Radio fields
    radio_quality = None
    radio_connection_status = None
    radio_state = None
    device_state = None
    # Ambient temperature
    ambient_temperature = None
    frost_warning = None
    firmware_status = None

    """Used to map data between 'device_info' ability fields and class fields"""
    device_info_ability_fields = {
        "serial_number": "serial_number",
        "version": "version",
        "last_time_online": "last_time_online",
    }

    battery_ability_fields = {
        "level": "battery_level",
        "rechargable_battery_status": "battery_status",
        "charging": "battery_charging",
        "disposable_battery_status": "battery_status",
    }

    radio_ability_fields = {
        "quality": "radio_quality",
        "connection_status": "radio_connection_status",
        "state": "radio_state",
    }

    ambient_temperature_ability_fields = {
        "temperature": "ambient_temperature",
        "frost_warning": "frost_warning",
    }

    firmware_ability_fields = {"firmware_status": "firmware_status"}

    device_ability_type_maps = {
        "device_info": device_info_ability_fields,
        "battery_power": battery_ability_fields,
        "radio_link": radio_ability_fields,
        "ambient_temperature_sensor": ambient_temperature_ability_fields,
        "firmware": firmware_ability_fields,
    }

    def handle_abilities(self, abilities):
        for ability in abilities:
            if ability["type"] in self.device_ability_type_maps:
                self.set_ability_field(
                    ability, self.device_ability_type_maps[ability["type"]]
                )
            else:
                self.update_specific_device_info(ability)

    def update_specific_device_info(self, device_specific_information):
        map = self.get_device_specific_ability_type_maps()
        if device_specific_information["type"] in map:
            self.set_ability_field(
                device_specific_information, map[device_specific_information["type"]]
            )

    def get_device_specific_ability_type_maps(self):
        return {}

    def set_ability_field(self, hashmap, fields_hashmap):
        for prop in hashmap["properties"]:
            if prop["name"] in fields_hashmap:
                setattr(self, fields_hashmap[prop["name"]], prop["value"])

    def update_information(self, information):
        super(BaseGardenaDeviceClass, self).update_information(information)
        self.set_field_if_exists(information, "description", "description")
        self.set_field_if_exists(information, "category", "category")
        self.set_field_if_exists(information, "device_state", "device_state")
        self.set_field_if_exists(
            information, "configuration_synchronized", "is_configuration_synchronized"
        )
        if "abilities" in information:
            self.handle_abilities(information["abilities"])
