from gardena.base_gardena_class import BaseGardenaClass
from .services.common import Common
from .services.valve import Valve


class Device(BaseGardenaClass):
    """Keep informations about gardena devices"""

    def __init__(self):
        self.data = {}
        self.services = {}

    def update_data(self, message):
        self._update_field_if_exists(self.data, "id", message["id"])

    def update_service(self, message):
        if message["id"] not in self.services:
            self.services[message["type"]] = self._build_service(message)
        self.services[message["type"]].update_service(message)

    def _build_service(self, message):
        if message["type"] == "COMMON":
            return Common("COMMON")
        elif message["type"] == "VALVE":
            return Valve("VALVE")
        else:
            print(f"message type {message[type]} not handled !")

    def __str__(self):
        str = "{data : {"
        for key, value in self.data.items():
            str += f"{key}:{value}, "
        str += "}}"
        str += "{services : {"
        for key, value in self.services.items():
            str += f"{key}:{value}, "
        str += "}}"
        return str
