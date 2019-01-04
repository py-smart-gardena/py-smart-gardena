from gardena.base_gardena_class import BaseGardenaClass


class Gateway(BaseGardenaClass):
    """Class to hold informations about gateways"""

    description = "N/A"
    category = "N/A"
    is_configuration_synchronized = "N/A"
    ip_address = "N/A"
    timezone = "N/A"
    serial_number = "N/A"
    version = "N/A"
    last_time_online = "N/A"

    data_fields = {
        "gateway": {"ip_address": "ip_address", "time_zone": "timezone"},
        "device_info": {
            "serial_number": "serial_number",
            "version": "version",
            "last_time_online": "last_time_online",
        },
    }

    def update_information(self, information):
        super(Gateway, self).update_information(information)
        self.description = information["description"]
        self.category = information["category"]
        self.is_configuration_synchronized = information["configuration_synchronized"]
        for ability in information["abilities"]:
            self.update_property(ability)

    def update_property(self, ability):
        for prop in ability["properties"]:
            if prop["name"] in self.data_fields[ability["type"]]:
                setattr(
                    self, self.data_fields[ability["type"]][prop["name"]], prop["value"]
                )
