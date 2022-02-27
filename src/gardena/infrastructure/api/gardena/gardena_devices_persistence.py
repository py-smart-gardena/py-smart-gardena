from gardena.domain.entities.devices import Devices
from gardena.domain.entities.location import Location
from gardena.infrastructure.api.gardena.entities.gardena_device_api import (
    GardenaDeviceApi,
)
from gardena.infrastructure.api.gardena.entities.gardena_device_factory import (
    GardenaDeviceFactory,
)
from gardena.infrastructure.api.gardena.gardena_api_client import GardenaApiClient


class GardenaDevicesPersistence:
    def __init__(self, gardena_api: GardenaApiClient):
        self.gardena_api = gardena_api
        self.gardena_api.authenticate()

    def get_devices(self, location: Location) -> Devices:
        response_data = self.gardena_api.call_smart_system_get(
            f"/v1/locations/{location.id}"
        )
        if response_data is not None:
            #  TODO : test if key exists
            if not self.__does_response_contains_any_devices(response_data):
                # XXX : self.logger.error("No device found....")
                return
            devices = Devices()
            devices_by_id = self.__get_devices_by_id(response_data)
            for device in devices_by_id.values():
                device_obj = GardenaDeviceFactory.build(device)
                if device_obj is not None:
                    devices.add_device(device_obj.toDomainObject())
            return devices

    def __does_response_contains_any_devices(self, response):
        return (
            "data" in response
            and "relationships" in response["data"]
            and "devices" in response["data"]["relationships"]
            and "data" in response["data"]["relationships"]["devices"]
            and len(response["data"]["relationships"]["devices"]["data"]) >= 1
        )

    def __get_devices_by_id(self, data):
        devices = {}
        for gardena_device in data["included"]:
            device = GardenaDeviceApi(gardena_device)
            if device.id not in devices:
                devices[device.id] = {}
            if device.type not in devices[device.id]:
                devices[device.id][device.type] = []
            devices[device.id][device.type].append(device.gardena_device)
        return devices
