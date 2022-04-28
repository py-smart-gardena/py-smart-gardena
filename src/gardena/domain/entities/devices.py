from gardena.domain.entities.device_type import DeviceType
from gardena.domain.entities.mower import Mower
from gardena.domain.entities.power_socket import PowerSocket
from gardena.domain.entities.sensor import Sensor
from gardena.domain.entities.smart_irrigation_control import IrrigationControl


class Devices:
    def __init__(
        self,
        mowers: [Mower] = [],
        power_sockets: [PowerSocket] = [],
        sensors: [Sensor] = [],
        smart_irrigation_controls: [IrrigationControl] = [],
    ):
        self.mowers: [Mower] = mowers
        self.power_sockets: [PowerSocket] = power_sockets
        self.sensors: [Sensor] = sensors
        self.irrigation_controls: [
            IrrigationControl
        ] = smart_irrigation_controls

    def add_device(self, device):
        if device.type == DeviceType.MOWER:
            self.mowers.append(device)
        elif device.type == DeviceType.POWER_SOCKET:
            self.power_sockets.append(device)
        elif device.type == DeviceType.SENSOR:
            self.sensors.append(device)
        elif device.type == DeviceType.SMART_IRRIGATION_CONTROL:
            self.irrigation_controls.append(device)
