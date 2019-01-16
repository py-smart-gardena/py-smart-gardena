import json

from gardena.base_gardena_class import BaseGardenaClass
from gardena.devices.gateway import Gateway
from gardena.devices.mower import Mower
from gardena.devices.power import Power
from gardena.devices.sensor import Sensor
from gardena.devices.water_control import WaterControl


class Location(BaseGardenaClass):
    """Keep informations about gardena locations (gardens, ..) and devices"""

    """Used to configure device instance assignements"""

    def __init__(self, smart_system=None):
        super(Location, self).__init__(smart_system=smart_system)
        self.latitude = None
        self.longitude = None
        self.address = None
        self.city = None
        self.sunrise = None
        self.sunset = None
        self.time_zone = None
        self.time_zone_offset = None
        self.gateways = {}
        self.mowers = {}
        self.sensors = {}
        self.water_controls = {}
        self.powers = {}
        self.device_types_configuration = {
            "gateway": {"class": Gateway, "map": self.gateways},
            "mower": {"class": Mower, "map": self.mowers},
            "sensor": {"class": Sensor, "map": self.sensors},
            "watering_computer": {"class": WaterControl, "map": self.water_controls},
            "power": {"class": Power, "map": self.powers},
        }

    def update_information(self, information):
        super(Location, self).update_information(information)
        if "geo_position" in information:
            self.set_field_if_exists(
                information["geo_position"], "latitude", "latitude"
            )
            self.set_field_if_exists(
                information["geo_position"], "longitude", "longitude"
            )
            self.set_field_if_exists(information["geo_position"], "address", "address")
            self.set_field_if_exists(information["geo_position"], "city", "city")
            self.set_field_if_exists(information["geo_position"], "sunrise", "sunrise")
            self.set_field_if_exists(information["geo_position"], "sunset", "sunset")
            self.set_field_if_exists(
                information["geo_position"], "time_zone", "time_zone"
            )
            self.set_field_if_exists(
                information["geo_position"], "time_zone_offset", "time_zone_offset"
            )

    def add_or_update_device(self, device=None):
        if device is None:
            return
        if device["category"] not in self.device_types_configuration:
            return

        device_class = self.device_types_configuration[device["category"]]["class"]
        device_map = self.device_types_configuration[device["category"]]["map"]
        if device["id"] not in device_map:
            device_map[device["id"]] = device_class(
                smart_system=self.smart_system, location=self
            )
        device_map[device["id"]].update_information(device)

    def update_devices(self):
        url = "https://smart.gardena.com/sg-1/devices/"
        params = (("locationId", self.id),)
        response = self.smart_system.request_session.get(
            url, headers=self.smart_system.create_header(), params=params
        )
        response.raise_for_status()
        response_data = json.loads(response.content.decode("utf-8"))
        for device in response_data["devices"]:
            self.add_or_update_device(device)
