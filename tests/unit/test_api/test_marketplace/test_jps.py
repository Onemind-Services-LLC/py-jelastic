from . import *


def test_execute_app_action(client):
    client._get.return_value = success_response
    response = client.Jps.ExecuteAppAction(
        "app_unique_name", "action", "other", "params", "lang", "ruk"
    )
    client._get.assert_called_with(
        "ExecuteAppAction",
        params={
            "appUniqueName": "app_unique_name",
            "action": "action",
            "settingsId": "other",
            "params": "params",
            "lang": "lang",
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_get_app_info(client):
    client._get.return_value = success_response
    response = client.Jps.GetAppInfo("jps", "lang", 11, "ruk")
    client._get.assert_called_with(
        "GetAppInfo",
        params={
            "jps": "jps",
            "lang": "lang",
            "ownerUid": 11,
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_get_app_settings(client):
    client._get.return_value = success_response
    response = client.Jps.GetAppSettings("app_unique_name", "other", "lang", "ruk")
    client._get.assert_called_with(
        "GetAppSettings",
        params={
            "appUniqueName": "app_unique_name",
            "settingsId": "other",
            "lang": "lang",
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_get_engine_version(client):
    client._get.return_value = success_response
    response = client.Jps.GetEngineVersion("ruk")
    client._get.assert_called_with("GetEngineVersion", params={"ruk":"ruk"})
    assert response == success_response


def test_get_scripting_appid(client):
    client._get.return_value = success_response
    response = client.Jps.GetScriptingAppid("ruk")
    client._get.assert_called_with("GetScriptingAppid", params={"ruk":"ruk"})
    assert response == success_response


def test_install(client):
    client._get.return_value = success_response
    response = client.Jps.Install(
        "jps",
        "envName",
        "settings",
        "nodeGroup",
        "displayName",
        "region",
        "envGroups",
        1,
        "logsPath",
        True,
        True,
        "ruk"
    )
    client._get.assert_called_with(
        "Install",
        params={
            "jps": "jps",
            "envName": "envName",
            "settings": "settings",
            "nodeGroup": "nodeGroup",
            "displayName": "displayName",
            "region": "region",
            "envGroups": "envGroups",
            "ownerUid": 1,
            "logsPath": "logsPath",
            "writeOutputTasks": True,
            "skipNodeEmails": True,
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_uninstall(client):
    client._get.return_value = success_response
    response = client.Jps.Uninstall("app_unique_name", False, "ruk")
    client._get.assert_called_with(
        "Uninstall",
        params={
            "appUniqueName": "app_unique_name",
            "force": False,
            "ruk":"ruk"
        },
    )
    assert response == success_response
