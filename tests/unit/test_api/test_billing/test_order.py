from . import *


def test_add_stats(client):
    client._get.return_value = success_response
    response = client.Order.AddStats(
        "resource",
        1,
        1,
        ["2022-11-11", "2022-11-22", "2022-11-21"],
        ["2022-11-22", "2022-11-12", "2022-11-13"],
        ["env1", "env2", "env3"],
        [1, 2, 3],
        ["note1", "note2", "note3"],
        ["value1", "value2", "value3"],
    )
    client._get.assert_called_with(
        "AddStats",
        params={
            "resourceName": "resource",
            "uid": 1,
            "value": 1,
            "startDate": ["2022-11-11", "2022-11-22", "2022-11-21"],
            "endDate": ["2022-11-22", "2022-11-12", "2022-11-13"],
            "envName": ["env1", "env2", "env3"],
            "nodeId": [1, 2, 3],
            "note": ["note1", "note2", "note3"],
            "valueGroup": ["value1", "value2", "value3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_env_resources(client):
    client._get.return_value = success_response
    response = client.Order.EnvResources(CURRENT_DATETIME, CURRENT_DATETIME)
    client._get.assert_called_with(
        "EnvResources",
        params={
            "startDate": CURRENT_DATETIME.strftime("%Y-%m-%d"),
            "endDate": CURRENT_DATETIME.strftime("%Y-%m-%d"),
        },
    )
    assert response == success_response


def test_envs_resources(client):
    client._get.return_value = success_response
    response = client.Order.EnvsResources(CURRENT_DATETIME, CURRENT_DATETIME, "tid_1", "checksum")
    client._get.assert_called_with(
        "EnvsResources",
        params={
            "startDate": CURRENT_DATETIME.strftime("%Y-%m-%d"),
            "endDate": CURRENT_DATETIME.strftime("%Y-%m-%d"),
            "targetAppId": "tid_1",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_envs_resources_by_account(client):
    client._get.return_value = success_response
    response = client.Order.EnvsResourcesByAccount(CURRENT_DATETIME, CURRENT_DATETIME, 1, "checksum")
    client._get.assert_called_with(
        "EnvsResourcesByAccount",
        params={
            "startDate": CURRENT_DATETIME.strftime("%Y-%m-%d"),
            "endDate": CURRENT_DATETIME.strftime("%Y-%m-%d"),
            "uid": 1,
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_get_options(client):
    client._get.return_value = success_response
    response = client.Order.GetOptions("env", "group")
    client._get.assert_called_with(
        "GetOptions",
        params={
            "targetEnvName": "env",
            "nodeGroup": "group",
        },
    )
    assert response == success_response


def test_set_options(client):
    client._get.return_value = success_response
    response = client.Order.SetOptions(
        "env",
        "group",
        "option",
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "SetOptions",
        params={
            "targetEnvName": "env",
            "nodeGroup": "group",
            "options": "option",
            "nodeId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response
