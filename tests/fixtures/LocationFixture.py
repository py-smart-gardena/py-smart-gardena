from gardena.location import Location
from tests.fixtures import SmartSystemFixture


def get_location_fixture():
    return Location(smart_system=SmartSystemFixture.get_smart_system_fixture())
