from . import *


def test_clean_check_request_cache(client):
    client._get.return_value = success_response
    response = client.System.CleanCheckRequestCache(
        1,
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "CleanCheckRequestCache",
        params={
            "uid": 1,
            "localOnly": True,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_event_Sys(client):
    client._get.return_value = success_response
    response = client.System.Event(
        "topic",
        "message",
        True,
        "ruk",
    )
    client._get.assert_called_with(
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
    response = client.System.GetAPIDescriptions(
        False,
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "GetAPIDescriptions",
        params={
            "isPublicOnly": False,
            "isToken": True,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_auto_percent(client):
    client._get.return_value = success_response
    response = client.System.GetAutoPercent(
        "ruk",
    )
    client._get.assert_called_with(
        "GetAutoPercent",
        params={
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_cache_stats(client):
    client._get.return_value = success_response
    response = client.System.GetCacheStats(
        "ruk",
    )
    client._get.assert_called_with(
        "GetCacheStats",
        params={
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_cache_status(client):
    client._get.return_value = success_response
    response = client.System.GetCacheStatus(
        "ruk",
    )
    client._get.assert_called_with(
        "GetCacheStatus",
        params={
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_instance_cache_status(client):
    client._get.return_value = success_response
    response = client.System.GetInstanceCacheStatus(
        "ruk",
    )
    client._get.assert_called_with(
        "GetInstanceCacheStatus",
        params={
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_status(client):
    client._get.return_value = success_response
    response = client.System.GetStatus(
        "checksum",
        "ruk",
    )
    client._get.assert_called_with(
        "GetStatus",
        params={
            "checksum": "checksum",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_version(client):
    client._get.return_value = success_response
    response = client.System.GetVersion(
        "ruk",
    )
    client._get.assert_called_with(
        "GetVersion",
        params={
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_refresh_email_templates(client):
    client._get.return_value = success_response
    response = client.System.RefreshEmailTemplates(
        "ruk",
    )
    client._get.assert_called_with(
        "RefreshEmailTemplates",
        params={
            "ruk": "ruk",
        },
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
        params={
            "language": "language",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_reload_configuration(client):
    client._get.return_value = success_response
    response = client.System.ReloadConfiguration(
        1,
        "place holder",
        "ruk",
    )
    client._get.assert_called_with(
        "ReloadConfiguration",
        params={
            "resellerId": 1,
            "changedPlaceholders": "place holder",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_send_email(client):
    client._get.return_value = success_response
    response = client.System.SendEmail(
        "template",
        "test1@email.com",
        "language",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "SendEmail",
        params={
            "template": "template",
            "email": "test1@email.com",
            "language": "language",
            "timeout": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_validate(client):
    client._get.return_value = success_response
    response = client.System.Validate(
        "ruk",
    )
    client._get.assert_called_with(
        "Validate",
        params={
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_validate_all(client):
    client._get.return_value = success_response
    response = client.System.ValidateAll(
        "ruk",
    )
    client._get.assert_called_with(
        "ValidateAll",
        params={
            "ruk": "ruk",
        },
    )
    assert response == success_response
