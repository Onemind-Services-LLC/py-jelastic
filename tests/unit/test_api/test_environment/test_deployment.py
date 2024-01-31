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
        "hooks","ruk",
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
            "hooks": "hooks","ruk": "ruk",
        },
    )
    assert response == success_response


def test_add_repo(client):
    client._get.return_value = success_response
    response = client.Deployment.AddRepo(
        "name", "url", "type", "branch", 1, "login", "password", "description","ruk",
    )
    client._get.assert_called_with(
        "AddRepo",
        params={
            "name": "name",
            "url": "url",
            "type": "type",
            "branch": "branch",
            "keyId": 1,
            "login": "login",
            "password": "password",
            "description": "description","ruk": "ruk",
        },
    )
    assert response == success_response


def test_deployment_build_deploy_project(client):
    client._get.return_value = success_response
    response = client.Deployment.BuildDeployProject("env_name", 1, "project", True, 1,"ruk",)
    client._get.assert_called_with(
        "BuildDeployProject",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "project": "project",
            "skipUpdate": True,
            "delay": 1,"ruk": "ruk",
        },
    )
    assert response == success_response


def test_build_project(client):
    client._get.return_value = success_response
    response = client.Deployment.BuildProject("env_name", 1, "project", True, True,"ruk",)
    client._get.assert_called_with(
        "BuildProject",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "project": "project",
            "skipUpload": True,
            "skipUpdate": True,"ruk": "ruk",
        },
    )
    assert response == success_response


def test_deploy(client):
    client._get.return_value = success_response
    response = client.Deployment.Deploy(
        "env_name",
        "repo",
        "context",
        "nodeGroup",
        1,
        {"settings1": "settings1", "settings2": "settings2"},
        "hooks",
        1,"ruk",
    )
    client._get.assert_called_with(
        "Deploy",
        params={
            "envName": "env_name",
            "repo": "repo",
            "context": "context",
            "nodeGroup": "nodeGroup",
            "buildNodeId": 1,
            "settings": {"settings1": "settings1", "settings2": "settings2"},
            "hooks": "hooks",
            "delay": 1,"ruk": "ruk",
        },
    )
    assert response == success_response


def test_deploy_archive(client):
    client._get.return_value = success_response
    response = client.Deployment.DeployArchive(
        "env_name", "file_url", "file_name", "nodeGroup", "context", "zdt", "hooks", 1,"ruk",
    )
    client._get.assert_called_with(
        "DeployArchive",
        params={
            "envName": "env_name",
            "fileUrl": "file_url",
            "fileName": "file_name",
            "nodeGroup": "nodeGroup",
            "context": "context",
            "zdt": "zdt",
            "hooks": "hooks",
            "delay": 1,"ruk": "ruk",
        },
    )
    assert response == success_response


def test_deploy_project(client):
    client._get.return_value = success_response
    response = client.Deployment.DeployProject(
        "env_name",
        1,
        "project","ruk",
    )
    client._get.assert_called_with(
        "DeployProject",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "project": "project","ruk": "ruk",
        },
    )
    assert response == success_response


def test_edit_build_project(client):
    client._get.return_value = success_response
    response = client.Deployment.EditBuildProject(
        "env_name",
        1,
        "project",
        "name",
        "repo",
        {"deployment1": "deployment1", "deployment2": "deployment2"},
        {"settings1": "settings1", "settings2": "settings2"},
        "hooks","ruk",
    )
    client._get.assert_called_with(
        "EditBuildProject",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "project": "project",
            "name": "name",
            "repo": "repo",
            "deployment": {"deployment1": "deployment1", "deployment2": "deployment2"},
            "settings": {"settings1": "settings1", "settings2": "settings2"},
            "hooks": "hooks","ruk": "ruk",
        },
    )
    assert response == success_response


def test_edit_project(client):
    client._get.return_value = success_response
    response = client.Deployment.EditProject(
        "env_name",
        "node_group",
        "context",
        "newContext",
        "repo",
        {"settings1": "settings1", "settings2": "settings2"},
        "hooks",
        1,"ruk",
    )
    client._get.assert_called_with(
        "EditProject",
        params={
            "envName": "env_name",
            "nodeGroup": "node_group",
            "context": "context",
            "newContext": "newContext",
            "repo": "repo",
            "settings": {"settings1": "settings1", "settings2": "settings2"},
            "hooks": "hooks",
            "delay": 1,"ruk": "ruk",
        },
    )
    assert response == success_response


def test_edit_repo(client):
    client._get.return_value = success_response
    response = client.Deployment.EditRepo(
        1, "name", "type", "url", "branch", 1, "login", "password", "description","ruk",
    )
    client._get.assert_called_with(
        "EditRepo",
        params={
            "id": 1,
            "name": "name",
            "type": "type",
            "url": "url",
            "branch": "branch",
            "keyId": 1,
            "login": "login",
            "password": "password",
            "description": "description","ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_build_project_info(client):
    client._get.return_value = success_response
    response = client.Deployment.GetBuildProjectInfo("env_name", 1, "project","ruk",)
    client._get.assert_called_with(
        "GetBuildProjectInfo",
        params={"envName": "env_name", "nodeId": 1, "project": "project","ruk": "ruk",},
    )
    assert response == success_response


def test_get_build_project(client):
    client._get.return_value = success_response
    response = client.Deployment.GetBuildProjects("env_name", "nodeGroup", 1,"ruk",)
    client._get.assert_called_with(
        "GetBuildProjects",
        params={"envName": "env_name", "nodeGroup": "nodeGroup", "nodeId": 1,"ruk": "ruk",},
    )
    assert response == success_response


def test_get_deployments(client):
    client._get.return_value = success_response
    response = client.Deployment.GetDeployments("env_name", "node_group","ruk",)
    client._get.assert_called_with(
        "GetDeployments", params={"envName": "env_name", "nodeGroup": "node_group","ruk": "ruk",}
    )
    assert response == success_response


def test_get_hooks(client):
    client._get.return_value = success_response
    response = client.Deployment.GetHooks(
        "env_name", "nodeGroup", 1, "context", "project","ruk",
    )
    client._get.assert_called_with(
        "GetHooks",
        params={
            "envName": "env_name",
            "nodeGroup": "nodeGroup",
            "nodeId": 1,
            "context": "context",
            "project": "project","ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_project_info(client):
    client._get.return_value = success_response
    response = client.Deployment.GetProjectInfo("env_name", "context", "nodeGroup","ruk",)
    client._get.assert_called_with(
        "GetProjectInfo",
        params={"envName": "env_name", "context": "context", "nodeGroup": "nodeGroup","ruk": "ruk",},
    )
    assert response == success_response


def test_get_repos(client):
    client._get.return_value = success_response
    response = client.Deployment.GetRepos(1,"ruk",)
    client._get.assert_called_with("GetRepos", params={"id": 1,"ruk": "ruk",})
    assert response == success_response


def test_remove_build_project(client):
    client._get.return_value = success_response
    response = client.Deployment.RemoveBuildProject("env_name", 1, "project","ruk",)
    client._get.assert_called_with(
        "RemoveBuildProject",
        params={"envName": "env_name", "nodeId": 1, "project": "project","ruk": "ruk",},
    )
    assert response == success_response


def test_remove_repos(client):
    client._get.return_value = success_response
    response = client.Deployment.RemoveRepo(1,"ruk",)
    client._get.assert_called_with("RemoveRepo", params={"id": 1,"ruk": "ruk",})
    assert response == success_response


def test_rename_context(client):
    client._get.return_value = success_response
    response = client.Deployment.RenameContext(
        "env_name",
        "node_group",
        "old_context",
        "new_context","ruk",
    )
    client._get.assert_called_with(
        "RenameContext",
        params={
            "envName": "env_name",
            "nodeGroup": "node_group",
            "oldContext": "old_context",
            "newContext": "new_context","ruk": "ruk",
        },
    )
    assert response == success_response


def test_undeploy(client):
    client._get.return_value = success_response
    response = client.Deployment.Undeploy("env_name", "node_group", "context","ruk",)
    client._get.assert_called_with(
        "Undeploy",
        params={
            "envName": "env_name",
            "nodeGroup": "node_group",
            "context": "context","ruk": "ruk",
        },
    )
    assert response == success_response


def test_update(client):
    client._get.return_value = success_response
    response = client.Deployment.Update(
        "env_name", "nodeGroup", 1, "context", "project", "delay","ruk",
    )
    client._get.assert_called_with(
        "Update",
        params={
            "envName": "env_name",
            "nodeGroup": "nodeGroup",
            "nodeId": 1,
            "context": "context",
            "project": "project",
            "delay": "delay","ruk": "ruk",
        },
    )
    assert response == success_response
