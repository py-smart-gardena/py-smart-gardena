from gardena.base_gardena_class import BaseGardenaClass


class Location(BaseGardenaClass):
    """Keep informations about gardena locations (gardens, ..)"""

    def get_devices(self):
        return self.api_information["devices"]
