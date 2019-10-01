import pytest
import unittest

from gardena.smart_system import SmartSystem
from gardena.devices.smart_irrigation_control import SmartIrrigationControl
from fixtures import smart_irrigation_fixture


class SmartIrrigationControlTest(unittest.TestCase):
    def setup_method(self, method):
        self.sm = SmartSystem(email="login", password="password", client_id="client_id")

    def test_smart_irrigation_control(self):
        device = SmartIrrigationControl(self.sm, smart_irrigation_fixture)
        assert device.id == "28c26146-d4c1-42d7-964a-89f5237550ce"
        assert device.type == "SMART_IRRIGATION_CONTROL"
        assert device.battery_level == "N/A"
        assert device.battery_state == "NO_BATTERY"
        assert device.name == "Irrigation Control"
        assert device.rf_link_level == 100
        assert device.rf_link_state == "OFFLINE"
        assert device.serial == "00001834"
        assert device.valve_set_id == "28c26146-d4c1-42d7-964a-89f5237550ce"
        assert device.valve_set_state == "OK"
        assert device.valve_set_last_error_code == "NO_MESSAGE"
        assert len(device.valves) == 6
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:1"]["id"]
            == "28c26146-d4c1-42d7-964a-89f5237550ce:1"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:1"]["activity"]
            == "CLOSED"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:1"]["last_error_code"]
            == "NO_MESSAGE"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:1"]["name"]
            == "Clapet 1"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:1"]["state"]
            == "UNAVAILABLE"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:2"]["id"]
            == "28c26146-d4c1-42d7-964a-89f5237550ce:2"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:2"]["activity"]
            == "CLOSED"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:2"]["last_error_code"]
            == "NO_MESSAGE"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:2"]["name"] == "Valve 2"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:2"]["state"]
            == "UNAVAILABLE"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:3"]["id"]
            == "28c26146-d4c1-42d7-964a-89f5237550ce:3"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:3"]["activity"]
            == "CLOSED"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:3"]["last_error_code"]
            == "NO_MESSAGE"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:3"]["name"] == "Valve 3"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:3"]["state"]
            == "UNAVAILABLE"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:4"]["id"]
            == "28c26146-d4c1-42d7-964a-89f5237550ce:4"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:4"]["activity"]
            == "CLOSED"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:4"]["last_error_code"]
            == "NO_MESSAGE"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:4"]["name"] == "Valve 4"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:4"]["state"]
            == "UNAVAILABLE"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:5"]["id"]
            == "28c26146-d4c1-42d7-964a-89f5237550ce:5"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:5"]["activity"]
            == "CLOSED"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:5"]["last_error_code"]
            == "NO_MESSAGE"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:5"]["name"] == "Valve 5"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:5"]["state"]
            == "UNAVAILABLE"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:6"]["id"]
            == "28c26146-d4c1-42d7-964a-89f5237550ce:6"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:6"]["activity"]
            == "CLOSED"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:6"]["last_error_code"]
            == "NO_MESSAGE"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:6"]["name"] == "Valve 6"
        )
        assert (
            device.valves["28c26146-d4c1-42d7-964a-89f5237550ce:6"]["state"]
            == "UNAVAILABLE"
        )
