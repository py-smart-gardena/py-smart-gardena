import pytest
import unittest
from gardena.gateway import Gateway
from gardena.smart_system import SmartSystem


class GatewayTestCase(unittest.TestCase):
    def test_init(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        gw = Gateway(smart_system=smart_system)
        assert gw.smart_system == smart_system

    def test_init_exception_without_smart_system(self):
        with pytest.raises(ValueError):
            Gateway()
