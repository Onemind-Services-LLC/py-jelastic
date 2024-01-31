from . import *


def test_create_project(client):
    client._get.return_value = success_response
    response = client.Vcs.CreateProject(
        "env_name",
        "type",
        "context",
        "url",
        "branch",
        1,
        "login",
        "password",
        True,
        "interval",
        True,
        True,
        True,
        "nodeGroup",
        "hooks",
        1,
        "repoHash",
        "ruk",
    )
    client._get.assert_called_with(
        "CreateProject",
        params={
            "envName": "env_name",
            "type": "type",
            "context": "context",
            "url": "url",
            "branch": "branch",
            "keyId": 1,
            "login": "login",
            "password": "password",
            "autoupdate": True,
            "interval": "interval",
            "autoResolveConflict": True,
            "zdt": True,
            "updateNow": True,
            "nodeGroup": "nodeGroup",
            "hooks": "hooks",
            "delay": 1,
            "repoHash": "repoHash",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_delete_project(client):
    client._get.return_value = success_response
    response = client.Vcs.DeleteProject(
        "env_name",
        "context",
        "nodeGroup",
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteProject",
        params={
            "envName": "env_name",
            "context": "context",
            "nodeGroup": "nodeGroup",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_edit_project(client):
    client._get.return_value = success_response
    response = client.Vcs.EditProject(
        "env_name",
        "type",
        "oldcontext",
        "newcontext",
        "url",
        "branch",
        True,
        True,
        True,
        1,
        "login",
        "password",
        "interval",
        "nodeGroup",
        "hooks",
        1,
        "repoHash",
        "ruk",
    )
    client._get.assert_called_with(
        "EditProject",
        params={
            "envName": "env_name",
            "type": "type",
            "oldcontext": "oldcontext",
            "newcontext": "newcontext",
            "url": "url",
            "branch": "branch",
            "autoupdate": True,
            "autoResolveConflict": True,
            "zdt": True,
            "keyId": 1,
            "login": "login",
            "password": "password",
            "interval": "interval",
            "nodeGroup": "nodeGroup",
            "hooks": "hooks",
            "delay": 1,
            "repoHash": "repoHash",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_project(client):
    client._get.return_value = success_response
    response = client.Vcs.GetProject(
        "env_name",
        "context",
        "nodeGroup",
        "ruk",
    )
    client._get.assert_called_with(
        "GetProject",
        params={
            "envName": "env_name",
            "context": "context",
            "nodeGroup": "nodeGroup",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_update(client):
    client._get.return_value = success_response
    response = client.Vcs.Update(
        "env_name",
        "context",
        "nodeGroup",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "Update",
        params={
            "envName": "env_name",
            "context": "context",
            "nodeGroup": "nodeGroup",
            "delay": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response
