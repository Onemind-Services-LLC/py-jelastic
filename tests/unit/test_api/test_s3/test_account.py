from . import *


def test_create(client):
    client._get.return_value = success_response
    response = client.Account.Create("COLUMBUS", "test_project", 1)
    client._get.assert_called_with(
        "Create",
        params={
            "hostGroup": "COLUMBUS",
            "name": "test_project",
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_delete(client):
    client._get.return_value = success_response
    response = client.Account.Delete("COLUMBUS", "proj1", 1)
    client._get.assert_called_with(
        "Delete",
        params={
            "hostGroup": "COLUMBUS",
            "name": "proj1",
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_generate_keys(client):
    client._get.return_value = success_response
    response = client.Account.GenerateKey("COLUMBUS", "proj1", 1)
    client._get.assert_called_with(
        "GenerateKey",
        params={
            "hostGroup": "COLUMBUS",
            "ownerUid": 1,
            "name": "proj1",
        },
    )
    assert response == success_response


def test_get_keys(client):
    client._get.return_value = success_response
    response = client.Account.GetKeys(1)
    client._get.assert_called_with(
        "GetKeys",
        params={
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_regenerate_keys(client):
    client._get.return_value = success_response
    response = client.Account.RegenerateKeys("COLUMBUS", "access_key", 1)
    client._get.assert_called_with(
        "RegenerateKeys",
        params={
            "hostGroup": "COLUMBUS",
            "ownerUid": 1,
            "accKey": "access_key",
        },
    )
    assert response == success_response


def test_revoke_key(client):
    client._get.return_value = success_response
    response = client.Account.RevokeKey("COLUMBUS", "access_key", 123)
    client._get.assert_called_with(
        "RevokeKey",
        params={
            "hostGroup": "COLUMBUS",
            "ownerUid": 123,
            "accKey": "access_key",
        },
    )
    assert response == success_response
