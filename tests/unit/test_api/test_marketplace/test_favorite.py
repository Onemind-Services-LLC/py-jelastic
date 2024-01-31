from . import *


def test_add(client):
    client._get.return_value = success_response
    response = client.Favorite.Add("id", "ruk")
    client._get.assert_called_with(
        "Add",
        params={"id": "id", "ruk":"ruk"},
    )
    assert response == success_response


def test_add_manifest(client):
    client._get.return_value = success_response
    response = client.Favorite.AddManifest("manifest", "ruk")
    client._get.assert_called_with(
        "AddManifest",
        params={"manifest": "manifest", "ruk":"ruk"},
    )
    assert response == success_response


def test_delete(client):
    client._get.return_value = success_response
    response = client.Favorite.Delete("id", "ruk")
    client._get.assert_called_with(
        "Delete",
        params={"id": "id", "ruk":"ruk"},
    )

    assert response == success_response


def test_get_list(client):
    client._get.return_value = success_response
    response = client.Favorite.GetList(
        {"search1": "value1", "search2": "value2", "search3": "value3"},
        "lang",
        "checksum",
        "ruk"
    )
    client._get.assert_called_with(
        "GetList",
        params={
            "search": {"search1": "value1", "search2": "value2", "search3": "value3"},
            "lang": "lang",
            "checksum": "checksum",
            "ruk":"ruk"
        },
    )

    assert response == success_response
