from unittest.mock import Mock

from gardena.domain.entities.mower import Mower
from gardena.use_cases.list_mowers import ListMowers


class TestListMowers:
    def test_execute_should_return_a_list_of_mower(self):
        # Given
        mowers = [
            Mower(),
            Mower(),
        ]
        mower_persistence_mock = Mock()
        mower_persistence_mock.get_mowers.return_value = mowers

        list_mower = ListMowers(mower_persistence=mower_persistence_mock)
        # When
        returned_mowers = list_mower.execute()

        # Then
        assert len(returned_mowers) == 2
        assert returned_mowers[0].type == "MOWER"
        assert returned_mowers[0].activity == "N/A"
        assert returned_mowers[0].operating_hours == "N/A"
        assert returned_mowers[0].state == "N/A"
        assert returned_mowers[0].last_error_code == "N/A"
        assert returned_mowers[0].id == "None"
        assert returned_mowers[0].battery_level == "N/A"
        assert returned_mowers[0].battery_state == "N/A"
        assert returned_mowers[0].name == "N/A"
        assert returned_mowers[0].rf_link_level == "N/A"
        assert returned_mowers[0].rf_link_state == "N/A"
        assert returned_mowers[0].serial == "N/A"
        assert returned_mowers[0].model_type == "N/A"
        assert returned_mowers[0].callbacks == []
        assert returned_mowers[1].type == "MOWER"
        assert returned_mowers[1].activity == "N/A"
        assert returned_mowers[1].operating_hours == "N/A"
        assert returned_mowers[1].state == "N/A"
        assert returned_mowers[1].last_error_code == "N/A"
        assert returned_mowers[1].id == "None"
        assert returned_mowers[1].battery_level == "N/A"
        assert returned_mowers[1].battery_state == "N/A"
        assert returned_mowers[1].name == "N/A"
        assert returned_mowers[1].rf_link_level == "N/A"
        assert returned_mowers[1].rf_link_state == "N/A"
        assert returned_mowers[1].serial == "N/A"
        assert returned_mowers[1].model_type == "N/A"
        assert returned_mowers[1].callbacks == []
