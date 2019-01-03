from gardena.base_gardena_device import BaseGardenaClass


class Gateway(BaseGardenaClass):
    """Class to hold informations about gateways"""

    def get_description(self):
        return self.api_information["description"]

    def get_category(self):
        return self.api_information["category"]

    def get_configuration_synchronized(self):
        return self.api_information["configuration_synchronized"]
