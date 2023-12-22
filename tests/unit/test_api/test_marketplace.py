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


def test_add_app(client):
    client._get.return_value = success_response
    response = client.Admin.AddApp(
        "env",
        "manifest",
    )
    client._get.assert_called_with(
        "AddApp",
        params={
            "envName": "env",
            "manifest": "manifest",
        },
    )
    assert response == success_response


def test_delete_app(client):
    client._get.return_value = success_response
    response = client.Admin.DeleteApp(
        "env",
        1,
    )
    client._get.assert_called_with(
        "DeleteApp",
        params={
            "envName": "env",
            "id": 1,
        },
    )
    assert response == success_response


def test_edit_app(client):
    client._get.return_value = success_response
    response = client.Admin.EditApp(
        "env",
        1,
        "manifest",
    )
    client._get.assert_called_with(
        "EditApp",
        params={
            "envName": "env",
            "id": 1,
            "manifest": "manifest",
        },
    )
    assert response == success_response


def test_get_app_manifest(client):
    client._get.return_value = success_response
    response = client.Admin.GetAppManifest(
        "env",
        1,
    )
    client._get.assert_called_with(
        "GetAppManifest",
        params={"envName": "env", "id": 1},
    )
    assert response == success_response


def test_get_apps(client):
    client._get.return_value = success_response
    response = client.Admin.GetApps("env", ["search1", "search2", "search3"])
    client._get.assert_called_with(
        "GetApps",
        params={"envName": "env", "search": ["search1", "search2", "search3"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_jps_samples(client):
    client._get.return_value = success_response
    response = client.Admin.GetJpsSamples("env", ["type1", "type2", "type3"])
    client._get.assert_called_with(
        "GetJpsSamples",
        params={"envName": "env", "type": ["type1", "type2", "type3"]},
        delimiter=",",
    )
    assert response == success_response


def test_publish_app(client):
    client._get.return_value = success_response
    response = client.Admin.PublishApp("env", 1)
    client._get.assert_called_with(
        "PublishApp",
        params={"envName": "env", "id": 1},
    )
    assert response == success_response


def test_schedule_apps_sync(client):
    client._get.return_value = success_response
    response = client.Admin.ScheduleAppsSync(
        "env",
    )
    client._get.assert_called_with(
        "ScheduleAppsSync",
        params={
            "envName": "env",
        },
    )
    assert response == success_response


def test_set_setting(client):
    client._get.return_value = success_response
    response = client.Admin.SetSetting(
        "env",
        "name",
        "values",
        [True, False, True],
    )
    client._get.assert_called_with(
        "SetSetting",
        params={
            "envName": "env",
            "name": "name",
            "values": "values",
            "override": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_sync_external_apps(client):
    client._get.return_value = success_response
    response = client.Admin.SyncExternalApps(
        "env",
    )
    client._get.assert_called_with(
        "SyncExternalApps",
        params={
            "envName": "env",
        },
    )
    assert response == success_response


def test_sync_system_apps(client):
    client._get.return_value = success_response
    response = client.Admin.SyncSystemApps(
        "env",
    )
    client._get.assert_called_with(
        "SyncSystemApps",
        params={
            "envName": "env",
        },
    )
    assert response == success_response


def test_unpublish_app(client):
    client._get.return_value = success_response
    response = client.Admin.UnpublishApp("env", 1)
    client._get.assert_called_with(
        "UnpublishApp",
        params={
            "envName": "env",
            "id": 1,
        },
    )
    assert response == success_response


def test_update_app_rating(client):
    client._get.return_value = success_response
    response = client.Admin.UpdateAppRating("env", 1, 9)
    client._get.assert_called_with(
        "UpdateAppRating",
        params={
            "envName": "env",
            "id": 1,
            "rating": 9,
        },
    )
    assert response == success_response


def test_update_app_visibility_levels(client):
    client._get.return_value = success_response
    response = client.Admin.UpdateAppVisibilityLevels("env", 1, "visibility_levels")
    client._get.assert_called_with(
        "UpdateAppVisibilityLevels",
        params={
            "envName": "env",
            "id": 1,
            "visibilityLevels": "visibility_levels",
        },
    )
    assert response == success_response
