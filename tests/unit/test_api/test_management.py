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
        ["search1", "search2", "search3"],
    )
    client._get.assert_called_with(
        "GetAddonList",
        params={
            "envName": "env",
            "nodeGroup": ["nodegroup1", "nodegroup2", "nodegroup3"],
            "search": ["search1", "search2", "search3"],
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
    assert response == success_response


def test_install(client):
    client._get.return_value = success_response
    response = client.App.Install(
        "2",
        ["env1", "env2", "env3"],
        ["setting1", "setting2", "setting3"],
        ["name1", "name2", "name3"],
        ["region1", "region2", "region3"],
        ["envGroup1", "envGroup2", "envGroup3"],
        [87, 46, 3],
        ["node1", "node2", "node3"],
        [False, False, True],
        [False, True, False],
        [False, True, False],
    )
    client._get.assert_called_with(
        "Install",
        params={
            "id": "2",
            "envName": ["env1", "env2", "env3"],
            "settings": ["setting1", "setting2", "setting3"],
            "displayName": ["name1", "name2", "name3"],
            "region": ["region1", "region2", "region3"],
            "envGroups": ["envGroup1", "envGroup2", "envGroup3"],
            "ownerUid": [87, 46, 3],
            "nodes": ["node1", "node2", "node3"],
            "overrideNodes": [False, False, True],
            "skipEmail": [False, True, False],
            "skipNodeEmails": [False, True, False],
        },
        delimiter=",",
    )
    assert response == success_response


def test_install_addon(client):
    client._get.return_value = success_response
    response = client.App.InstallAddon(
        "2",
        ["setting1", "setting2", "setting3"],
        ["nodeGroup1", "nodeGroup2", "nodeGroup3"],
        [False, True, False],
    )
    client._get.assert_called_with(
        "InstallAddon",
        params={
            "id": "2",
            "settings": ["setting1", "setting2", "setting3"],
            "nodeGroup": ["nodeGroup1", "nodeGroup2", "nodeGroup3"],
            "skipEmail": [False, True, False],
        },
        delimiter=",",
    )
    assert response == success_response
