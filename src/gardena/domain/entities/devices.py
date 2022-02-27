from gardena.domain.entities.device_type import DeviceType
from gardena.domain.entities.mower import Mower
from gardena.domain.entities.power_socket import PowerSocket


class Devices:
    def __init__(self, mowers: [Mower] = [], power_sockets: [PowerSocket] = []):
        self.power_sockets = power_sockets
        self.mowers = mowers

    def add_device(self, device):
        if device.type == DeviceType.MOWER:
            self.mowers.append(device)
        if device.type == DeviceType.POWER_SOCKET:
            self.power_sockets.append(device)
