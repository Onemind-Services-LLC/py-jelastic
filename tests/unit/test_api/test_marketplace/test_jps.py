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
        "netbox",
        "env_name",
        {"settings": "settings"},
        "node_group",
        "display_name",
        "region",
        ["env_groups1", "env_groups2"],
        123,
        "/logs_path",
        True,
        True,
    )
    client._get.assert_called_with(
        "Install",
        params={
            "jps": "netbox",
            "envName": "env_name",
            "settings": {"settings": "settings"},
            "nodeGroup": "node_group",
            "displayName": "display_name",
            "region": "region",
            "envGroups": ["env_groups1", "env_groups2"],
            "ownerUid": 123,
            "logsPath": "/logs_path",
            "writeOutputTasks": True,
            "skipNodeEmails": True,
        },
    )
    assert response == success_response
