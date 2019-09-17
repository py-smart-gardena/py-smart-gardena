from .base_gardena_class import BaseGardenaClass
from gardena.devices.device import Device


class Location(BaseGardenaClass):
    """Keep informations about gardena locations (gardens, ..) and devices"""

    def __init__(self):
        self.data = {}
        self.devices = {}

    def update_data(self, message):
        self._update_field_if_exists(self.data, "id", message["id"])
        self._update_field_if_exists(self.data, "name", message["attributes"]["name"])

    def update_device(self, device):
        if device["id"] not in self.devices:
            self.devices[device["id"]] = Device()
        self.devices[device["id"]].update_data(device)

    def __str__(self):
        str = '{"data" : {'
        for key, value in self.data.items():
            str += f'"{key}":{value}, '
        str += "}}, "
        str += '{"devices" : {'
        for key, value in self.devices.items():
            str += f'"{key}":{value}, '
        str += "}}"
        return str
