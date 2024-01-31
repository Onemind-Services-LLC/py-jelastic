from . import *


def test_event(client):
    client._get.return_value = success_response
    response = client.System.Event(
        "topic",
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "Event",
        params={"topic": "topic", "publishLocal": True, "ruk": "ruk"},
    )
    assert response == success_response


def test_get_api_descriptions(client):
    client._get.return_value = success_response
    response = client.System.GetAPIDescriptions(
        True,
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "GetAPIDescriptions",
        params={"isPublicOnly": True, "isToken": True, "ruk": "ruk"},
    )
    assert response == success_response


def test_get_cache_status(client):
    client._get.return_value = success_response
    response = client.System.GetCacheStatus(
        "ruk",
    )
    client._get.assert_called_with(
        "GetCacheStatus",
        params={"ruk": "ruk"},
    )
    assert response == success_response


def test_get_instance_cache_status(client):
    client._get.return_value = success_response
    response = client.System.GetInstanceCacheStatus(
        "ruk",
    )
    client._get.assert_called_with(
        "GetInstanceCacheStatus",
        params={"ruk": "ruk"},
    )
    assert response == success_response


def test_get_version(client):
    client._get.return_value = success_response
    response = client.System.GetVersion(
        "ruk",
    )
    client._get.assert_called_with(
        "GetVersion",
        params={"ruk": "ruk"},
    )
    assert response == success_response


def test_refresh_email_templates(client):
    client._get.return_value = success_response
    response = client.System.RefreshEmailTemplates(
        "ruk",
    )
    client._get.assert_called_with(
        "RefreshEmailTemplates",
        params={"ruk": "ruk"},
    )
    assert response == success_response


def test_refresh_user(client):
    client._get.return_value = success_response
    response = client.System.RefreshUser(
        "language",
        "ruk",
    )
    client._get.assert_called_with(
        "RefreshUser",
        params={"language": "language", "ruk": "ruk"},
    )
    assert response == success_response


def test_reload_configuration(client):
    client._get.return_value = success_response
    response = client.System.ReloadConfiguration(
        1,
        "changedPlaceholders",
        "ruk",
    )
    client._get.assert_called_with(
        "ReloadConfiguration",
        params={
            "resellerId": 1,
            "changedPlaceholders": "changedPlaceholders",
            "ruk": "ruk",
        },
    )
    assert response == success_response
