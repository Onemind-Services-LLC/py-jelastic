from . import *


def test_add_app(client):
    client._get.return_value = success_response
    response = client.App.AddApp("manifest")
    client._get.assert_called_with(
        "AddApp",
        params={
            "manifest": "manifest",
        },
    )
    assert response == success_response


def test_delete_app(client):
    client._get.return_value = success_response
    response = client.App.DeleteApp("1")
    client._get.assert_called_with(
        "DeleteApp",
        params={
            "id": "1",
        },
    )
    assert response == success_response


def test_edit_app(client):
    client._get.return_value = success_response
    response = client.App.EditApp(
        "1",
        "manifest",
    )
    client._get.assert_called_with(
        "EditApp",
        params={
            "id": "1",
            "manifest": "manifest",
        },
    )
    assert response == success_response


def test_get_addon_list(client):
    client._get.return_value = success_response
    response = client.App.GetAddonList(
        "env",
        ["nodegroup1", "nodegroup2", "nodegroup3"],
        {"search1": "value1", "search2": "value2", "search3": "value3"},
    )
    client._get.assert_called_with(
        "GetAddonList",
        params={
            "envName": "env",
            "nodeGroup": ["nodegroup1", "nodegroup2", "nodegroup3"],
            "search": {"search1": "value1", "search2": "value2", "search3": "value3"},
        },
    )
    assert response == success_response


def test_get_app_info(client):
    client._get.return_value = success_response
    response = client.App.GetAppInfo(
        "1",
        ["lang1", "lang2", "lang3"],
        [3, 2, 5],
    )
    client._get.assert_called_with(
        "GetAppInfo",
        params={
            "id": "1",
            "lang": ["lang1", "lang2", "lang3"],
            "ownerUid": [3, 2, 5],
        },
    )
    assert response == success_response


def test_get_categories(client):
    client._get.return_value = success_response
    response = client.App.GetCategories()
    client._get.assert_called_with(
        "GetCategories",
        params={},
    )
    assert response == success_response


def test_get_checksum(client):
    client._get.return_value = success_response
    response = client.App.GetChecksum()
    client._get.assert_called_with(
        "GetChecksum",
        params={},
    )
    assert response == success_response


def test_get_list(client):
    client._get.return_value = success_response
    response = client.App.GetList(["search1", "search2", "search3"])
    client._get.assert_called_with(
        "GetList",
        params={"search": ["search1", "search2", "search3"]},
    )
    response = client.Favorite.GetList(
        "search",
        "lang",
        "checksum",
    )
    assert response == success_response


def test_install(client):
    client._get.return_value = success_response
    response = client.App.Install(
        "netbox",
        "envName",
        {"key": "value"},
        "displayName",
        "region",
        ["envGroup1", "envGroup2", "envGroup3"],
        123,
        {"node1": "node1", "node2": "node2", "node3": "node3"},
        True,
        True,
        True,
    )
    client._get.assert_called_with(
        "Install",
        params={
            "id": "netbox",
            "envName": "envName",
            "settings": {"key": "value"},
            "displayName": "displayName",
            "region": "region",
            "envGroups": ["envGroup1", "envGroup2", "envGroup3"],
            "ownerUid": 123,
            "nodes": {"node1": "node1", "node2": "node2", "node3": "node3"},
            "overrideNodes": True,
            "skipEmail": True,
            "skipNodeEmails": True,
        },
    )
    assert response == success_response
