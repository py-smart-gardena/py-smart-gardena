from gardena.base_gardena_class import BaseGardenaClass
from .services.service import Service

supported_devices_types = {"VALVE_SET", "POWER_SOCKET", "MOWER", "SENSOR"}


class Device(BaseGardenaClass):
    """Keep informations about gardena devices"""

    def __init__(self, smart_system):
        self.data = {}
        self.services = {}
        self.type = "UNKNOWN"
        self.commons = {}
        self.smart_system = smart_system

    def update_data(self, message):
        self._update_field_if_exists(self.data, "id", message["id"])

    def update_service(self, message):
        if message["type"] == "COMMON":
            self.commons = message["attributes"]
        else:
            if message["type"] not in self.services:
                self.services[message["type"]] = {}
                if message["type"] in supported_devices_types:
                    self.type = message["type"]
            if message["id"] not in self.services[message["type"]]:
                self.services[message["type"]][message["id"]] = Service()
                self.services[message["type"]][message["id"]].type = message["type"]
            self.services[message["type"]][message["id"]].update_service(message)

    def call_service(self, service_id, data):
        self.smart_system.call_smart_system_service(service_id, data)
