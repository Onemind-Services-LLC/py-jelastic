from unittest.mock import patch, Mock
from datetime import datetime
import pytest

from jelastic.api import Statistic

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}

CURRENT_DATETIME = datetime.now()


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        statistic = Statistic(session=Mock(), token="token")
        statistic._get = mock_get
        yield statistic


def test_create_stat_table(client):
    client._get.return_value = success_response
    response = client.Statistic.CreateStatTable("env_id", "checksum")
    client._get.assert_called_with(
        "CreateStatTable",
        params={
            "envid": "env_id",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_get_active_cloudlets(client):
    client._get.return_value = success_response
    response = client.Statistic.GetActiveCloudlets("checksum")
    client._get.assert_called_with(
        "GetActiveCloudlets",
        params={
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_get_agg_stats(client):
    client._get.return_value = success_response
    response = client.Statistic.GetAggStats(
        CURRENT_DATETIME,
        "env_id",
        "checksum",
        [CURRENT_DATETIME, CURRENT_DATETIME],
    )
    client._get.assert_called_with(
        "GetAggStats",
        params={
            "starttime": CURRENT_DATETIME,
            "envid": "env_id",
            "checksum": "checksum",
            "endtime": [CURRENT_DATETIME, CURRENT_DATETIME],
        },
        delimeter=",",
    )
    assert response == success_response


def test_get_all_agg_sum_stat_by_uid(client):
    client._get.return_value = success_response
    response = client.Statistic.GetAllAggSumStatByUid(
        CURRENT_DATETIME, "env_id", "checksum", CURRENT_DATETIME
    )
    client._get.assert_called_with(
        "GetAllAggSumStatByUid",
        params={
            "startTime": CURRENT_DATETIME,
            "envid": "env_id",
            "checksum": "checksum",
            "endTime": CURRENT_DATETIME,
        },
    )
    assert response == success_response


def test_get_all_sum_stat_by_uid(client):
    client._get.return_value = success_response
    response = client.Statistic.GetAllSumStatByUid(
        1,
        1,
        "checksum",
        [CURRENT_DATETIME, CURRENT_DATETIME],
    )
    client._get.assert_called_with(
        "GetAllSumStatByUid",
        params={
            "uid": 1,
            "duration": 1,
            "checksum": "checksum",
            "endtime": [CURRENT_DATETIME, CURRENT_DATETIME],
        },
        delimeter=",",
    )
    assert response == success_response


def test_get_current_statistics_for_all_containers(client):
    client._get.return_value = success_response
    response = client.Statistic.GetCurrentStatisticsForAllContainers("checksum")
    client._get.assert_called_with(
        "GetCurrentStatisticsForAllContainers",
        params={
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_get_last_stats(client):
    client._get.return_value = success_response
    response = client.Statistic.GetLastStats(["node_group1", "node_group2"], [1, 1])
    client._get.assert_called_with(
        "GetLastStats",
        params={"nodeGroup": ["node_group1", "node_group2"], "nodeId": [1, 1]},
        delimiter=",",
    )
    assert response == success_response


def test_get_stats(client):
    client._get.return_value = success_response
    response = client.Statistic.GetStats(
        1,
        1,
        "checksum",
        [CURRENT_DATETIME, CURRENT_DATETIME],
        [1, 1],
        ["node_type1", "node_type2"],
        ["node_group1", "node_group2"],
    )
    client._get.assert_called_with(
        "GetStats",
        params={
            "duration": 1,
            "interval": 1,
            "checksum": "checksum",
            "end_time": [CURRENT_DATETIME, CURRENT_DATETIME],
            "nodeid": [1, 1],
            "nodetype": ["node_type1", "node_type2"],
            "nodeGroup": ["node_group1", "node_group2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_status(client):
    client._get.return_value = success_response
    response = client.Statistic.GetStatus("checksum")
    client._get.assert_called_with(
        "GetStatus",
        params={
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_get_all_sum_stat(client):
    client._get.return_value = success_response
    response = client.Statistic.GetSumStat(
        1,
        "checksum",
        [CURRENT_DATETIME, CURRENT_DATETIME],
    )
    client._get.assert_called_with(
        "GetSumStat",
        params={
            "duration": 1,
            "checksum": "checksum",
            "endtime": [CURRENT_DATETIME, CURRENT_DATETIME],
        },
        delimeter=",",
    )
    assert response == success_response


def test_get_sum_stats_by_period(client):
    client._get.return_value = success_response
    response = client.Statistic.GetSumStatsByPeriod(
        CURRENT_DATETIME,
        "env_id",
        "checksum",
        [CURRENT_DATETIME, CURRENT_DATETIME],
    )
    client._get.assert_called_with(
        "GetSumStatsByPeriod",
        params={
            "starttime": CURRENT_DATETIME,
            "envid": "env_id",
            "checksum": "checksum",
            "endtime": [CURRENT_DATETIME, CURRENT_DATETIME],
        },
        delimeter=",",
    )
    assert response == success_response


def test_search_nodes(client):
    client._get.return_value = success_response
    response = client.Statistic.SearchNodes("checksum", ["search1", "search2"])
    client._get.assert_called_with(
        "SearchNodes",
        params={"checksum": "checksum", "search": ["search1", "search2"]},
    )
    assert response == success_response


def test_generate_statistics(client):
    client._get.return_value = success_response
    response = client.Utils.GenerateStatistics(1, 1, "stat_json", "checksum")
    client._get.assert_called_with(
        "GenerateStatistics",
        params={
            "durationHours": 1,
            "nodeId": 1,
            "statJSON": "stat_json",
            "checksum": "checksum",
        },
    )
    assert response == success_response
