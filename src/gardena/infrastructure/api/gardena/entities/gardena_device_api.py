class GardenaDeviceApi:
    supported_services = [
        "COMMON",
        "VALVE",
        "VALVE_SET",
        "SENSOR",
        "MOWER",
        "POWER_SOCKET",
        "DEVICE",
    ]

    def __init__(self, device):
        if device["type"] in self.supported_services:
            self.type = device["type"]
            self.id = device["id"].split(":")[0]
            self.gardena_device = device
        else:
            self.type = None
            self.id = None
            self.gardena_device = None
