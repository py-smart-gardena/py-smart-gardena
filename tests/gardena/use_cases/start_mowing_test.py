import uuid
from unittest.mock import Mock

from gardena.domain.entities.device_type import DeviceType
from gardena.domain.entities.location import Location
from gardena.domain.entities.mower import Mower
from gardena.use_cases.list_devices import ListDevice
from gardena.use_cases.start_mowing import StartMowing


class TestStartMowing:
    def test_execute_should_call_persistence(self):
        # Given
        mowers_persistence_mock = Mock()
        mower = Mower(id=uuid.uuid4())
        duration = 20
        start_mowing = StartMowing(mowers_persistence=mowers_persistence_mock)

        # When
        start_mowing.execute(mower=mower, duration=duration)

        # Then
        mowers_persistence_mock.start_and_override_schedule.assert_called_once_with(
            mower_id=mower.id, duration=duration
        )
