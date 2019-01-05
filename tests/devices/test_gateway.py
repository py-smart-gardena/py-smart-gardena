import unittest

from gardena.devices.gateway import Gateway
from tests.gardena_api_return.devices_return import device_gateway_return
from tests.fixtures import SmartSystemFixture, LocationFixture


class GatewayTestCase(unittest.TestCase):
    def test_gateway_information(self):
        smart_system_fixture = SmartSystemFixture.get_smart_system_fixture()
        gateway = Gateway(
            smart_system=smart_system_fixture,
            location=LocationFixture.get_location_fixture(),
        )
        gateway.update_information(information=device_gateway_return)
        assert gateway.id == device_gateway_return["id"]
        assert gateway.name == device_gateway_return["name"]
        assert gateway.description == device_gateway_return["description"]
        assert gateway.category == device_gateway_return["category"]
        assert (
            gateway.is_configuration_synchronized
            == device_gateway_return["configuration_synchronized"]
        )
        assert gateway.serial_number == "12345678"
        assert gateway.version == "1.2.1"
        assert gateway.last_time_online == "N/A"
        assert gateway.ip_address == "192.168.1.217"
        assert gateway.timezone == "Europe/Vienna (CEST, +0200)"
        assert gateway.device_state == "ok"
