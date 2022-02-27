from gardena.domain.entities.devices import Devices
from gardena.domain.entities.location import Location
from gardena.use_cases.persistence.devices_persistence import DevicesPersistence


class ListDevice:
    def __init__(self, devices_persistence: DevicesPersistence):
        self.devices_persistence = devices_persistence

    def execute(self, location: Location) -> Devices:
        return self.devices_persistence.get_devices(location)
