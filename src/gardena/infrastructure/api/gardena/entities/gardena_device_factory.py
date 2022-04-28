from gardena.infrastructure.api.gardena.entities.gardena_mower_api import (
    GardenaMowerApi,
)
from gardena.infrastructure.api.gardena.entities.gardena_power_socket_api import (
    GardenaPowerSocketApi,
)
from gardena.infrastructure.api.gardena.entities.gardena_sensor_api import (
    GardenaSensorApi,
)
from gardena.infrastructure.api.gardena.entities.irrigation_control_api import (
    SmartIrrigationControlApi,
)


class GardenaDeviceFactory:
    @staticmethod
    def build(device_map):
        if "MOWER" in device_map:
            return GardenaMowerApi(device_map)
        elif "POWER_SOCKET" in device_map:
            return GardenaPowerSocketApi(device_map)
        elif "SENSOR" in device_map:
            return GardenaSensorApi(device_map)
        elif "VALVE" in device_map:
            return SmartIrrigationControlApi(device_map)
