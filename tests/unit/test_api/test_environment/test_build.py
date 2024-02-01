from . import *


def test_add_project(client):
    client._get.return_value = success_response
    response = client.Build.AddProject(
        True,
        True,
        "env_name",
        1,
        "name",
        "type",
        "path",
        1,
        "login",
        "password",
        "targetEnv",
        "context",
        "branch",
        "interval",
        1,
        True,
        "hooks",
        "workDir",
        "target_node_group",
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "AddProject",
        params={
            "autoUpdate": True,
            "autoResolveConflict": True,
            "envName": "env_name",
            "nodeId": 1,
            "name": "name",
            "type": "type",
            "path": "path",
            "keyId": 1,
            "login": "login",
            "password": "password",
            "targetEnv": "targetEnv",
            "context": "context",
            "branch": "branch",
            "interval": "interval",
            "delay": 1,
            "deployNow": True,
            "hooks": "hooks",
            "workDir": "workDir",
            "targetNodeGroup": "target_node_group",
            "isSequential": True,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_add_project_with_creds(client):
    client._get.return_value = success_response
    response = client.Build.AddProjectWithCreds(
        True,
        True,
        "env_name",
        1,
        "name",
        "type",
        "path",
        "targetEnv",
        "login",
        "password",
        "context",
        "branch",
        "interval",
        1,
        True,
        "hooks",
        "workDir",
        "ruk",
    )
    client._get.assert_called_with(
        "AddProjectWithCreds",
        params={
            "autoUpdate": True,
            "autoResolveConflict": True,
            "envName": "env_name",
            "nodeId": 1,
            "name": "name",
            "type": "type",
            "path": "path",
            "targetEnv": "targetEnv",
            "login": "login",
            "password": "password",
            "context": "context",
            "branch": "branch",
            "interval": "interval",
            "delay": 1,
            "deployNow": True,
            "hooks": "hooks",
            "workDir": "workDir",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_add_project_with_key(client):
    client._get.return_value = success_response
    response = client.Build.AddProjectWithKey(
        True,
        True,
        "env_name",
        1,
        "name",
        "type",
        "path",
        "targetEnv",
        1,
        "context",
        "branch",
        "interval",
        1,
        True,
        "hooks",
        "workDir",
        "ruk",
    )
    client._get.assert_called_with(
        "AddProjectWithKey",
        params={
            "autoUpdate": True,
            "autoResolveConflict": True,
            "envName": "env_name",
            "nodeId": 1,
            "name": "name",
            "type": "type",
            "path": "path",
            "targetEnv": "targetEnv",
            "keyId": 1,
            "context": "context",
            "branch": "branch",
            "interval": "interval",
            "delay": 1,
            "deployNow": True,
            "hooks": "hooks",
            "workDir": "workDir",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_build_deploy(client):
    client._get.return_value = success_response
    response = client.Build.BuildDeploy(
        "env_name",
        "project_name",
        "ruk",
    )
    client._get.assert_called_with(
        "BuildDeploy",
        params={
            "envName": "env_name",
            "projectName": "project_name",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_build_build_deploy_project(client):
    client._get.return_value = success_response
    response = client.Build.BuildDeployProject(
        "env_name",
        1,
        "project_id",
        1,
        True,
        True,
        "ruk",
    )
    assert response == success_response
    client._get.assert_called_with(
        "BuildDeployProject",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "projectid": "project_id",
            "delay": 1,
            "update": True,
            "isSequential": True,
            "ruk": "ruk",
        },
    )


def test_build_build_project(client):
    client._get.return_value = success_response
    response = client.Build.BuildProject(
        "env_name",
        1,
        "project_id",
        True,
        True,
        True,
        "ruk",
    )
    assert response == success_response
    client._get.assert_called_with(
        "BuildProject",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "projectid": "project_id",
            "update": True,
            "skipPublish": True,
            "async": True,
            "ruk": "ruk",
        },
    )


def test_build_deploy_project(client):
    client._get.return_value = success_response
    response = client.Build.DeployProject(
        "env_name",
        1,
        "project_id",
        1,
        True,
        "ruk",
    )
    assert response == success_response
    client._get.assert_called_with(
        "DeployProject",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "projectid": "project_id",
            "delay": 1,
            "isSequential": True,
            "ruk": "ruk",
        },
    )


def test_build_edit_project(client):
    client._get.return_value = success_response
    response = client.Build.EditProject(
        "env_name",
        1,
        1,
        "name",
        "type",
        "path",
        1,
        "login",
        "password",
        "env",
        "context",
        "branch",
        True,
        "interval",
        True,
        1,
        "hooks",
        "workDir",
        "targetNodeGroup",
        "ruk",
    )
    client._get.assert_called_with(
        "EditProject",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "projectid": 1,
            "name": "name",
            "type": "type",
            "path": "path",
            "keyId": 1,
            "login": "login",
            "password": "password",
            "env": "env",
            "context": "context",
            "branch": "branch",
            "autoUpdate": True,
            "interval": "interval",
            "autoResolveConflict": True,
            "delay": 1,
            "hooks": "hooks",
            "workDir": "workDir",
            "targetNodeGroup": "targetNodeGroup",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_build_get_project_info(client):
    client._get.return_value = success_response
    response = client.Build.GetProjectInfo(
        "env_name",
        1,
        1,
        "project",
        "ruk",
    )
    assert response == success_response
    client._get.assert_called_with(
        "GetProjectInfo",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "projectid": 1,
            "projectName": "project",
            "ruk": "ruk",
        },
    )


def test_get_project(client):
    client._get.return_value = success_response
    response = client.Build.GetProjects(
        "env_name",
        "nodeGroup",
        1,
        "ruk",
    )
    assert response == success_response
    client._get.assert_called_with(
        "GetProjects",
        params={
            "envName": "env_name",
            "nodeGroup": "nodeGroup",
            "nodeid": 1,
            "ruk": "ruk",
        },
    )


def test_remove_project(client):
    client._get.return_value = success_response
    response = client.Build.RemoveProject(
        "env_name",
        1,
        1,
        "ruk",
    )
    assert response == success_response
    client._get.assert_called_with(
        "RemoveProject",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "projectid": 1,
            "ruk": "ruk",
        },
    )


def test_build_update(client):
    client._get.return_value = success_response
    response = client.Build.Update(
        "env_name",
        1,
        1,
        "context",
        "ruk",
    )
    assert response == success_response
    client._get.assert_called_with(
        "Update",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "projectId": 1,
            "context": "context",
            "ruk": "ruk",
        },
    )
