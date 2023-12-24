from . import *


def test_add_build_project(client):
    client._get.return_value = success_response
    response = client.Deployment.AddBuildProject(
        "env_name",
        1,
        "name",
        "repo",
        {"deployment1": "deployment1", "deployment2": "deployment2"},
        {"settings1": "settings1", "settings2": "settings2"},
        ["hooks1", "hooks2"],
    )
    client._get.assert_called_with(
        "AddBuildProject",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "name": "name",
            "repo": "repo",
            "deployment": {"deployment1": "deployment1", "deployment2": "deployment2"},
            "settings": {"settings1": "settings1", "settings2": "settings2"},
            "hooks": ["hooks1", "hooks2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_repo(client):
    client._get.return_value = success_response
    response = client.Deployment.AddRepo(
        "name",
        "url",
        "type",
        ["branch1", "branch2"],
        [1, 1],
        ["login1", "login2"],
        ["password1", "password2"],
        ["description", "description2"],
    )
    client._get.assert_called_with(
        "AddRepo",
        params={
            "name": "name",
            "url": "url",
            "type": "type",
            "branch": ["branch1", "branch2"],
            "keyId": [1, 1],
            "login": ["login1", "login2"],
            "password": ["password1", "password2"],
            "description": ["description", "description2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_deployment_build_deploy_project(client):
    client._get.return_value = success_response
    response = client.Deployment.BuildDeployProject(
        "env_name", 1, "project", [True, True], [1, 1]
    )
    client._get.assert_called_with(
        "BuildDeployProject",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "project": "project",
            "skipUpdate": [True, True],
            "delay": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_build_project(client):
    client._get.return_value = success_response
    response = client.Deployment.BuildProject(
        "env_name", 1, "project", [True, True], [True, True]
    )
    client._get.assert_called_with(
        "BuildProject",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "project": "project",
            "skipUpload": [True, True],
            "skipUpdate": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_deploy(client):
    client._get.return_value = success_response
    response = client.Deployment.Deploy(
        "env_name",
        "repo",
        "context",
        ["node_group1", "node_group2"],
        [1, 1],
        {"settings1": "settings1", "settings2": "settings2"},
        ["hooks1", "hooks2"],
        [1, 1],
    )
    client._get.assert_called_with(
        "Deploy",
        params={
            "envName": "env_name",
            "repo": "repo",
            "context": "context",
            "nodeGroup": ["node_group1", "node_group2"],
            "buildNodeId": [1, 1],
            "settings": {"settings1": "settings1", "settings2": "settings2"},
            "hooks": ["hooks1", "hooks2"],
            "delay": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_deploy_archive(client):
    client._get.return_value = success_response
    response = client.Deployment.DeployArchive(
        "env_name",
        "file_url",
        "file_name",
        ["node_group1", "node_group2"],
        ["context1", "context2"],
        ["zdt1", "zdt2"],
        ["hooks1", "hooks2"],
        [1, 1],
    )
    client._get.assert_called_with(
        "DeployArchive",
        params={
            "envName": "env_name",
            "fileUrl": "file_url",
            "fileName": "file_name",
            "nodeGroup": ["node_group1", "node_group2"],
            "context": ["context1", "context2"],
            "zdt": ["zdt1", "zdt2"],
            "hooks": ["hooks1", "hooks2"],
            "delay": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_deploy_project(client):
    client._get.return_value = success_response
    response = client.Deployment.DeployProject(
        "env_name",
        1,
        "project",
    )
    client._get.assert_called_with(
        "DeployProject",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "project": "project",
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_build_project(client):
    client._get.return_value = success_response
    response = client.Deployment.EditBuildProject(
        "env_name",
        1,
        "project",
        ["name1", "name2"],
        ["repo1", "repo2"],
        {"deployment1": "deployment1", "deployment2": "deployment2"},
        {"settings1": "settings1", "settings2": "settings2"},
        ["hooks1", "hooks2"],
    )
    client._get.assert_called_with(
        "EditBuildProject",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "project": "project",
            "name": ["name1", "name2"],
            "repo": ["repo1", "repo2"],
            "deployment": {"deployment1": "deployment1", "deployment2": "deployment2"},
            "settings": {"settings1": "settings1", "settings2": "settings2"},
            "hooks": ["hooks1", "hooks2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_project(client):
    client._get.return_value = success_response
    response = client.Deployment.EditProject(
        "env_name",
        "node_group",
        "context",
        ["new_context1", "new_context2"],
        ["repo1", "repo2"],
        {"settings1": "settings1", "settings2": "settings2"},
        ["hooks1", "hooks2"],
        [1, 2],
    )
    client._get.assert_called_with(
        "EditProject",
        params={
            "envName": "env_name",
            "nodeGroup": "node_group",
            "context": "context",
            "newContext": ["new_context1", "new_context2"],
            "repo": ["repo1", "repo2"],
            "settings": {"settings1": "settings1", "settings2": "settings2"},
            "hooks": ["hooks1", "hooks2"],
            "delay": [1, 2],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_repo(client):
    client._get.return_value = success_response
    response = client.Deployment.EditRepo(
        1,
        ["name1", "name2"],
        ["type1", "type2"],
        ["url1", "url2"],
        ["branch1", "branch2"],
        [1, 1],
        ["login1", "login2"],
        ["password1", "password2"],
        ["description", "description2"],
    )
    client._get.assert_called_with(
        "EditRepo",
        params={
            "id": 1,
            "name": ["name1", "name2"],
            "type": ["type1", "type2"],
            "url": ["url1", "url2"],
            "branch": ["branch1", "branch2"],
            "keyId": [1, 1],
            "login": ["login1", "login2"],
            "password": ["password1", "password2"],
            "description": ["description", "description2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_build_project_info(client):
    client._get.return_value = success_response
    response = client.Deployment.GetBuildProjectInfo("env_name", 1, "project")
    client._get.assert_called_with(
        "GetBuildProjectInfo",
        params={"envName": "env_name", "nodeId": 1, "project": "project"},
        delimiter=",",
    )
    assert response == success_response


def test_get_build_project(client):
    client._get.return_value = success_response
    response = client.Deployment.GetBuildProjects(
        "env_name", ["node_group1", "node_group2"], [1, 2]
    )
    client._get.assert_called_with(
        "GetBuildProjects",
        params={
            "envName": "env_name",
            "nodeGroup": ["node_group1", "node_group2"],
            "nodeId": [1, 2],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_deployments(client):
    client._get.return_value = success_response
    response = client.Deployment.GetDeployments("env_name", "node_group")
    client._get.assert_called_with(
        "GetDeployments",
        params={"envName": "env_name", "nodeGroup": "node_group"},
        delimiter=",",
    )
    assert response == success_response


def test_get_hooks(client):
    client._get.return_value = success_response
    response = client.Deployment.GetHooks(
        "env_name",
        ["node_group1", "node_group2"],
        [1, 2],
        ["context1", "context2"],
        ["project1", "project2"],
    )
    client._get.assert_called_with(
        "GetHooks",
        params={
            "envName": "env_name",
            "nodeGroup": ["node_group1", "node_group2"],
            "nodeId": [1, 2],
            "context": ["context1", "context2"],
            "project": ["project1", "project2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_project_info(client):
    client._get.return_value = success_response
    response = client.Deployment.GetProjectInfo(
        "env_name", "context", ["node_group1", "node_group2"]
    )
    client._get.assert_called_with(
        "GetProjectInfo",
        params={
            "envName": "env_name",
            "context": "context",
            "nodeGroup": ["node_group1", "node_group2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_repos(client):
    client._get.return_value = success_response
    response = client.Deployment.GetRepos([1, 2])
    client._get.assert_called_with(
        "GetRepos",
        params={"id": [1, 2]},
        delimiter=",",
    )
    assert response == success_response


def test_remove_build_project(client):
    client._get.return_value = success_response
    response = client.Deployment.RemoveBuildProject("env_name", 1, "project")
    client._get.assert_called_with(
        "RemoveBuildProject",
        params={"envName": "env_name", "nodeId": 1, "project": "project"},
        delimiter=",",
    )
    assert response == success_response


def test_remove_repos(client):
    client._get.return_value = success_response
    response = client.Deployment.RemoveRepo(1)
    client._get.assert_called_with("RemoveRepo", params={"id": 1})
    assert response == success_response


def test_rename_context(client):
    client._get.return_value = success_response
    response = client.Deployment.RenameContext(
        "env_name",
        "node_group",
        "old_context",
        "new_context",
    )
    client._get.assert_called_with(
        "RenameContext",
        params={
            "envName": "env_name",
            "nodeGroup": "node_group",
            "oldContext": "old_context",
            "newContext": "new_context",
        },
    )
    assert response == success_response


def test_undeploy(client):
    client._get.return_value = success_response
    response = client.Deployment.Undeploy("env_name", "node_group", "context")
    client._get.assert_called_with(
        "Undeploy",
        params={
            "envName": "env_name",
            "nodeGroup": "node_group",
            "context": "context",
        },
    )
    assert response == success_response


def test_update(client):
    client._get.return_value = success_response
    response = client.Deployment.Update(
        "env_name",
        ["node_group1", "node_group2"],
        [1, 2],
        ["context1", "context2"],
        ["project1", "project2"],
        ["delay1", "delay2"],
    )
    client._get.assert_called_with(
        "Update",
        params={
            "envName": "env_name",
            "nodeGroup": ["node_group1", "node_group2"],
            "nodeId": [1, 2],
            "context": ["context1", "context2"],
            "project": ["project1", "project2"],
            "delay": ["delay1", "delay2"],
        },
        delimiter=",",
    )
    assert response == success_response
