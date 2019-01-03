import pytest
import unittest
from gardena.mower import Mower
from gardena.smart_system import SmartSystem


class MowerTestCase(unittest.TestCase):
    def test_init(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        mower = Mower(smart_system=smart_system)
        assert mower.smart_system == smart_system

    def test_init_exception_without_smart_system(self):
        with pytest.raises(ValueError):
            Mower()
