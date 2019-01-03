import pytest
import unittest
from gardena.mower import Mower
from gardena.smart_system import SmartSystem


class MowerTestCase(unittest.TestCase):
    def test_init(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        device_info = []
        mower = Mower(smart_system=smart_system, device_info=device_info)
        assert mower.smart_system == smart_system
        assert mower.device_info == device_info

    def test_init_exception_without_smart_system(self):
        device_info = []
        with pytest.raises(ValueError):
            Mower(device_info=device_info)

    def test_init_exception_without_device_info(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        with pytest.raises(ValueError):
            Mower(smart_system=smart_system)
