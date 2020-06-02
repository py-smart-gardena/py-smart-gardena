from .mower import Mower
from .sensor import Sensor
from .water_control import WaterControl
from .smart_irrigation_control import SmartIrrigationControl
from .power_socket import PowerSocket


class DeviceFactory:
    @staticmethod
    def build(smart_system, device_map):
        if "MOWER" in device_map:
            return Mower(smart_system, device_map)
        elif "SENSOR" in device_map:
            return Sensor(smart_system, device_map)
        elif "POWER_SOCKET" in device_map:
            return PowerSocket(smart_system, device_map)
        elif "VALVE" in device_map:
            if len(device_map["VALVE"]) > 1:
                return SmartIrrigationControl(smart_system, device_map)
            else:
                return WaterControl(smart_system, device_map)
