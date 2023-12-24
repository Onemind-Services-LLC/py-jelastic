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
        [1, 1],
        ["login1", "login2"],
        ["password1", "password2"],
        ["target_env1", "target_env2"],
        ["context1", "context2"],
        ["branch1", "branch2"],
        ["interval1", "interval2"],
        [1, 1],
        [True, True],
        ["hooks1", "hooks2"],
        ["work_dir1", "work_dir2"],
        ["target_node_group1", "target_node_group2"],
        [True, True],
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
            "keyId": [1, 1],
            "login": ["login1", "login2"],
            "password": ["password1", "password2"],
            "targetEnv": ["target_env1", "target_env2"],
            "context": ["context1", "context2"],
            "branch": ["branch1", "branch2"],
            "interval": ["interval1", "interval2"],
            "delay": [1, 1],
            "deployNow": [True, True],
            "hooks": ["hooks1", "hooks2"],
            "workDir": ["work_dir1", "work_dir2"],
            "targetNodeGroup": ["target_node_group1", "target_node_group2"],
            "isSequential": [True, True],
        },
        delimiter=",",
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
        ["target_env1", "target_env2"],
        ["login1", "login2"],
        ["password1", "password2"],
        ["context1", "context2"],
        ["branch1", "branch2"],
        ["interval1", "interval2"],
        [1, 1],
        [True, True],
        ["hooks1", "hooks2"],
        ["work_dir1", "work_dir2"],
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
            "targetEnv": ["target_env1", "target_env2"],
            "login": ["login1", "login2"],
            "password": ["password1", "password2"],
            "context": ["context1", "context2"],
            "branch": ["branch1", "branch2"],
            "interval": ["interval1", "interval2"],
            "delay": [1, 1],
            "deployNow": [True, True],
            "hooks": ["hooks1", "hooks2"],
            "workDir": ["work_dir1", "work_dir2"],
        },
        delimiter=",",
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
        ["target_env1", "target_env2"],
        [1, 1],
        ["context1", "context2"],
        ["branch1", "branch2"],
        ["interval1", "interval2"],
        [1, 1],
        [True, True],
        ["hooks1", "hooks2"],
        ["work_dir1", "work_dir2"],
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
            "targetEnv": ["target_env1", "target_env2"],
            "keyId": [1, 1],
            "context": ["context1", "context2"],
            "branch": ["branch1", "branch2"],
            "interval": ["interval1", "interval2"],
            "delay": [1, 1],
            "deployNow": [True, True],
            "hooks": ["hooks1", "hooks2"],
            "workDir": ["work_dir1", "work_dir2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_build_deploy(client):
    client._get.return_value = success_response
    response = client.Build.BuildDeploy("env_name", "project_name")
    client._get.assert_called_with(
        "BuildDeploy",
        params={
            "envName": "env_name",
            "projectName": "project_name",
        },
    )
    assert response == success_response


def test_build_build_deploy_project(client):
    client._get.return_value = success_response
    response = client.Build.BuildDeployProject(
        "env_name", 1, "project_id", [1, 1], [True, False], [True, False]
    )
    assert response == success_response
    client._get.assert_called_with(
        "BuildDeployProject",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "projectid": "project_id",
            "delay": [1, 1],
            "update": [True, False],
            "isSequential": [True, False],
        },
        delimiter=",",
    )


def test_build_build_project(client):
    client._get.return_value = success_response
    response = client.Build.BuildProject(
        "env_name", 1, "project_id", [True, False], [True, False], [True, False]
    )
    assert response == success_response
    client._get.assert_called_with(
        "BuildProject",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "projectid": "project_id",
            "update": [True, False],
            "skipPublish": [True, False],
            "async": [True, False],
        },
        delimiter=",",
    )


def test_build_deploy_project(client):
    client._get.return_value = success_response
    response = client.Build.DeployProject(
        "env_name", 1, "project_id", [1, 1], [True, False]
    )
    assert response == success_response
    client._get.assert_called_with(
        "DeployProject",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "projectid": "project_id",
            "delay": [1, 1],
            "isSequential": [True, False],
        },
        delimiter=",",
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
        [1, 1],
        ["login1", "login2"],
        ["password1", "password2"],
        ["env1", "env2"],
        ["context1", "context2"],
        ["branch1", "branch2"],
        True,
        ["interval1", "interval2"],
        True,
        [1, 1],
        ["hooks1", "hooks2"],
        ["work_dir1", "work_dir2"],
        ["target_node_group1", "target_node_group2"],
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
            "keyId": [1, 1],
            "login": ["login1", "login2"],
            "password": ["password1", "password2"],
            "env": ["env1", "env2"],
            "context": ["context1", "context2"],
            "branch": ["branch1", "branch2"],
            "autoUpdate": True,
            "interval": ["interval1", "interval2"],
            "autoResolveConflict": True,
            "delay": [1, 1],
            "hooks": ["hooks1", "hooks2"],
            "workDir": ["work_dir1", "work_dir2"],
            "targetNodeGroup": ["target_node_group1", "target_node_group2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_build_get_project_info(client):
    client._get.return_value = success_response
    response = client.Build.GetProjectInfo(
        "env_name", 1, [1, 1], ["project1", "project2"]
    )
    assert response == success_response
    client._get.assert_called_with(
        "GetProjectInfo",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "projectid": [1, 1],
            "projectName": ["project1", "project2"],
        },
        delimiter=",",
    )


def test_get_project(client):
    client._get.return_value = success_response
    response = client.Build.GetProjects(
        "env_name", ["node_group1", "node_group2"], [1, 1]
    )
    assert response == success_response
    client._get.assert_called_with(
        "GetProjects",
        params={
            "envName": "env_name",
            "nodeGroup": ["node_group1", "node_group2"],
            "nodeid": [1, 1],
        },
        delimiter=",",
    )


def test_remove_project(client):
    client._get.return_value = success_response
    response = client.Build.RemoveProject("env_name", 1, 1)
    assert response == success_response
    client._get.assert_called_with(
        "RemoveProject",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "projectid": 1,
        },
        delimiter=",",
    )


def test_build_update(client):
    client._get.return_value = success_response
    response = client.Build.Update("env_name", 1, [1, 1], ["context1", "context2"])
    assert response == success_response
    client._get.assert_called_with(
        "Update",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "projectId": [1, 1],
            "context": ["context1", "context2"],
        },
        delimiter=",",
    )
