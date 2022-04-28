from gardena.infrastructure.api.gardena.entities.gardena_mower_api import (
    GardenaMowerApi,
)
from gardena.infrastructure.api.gardena.entities.gardena_power_socket_api import (
    GardenaPowerSocketApi,
)
from gardena.infrastructure.api.gardena.entities.gardena_sensor_api import (
    GardenaSensorApi,
)
from gardena.infrastructure.api.gardena.entities.gardena_smart_irrigation_control_api import (
    GardenaSmartIrrigationControlApi,
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
            if len(device_map["VALVE"]) > 1:
                return GardenaSmartIrrigationControlApi(device_map)
        #     else:
        #         return WaterControl(smart_system, device_map)
        # elif "POWER_SOCKET" in device_map:
        #     return PowerSocket(smart_system, device_map)
