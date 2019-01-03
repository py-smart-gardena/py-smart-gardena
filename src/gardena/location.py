from gardena.base_gardena_device import BaseGardenaClass


class Location(BaseGardenaClass):
    """Keep informations about gardena locations (gardens, ..)"""

    def get_id(self):
        return self.api_information["id"]

    def get_name(self):
        return self.api_information["name"]
