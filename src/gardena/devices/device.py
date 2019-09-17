from gardena.base_gardena_class import BaseGardenaClass
from .services.service import Service


class Device(BaseGardenaClass):
    """Keep informations about gardena devices"""

    def __init__(self):
        self.data = {}
        self.services = {}

    def update_data(self, message):
        self._update_field_if_exists(self.data, "id", message["id"])

    def update_service(self, message):
        if message["type"] not in self.services:
            self.services[message["type"]] = {}
        if message["id"] not in self.services[message["type"]]:
            self.services[message["type"]][message["id"]] = Service()
            self.services[message["type"]][message["id"]].type = message["type"]
        self.services[message["type"]][message["id"]].update_service(message)
