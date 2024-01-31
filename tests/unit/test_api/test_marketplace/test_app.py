from . import *


def test_add_app(client):
    client._get.return_value = success_response
    response = client.App.AddApp("manifest", "ruk",)
    client._get.assert_called_with(
        "AddApp",
        params={
            "manifest": "manifest",
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_delete_app(client):
    client._get.return_value = success_response
    response = client.App.DeleteApp("1", "ruk",)
    client._get.assert_called_with(
        "DeleteApp",
        params={
            "id": "1",
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_edit_app(client):
    client._get.return_value = success_response
    response = client.App.EditApp(
        "1",
        "manifest",
        "ruk",
    )
    client._get.assert_called_with(
        "EditApp",
        params={
            "id": "1",
            "manifest": "manifest",
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_get_addon_list(client):
    client._get.return_value = success_response
    response = client.App.GetAddonList(
        "env",
        "nodeGroup",
        {"search1": "value1", "search2": "value2", "search3": "value3"},
        "ruk",
    )
    client._get.assert_called_with(
        "GetAddonList",
        params={
            "envName": "env",
            "nodeGroup": "nodeGroup",
            "search": {"search1": "value1", "search2": "value2", "search3": "value3"},
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_get_app_info(client):
    client._get.return_value = success_response
    response = client.App.GetAppInfo("1", "lang", 1, "ruk",)
    client._get.assert_called_with(
        "GetAppInfo",
        params={"id": "1", "lang": "lang", "ownerUid": 1, "ruk":"ruk"},
    )
    assert response == success_response


def test_get_categories(client):
    client._get.return_value = success_response
    response = client.App.GetCategories("ruk")
    client._get.assert_called_with(
        "GetCategories",
        params={"ruk":"ruk"},
    )
    assert response == success_response


def test_get_checksum(client):
    client._get.return_value = success_response
    response = client.App.GetChecksum("ruk")
    client._get.assert_called_with(
        "GetChecksum",
        params={"ruk":"ruk"},
    )
    assert response == success_response


def test_get_list(client):
    client._get.return_value = success_response
    response = client.App.GetList("search", "ruk")
    client._get.assert_called_with(
        "GetList",
        params={"search": "search", "ruk":"ruk"},
    )
    assert response == success_response


def test_install(client):
    client._get.return_value = success_response
    response = client.App.Install(
        "2",
        "envName",
        {
            "settings1": "value1",
            "settings2": "value2",
            "settings3": "value3",
            "settings4": "value4",
        },
        "displayName",
        "region",
        "envGroups",
        1,
        "nodes",
        False,
        False,
        False,
        "ruk"
    )
    client._get.assert_called_with(
        "Install",
        params={
            "id": "2",
            "envName": "envName",
            "settings": {
                "settings1": "value1",
                "settings2": "value2",
                "settings3": "value3",
                "settings4": "value4",
            },
            "displayName": "displayName",
            "region": "region",
            "envGroups": "envGroups",
            "ownerUid": 1,
            "nodes": "nodes",
            "overrideNodes": False,
            "skipEmail": False,
            "skipNodeEmails": False,
            "ruk":"ruk"
        },
    )
    assert response == success_response


def test_install_addon(client):
    client._get.return_value = success_response
    response = client.App.InstallAddon(
        "env",
        "id",
        {"settings1": "value1", "settings2": "value2", "settings3": "value3"},
        "nodeGroup",
        "skip_email",
        "ruk"
    )
    client._get.assert_called_with(
        "InstallAddon",
        params={
            "envName": "env",
            "id": "id",
            "settings": {
                "settings1": "value1",
                "settings2": "value2",
                "settings3": "value3",
            },
            "nodeGroup": "nodeGroup",
            "skipEmail": "skip_email",
            "ruk":"ruk"
        },
    )
    assert response == success_response
