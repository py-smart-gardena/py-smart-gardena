from gardena.domain.entities.devices import Devices
from gardena.domain.entities.location import Location


class DevicesPersistence:
    """Interface for Location API"""

    def get_devices(self, location: Location) -> Devices:
        pass
