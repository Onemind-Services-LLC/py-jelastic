from . import *


def test_event(client):
    client._get.return_value = success_response
    response = client.System.Event("topic", [True, False])
    client._get.assert_called_with(
        "Event",
        params={"topic": "topic", "publishLocal": [True, False]},
    )
    assert response == success_response


def test_get_api_descriptions(client):
    client._get.return_value = success_response
    response = client.System.GetAPIDescriptions([True, True], [True, True])
    client._get.assert_called_with(
        "GetAPIDescriptions",
        params={"isPublicOnly": [True, True], "isToken": [True, True]},
    )
    assert response == success_response


def test_get_cache_status(client):
    client._get.return_value = success_response
    response = client.System.GetCacheStatus()
    client._get.assert_called_with(
        "GetCacheStatus",
        params={},
    )
    assert response == success_response


def test_get_instance_cache_status(client):
    client._get.return_value = success_response
    response = client.System.GetInstanceCacheStatus()
    client._get.assert_called_with(
        "GetInstanceCacheStatus",
        params={},
    )
    assert response == success_response


def test_get_version(client):
    client._get.return_value = success_response
    response = client.System.GetVersion()
    client._get.assert_called_with(
        "GetVersion",
        params={},
    )
    assert response == success_response


def test_refresh_email_templates(client):
    client._get.return_value = success_response
    response = client.System.RefreshEmailTemplates()
    client._get.assert_called_with(
        "RefreshEmailTemplates",
        params={},
    )
    assert response == success_response


def test_refresh_user(client):
    client._get.return_value = success_response
    response = client.System.RefreshUser("language")
    client._get.assert_called_with(
        "RefreshUser",
        params={"language": "language"},
    )
    assert response == success_response


def test_reload_configuration(client):
    client._get.return_value = success_response
    response = client.System.ReloadConfiguration(
        [1, 1], ["changed_place_holders1", "changed_place_holders2"]
    )
    client._get.assert_called_with(
        "ReloadConfiguration",
        params={
            "resellerId": [1, 1],
            "changedPlaceholders": ["changed_place_holders1", "changed_place_holders2"],
        },
    )
    assert response == success_response
