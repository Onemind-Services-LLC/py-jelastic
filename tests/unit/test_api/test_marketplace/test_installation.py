from . import *


def test_execute_action(client):
    client._get.return_value = success_response
    response = client.Installation.ExecuteAction(
        "app_unique_name",
        "action",
        "other",
        {"key": "value"},
        "en",
    )
    client._get.assert_called_with(
        "ExecuteAction",
        params={
            "appUniqueName": "app_unique_name",
            "action": "action",
            "settingsId": "other",
            "params": {"key": "value"},
            "lang": "en",
        },
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
    response = client.Installation.GetSettings("app_unique_name", "other", "lang")
    client._get.assert_called_with(
        "GetSettings",
        params={
            "appUniqueName": "app_unique_name",
            "settingsId": "other",
            "lang": "lang",
        },
    )
    assert response == success_response


def test_install_addon(client):
    client._get.return_value = success_response
    response = client.App.InstallAddon(
        "env_name",
        "2",
        {"key": "value"},
        "nodeGroup",
        True,
    )
    client._get.assert_called_with(
        "InstallAddon",
        params={
            "id": "2",
            "envName": "env_name",
            "settings": {"key": "value"},
            "nodeGroup": "nodeGroup",
            "skipEmail": True,
        },
    )
    assert response == success_response


def test_uninstall(client):
    client._get.return_value = success_response
    response = client.Installation.Uninstall(
        "app_unique_name", "target_app_id", "app_template_id", True
    )
    client._get.assert_called_with(
        "Uninstall",
        params={
            "appUniqueName": "app_unique_name",
            "targetAppId": "target_app_id",
            "appTemplateId": "app_template_id",
            "force": True,
        },
    )
    assert response == success_response
