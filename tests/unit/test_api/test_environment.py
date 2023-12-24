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


def test_add_domains(client):
    client._get.return_value = success_response
    response = client.Binder.AddDomains(
        "env_name",
        "domains",
        ["node_group1", "node_group2"],
        [1, 2],
        ["subdomain1", "subdomain2"],
    )
    client._get.assert_called_with(
        "AddDomains",
        params={
            "envName": "env_name",
            "domains": "domains",
            "nodeGroup": ["node_group1", "node_group2"],
            "nodeId": [1, 2],
            "subdomain": ["subdomain1", "subdomain2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_ssl_cert(client):
    client._get.return_value = success_response
    response = client.Binder.AddSSLCert(
        "env_name", "key", "cert", ["interm1", "interm2"]
    )
    client._get.assert_called_with(
        "AddSSLCert",
        params={
            "envName": "env_name",
            "key": "key",
            "cert": "cert",
            "interm": ["interm1", "interm2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_attach_ext_ip(client):
    client._get.return_value = success_response
    response = client.Binder.AttachExtIp("env_name", "nodeid", ["type1", "type2"])
    client._get.assert_called_with(
        "AttachExtIp",
        params={"envName": "env_name", "nodeid": "nodeid", "type": ["type1", "type2"]},
        delimiter=",",
    )
    assert response == success_response


def test_bind_ext_domain(client):
    client._get.return_value = success_response
    response = client.Binder.BindExtDomain("env_name", "extdomain", [1, 2])
    client._get.assert_called_with(
        "BindExtDomain",
        params={"envName": "env_name", "extdomain": "extdomain", "certId": [1, 2]},
        delimiter=",",
    )
    assert response == success_response


def test_bind_ext_domains(client):
    client._get.return_value = success_response
    response = client.Binder.BindExtDomains("env_name", "extdomains", [1, 2])
    client._get.assert_called_with(
        "BindExtDomains",
        params={"envName": "env_name", "extdomains": "extdomains", "certId": [1, 2]},
        delimiter=",",
    )
    assert response == success_response


def test_bind_ssl(client):
    client._get.return_value = success_response
    response = client.Binder.BindSSL("env_name", "cert_key", "cert", "intermediate")
    client._get.assert_called_with(
        "BindSSL",
        params={
            "envName": "env_name",
            "cert_key": "cert_key",
            "cert": "cert",
            "intermediate": "intermediate",
        },
    )
    assert response == success_response


def test_bind_ssl_cert(client):
    client._get.return_value = success_response
    response = client.Binder.BindSSLCert(
        "env_name",
        1,
        ["entry_point1", "entry_point2"],
        ["ext_domains1", "ext_domains2"],
    )
    client._get.assert_called_with(
        "BindSSLCert",
        params={
            "envName": "env_name",
            "certId": 1,
            "entryPoint": ["entry_point1", "entry_point2"],
            "extDomains": ["ext_domains1", "ext_domains2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_check_domain(client):
    client._get.return_value = success_response
    response = client.Binder.CheckDomain("env_name", "domain", ["region1", "region2"])
    client._get.assert_called_with(
        "CheckDomain",
        params={
            "envName": "env_name",
            "domain": "domain",
            "region": ["region1", "region2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_check_ext_domain(client):
    client._get.return_value = success_response
    response = client.Binder.CheckExtDomain("env_name", "extdomains")
    client._get.assert_called_with(
        "CheckExtDomain",
        params={
            "envName": "env_name",
            "extdomains": "extdomains",
        },
    )
    assert response == success_response


def test_delete_ssl(client):
    client._get.return_value = success_response
    response = client.Binder.DeleteSSL(
        "env_name",
    )
    client._get.assert_called_with(
        "DeleteSSL",
        params={
            "envName": "env_name",
        },
    )
    assert response == success_response


def test_detach_ext_ip(client):
    client._get.return_value = success_response
    response = client.Binder.DetachExtIp("env_name", 1, "ip")
    client._get.assert_called_with(
        "DetachExtIp",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "ip": "ip",
        },
    )
    assert response == success_response


def test_disable_ssl(client):
    client._get.return_value = success_response
    response = client.Binder.DisableSSL(
        "env_name",
    )
    client._get.assert_called_with(
        "DisableSSL",
        params={
            "envName": "env_name",
        },
    )
    assert response == success_response


def test_edit_ssl_cert(client):
    client._get.return_value = success_response
    response = client.Binder.EditSSLCert(
        "env_name", 1, ["key1", "key2"], ["cert1", "cert2"], ["interm1", "interm2"]
    )
    client._get.assert_called_with(
        "EditSSLCert",
        params={
            "envName": "env_name",
            "id": 1,
            "key": ["key1", "key2"],
            "cert": ["cert1", "cert2"],
            "interm": ["interm1", "interm2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_domain_info(client):
    client._get.return_value = success_response
    response = client.Binder.GetDomainInfo("env_name", "domain")
    client._get.assert_called_with(
        "GetDomainInfo",
        params={
            "envName": "env_name",
            "domain": "domain",
        },
    )
    assert response == success_response


def test_get_domains(client):
    client._get.return_value = success_response
    response = client.Binder.GetDomains(
        "env_name", ["node_group1", "node_group2"], [1, 2], [True, True]
    )
    client._get.assert_called_with(
        "GetDomains",
        params={
            "envName": "env_name",
            "nodeGroup": ["node_group1", "node_group2"],
            "nodeId": [1, 2],
            "inShort": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_ext_domains(client):
    client._get.return_value = success_response
    response = client.Binder.GetExtDomains(
        "env_name",
    )
    client._get.assert_called_with(
        "GetExtDomains",
        params={
            "envName": "env_name",
        },
    )
    assert response == success_response


def test_get_ssl(client):
    client._get.return_value = success_response
    response = client.Binder.GetSSL(
        "env_name",
    )
    client._get.assert_called_with(
        "GetSSL",
        params={
            "envName": "env_name",
        },
    )
    assert response == success_response


def test_get_ssl_certs(client):
    client._get.return_value = success_response
    response = client.Binder.GetSSLCerts("env_name", ["id1", "id2"])
    client._get.assert_called_with(
        "GetSSLCerts",
        params={"envName": "env_name", "ids": ["id1", "id2"]},
        delimiter=",",
    )
    assert response == success_response


def test_manage_node_dns_state(client):
    client._get.return_value = success_response
    response = client.Binder.ManageNodeDnsState("env_name", [1, 2], [True, True])
    client._get.assert_called_with(
        "ManageNodeDnsState",
        params={"envName": "env_name", "nodeId": [1, 2], "enabled": [True, True]},
        delimiter=",",
    )
    assert response == success_response


def test_move_ext_ips(client):
    client._get.return_value = success_response
    response = client.Binder.MoveExtIps("env_name", 1, 2, "ips")
    client._get.assert_called_with(
        "MoveExtIps",
        params={
            "envName": "env_name",
            "sourceNodeId": 1,
            "targetNodeId": 2,
            "ips": "ips",
        },
    )
    assert response == success_response


def test_remove_domains(client):
    client._get.return_value = success_response
    response = client.Binder.RemoveDomains(
        "env_name", "domains", ["node_group1", "node_group2"], [1, 2]
    )
    client._get.assert_called_with(
        "RemoveDomains",
        params={
            "envName": "env_name",
            "domains": "domains",
            "nodeGroup": ["node_group1", "node_group2"],
            "node_id": [1, 2],
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_ext_domains(client):
    client._get.return_value = success_response
    response = client.Binder.RemoveExtDomains("env_name", "extdomains")
    client._get.assert_called_with(
        "RemoveExtDomains",
        params={
            "envName": "env_name",
            "extdomain": "extdomains",
        },
    )
    assert response == success_response


def test_remove_ssl(client):
    client._get.return_value = success_response
    response = client.Binder.RemoveSSL("env_name")
    client._get.assert_called_with(
        "RemoveSSL",
        params={
            "envName": "env_name",
        },
    )
    assert response == success_response


def test_remove_ssl_certs(client):
    client._get.return_value = success_response
    response = client.Binder.RemoveSSLCerts("env_name", "ids")
    client._get.assert_called_with(
        "RemoveSSLCerts",
        params={
            "envName": "env_name",
            "ids": "ids",
        },
    )
    assert response == success_response


def test_set_ext_ip_count(client):
    client._get.return_value = success_response
    response = client.Binder.SetExtIpCount(
        "env_name", "type", 1, ["node_group1", "node_group2"], [1, 2]
    )
    client._get.assert_called_with(
        "SetExtIpCount",
        params={
            "envName": "env_name",
            "type": "type",
            "count": 1,
            "nodeGroup": ["node_group1", "node_group2"],
            "node_id": [1, 2],
        },
        delimiter=",",
    )
    assert response == success_response


def test_swap_ext_domains(client):
    client._get.return_value = success_response
    response = client.Binder.SwapExtDomains("env_name", "targetappid")
    client._get.assert_called_with(
        "SwapExtDomains",
        params={
            "envName": "env_name",
            "targetappid": "targetappid",
        },
    )
    assert response == success_response


def test_swap_ext_ips(client):
    client._get.return_value = success_response
    response = client.Binder.SwapExtIps(
        "env_name", 1, 2, ["source_ip1", "source_ip2"], ["target_ip1", "target_ip2"]
    )
    client._get.assert_called_with(
        "SwapExtIps",
        params={
            "envName": "env_name",
            "sourceNodeId": 1,
            "targetNodeId": 2,
            "sourceIp": ["source_ip1", "source_ip2"],
            "targetIp": ["target_ip1", "target_ip2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_unbind_ssl_cert(client):
    client._get.return_value = success_response
    response = client.Binder.UnbindSSLCert("env_name", ["extdomains1", "extdomains2"])
    client._get.assert_called_with(
        "UnbindSSLCert",
        params={"envName": "env_name", "extDomains": ["extdomains1", "extdomains2"]},
        delimiter=",",
    )
    assert response == success_response


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
        delimeter=",",
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
        delimeter=",",
    )
    assert response == success_response


def test_build_deploy_project(client):
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
        delimeter=",",
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
        delimeter=",",
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
        delimeter=",",
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
        delimeter=",",
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
        delimeter=",",
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
        delimeter=",",
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
        delimeter=",",
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
        delimeter=",",
    )
    assert response == success_response


def test_get_build_project_info(client):
    client._get.return_value = success_response
    response = client.Deployment.GetBuildProjectInfo("env_name", 1, "project")
    client._get.assert_called_with(
        "GetBuildProjectInfo",
        params={"envName": "env_name", "nodeId": 1, "project": "project"},
        delimeter=",",
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
        delimeter=",",
    )
    assert response == success_response


def test_get_deployments(client):
    client._get.return_value = success_response
    response = client.Deployment.GetDeployments("env_name", "node_group")
    client._get.assert_called_with(
        "GetDeployments",
        params={"envName": "env_name", "nodeGroup": "node_group"},
        delimeter=",",
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
        delimeter=",",
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
        delimeter=",",
    )
    assert response == success_response


def test_get_repos(client):
    client._get.return_value = success_response
    response = client.Deployment.GetRepos([1, 2])
    client._get.assert_called_with(
        "GetRepos",
        params={"id": [1, 2]},
        delimeter=",",
    )
    assert response == success_response


def test_remove_build_project(client):
    client._get.return_value = success_response
    response = client.Deployment.RemoveBuildProject("env_name", 1, "project")
    client._get.assert_called_with(
        "RemoveBuildProject",
        params={"envName": "env_name", "nodeId": 1, "project": "project"},
        delimeter=",",
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
        delimeter=",",
    )
    assert response == success_response
