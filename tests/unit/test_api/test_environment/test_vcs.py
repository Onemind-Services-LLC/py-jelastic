from . import *


def test_create_project(client):
    client._get.return_value = success_response
    response = client.Vcs.CreateProject(
        "env_name",
        "type",
        "context",
        "url",
        ["branch1", "branch2"],
        [1, 2],
        ["login1", "login2"],
        ["password1", "password2"],
        [True, True],
        ["interval1", "interval2"],
        [True, True],
        [True, True],
        [True, True],
        ["node_group1", "node_group2"],
        ["hooks1", "hooks2"],
        [1, 1],
        ["repo_hash1", "repo_hash2"],
    )
    client._get.assert_called_with(
        "CreateProject",
        params={
            "envName": "env_name",
            "type": "type",
            "context": "context",
            "url": "url",
            "branch": ["branch1", "branch2"],
            "keyId": [1, 2],
            "login": ["login1", "login2"],
            "password": ["password1", "password2"],
            "autoupdate": [True, True],
            "interval": ["interval1", "interval2"],
            "autoResolveConflict": [True, True],
            "zdt": [True, True],
            "updateNow": [True, True],
            "nodeGroup": ["node_group1", "node_group2"],
            "hooks": ["hooks1", "hooks2"],
            "delay": [1, 1],
            "repoHash": ["repo_hash1", "repo_hash2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_project(client):
    client._get.return_value = success_response
    response = client.Vcs.DeleteProject(
        "env_name", "context", ["node_group1", "node_group2"]
    )
    client._get.assert_called_with(
        "DeleteProject",
        params={
            "envName": "env_name",
            "context": "context",
            "nodeGroup": ["node_group1", "node_group2"],
        },
        delimiter=",",
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
        [1, 2],
        ["login1", "login2"],
        ["password1", "password2"],
        ["interval1", "interval2"],
        ["node_group1", "node_group2"],
        ["hooks1", "hooks2"],
        [1, 1],
        ["repo_hash1", "repo_hash2"],
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
            "keyId": [1, 2],
            "login": ["login1", "login2"],
            "password": ["password1", "password2"],
            "interval": ["interval1", "interval2"],
            "nodeGroup": ["node_group1", "node_group2"],
            "hooks": ["hooks1", "hooks2"],
            "delay": [1, 1],
            "repoHash": ["repo_hash1", "repo_hash2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_project(client):
    client._get.return_value = success_response
    response = client.Vcs.GetProject(
        "env_name", ["context1", "context2"], ["node_group1", "node_group2"]
    )
    client._get.assert_called_with(
        "GetProject",
        params={
            "envName": "env_name",
            "context": ["context1", "context2"],
            "nodeGroup": ["node_group1", "node_group2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_update(client):
    client._get.return_value = success_response
    response = client.Vcs.Update(
        "env_name", "context", ["node_group1", "node_group2"], [1, 2]
    )
    client._get.assert_called_with(
        "Update",
        params={
            "envName": "env_name",
            "context": "context",
            "nodeGroup": ["node_group1", "node_group2"],
            "delay": [1, 2],
        },
        delimiter=",",
    )
    assert response == success_response
