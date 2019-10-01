from .base_gardena_class import BaseGardenaClass


class Location(BaseGardenaClass):
    """Keep informations about gardena locations (gardens, ..) and devices"""

    id = "N/A"
    name = "N/A"
    devices = {}

    def __init__(self, smart_system, location):
        self.smart_system = smart_system
        self.update_location_data(location)

    def update_location_data(self, location):
        self.id = location["id"]
        self.name = location["attributes"]["name"]

    def add_device(self, device):
        self.devices[device.id] = device

    def find_device_by_type(self, device_type):
        devices = []
        for device in self.devices.values():
            if device.type == device_type:
                devices.append(device)
        return devices
