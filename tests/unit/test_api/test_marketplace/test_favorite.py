from . import *


def test_add(client):
    client._get.return_value = success_response
    response = client.Favorite.Add("id")
    client._get.assert_called_with(
        "Add",
        params={"id": "id"},
    )
    assert response == success_response


def test_add_manifest(client):
    client._get.return_value = success_response
    response = client.Favorite.AddManifest("manifest")
    client._get.assert_called_with(
        "AddManifest",
        params={"manifest": "manifest"},
    )
    assert response == success_response


def test_delete(client):
    client._get.return_value = success_response
    response = client.Favorite.Delete("id")
    client._get.assert_called_with(
        "Delete",
        params={"id": "id"},
    )

    assert response == success_response


def test_get_list(client):
    client._get.return_value = success_response
    response = client.Favorite.GetList(
        {"search1": "value1", "search2": "value2", "search3": "value3"},
        "lang",
        "checksum",
    )
    client._get.assert_called_with(
        "GetList",
        params={
            "search": {"search1": "value1", "search2": "value2", "search3": "value3"},
            "lang": "lang",
            "checksum": "checksum",
        },
    )

    assert response == success_response
