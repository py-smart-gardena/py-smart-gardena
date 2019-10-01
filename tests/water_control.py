import pytest
import unittest

from gardena.smart_system import SmartSystem
from gardena.devices.water_control import WaterControl
from fixtures import water_control_fixture


class WaterControlTest(unittest.TestCase):
    def setup_method(self, method):
        self.sm = SmartSystem(email="login", password="password", client_id="client_id")

    def test_water_control(self):
        device = WaterControl(self.sm, water_control_fixture)
        assert device.id == "d6459669-8171-488c-ab8e-bcf3a06a58bf"
        assert device.type == "WATER_CONTROL"
        assert device.battery_level == 99
        assert device.battery_state == "OK"
        assert device.name == "Water Control"
        assert device.rf_link_level == 70
        assert device.rf_link_state == "ONLINE"
        assert device.serial == "00019796"
        assert device.valve_set_id == "d6459669-8171-488c-ab8e-bcf3a06a58bf:wc"
        assert device.valve_id == "d6459669-8171-488c-ab8e-bcf3a06a58bf"
        assert device.valve_activity == "CLOSED"
        assert device.valve_name == "Water Control"
        assert device.valve_state == "OK"
