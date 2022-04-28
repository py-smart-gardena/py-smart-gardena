import uuid
from unittest.mock import Mock

from gardena.domain.entities.mower import Mower
from gardena.use_cases.stop_mowing import StopMowing


class TestStopMowing:
    def test_execute_should_call_persistence(self):
        # Given
        mowers_persistence_mock = Mock()
        mower = Mower(id=uuid.uuid4())
        duration = 20
        stop_mowing = StopMowing(mowers_persistence=mowers_persistence_mock)

        # When
        stop_mowing.execute(mower=mower)

        # Then
        mowers_persistence_mock.park_until_next_task.assert_called_once_with(
            mower_id=mower.id
        )
