from . import *


def test_check_app_id(client):
    client._get.return_value = success_response
    response = client.Service.CheckAppid(
        "referer",
        "checksum",
        "ruk",
    )
    client._get.assert_called_once_with(
        "CheckAppid",
        params={"referer": "referer", "checksum": "checksum", "ruk": "ruk"},
    )
    assert response == success_response


def test_check_request(client):
    client._get.return_value = success_response
    response = client.Service.CheckRequest(
        "params",
        "checksum",
        "ruk",
    )
    client._get.assert_called_once_with(
        "CheckRequest",
        params={"params": "params", "checksum": "checksum", "ruk": "ruk"},
    )
    assert response == success_response


def test_event(client):
    client._get.return_value = success_response
    response = client.Service.Event(
        "topic",
        "message",
        True,
        "ruk",
    )
    client._get.assert_called_once_with(
        "Event",
        params={
            "topic": "topic",
            "message": "message",
            "publishLocal": True,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_api_description(client):
    client._get.return_value = success_response
    response = client.Service.GetAPIDescriptions(
        True,
        True,
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetAPIDescriptions",
        params={"isPublicOnly": True, "isToken": True, "ruk": "ruk"},
    )
    assert response == success_response


def test_get_apps(client):
    client._get.return_value = success_response
    response = client.Service.GetApps(
        "checksum",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetApps",
        params={"checksum": "checksum", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_cache_status(client):
    client._get.return_value = success_response
    response = client.Service.GetCacheStatus(
        "ruk",
    )
    client._get.assert_called_once_with("GetCacheStatus", params={"ruk": "ruk"})
    assert response == success_response


def test_get_instance_cache_status(client):
    client._get.return_value = success_response
    response = client.Service.GetInstanceCacheStatus(
        "ruk",
    )
    client._get.assert_called_once_with("GetInstanceCacheStatus", params={"ruk": "ruk"})
    assert response == success_response


def test_get_property(client):
    client._get.return_value = success_response
    response = client.Service.GetProperty(
        "name",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetProperty",
        params={"name": "name", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_status(client):
    client._get.return_value = success_response
    response = client.Service.GetStatus(
        "checksum",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetStatus",
        params={"checksum": "checksum", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_version(client):
    client._get.return_value = success_response
    response = client.Service.GetVersion(
        "ruk",
    )
    client._get.assert_called_once_with("GetVersion", params={"ruk": "ruk"})
    assert response == success_response


def test_notify_event(client):
    client._get.return_value = success_response
    response = client.Service.NotifyEvent(
        "checksum",
        "params",
        "ruk",
    )
    client._get.assert_called_once_with(
        "NotifyEvent", params={"checksum": "checksum", "params": "params", "ruk": "ruk"}
    )
    assert response == success_response


def test_refresh_email_templates(client):
    client._get.return_value = success_response
    response = client.Service.RefreshEmailTemplates(
        "ruk",
    )
    client._get.assert_called_once_with("RefreshEmailTemplates", params={"ruk": "ruk"})
    assert response == success_response


def test_refresh_user(client):
    client._get.return_value = success_response
    response = client.Service.RefreshUser(
        "language",
        "ruk",
    )
    client._get.assert_called_once_with(
        "RefreshUser", params={"language": "language", "ruk": "ruk"}
    )
    assert response == success_response


def test_reload_configuration(client):
    client._get.return_value = success_response
    response = client.Service.ReloadConfiguration(
        "rid",
        "placeholder",
        "ruk",
    )
    client._get.assert_called_once_with(
        "ReloadConfiguration",
        params={
            "resellerId": "rid",
            "changedPlaceholders": "placeholder",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_set_standby_mode(client):
    client._get.return_value = success_response
    response = client.Service.SetStandbyMode(
        True,
        "ruk",
    )
    client._get.assert_called_once_with(
        "SetStandbyMode",
        params={"enabled": True, "ruk": "ruk"},
    )
    assert response == success_response
