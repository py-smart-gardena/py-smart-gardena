import pytest
import unittest
from gardena.gateway import Gateway
from gardena.smart_system import SmartSystem


class GatewayTestCase(unittest.TestCase):
    def test_init(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        device_info = []
        gw = Gateway(smart_system=smart_system, device_info=device_info)
        assert gw.smart_system == smart_system
        assert gw.device_info == device_info

    def test_init_exception_without_smart_system(self):
        device_info = []
        with pytest.raises(ValueError):
            Gateway(device_info=device_info)

    def test_init_exception_without_device_info(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        with pytest.raises(ValueError):
            Gateway(smart_system=smart_system)
