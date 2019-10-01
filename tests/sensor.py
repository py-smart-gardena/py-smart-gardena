import pytest
import unittest

from gardena.smart_system import SmartSystem
from gardena.devices.sensor import Sensor
from fixtures import sensor_fixture


class SensorTest(unittest.TestCase):
    def setup_method(self, method):
        self.sm = SmartSystem(email="login", password="password", client_id="client_id")

    def test_sensor(self):
        device = Sensor(self.sm, sensor_fixture)
        assert device.id == "a134596e-6127-4020-aaa5-b6d2f24d0d03"
        assert device.type == "SENSOR"
        assert device.battery_level == 93
        assert device.battery_state == "OK"
        assert device.name == "Sensor"
        assert device.rf_link_level == 70
        assert device.rf_link_state == "ONLINE"
        assert device.serial == "00028462"
        assert device.ambient_temperature == 21
        assert device.light_intensity == 15
        assert device.soil_humidity == 0
        assert device.soil_temperature == 22
