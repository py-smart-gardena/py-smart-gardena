from gardena.base_gardena_class import BaseGardenaClass


class BaseGardenaDeviceClass(BaseGardenaClass):
    """Base class for Gardena devices"""

    description = None
    category = None

    def update_information(self, information):
        super(BaseGardenaDeviceClass, self).update_information(information)
        self.set_field_if_exists(information, "description", "description")
        self.set_field_if_exists(information, "category", "category")
