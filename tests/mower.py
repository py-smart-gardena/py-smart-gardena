import pytest
import unittest

from gardena.smart_system import SmartSystem
from gardena.devices.mower import Mower
from fixtures import mower_fixture


class MowerTest(unittest.TestCase):
    def setup_method(self, method):
        self.sm = SmartSystem(client_id="client_id", client_secret="client_secret")

    def test_mower(self):
        device = Mower(self.sm, mower_fixture)
        assert device.id == "7859acbd-b23e-dabf-bec6-62c1453fc44c"
        assert device.type == "MOWER"
        assert device.battery_level == 100
        assert device.battery_state == "OK"
        assert device.name == "SILENO"
        assert device.rf_link_level == 50
        assert device.rf_link_state == "ONLINE"
        assert device.serial == "00003676"
        assert device.activity == "PARKED_PARK_SELECTED"
        assert device.operating_hours == 40
        assert device.state == "OK"
        assert device.last_error_code == "N/A"
