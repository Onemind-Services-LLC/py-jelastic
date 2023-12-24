from . import *


def test_execute_action(client):
    client._get.return_value = success_response
    response = client.Installation.ExecuteAction(
        "app_unique_name",
        ["action1", "action2"],
        ["settings_id1", "settings_id2"],
        ["params1", "params2"],
        ["lang1", "lang2"],
    )
    client._get.assert_called_with(
        "ExecuteAction",
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


def test_get_env_appid(client):
    client._get.return_value = success_response
    response = client.Installation.GetEnvAppid("app_unique_name")
    client._get.assert_called_with(
        "GetEnvAppid",
        params={
            "appUniqueName": "app_unique_name",
        },
    )
    assert response == success_response


def test_get_info(client):
    client._get.return_value = success_response
    response = client.Installation.GetInfo("app_unique_name")
    client._get.assert_called_with(
        "GetInfo",
        params={
            "appUniqueName": "app_unique_name",
        },
    )
    assert response == success_response


def test_get_scripting_appid(client):
    client._get.return_value = success_response
    response = client.Installation.GetScriptingAppid()
    client._get.assert_called_with("GetScriptingAppid", params={})
    assert response == success_response


def test_get_settings(client):
    client._get.return_value = success_response
    response = client.Installation.GetSettings(
        "app_unique_name",
        ["settings_id1", "settings_id2"],
        ["lang1", "lang2"],
    )
    client._get.assert_called_with(
        "GetSettings",
        params={
            "appUniqueName": "app_unique_name",
            "settingsId": ["settings_id1", "settings_id2"],
            "lang": ["lang1", "lang2"],
        },
        delimiter=",",
    )


def test_install_addon(client):
    client._get.return_value = success_response
    response = client.App.InstallAddon(
        "2",
        ["setting1", "setting2", "setting3"],
        ["nodeGroup1", "nodeGroup2", "nodeGroup3"],
        [False, True, False],
    )
    client._get.assert_called_with(
        "InstallAddon",
        params={
            "id": "2",
            "settings": ["setting1", "setting2", "setting3"],
            "nodeGroup": ["nodeGroup1", "nodeGroup2", "nodeGroup3"],
            "skipEmail": [False, True, False],
        },
        delimiter=",",
    )
    assert response == success_response


def test_uninstall(client):
    client._get.return_value = success_response
    response = client.Installation.Uninstall(
        "app_unique_name",
        [True, True],
    )
    client._get.assert_called_with(
        "Uninstall",
        params={
            "appUniqueName": "app_unique_name",
            "force": [True, True],
        },
        delimiter=",",
    )
