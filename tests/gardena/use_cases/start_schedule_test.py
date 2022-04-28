import uuid
from unittest.mock import Mock

from gardena.domain.entities.mower import Mower
from gardena.use_cases.start_schedule import StartSchedule


class TestStartSchedule:
    def test_execute_should_call_persistence(self):
        # Given
        mowers_persistence_mock = Mock()
        mower = Mower(id=uuid.uuid4())
        duration = 20
        start_schedule = StartSchedule(mowers_persistence=mowers_persistence_mock)

        # When
        start_schedule.execute(mower=mower, duration=duration)

        # Then
        mowers_persistence_mock.start_and_dont_override_schedule.assert_called_once_with(
            mower_id=mower.id, duration=duration
        )
