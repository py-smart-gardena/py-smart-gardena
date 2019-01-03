from gardena.base_gardena_class import BaseGardenaClass


class Gateway(BaseGardenaClass):
    """Class to hold informations about gateways"""

    description = None
    category = None
    is_configuration_synchronized = None

    def update_information(self, information):
        super(Gateway, self).update_information(information)
        self.description = information["description"]
        self.category = information["category"]
        self.is_configuration_synchronized = information["configuration_synchronized"]
