from . import *


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
        CURRENT_DATETIME,
    )
    client._get.assert_called_with(
        "GetAggStats",
        params={
            "starttime": CURRENT_DATETIME,
            "envid": "env_id",
            "checksum": "checksum",
            "endtime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
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
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_all_sum_stat_by_uid(client):
    client._get.return_value = success_response
    response = client.Statistic.GetAllSumStatByUid(
        1,
        1,
        "checksum",
        CURRENT_DATETIME,
    )
    client._get.assert_called_with(
        "GetAllSumStatByUid",
        params={
            "uid": 1,
            "duration": 1,
            "checksum": "checksum",
            "endtime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
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
    response = client.Statistic.GetLastStats("nodeGroup", 1)
    client._get.assert_called_with(
        "GetLastStats", params={"nodeGroup": "nodeGroup", "nodeId": 1}
    )
    assert response == success_response


def test_get_stats(client):
    client._get.return_value = success_response
    response = client.Statistic.GetStats(
        1, 1, "checksum", CURRENT_DATETIME, 1, "nodetype", "nodeGroup"
    )
    client._get.assert_called_with(
        "GetStats",
        params={
            "duration": 1,
            "interval": 1,
            "checksum": "checksum",
            "end_time": CURRENT_DATETIME,
            "nodeid": 1,
            "nodetype": "nodetype",
            "nodeGroup": "nodeGroup",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
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
    response = client.Statistic.GetSumStat(1, "checksum", CURRENT_DATETIME)
    client._get.assert_called_with(
        "GetSumStat",
        params={"duration": 1, "checksum": "checksum", "endtime": CURRENT_DATETIME},
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_sum_stats_by_period(client):
    client._get.return_value = success_response
    response = client.Statistic.GetSumStatsByPeriod(
        CURRENT_DATETIME, "env_id", "checksum", CURRENT_DATETIME
    )
    client._get.assert_called_with(
        "GetSumStatsByPeriod",
        params={
            "starttime": CURRENT_DATETIME,
            "envid": "env_id",
            "checksum": "checksum",
            "endtime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_search_nodes(client):
    client._get.return_value = success_response
    response = client.Statistic.SearchNodes("checksum", "search")
    client._get.assert_called_with(
        "SearchNodes",
        params={"checksum": "checksum", "search": "search"},
    )
    assert response == success_response
