import pytest
import unittest
from gardena.gateway import Gateway
from tests.base_test_device import BaseTestDevice
from tests.gardena_api_return.devices_return import device_gateway_return


class GatewayTestCase(unittest.TestCase, BaseTestDevice):
    def test_init(self):
        gw = Gateway(smart_system=self.smart_system_test_info)
        assert gw.smart_system == self.smart_system_test_info

    def test_init_exception_without_smart_system(self):
        with pytest.raises(ValueError):
            Gateway()

    def test_gateway_information(self):
        gateway = Gateway(smart_system=self.smart_system_test_info)
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
