from datetime import datetime
from unittest.mock import patch, Mock

import pytest

from jelastic.api import Environment

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}
CURRENT_DATETIME = datetime.now()


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        env = Environment(session=Mock(), token="token")
        env._get = mock_get
        yield env


def test_billing_add_stats(client):
    client._get.return_value = success_response
    response = client.Billing.AddStats(
        "resource_name",
        1,
        CURRENT_DATETIME.date(),
        CURRENT_DATETIME.date(),
        "env_name",
        1,
        1.0,
        "note",
        "value_group",
    )
    client._get.assert_called_with(
        "AddStats",
        params={
            "resourceName": "resource_name",
            "uid": 1,
            "startDate": CURRENT_DATETIME.date(),
            "endDate": CURRENT_DATETIME.date(),
            "envName": "env_name",
            "nodeId": 1,
            "value": 1.0,
            "note": "note",
            "valueGroup": "value_group",
        },
        datetime_format="%Y-%m-%d",
    )

    assert response == success_response


def test_billing_env_resources(client):
    client._get.return_value = success_response
    response = client.Billing.EnvResources(CURRENT_DATETIME, CURRENT_DATETIME)
    client._get.assert_called_with(
        "EnvResources",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_billing_envs_resources(client):
    client._get.return_value = success_response
    response = client.Billing.EnvsResources(
        CURRENT_DATETIME, CURRENT_DATETIME, "app_id", "checksum"
    )
    client._get.assert_called_with(
        "EnvsResources",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "targetAppid": "app_id",
            "checksum": "checksum",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_billing_envs_resources_by_account(client):
    client._get.return_value = success_response
    response = client.Billing.EnvsResourcesByAccount(
        CURRENT_DATETIME, CURRENT_DATETIME, 1, "checksum"
    )
    client._get.assert_called_with(
        "EnvsResourcesByAccount",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "uid": 1,
            "checksum": "checksum",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_billing_get_options(client):
    client._get.return_value = success_response
    response = client.Billing.GetOptions("env_name", "node_group")
    client._get.assert_called_with(
        "GetOptions",
        params={
            "targetEnvName": "env_name",
            "nodeGroup": "node_group",
        },
    )
    assert response == success_response


def test_billing_set_options(client):
    client._get.return_value = success_response
    response = client.Billing.SetOptions("env_name", "node_group", {"key": "value"}, 1)
    client._get.assert_called_with(
        "SetOptions",
        params={
            "targetEnvName": "env_name",
            "nodeGroup": "node_group",
            "options": '{"key": "value"}',
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_export_create(client):
    client._get.return_value = success_response
    response = client.Export.Create({"key": "value"})
    client._get.assert_called_with(
        "Create",
        params={
            "settings": '{"key": "value"}',
        },
    )
    assert response == success_response


def test_export_delete(client):
    client._get.return_value = success_response
    response = client.Export.Delete("test")
    client._get.assert_called_with("Delete", params={"id": "test"})
    assert response == success_response


def test_export_delete_exported_data(client):
    client._get.return_value = success_response
    response = client.Export.DeleteExportedData("env", "file")
    client._get.assert_called_with(
        "DeleteExportedData", params={"envName": "env", "fileName": "file"}
    )
    assert response == success_response


def test_export_get_list(client):
    client._get.return_value = success_response
    response = client.Export.GetList("env")
    client._get.assert_called_with("GetList", params={"envName": "env"})
    assert response == success_response


def test_export_get_manifest(client):
    client._get.return_value = success_response
    response = client.Export.GetManifest("env", "manifest-id")
    client._get.assert_called_with(
        "GetManifest", params={"envName": "env", "id": "manifest-id"}
    )
    assert response == success_response


def test_jerror_error(client):
    client._get.return_value = success_response
    response = client.JError.Error(
        "name", "param", 82, 1, "dummy@example.com", "not found"
    )
    client._get.assert_called_with(
        "Error",
        params={
            "actionName": "name",
            "callParameters": "param",
            "errorCode": 82,
            "priority": 1,
            "email": "dummy@example.com",
            "errorMessage": "not found",
        },
    )
    assert response == success_response


def test_node_send_event(client):
    client._get.return_value = success_response
    response = client.Node.SendEvent({"key": "value"}, "OOM_KILLER")
    client._get.assert_called_with(
        "SendEvent", params={"params": '{"key": "value"}', "eventName": "OOM_KILLER"}
    )
    assert response == success_response


def test_node_send_notification(client):
    client._get.return_value = success_response
    response = client.Node.SendNotification("message", "title")
    client._get.assert_called_with(
        "SendNotification", params={"message": "message", "name": "title"}
    )
    assert response == success_response


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


def test_build_deploy_project(client):
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


def test_build_project(client):
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


def test_deploy_project(client):
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


def test_edit_project(client):
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


def test_get_project_info(client):
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


def test_update(client):
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
