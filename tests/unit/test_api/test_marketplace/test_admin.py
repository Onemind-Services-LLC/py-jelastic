from . import *


def test_add_app(client):
    client._get.return_value = success_response
    response = client.Admin.AddApp(
        "env",
        "manifest",
        "ruk"
    )
    client._get.assert_called_with(
        "AddApp",
        params={
            "envName": "env",
            "manifest": "manifest",
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_delete_app(client):
    client._get.return_value = success_response
    response = client.Admin.DeleteApp(
        "env",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteApp",
        params={
            "envName": "env",
            "id": 1,
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_edit_app(client):
    client._get.return_value = success_response
    response = client.Admin.EditApp(
        "env",
        1,
        "manifest",
        "ruk",
    )
    client._get.assert_called_with(
        "EditApp",
        params={
            "envName": "env",
            "id": 1,
            "manifest": "manifest",
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_get_app_manifest(client):
    client._get.return_value = success_response
    response = client.Admin.GetAppManifest(
        "env",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "GetAppManifest",
        params={"envName": "env", "id": 1, "ruk":"ruk"},
    )
    assert response == success_response


def test_get_apps(client):
    client._get.return_value = success_response
    response = client.Admin.GetApps("env", "search", "ruk",)
    client._get.assert_called_with(
        "GetApps", params={"envName": "env", "search": "search", "ruk":"ruk"}
    )
    assert response == success_response


def test_get_jps_samples(client):
    client._get.return_value = success_response
    response = client.Admin.GetJpsSamples("env", "type", "ruk",)
    client._get.assert_called_with(
        "GetJpsSamples", params={"envName": "env", "type": "type", "ruk":"ruk"}
    )
    assert response == success_response


def test_publish_app(client):
    client._get.return_value = success_response
    response = client.Admin.PublishApp("env", 1, "ruk",)
    client._get.assert_called_with(
        "PublishApp",
        params={"envName": "env", "id": 1, "ruk":"ruk"},
    )
    assert response == success_response


def test_schedule_apps_sync(client):
    client._get.return_value = success_response
    response = client.Admin.ScheduleAppsSync(
        "env",
        "ruk",
    )
    client._get.assert_called_with(
        "ScheduleAppsSync",
        params={
            "envName": "env",
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_set_setting(client):
    client._get.return_value = success_response
    response = client.Admin.SetSetting("env", "name", "values", True, "ruk",)
    client._get.assert_called_with(
        "SetSetting",
        params={"envName": "env", "name": "name", "values": "values", "override": True, "ruk":"ruk"},
    )
    assert response == success_response


def test_sync_external_apps(client):
    client._get.return_value = success_response
    response = client.Admin.SyncExternalApps(
        "env",
        "ruk",
    )
    client._get.assert_called_with(
        "SyncExternalApps",
        params={
            "envName": "env",
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_sync_system_apps(client):
    client._get.return_value = success_response
    response = client.Admin.SyncSystemApps(
        "env",
        "ruk",
    )
    client._get.assert_called_with(
        "SyncSystemApps",
        params={
            "envName": "env",
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_unpublish_app(client):
    client._get.return_value = success_response
    response = client.Admin.UnpublishApp("env", 1, "ruk",)
    client._get.assert_called_with(
        "UnpublishApp",
        params={
            "envName": "env",
            "id": 1,
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_update_app_rating(client):
    client._get.return_value = success_response
    response = client.Admin.UpdateAppRating("env", 1, 9, "ruk",)
    client._get.assert_called_with(
        "UpdateAppRating",
        params={
            "envName": "env",
            "id": 1,
            "rating": 9,
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_update_app_visibility_levels(client):
    client._get.return_value = success_response
    response = client.Admin.UpdateAppVisibilityLevels("env", 1, "visibility_levels", "ruk",)
    client._get.assert_called_with(
        "UpdateAppVisibilityLevels",
        params={
            "envName": "env",
            "id": 1,
            "visibilityLevels": "visibility_levels",
            "ruk":"ruk"
        },
    )
    assert response == success_response
