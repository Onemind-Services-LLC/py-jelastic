from . import *


def test_check_app_id(client):
    client._get.return_value = success_response
    response = client.Service.CheckAppid("referer", "checksum")
    client._get.assert_called_once_with(
        "CheckAppid",
        params={
            "referer": "referer",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_check_request(client):
    client._get.return_value = success_response
    response = client.Service.CheckRequest("params", "checksum")
    client._get.assert_called_once_with(
        "CheckRequest",
        params={
            "params": "params",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_event(client):
    client._get.return_value = success_response
    response = client.Service.Event("topic", "message", True)
    client._get.assert_called_once_with(
        "Event", params={"topic": "topic", "message": "message", "publishLocal": True}
    )
    assert response == success_response


def test_get_api_description(client):
    client._get.return_value = success_response
    response = client.Service.GetAPIDescriptions(
        True,
        True,
    )
    client._get.assert_called_once_with(
        "GetAPIDescriptions",
        params={
            "isPublicOnly": True,
            "isToken": True,
        },
    )
    assert response == success_response


def test_get_apps(client):
    client._get.return_value = success_response
    response = client.Service.GetApps("checksum")
    client._get.assert_called_once_with(
        "GetApps",
        params={
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_get_cache_status(client):
    client._get.return_value = success_response
    response = client.Service.GetCacheStatus()
    client._get.assert_called_once_with("GetCacheStatus", params={})
    assert response == success_response


def test_get_instance_cache_status(client):
    client._get.return_value = success_response
    response = client.Service.GetInstanceCacheStatus()
    client._get.assert_called_once_with("GetInstanceCacheStatus", params={})
    assert response == success_response


def test_get_property(client):
    client._get.return_value = success_response
    response = client.Service.GetProperty("name")
    client._get.assert_called_once_with(
        "GetProperty",
        params={
            "name": "name",
        },
    )
    assert response == success_response


def test_get_status(client):
    client._get.return_value = success_response
    response = client.Service.GetStatus("checksum")
    client._get.assert_called_once_with(
        "GetStatus",
        params={
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_get_version(client):
    client._get.return_value = success_response
    response = client.Service.GetVersion()
    client._get.assert_called_once_with("GetVersion", params={})
    assert response == success_response


def test_notify_event(client):
    client._get.return_value = success_response
    response = client.Service.NotifyEvent("checksum", "params")
    client._get.assert_called_once_with(
        "NotifyEvent", params={"checksum": "checksum", "params": "params"}
    )
    assert response == success_response


def test_refresh_email_templates(client):
    client._get.return_value = success_response
    response = client.Service.RefreshEmailTemplates()
    client._get.assert_called_once_with("RefreshEmailTemplates", params={})
    assert response == success_response


def test_refresh_user(client):
    client._get.return_value = success_response
    response = client.Service.RefreshUser("language")
    client._get.assert_called_once_with("RefreshUser", params={"language": "language"})
    assert response == success_response


def test_reload_configuration(client):
    client._get.return_value = success_response
    response = client.Service.ReloadConfiguration("rid", "placeholder")
    client._get.assert_called_once_with(
        "ReloadConfiguration",
        params={"resellerId": "rid", "changedPlaceholders": "placeholder"},
    )
    assert response == success_response


def test_set_standby_mode(client):
    client._get.return_value = success_response
    response = client.Service.SetStandbyMode(True)
    client._get.assert_called_once_with(
        "SetStandbyMode",
        params={
            "enabled": True,
        },
    )
    assert response == success_response
