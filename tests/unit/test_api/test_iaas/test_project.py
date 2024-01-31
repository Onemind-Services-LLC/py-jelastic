from . import *


def test_create(client):
    client._get.return_value = success_response
    response = client.Project.Create(
        "COLUMBUS",
        "test_project",
        1,
        "test_description",
        "ruk",
    )
    client._get.assert_called_with(
        "Create",
        params={
            "hostGroup": "COLUMBUS",
            "projectName": "test_project",
            "ownerUid": 1,
            "description": "test_description",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_delete(client):
    client._get.return_value = success_response
    response = client.Project.Delete(
        "COLUMBUS",
        "proj1",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "Delete",
        params={
            "hostGroup": "COLUMBUS",
            "projectId": "proj1",
            "ownerUid": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get(client):
    client._get.return_value = success_response
    response = client.Project.Get(
        "COLUMBUS",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "Get",
        params={
            "hostGroup": "COLUMBUS",
            "ownerUid": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_update(client):
    client._get.return_value = success_response
    response = client.Project.Update(
        "COLUMBUS",
        "proj1",
        "New Project Name",
        123,
        "description",
        "ruk",
    )
    client._get.assert_called_with(
        "Update",
        params={
            "hostGroup": "COLUMBUS",
            "projectId": "proj1",
            "projectName": "New Project Name",
            "ownerUid": 123,
            "description": "description",
            "ruk": "ruk",
        },
    )
    assert response == success_response
