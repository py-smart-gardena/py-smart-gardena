from gardena.base_gardena_class import BaseGardenaClass


class Gateway(BaseGardenaClass):
    """Class to hold informations about gateways"""

    description = None
    category = None
    is_configuration_synchronized = None
    ip_address = None
    timezone = None
    serial_number = None
    version = None
    last_time_online = None

    def update_information(self, information):
        super(Gateway, self).update_information(information)
        self.description = information["description"]
        self.category = information["category"]
        self.is_configuration_synchronized = information["configuration_synchronized"]
        for ability in information["abilities"]:
            if ability["type"] == "device_info":
                self.update_gateway_device_info(ability)
            if ability["type"] == "gateway":
                self.update_gateway_ability(ability)

    def update_gateway_ability(self, ability):
        for prop in ability["properties"]:
            if prop["name"] == "ip_address":
                self.ip_address = prop["value"]
            elif prop["name"] == "time_zone":
                self.timezone = prop["value"]

    def update_gateway_device_info(self, ability):
        for prop in ability["properties"]:
            if prop["name"] == "serial_number":
                self.serial_number = prop["value"]
            elif prop["name"] == "version":
                self.version = prop["value"]
            elif prop["name"] == "last_time_online":
                self.last_time_online = prop["value"]
