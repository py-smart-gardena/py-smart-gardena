import uuid
from unittest.mock import Mock

from gardena.domain.entities.mower import Mower
from gardena.use_cases.stop_schedule import StopSchedule


class TestStopSchedule:
    def test_execute_should_call_persistence(self):
        # Given
        mowers_persistence_mock = Mock()
        mower = Mower(id=uuid.uuid4())
        duration = 20
        stop_schedule = StopSchedule(mowers_persistence=mowers_persistence_mock)

        # When
        stop_schedule.execute(mower=mower)

        # Then
        mowers_persistence_mock.park_until_further_notice.assert_called_once_with(
            mower_id=mower.id
        )
