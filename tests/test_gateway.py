import pytest
import unittest
from gardena.gateway import Gateway
from tests.base_test_device import BaseTestDevice


class GatewayTestCase(unittest.TestCase, BaseTestDevice):

    gateway_test_info = {
        "id": "75cfc1f8-a20c-51d6-c5ea-1b5ecdde80c1",
        "name": "Gardena Zentrale",
        "description": "Gateway device",
        "category": "gateway",
        "configuration_synchronized": True,
        "abilities": [
            {
                "id": "f9667bc2-b5e2-11e5-b6a5-32212aec0665",
                "name": "device_info",
                "type": "device_info",
                "properties": [
                    {
                        "id": "f9667bc2-b5e2-11e5-b6a5-100000000000",
                        "name": "manufacturer",
                        "value": "Seluxit",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "f9667bc2-b5e2-11e5-b6a5-100000000001",
                        "name": "product",
                        "value": "1-GATEWAY",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "f9667bc2-b5e2-11e5-b6a5-100000000002",
                        "name": "serial_number",
                        "value": "N/A",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "f9667bc2-b5e2-11e5-b6a5-100000000003",
                        "name": "sgtin",
                        "value": "N/A",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "f9667bc2-b5e2-11e5-b6a5-100000000004",
                        "name": "version",
                        "value": "1.2.1",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "f9667bc2-b5e2-11e5-b6a5-100000000005",
                        "name": "category",
                        "value": "gateway",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "f9667bc2-b5e2-11e5-b6a5-100000000006",
                        "name": "last_time_online",
                        "value": "N/A",
                        "writeable": False,
                        "supported_values": [],
                    },
                ],
            },
            {
                "id": "b74cbb14-b5e4-11e5-86c5-32212aec0665",
                "name": "gateway",
                "type": "gateway",
                "properties": [
                    {
                        "id": "b74cbb14-b5e4-11e5-86c5-100000000000",
                        "name": "ip_address",
                        "value": "192.168.1.217",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "b74cbb14-b5e4-11e5-86c5-100000000001",
                        "name": "time_zone",
                        "value": " Europe/Vienna (CEST, +0200)",
                        "writeable": False,
                        "supported_values": [],
                    },
                ],
            },
        ],
        "scheduled_events": [],
        "status_report_history": [],
        "constraints": [],
    }

    def test_init(self):
        gw = Gateway(
            smart_system=self.smart_system_test_info, device_info=self.gateway_test_info
        )
        assert gw.smart_system == self.smart_system_test_info
        assert gw.device_info == self.gateway_test_info

    def test_init_exception_without_smart_system(self):
        with pytest.raises(ValueError):
            Gateway(device_info=self.gateway_test_info)

    def test_init_exception_without_device_info(self):
        with pytest.raises(ValueError):
            Gateway(smart_system=self.smart_system_test_info)
