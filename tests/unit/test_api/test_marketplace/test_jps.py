from . import *


def test_execute_app_action(client):
    client._get.return_value = success_response
    response = client.Jps.ExecuteAppAction(
        "app_unique_name",
        ["action1", "action2"],
        ["settings_id1", "settings_id2"],
        ["params1", "params2"],
        ["lang1", "lang2"],
    )
    client._get.assert_called_with(
        "ExecuteAppAction",
        params={
            "appUniqueName": "app_unique_name",
            "action": ["action1", "action2"],
            "settingsId": ["settings_id1", "settings_id2"],
            "params": ["params1", "params2"],
            "lang": ["lang1", "lang2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_app_info(client):
    client._get.return_value = success_response
    response = client.Jps.GetAppInfo(
        ["jps1", "jps2"],
        ["lang1", "lang2"],
        ["owner_uid1", "owner_uid2"],
    )
    client._get.assert_called_with(
        "GetAppInfo",
        params={
            "jps": ["jps1", "jps2"],
            "lang": ["lang1", "lang2"],
            "ownerUid": ["owner_uid1", "owner_uid2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_app_settings(client):
    client._get.return_value = success_response
    response = client.Jps.GetAppSettings(
        "app_unique_name",
        ["settings_id1", "settings_id2"],
        ["lang1", "lang2"],
    )
    client._get.assert_called_with(
        "GetAppSettings",
        params={
            "appUniqueName": "app_unique_name",
            "settingsId": ["settings_id1", "settings_id2"],
            "lang": ["lang1", "lang2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_engine_version(client):
    client._get.return_value = success_response
    response = client.Jps.GetEngineVersion()
    client._get.assert_called_with("GetEngineVersion", params={})
    assert response == success_response


def test_get_scripting_appid(client):
    client._get.return_value = success_response
    response = client.Jps.GetScriptingAppid()
    client._get.assert_called_with("GetScriptingAppid", params={})
    assert response == success_response


def test_install(client):
    client._get.return_value = success_response
    response = client.Jps.Install(
        "jps",
        ["env_name1", "env_name2"],
        ["settings1", "settings2"],
        ["node_group1", "node_group2"],
        ["display_name1", "display_name2"],
        ["region1", "region2"],
        ["env_groups1", "env_groups2"],
        [1, 1],
        ["logs_path1", "logs_path2"],
        [True, True],
        [True, True],
    )
    client._get.assert_called_with(
        "Install",
        params={
            "jps": "jps",
            "envName": ["env_name1", "env_name2"],
            "settingsId": ["settings1", "settings2"],
            "nodeGroup": ["node_group1", "node_group2"],
            "displayName": ["display_name1", "display_name2"],
            "region": ["region1", "region2"],
            "envGroups": ["env_groups1", "env_groups2"],
            "ownerUid": [1, 1],
            "logsPath": ["logs_path1", "logs_path2"],
            "writeOutputTasks": [True, True],
            "skipNodeEmails": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_uninstall(client):
    client._get.return_value = success_response
    response = client.Jps.Uninstall(
        "app_unique_name",
        [True, False],
    )
    client._get.assert_called_with(
        "Uninstall",
        params={
            "appUniqueName": "app_unique_name",
            "force": [True, False],
        },
        delimiter=",",
    )
    assert response == success_response
