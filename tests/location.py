import pytest
import unittest

from gardena.smart_system import SmartSystem
from gardena.location import Location
from fixtures import location_fixture


class LocationTest(unittest.TestCase):
    def setup_method(self, method):
        self.sm = SmartSystem(client_id="client_id", client_secret="client_secret")

    def test_location(self):
        loc = Location(self.sm, location_fixture)
        assert loc.id == "753aecac-4c46-470e-aa96-d92436f11e77"
        assert loc.name == "My Garden"
