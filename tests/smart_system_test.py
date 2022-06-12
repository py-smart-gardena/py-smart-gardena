import pytest
import unittest
import json
from gardena.smart_system import SmartSystem
from gardena.location import Location
from gardena.devices.mower import Mower
from fixtures import location_fixture, mower_fixture


class SmartSystemTest(unittest.TestCase):
    def setup_method(self, method):
        self.sm = SmartSystem(client_id="client_id", client_secret="client_secret")
        loc = Location(self.sm, location_fixture)
        self.sm.locations[loc.id] = loc
        device = Mower(self.sm, mower_fixture)
        loc.add_device(device)

    def test_smart_system(self):
        self.sm.on_message(json.dumps(location_fixture))
        assert len(self.sm.locations) == 1

    def test_location_message(self):
        self.sm.locations["753aecac-4c46-470e-aa96-d92436f11e77"].id = "WRONG_VALUE"
        self.sm.locations["753aecac-4c46-470e-aa96-d92436f11e77"].name = "WRONG_VALUE"
        self.sm.on_message(json.dumps(location_fixture))
        self.sm.on_message(json.dumps(mower_fixture["MOWER"][0]))

        location = self.sm.locations["753aecac-4c46-470e-aa96-d92436f11e77"]
        assert location.id == "753aecac-4c46-470e-aa96-d92436f11e77"
        assert location.name == "My Garden"
        assert len(location.devices) == 1

    def test_device(self):
        self.sm.on_message(json.dumps(location_fixture))
        self.sm.on_message(json.dumps(mower_fixture["MOWER"][0]))
        self.sm.locations["753aecac-4c46-470e-aa96-d92436f11e77"].devices[
            "7859acbd-b23e-dabf-bec6-62c1453fc44c"
        ].name == "WRONG_VALUE"
        device = self.sm.locations["753aecac-4c46-470e-aa96-d92436f11e77"].devices[
            "7859acbd-b23e-dabf-bec6-62c1453fc44c"
        ]
        assert device.id == "7859acbd-b23e-dabf-bec6-62c1453fc44c"
        assert device.name == "SILENO"
