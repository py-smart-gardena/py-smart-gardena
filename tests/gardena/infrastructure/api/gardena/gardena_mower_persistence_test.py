import uuid
from unittest.mock import Mock, patch

from gardena.infrastructure.api.gardena.gardena_mower_persistence import (
    GardenaMowersPersistence,
)


class TestGardenaMowersPersistence:
    @patch.object(uuid, "uuid1")
    def test_start_and_override_schedule_should_call_the_api_with_correct_data(
        self, mock_uuid
    ):
        # Given
        mower_id = uuid.uuid4()
        duration = 20
        command_id = "291bc0d0-c657-11ec-9d64-0242ac120002"
        mock_uuid.return_value = command_id

        gardena_api_mock = Mock()

        gardena_mowers_persistence_mock: GardenaMowersPersistence = (
            GardenaMowersPersistence(gardena_api_mock)
        )

        # When
        gardena_mowers_persistence_mock.start_and_override_schedule(
            mower_id=mower_id, duration=duration
        )

        # Then
        gardena_api_mock.call_command.assert_called_once_with(
            mower_id,
            {
                "id": command_id,
                "type": "MOWER_CONTROL",
                "attributes": {
                    "command": "START_SECONDS_TO_OVERRIDE",
                    "seconds": duration,
                },
            },
        )

    @patch.object(uuid, "uuid1")
    def test_start_and_dont_override_schedule_should_call_the_api_with_correct_data(
        self, mock_uuid
    ):
        # Given
        mower_id = uuid.uuid4()
        duration = 20
        command_id = "291bc0d0-c657-11ec-9d64-0242ac120002"
        mock_uuid.return_value = command_id

        gardena_api_mock = Mock()

        gardena_mowers_persistence_mock: GardenaMowersPersistence = (
            GardenaMowersPersistence(gardena_api_mock)
        )

        # When
        gardena_mowers_persistence_mock.start_and_dont_override_schedule(
            mower_id=mower_id, duration=duration
        )

        # Then
        gardena_api_mock.call_command.assert_called_once_with(
            mower_id,
            {
                "id": command_id,
                "type": "MOWER_CONTROL",
                "attributes": {"command": "START_DONT_OVERRIDE", "seconds": duration},
            },
        )

    @patch.object(uuid, "uuid1")
    def test_park_until_next_task_should_call_the_api_with_correct_data(
        self, mock_uuid
    ):
        # Given
        mower_id = uuid.uuid4()
        command_id = "291bc0d0-c657-11ec-9d64-0242ac120002"
        mock_uuid.return_value = command_id

        gardena_api_mock = Mock()

        gardena_mowers_persistence_mock: GardenaMowersPersistence = (
            GardenaMowersPersistence(gardena_api_mock)
        )

        # When
        gardena_mowers_persistence_mock.park_until_next_task(mower_id=mower_id)

        # Then
        gardena_api_mock.call_command.assert_called_once_with(
            mower_id,
            {
                "id": command_id,
                "type": "MOWER_CONTROL",
                "attributes": {"command": "PARK_UNTIL_NEXT_TASK"},
            },
        )

    @patch.object(uuid, "uuid1")
    def test_park_until_further_notice_should_call_the_api_with_correct_data(
        self, mock_uuid
    ):
        # Given
        mower_id = uuid.uuid4()
        command_id = "291bc0d0-c657-11ec-9d64-0242ac120002"
        mock_uuid.return_value = command_id

        gardena_api_mock = Mock()

        gardena_mowers_persistence_mock: GardenaMowersPersistence = (
            GardenaMowersPersistence(gardena_api_mock)
        )

        # When
        gardena_mowers_persistence_mock.park_until_further_notice(mower_id=mower_id)

        # Then
        gardena_api_mock.call_command.assert_called_once_with(
            mower_id,
            {
                "id": command_id,
                "type": "MOWER_CONTROL",
                "attributes": {"command": "PARK_UNTIL_FURTHER_NOTICE"},
            },
        )
