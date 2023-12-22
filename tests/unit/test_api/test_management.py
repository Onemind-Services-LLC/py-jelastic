from datetime import datetime
from unittest.mock import patch, Mock

import pytest

from jelastic.api import Marketplace

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}
CURRENT_DATETIME = datetime.now()


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        marketplace = Marketplace(session=Mock(), token="token")
        marketplace._get = mock_get
        yield marketplace


def test_add(client):
    client._get.return_value = success_response
    response = client.Favorite.Add("id")
    client._get.assert_called_with(
        "Add",
        params={"id": "id"},
    )


def test_clear_log(client):
    client._get.return_value = success_response
    response = client.Console.ClearLog()
    client._get.assert_called_with(
        "ClearLog",
        params={},
    )
    assert response == success_response


def test_read_log(client):
    client._get.return_value = success_response
    response = client.Console.ReadLog()
    client._get.assert_called_with(
        "ReadLog",
        params={},
    )


def test_add_manifest(client):
    client._get.return_value = success_response
    response = client.Favorite.AddManifest("manifest")
    client._get.assert_called_with(
        "AddManifest",
        params={"manifest": "manifest"},
    )
    assert response == success_response


def test_delete(client):
    client._get.return_value = success_response
    response = client.Favorite.Delete("id")
    client._get.assert_called_with(
        "Delete",
        params={"id": "id"},
    )
    assert response == success_response


def test_get_list(client):
    client._get.return_value = success_response
    response = client.Favorite.GetList(
        "search",
        "lang",
        "checksum",
    )
    client._get.assert_called_with(
        "Delete",
        params={
            "search": "search",
            "lang": "lang",
            "checksum": "checksum",
        },
    )
    assert response == success_response


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


def test_write_log(client):
    client._get.return_value = success_response
    response = client.Console.WriteLog("message")
    client._get.assert_called_with(
        "WriteLog",
        params={"message": "message"},
    )
    assert response == success_response
