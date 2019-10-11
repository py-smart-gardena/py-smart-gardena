import pytest
import unittest

from gardena.smart_system import SmartSystem
from gardena.devices.power_socket import PowerSocket
from fixtures import power_socket_fixture


class PowerSocketTest(unittest.TestCase):
    def setup_method(self, method):
        self.sm = SmartSystem(email="login", password="password", client_id="client_id")

    def test_sensor(self):
        device = PowerSocket(self.sm, power_socket_fixture)
        assert device.id == "58807078-f5d5-4a1a-814d-d632fbe9ae6b"
        assert device.type == "POWER_SOCKET"
        assert device.battery_level == "N/A"
        assert device.battery_state == "NO_BATTERY"
        assert device.name == "Prise jardin 3"
        assert device.rf_link_level == 60
        assert device.rf_link_state == "ONLINE"
        assert device.serial == "00017114"
        assert device.activity == "OFF"
        assert device.state == "OK"
