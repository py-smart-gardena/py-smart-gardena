import json
from gardena.base_gardena_class import BaseGardenaClass
from gardena.gateway import Gateway
from gardena.mower import Mower


class Location(BaseGardenaClass):
    """Keep informations about gardena locations (gardens, ..) and devices"""

    gateways = {}
    mowers = {}

    def update_devices(self):
        url = "https://smart.gardena.com/sg-1/devices/"
        params = (("locationId", self.id),)
        response = self.smart_system.request_session.get(
            url, headers=self.smart_system.create_header(), params=params
        )
        response.raise_for_status()
        response_data = json.loads(response.content.decode("utf-8"))
        for device in response_data["devices"]:
            if device["category"] == "gateway":
                if device["id"] not in self.gateways:
                    self.gateways[device["id"]] = Gateway(
                        smart_system=self.smart_system
                    )
                self.gateways[device["id"]].update_information(device)
            elif device["category"] == "mower":
                if device["id"] not in self.mowers:
                    self.mowers[device["id"]] = Mower(smart_system=self.smart_system)
                self.mowers[device["id"]].update_information(device)
