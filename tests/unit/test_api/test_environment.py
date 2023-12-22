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
        "env_name", "domains", ["node_group1", "node_group2"], [1, 2], ["subdomain1", "subdomain2"]
    )
    client._get.assert_called_with(
        "AddDomains",
        params={
            "envName": "env_name",
            "domains": "domains",
            "nodeGroup": ["node_group1", "node_group2"],
            "nodeId": [1, 2],
            "subdomain": ["subdomain1", "subdomain2"]
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
            "interm": ["interm1", "interm2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_attach_ext_ip(client):
    client._get.return_value = success_response
    response = client.Binder.AttachExtIp(
        "env_name", "nodeid", ["type1", "type2"]
    )
    client._get.assert_called_with(
        "AttachExtIp",
        params={
            "envName": "env_name",
            "nodeid": "nodeid",
            "type": ["type1", "type2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_bind_ext_domain(client):
    client._get.return_value = success_response
    response = client.Binder.BindExtDomain(
        "env_name", "extdomain", [1, 2]
    )
    client._get.assert_called_with(
        "BindExtDomain",
        params={
            "envName": "env_name",
            "extdomain": "extdomain",
            "certId": [1, 2]
        },
        delimiter=",",
    )
    assert response == success_response


def test_bind_ext_domains(client):
    client._get.return_value = success_response
    response = client.Binder.BindExtDomains(
        "env_name", "extdomains", [1, 2]
    )
    client._get.assert_called_with(
        "BindExtDomains",
        params={
            "envName": "env_name",
            "extdomains": "extdomains",
            "certId": [1, 2]
        },
        delimiter=",",
    )
    assert response == success_response


def test_bind_ssl(client):
    client._get.return_value = success_response
    response = client.Binder.BindSSL(
        "env_name", "cert_key", "cert", "intermediate"
    )
    client._get.assert_called_with(
        "BindSSL",
        params={
            "envName": "env_name",
            "cert_key": "cert_key",
            "cert": "cert",
            "intermediate": "intermediate"
        },

    )
    assert response == success_response


def test_bind_ssl_cert(client):
    client._get.return_value = success_response
    response = client.Binder.BindSSLCert(
        "env_name", 1, ["entry_point1", "entry_point2"], ["ext_domains1", "ext_domains2"]
    )
    client._get.assert_called_with(
        "BindSSLCert",
        params={
            "envName": "env_name",
            "certId": 1,
            "entryPoint": ["entry_point1", "entry_point2"],
            "extDomains": ["ext_domains1", "ext_domains2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_check_domain(client):
    client._get.return_value = success_response
    response = client.Binder.CheckDomain(
        "env_name", "domain", ["region1", "region2"]
    )
    client._get.assert_called_with(
        "CheckDomain",
        params={
            "envName": "env_name",
            "domain": "domain",
            "region": ["region1", "region2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_check_ext_domain(client):
    client._get.return_value = success_response
    response = client.Binder.CheckExtDomain(
        "env_name", "extdomains"
    )
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
    response = client.Binder.DetachExtIp(
        "env_name", 1, "ip"
    )
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
        "env_name",
        1, ["key1", "key2"], ["cert1", "cert2"], ["interm1", "interm2"]
    )
    client._get.assert_called_with(
        "EditSSLCert",
        params={
            "envName": "env_name",
            "id": 1,
            "key": ["key1", "key2"],
            "cert": ["cert1", "cert2"],
            "interm": ["interm1", "interm2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_domain_info(client):
    client._get.return_value = success_response
    response = client.Binder.GetDomainInfo(
        "env_name",
        "domain"
    )
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
            "inShort": [True, True]
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
    response = client.Binder.GetSSLCerts(
        "env_name", ["id1", "id2"]
    )
    client._get.assert_called_with(
        "GetSSLCerts",
        params={
            "envName": "env_name",
            "ids": ["id1", "id2"]
        }, delimiter=",",
    )
    assert response == success_response


def test_manage_node_dns_state(client):
    client._get.return_value = success_response
    response = client.Binder.ManageNodeDnsState(
        "env_name", [1, 2], [True, True]
    )
    client._get.assert_called_with(
        "ManageNodeDnsState",
        params={
            "envName": "env_name",
            "nodeId": [1, 2],
            "enabled": [True, True]
        }, delimiter=",",
    )
    assert response == success_response


def test_move_ext_ips(client):
    client._get.return_value = success_response
    response = client.Binder.MoveExtIps(
        "env_name", 1, 2, "ips"
    )
    client._get.assert_called_with(
        "MoveExtIps",
        params={
            "envName": "env_name",
            "sourceNodeId": 1,
            "targetNodeId": 2,
            "ips": "ips"
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
    response = client.Binder.RemoveExtDomains(
        "env_name", "extdomains"
    )
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
    response = client.Binder.RemoveSSL(
        "env_name"
    )
    client._get.assert_called_with(
        "RemoveSSL",
        params={
            "envName": "env_name",
        },
    )
    assert response == success_response


def test_remove_ssl_certs(client):
    client._get.return_value = success_response
    response = client.Binder.RemoveSSLCerts(
        "env_name", "ids"
    )
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
    response = client.Binder.SwapExtDomains(
        "env_name", "targetappid"
    )
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
            "targetIp": ["target_ip1", "target_ip2"]

        },
        delimiter=",",
    )
    assert response == success_response


def test_unbind_ssl_cert(client):
    client._get.return_value = success_response
    response = client.Binder.UnbindSSLCert(
        "env_name", ["extdomains1", "extdomains2"]
    )
    client._get.assert_called_with(
        "UnbindSSLCert",
        params={
            "envName": "env_name",
            "extDomains": ["extdomains1", "extdomains2"]

        },
        delimiter=",",
    )
    assert response == success_response


def test_add_backend(client):
    client._get.return_value = success_response
    response = client.Control.AddBackend(
        'env',
        1,
        1,
    )
    client._get.assert_called_with(
        "AddBackend",
        params={
            "envName": 'env',
            "backendNodeId": 1,
            "balancerNodeId": 1,
        }
    )
    assert response == success_response


def test_add_backends(client):
    client._get.return_value = success_response
    response = client.Control.AddBackends(
        'env',
        1,
        1,
    )
    client._get.assert_called_with(
        "AddBackends",
        params={
            "envName": 'env',
            "backendNodeId": 1,
            "balancerNodeId": 1,
        }
    )
    assert response == success_response


def test_add_balancer_node(client):
    client._get.return_value = success_response
    response = client.Control.AddBalancerNode(
        'env',
        'node type',
        [1, 2, 3],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ['name1', 'name2', 'name3'],
        ['group1', 'group2', 'group3'],
        [1, 2, 3],
        ['tag1', 'tag2', 'tag3'],
        ['meta1', 'meta2', 'meta3'],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ['node group1', 'node group2', 'node group3'],
    )
    client._get.assert_called_with(
        'AddBalancerNode',
        params={
            "envName": 'env',
            "nodeType": 'node type',
            "cloudLets": [1, 2, 3],
            "expIp": [True, False, True],
            "flexibleCloudlets": [1, 2, 3],
            'fixedCloudlets': [1, 2, 3],
            'displayName': ['name1', 'name2', 'name3'],
            'nodeGroup': ['group1', 'group2', 'group3'],
            'diskLimit': [1, 2, 3],
            'tag': ['tag1', 'tag2', 'tag3'],
            'metadata': ['meta1', 'meta2', 'meta3'],
            'startService': [True, False, True],
            'extIpv6Count': [1, 2, 3],
            'extIpCount': [1, 2, 3],
            'nodeGroupData': ['node group1', 'node group2', 'node group3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_build_node(client):
    client._get.return_value = success_response
    response = client.Control.AddBuildNode(
        'env',
        'node type',
        [1, 2, 3],
        [True, False, True],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ['group1', 'group2', 'group3'],
        ['nodeGroup1', 'nodeGroup2', 'nodeGroup3'],
        ['tag1', 'tag2', 'tag3'],
        ['meta1', 'meta2', 'meta3'],
        [True, False, True],
        ['engine1', 'engine2', 'engine3'],
        [1, 2, 3],
        [1, 2, 3, ],
        ['data1', 'data2', 'data3'],
        [1, 2, 3]
    )
    client._get.assert_called_once_with(
        'AddBuildNode',
        params={
            'envName': 'env',
            'nodeType': 'node type',
            'cloudlets': [1, 2, 3],
            'nodeId': [True, False, True],
            'expIp': [True, False, True],
            'flexibleCloudlets': [1, 2, 3],
            'fixedCloudlets': [1, 2, 3],
            'displayName': ['group1', 'group2', 'group3'],
            'nodeGroup': ['nodeGroup1', 'nodeGroup2', 'nodeGroup3'],
            'tag': ['tag1', 'tag2', 'tag3'],
            'metadata': ['meta1', 'meta2', 'meta3'],
            'startService': [True, False, True],
            'engine': ['engine1', 'engine2', 'engine3'],
            'extIpv6Count': [1, 2, 3],
            'extIpCount': [1, 2, 3, ],
            'nodeGroupData': ['data1', 'data2', 'data3'],
            'diskLimit': [1, 2, 3],
        },
        delimiter=",",
    )

    assert response == success_response


def test_add_cache_node(client):
    client._get.return_value = success_response
    response = client.Control.AddCacheNode(
        'env',
        'node type',
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        ['name1', 'name2', 'name3'],
        ['nodeGroup1', 'nodeGroup2', 'nodeGroup3'],
        [1, 2, 3],
        ['tag1', 'tag2', 'tag3'],
        ['meta1', 'meta2', 'meta3'],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ['data1', 'data2', 'data3'],
    )
    client._get.assert_called_once_with(
        'AddCacheNode',
        params={
            'envName': 'env',
            'nodeType': 'node type',
            'cloudlets': [1, 2, 3],
            'flexibleCloudlets': [1, 2, 3],
            'fixedCloudlets': [1, 2, 3],
            'displayName': ['name1', 'name2', 'name3'],
            'nodeGroup': ['nodeGroup1', 'nodeGroup2', 'nodeGroup3'],
            'diskLimit': [1, 2, 3],
            'tag': ['tag1', 'tag2', 'tag3'],
            'metadata': ['meta1', 'meta2', 'meta3'],
            'startService': [True, False, True],
            'expIpv6Count': [1, 2, 3],
            'expIpCount': [1, 2, 3],
            'nodeGroupData': ['data1', 'data2', 'data3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_computer_node(client):
    client._get.return_value = success_response
    response = client.Control.AddComputeNode(
        'env',
        'node type',
        [1, 2, 3],
        [1, 2, 3],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ['name1', 'name2', 'name3'],
        ['group1', 'group2', 'group3'],
        [1, 2, 3],
        ['tag1', 'tag2', 'tag3'],
        [True, False, True],
        [True, False, True],
        ['engine1', 'engine2', 'engine3'],
        [1, 2, 3],
        [1, 2, 3],
        ['data1', 'data2', 'data3'],
    )
    client._get.assert_called_once_with(
        'AddComputeNode',
        params={
            'envName': 'env',
            'nodeType': 'node type',
            'cloudlets': [1, 2, 3],
            'isMaster': [1, 2, 3],
            'expIp': [True, False, True],
            'flexibleCloudlets': [1, 2, 3],
            'fixedCloudlets': [1, 2, 3],
            'displayName': ['name1', 'name2', 'name3'],
            'nodeGroup': ['group1', 'group2', 'group3'],
            'diskLimit': [1, 2, 3],
            'tag': ['tag1', 'tag2', 'tag3'],
            'metadata': [True, False, True],
            'startService': [True, False, True],
            'engine': ['engine1', 'engine2', 'engine3'],
            'expIpv6Count': [1, 2, 3],
            'expIpCount': [1, 2, 3],
            'nodeGroupData': ['data1', 'data2', 'data3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_container_env_vars(client):
    client._get.return_value = success_response
    response = client.Control.AddContainerEnvVars(
        'env',
        'vars',
        ['group1', 'group2', 'group3'],
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        'AddContainerEnvVars',
        params={
            'envName': 'env',
            'vars': 'vars',
            'nodeGroup': ['group1', 'group2', 'group3'],
            'nodeId': [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_container_volume(client):
    client._get.return_value = success_response
    response = client.Control.AddContainerVolume(
        'env',
        1,
        'path'
    )
    client._get.assert_called_once_with(
        'AddContainerVolume',
        params={
            'envName': 'env',
            'nodeId': 1,
            'path': 'path',
        }
    )
    assert response == success_response


def test_add_container_volume_by_group(client):
    client._get.return_value = success_response
    response = client.Control.AddContainerVolumeByGroup(
        'env',
        'group',
        'path',
    )
    client._get.assert_called_once_with(
        'AddContainerVolumeByGroup',
        params={
            'envName': 'env',
            'nodeGroup': 'group',
            'path': 'path',
        }
    )
    assert response == success_response


def test_add_container_volumes(client):
    client._get.return_value = success_response
    response = client.Control.AddContainerVolumes(
        'env',
        'volume',
        ['group1', 'group2', 'group3'],
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        'AddContainerVolumes',
        params={
            'envName': 'env',
            'volumes': 'volume',
            'nodeGroup': ['group1', 'group2', 'group3'],
            'nodeId': [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_context(client):
    client._get.return_value = success_response
    response = client.Control.AddContext(
        'env',
        'name',
        'file name',
        'type',
        ['group1', 'group2', 'group3'],
    )
    client._get.assert_called_once_with(
        'AddContext',
        params={
            'envName': 'env',
            'name': 'name',
            'fileName': 'file name',
            'type': 'type',
            'nodeGroup': ['group1', 'group2', 'group3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_db_node(client):
    client._get.return_value = success_response
    response = client.Control.AddDBNode(
        'env',
        'type',
        [1, 2, 3],
        [True, False, True],
        ['password1', 'password2', 'password3'],
        [1, 2, 3],
        [1, 2, 3],
        ['name1', 'name2', 'name3'],
        ['group1', 'group2', 'group3'],
        [1, 2, 3],
        ['tag1', 'tag2', 'tag3'],
        [True, True, True],
        [True, True, True],
        [1, 2, 3],
        [1, 2, 3],
        ['data1', 'data2', 'data3'],
    )
    client._get.assert_called_once_with(
        'AddDBNode',
        params={
            'envName': 'env',
            'nodeType': 'type',
            'cloudlets': [1, 2, 3],
            'expIp': [True, False, True],
            'password': ['password1', 'password2', 'password3'],
            'flexibleCloudlets': [1, 2, 3],
            'fixedCloudlets': [1, 2, 3],
            'displayName': ['name1', 'name2', 'name3'],
            'nodeGroup': ['group1', 'group2', 'group3'],
            'diskLimit': [1, 2, 3],
            'tag': ['tag1', 'tag2', 'tag3'],
            'metadata': [True, True, True],
            'startService': [True, True, True],
            'expIpv6Count': [1, 2, 3],
            'expIpCount': [1, 2, 3],
            'nodeGroupData': ['data1', 'data2', 'data3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_docker_node(client):
    client._get.return_value = success_response
    response = client.Control.AddDockerNode(
        'env',
        'type',
        {
            'metadata1': 'val1',
            'metadata2': 'val2',
            'metadata3': 'val3',
            'metadata4': 'val4',
            'metadata5': 'val5',
        },
        [1, 2, 3],
        [True, True, True],
        ['pass1', 'pass2', 'pass3'],
        [1, 2, 3],
        [1, 2, 3],
        ['name1', 'name2', 'name3'],
        ['group1', 'group2', 'group3'],
        [1, 2, 3],
        [True, True, True],
        [1, 2, 3],
        [1, 2, 3],
        ['data1', 'data2', 'data3'],
    )
    client._get.assert_called_once_with(
        'AddDockerNode',
        params={
            'envName': 'env',
            'nodeType': 'type',
            'metadata': {
                'metadata1': 'val1',
                'metadata2': 'val2',
                'metadata3': 'val3',
                'metadata4': 'val4',
                'metadata5': 'val5',
            },
            'cloudlets': [1, 2, 3],
            'expIp': [True, True, True],
            'password': ['pass1', 'pass2', 'pass3'],
            'flexibleCloudlets': [1, 2, 3],
            'fixedCloudlets': [1, 2, 3],
            'displayName': ['name1', 'name2', 'name3'],
            'nodeGroup': ['group1', 'group2', 'group3'],
            'diskLimit': [1, 2, 3],
            'startService': [True, True, True],
            'expIpv6Count': [1, 2, 3],
            'expIpCount': [1, 2, 3],
            'nodeGroupData': ['data1', 'data2', 'data3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_docker_volume(client):
    client._get.return_value = success_response
    response = client.Control.AddDockerVolume(
        'env',
        1,
        'path',
    )
    client._get.assert_called_once_with(
        'AddDockerVolume',
        params={
            'envName': 'env',
            'nodeId': 1,
            'path': 'path'
        }
    )
    assert response == success_response


def test_add_docker_volume_by_groups(client):
    client._get.return_value = success_response
    response = client.Control.AddDockerVolumeByGroup(
        'env',
        1,
        'path',
    )
    client._get.assert_called_once_with(
        'AddDockerVolumeByGroup',
        params={
            'envName': 'env',
            'nodeGroup': 1,
            'path': 'path'
        }
    )
    assert response == success_response


def test_add_endpoint(client):
    client._get.return_value = success_response
    response = client.Control.AddEndpoint(
        'env',
        1,
        8000,
        'protocol',
        'name',
    )
    client._get.assert_called_once_with(
        'AddEndpoint',
        params={
            'envName': 'env',
            'nodeId': 1,
            'privatePort': 8000,
            'protocol': 'protocol',
            'name': 'name',
        }
    )
    assert response == success_response


def test_add_env_policy(client):
    client._get.return_value = success_response
    response = client.Control.AddEnvPolicy(
        'app id',
        'policy',
    )
    client._get.assert_called_once_with(
        'AddEnvPolicy',
        params={
            'targetAppId': 'app id',
            'policy': 'policy',
        }
    )
    assert response == success_response


def test_aad_env_property(client):
    client._get.return_value = success_response
    response = client.Control.AddEnvProperty('properties')
    client._get.assert_called_once_with(
        'AddEnvProperty',
        params={
            'properties': 'properties',
        }
    )
    assert response == success_response


def test_add_extra_node(client):
    client._get.return_value = success_response
    response = client.Control.AddExtraNode(
        'env',
        'type',
        [1, 2, 3],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ['name1', 'name2', 'name3'],
        ['group1', 'group2', 'group3'],
        [1, 2, 3],
        ['tag1', 'tag2', 'tag3'],
        [True, False, True],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ['date1', 'date2', 'date3'],
    )
    client._get.assert_called_once_with(
        'AddExtraNode',
        params={
            'envName': 'env',
            'nodeType': 'type',
            'cloudlets': [1, 2, 3],
            'expIp': [True, False, True],
            'flexibleCloudlets': [1, 2, 3],
            'fixedCloudlets': [1, 2, 3],
            'displayName': ['name1', 'name2', 'name3'],
            'nodeGroup': ['group1', 'group2', 'group3'],
            'diskLimit': [1, 2, 3],
            'tag': ['tag1', 'tag2', 'tag3'],
            'metadata': [True, False, True],
            'startService': [True, False, True],
            'expIpv6Count': [1, 2, 3],
            'expIpCount': [1, 2, 3],
            'nodeGroupData': ['date1', 'date2', 'date3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_node(client):
    client._get.return_value = success_response
    response = client.Control.AddNode(
        'env',
        'type',
        [1, 2, 3],
        ['ip1', 'ip2', 'ip3'],
        ['password1', 'password2', 'password3'],
        [1, 2, 3],
        [1, 2, 3],
        ['name1', 'name2', 'name3'],
        ['metadata1', 'metadata2', 'metadata3'],
        ['group1', 'group2', 'group3'],
        [True, False, True],
        [1, 2, 3],
        ['tag1', 'tag2', 'tag3'],
        ['engine1', 'engine2', 'engine3'],
        [1, 2, 3],
        [1, 2, 3],
        ['data1', 'data2', 'data3'],
        ['option1', 'option2', 'option3'],
    )
    client._get.assert_called_once_with(
        'AddNode',
        params={
            'envName': 'env',
            'nodeType': 'type',
            'cloudLets': [1, 2, 3],
            'extIp': ['ip1', 'ip2', 'ip3'],
            'password': ['password1', 'password2', 'password3'],
            'flexibleCloudLets': [1, 2, 3],
            'fixedCloudLets': [1, 2, 3],
            'displayName': ['name1', 'name2', 'name3'],
            'metadata': ['metadata1', 'metadata2', 'metadata3'],
            'nodeGroup': ['group1', 'group2', 'group3'],
            'startService': [True, False, True],
            'diskLimit': [1, 2, 3],
            'tag': ['tag1', 'tag2', 'tag3'],
            'engine': ['engine1', 'engine2', 'engine3'],
            'extipv4': [1, 2, 3],
            'extipv6': [1, 2, 3],
            'nodeGroupData': ['data1', 'data2', 'data3'],
            'options': ['option1', 'option2', 'option3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_port_redirect(client):
    client._get.return_value = success_response
    response = client.Control.AddPortRedirect(
        'env',
        1,
        8000,
        9000,
        'protocol',
        ['comment1', 'comment2', 'comment3'],
    )
    client._get.assert_called_once_with(
        'AddPortRedirect',
        params={
            'envName': 'env',
            'nodeId': 1,
            'srcPort': 8000,
            'dstPort': 9000,
            'protocol': 'protocol',
            'comments': ['comment1', 'comment2', 'comment3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_storage_node(client):
    client._get.return_value = success_response
    response = client.Control.AddStorageNode(
        'env',
        'type',
        [1, 2, 3],
        ['ip1', 'ip2', 'ip3'],
        [1, 2, 3],
        [1, 2, 3],
        ['name1', 'name2', 'name3'],
        ['group1', 'group2', 'group3'],
        [1, 2, 3],
        ['tag1', 'tag2', 'tag3'],
        ['metadata1', 'metadata2', 'metadata3'],
        [True, True, True],
        [1, 2, 3],
        [1, 2, 3],
        ['data1', 'data2', 'data3'],
    )
    client._get.assert_called_once_with(
        'AddStorageNode',
        params={
            'envName': 'env',
            'nodeType': 'type',
            'cloudlets': [1, 2, 3],
            'extIp': ['ip1', 'ip2', 'ip3'],
            'flexibleCloudLets': [1, 2, 3],
            'fixedCloudLets': [1, 2, 3],
            'displayName': ['name1', 'name2', 'name3'],
            'nodeGroup': ['group1', 'group2', 'group3'],
            'diskLimit': [1, 2, 3],
            'tag': ['tag1', 'tag2', 'tag3'],
            'metadata': ['metadata1', 'metadata2', 'metadata3'],
            'startService': [True, True, True],
            'extIpv6Count': [1, 2, 3],
            'extIpCount': [1, 2, 3],
            'nodeGroupData': ['data1', 'data2', 'data3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_vds_node(client):
    client._get.return_value = success_response
    response = client.Control.AddVdsNode(
        'env',
        'type',
        [1, 2, 3],
        ['ip1', 'ip2', 'ip3'],
        ['password1', 'password2', 'password3'],
        [1, 2, 3],
        [1, 2, 3],
        ['name1', 'name2', 'name3'],
        ['group1', 'group2', 'group3'],
        [1, 2, 3],
        ['tag1', 'tag2', 'tag3'],
        ['data1', 'data2', 'data3'],
        [True, False, False],
        [1, 2, 3],
        [1, 2, 3],
        ['data1', 'data2', 'data3'],
    )
    client._get.assert_called_once_with(
        'AddVdsNode',
        params={
            'envName': 'env',
            'nodeType': 'type',
            'cloudlets': [1, 2, 3],
            'extIp': ['ip1', 'ip2', 'ip3'],
            'password': ['password1', 'password2', 'password3'],
            'flexibleCloudLets': [1, 2, 3],
            'fixedCloudLets': [1, 2, 3],
            'displayName': ['name1', 'name2', 'name3'],
            'nodeGroup': ['group1', 'group2', 'group3'],
            'diskLimit': [1, 2, 3],
            'tag': ['tag1', 'tag2', 'tag3'],
            'metadata': ['data1', 'data2', 'data3'],
            'startService': [True, False, False],
            'extIpv6Count': [1, 2, 3],
            'extIpCount': [1, 2, 3],
            'nodeGroupData': ['data1', 'data2', 'data3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_vm_node(client):
    client._get.return_value = success_response
    response = client.Control.AddVmNode(
        'env',
        'type',
        'option',
        ['ip1', 'ip2', 'ip3'],
        ['name', 'name2', 'name3'],
        ['group1', 'group2', 'group3'],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        ['data1', 'data2', 'data3'],
        ['password1', 'password2', 'password3'],
    )
    client._get.assert_called_once_with(
        'AddVmNode',
        params={
            'envName': 'env',
            'nodeType': 'type',
            'options': 'option',
            'extIp': ['ip1', 'ip2', 'ip3'],
            'displayName': ['name', 'name2', 'name3'],
            'nodeGroup': ['group1', 'group2', 'group3'],
            'diskLimit': [1, 2, 3],
            'extIpv6Count': [1, 2, 3],
            'extIpCount': [1, 2, 3],
            'nodeGroupData': ['data1', 'data2', 'data3'],
            'password': ['password1', 'password2', 'password3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_append_nodes(client):
    client._get.return_value = success_response
    response = client.Control.AppendNodes(
        'name',
        1,
        'type'
    )
    client._get.assert_called_once_with(
        'AppendNodes',
        params={
            'envName': 'name',
            'count': 1,
            'nodeType': 'type',
        }
    )
    assert response == success_response


def test_apply_env_property(client):
    client._get.return_value = success_response
    response = client.Control.ApplyEnvProperty('name', 'properties')
    client._get.assert_called_once_with(
        'ApplyEnvProperty',
        params={
            'envName': 'name',
            'properties': 'properties',
        }
    )
    assert response == success_response


def test_apply_node_group_data(client):
    client._get.return_value = success_response
    response = client.Control.ApplyNodeGroupData('env', 'group', 'data')
    client._get.assert_called_once_with(
        'ApplyNodeGroupData',
        params={
            'envName': 'env',
            'nodeGroupData': 'group',
            'data': 'data',
        }
    )
    assert response == success_response


def test_apply_software_package_action(client):
    client._get.return_value = success_response
    response = client.Control.ApplySoftwarePackageAction(
        'env',
        'keyword',
        ['type1', 'type2', 'type3'],
        ['action1', 'action2', 'action3'],
        ['password1', 'password2', 'password3'],
        ['group1', 'group2', 'group3'],
    )
    client._get.assert_called_once_with(
        'ApplySoftwarePackageAction',
        params={
            'envName': 'env',
            'keywords': 'keyword',
            'nodeType': ['type1', 'type2', 'type3'],
            'action': ['action1', 'action2', 'action3'],
            'password': ['password1', 'password2', 'password3'],
            'nodeGroup': ['group1', 'group2', 'group3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_attach_env_group(client):
    client._get.return_value = success_response
    response = client.Control.AttachEnvGroup('env', 'group')
    client._get.assert_called_once_with(
        'AttachEnvGroup',
        params={
            'envName': 'env',
            'envGroup': 'group',
        }
    )
    assert response == success_response


def test_build_cluster(client):
    client._get.return_value = success_response
    response = client.Control.BuildCluster('env', 'group')
    client._get.assert_called_once_with(
        'BuildCluster',
        params={
            'envName': 'env',
            'nodeGroup': 'group'
        }
    )
    assert response == success_response


def test_cancel_transfer_request(client):
    client._get.return_value = success_response
    response = client.Control.CancelTransferRequest()
    client._get.assert_called_once_with(
        'CancelTransferRequest',
        params={}
    )
    assert response == success_response


def test_change_limits(client):
    client._get.return_value = success_response
    response = client.Control.ChangeLimits('env')
    client._get.assert_called_once_with(
        'ChangeLimits',
        params={'envName': 'env'}
    )
    assert response == success_response


def test_change_limit_inner(client):
    client._get.return_value = success_response
    response = client.Control.ChangeLimitsInner(
        'env',
        1,
        ['type1', 'type2', 'type3'],
    )
    client._get.assert_called_once_with(
        'ChangeLimitsInner',
        params={
            'envName': 'env',
            'uid': 1,
            'limitType': ['type1', 'type2', 'type3'],
        }
    )
    assert response == success_response


def test_change_topology(client):
    client._get.return_value = success_response
    response = client.Control.ChangeTopology(
        'env',
        {
            'envName1': 'value1',
            'envName2': 'value2',
            'envName3': 'value3',
            'envName4': 'value4',
            'envName5': 'value5',
        },
        {
            'node1': 'value1',
            'node2': 'value2',
            'node3': 'value3',
            'node4': 'value4',
            'node5': 'value5',
        },
        ['key1', 'key2', 'key3'],
    )
    client._get.assert_called_once_with(
        'ChangeTopology',
        params={
            'envName': 'env',
            'env': {
                'envName1': 'value1',
                'envName2': 'value2',
                'envName3': 'value3',
                'envName4': 'value4',
                'envName5': 'value5',
            },
            'nodes': {
                'node1': 'value1',
                'node2': 'value2',
                'node3': 'value3',
                'node4': 'value4',
                'node5': 'value5',
            },
            'actionkey': ['key1', 'key2', 'key3'],
        },
        delimiter=',',
    )
    assert response == success_response


def test_check_dependencies(client):
    client._get.return_value = success_response
    response = client.Control.CheckDependencies(
        'env',
        [1, 2, 3],
        ['filter1', 'filter2', 'filter3'],
    )
    client._get.assert_called_once_with(
        'CheckDependencies',
        params={
            'envName': 'env',
            'nodeId': [1, 2, 3],
            'filter': ['filter1', 'filter2', 'filter3'],
        },
        delimiter=',',
    )
    assert response == success_response


def test_check_ext_ip_count(client):
    client._get.return_value = success_response
    response = client.Control.CheckExtIpCount(
        1,
        [1, 2, 3],
        ['group1', 'group2', 'group3'],
    )
    client._get.assert_called_once_with(
        'CheckExtIpCount',
        params={
            'expIpv6': 1,
            'expIpv4': [1, 2, 3],
            'hardwareNodeGroup': ['group1', 'group2', 'group3'],
        },
        delimiter=',',
    )
    assert response == success_response


def test_check_migration_possibility(client):
    client._get.return_value = success_response
    response = client.Control.CheckMigrationPossibility(
        'env',
        ['group1', 'group2', 'group3'],
    )
    client._get.assert_called_once_with(
        'CheckMigrationPossibility',
        params={
            'envName': 'env',
            'hardwareNodeGroup': ['group1', 'group2', 'group3'],
        },
        delimiter=',',
    )
    assert response == success_response


def test_clear_log(client):
    client._get.return_value = success_response
    response = client.Control.ClearLog(
        'env',
        1,
        'path',
    )
    client._get.assert_called_once_with(
        'ClearLog',
        params={
            'envName': 'env',
            'nodeId': 1,
            'path': 'path',
        }
    )
    assert response == success_response


def test_clone_env(client):
    client._get.return_value = success_response
    response = client.Control.CloneEnv(
        'env',
        'env_name',
        [True, False, True],
    )
    client._get.assert_called_once_with(
        'CloneEnv',
        params={
            'srcEnvName': 'env',
            'ditEnvName': 'env_name',
            'useExternalMounts': [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_clone_node(client):
    client._get.return_value = success_response
    response = client.Control.CloneNode(
        'env',
        1,
        'group',
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        'CloneNode',
        params={
            'envName': 'env',
            'count': 1,
            'nodeGroup': 'group',
            'nodeId': [1, 2, 3],
        }
    )
    assert response == success_response


def test_confirm_transfer_request(client):
    client._get.return_value = success_response
    response = client.Control.ConfirmTransferRequest('key')
    client._get.assert_called_once_with(
        'ConfirmTransferRequest',
        params={
            'key': 'key',
        }
    )
    assert response == success_response


def test_create_env(client):
    client._get.return_value = success_response
    response = client.Control.CreateEnv(
        'env',
        {
            'settings1': 'value1',
            'settings2': 'value2',
            'settings3': 'value3',
            'settings4': 'value4',
            'settings5': 'value5',
        },
        [1, 2, 3],
        ['group1', 'group2', 'group3'],
        ['env 1', 'env 2', 'env 3'],
    )
    client._get.assert_called_once_with(
        'CreateEnv',
        params={
            'envName': 'env',
            'settings': {
                'settings1': 'value1',
                'settings2': 'value2',
                'settings3': 'value3',
                'settings4': 'value4',
                'settings5': 'value5',
            },
            'ownerUid': [1, 2, 3],
            'hardwareNodeGroups': ['group1', 'group2', 'group3'],
            'envGroups': ['env 1', 'env 2', 'env 3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_create_environment(client):
    client._get.return_value = success_response
    response = client.Control.CreateEnvironment(
        {
            'envName1': 'env1',
            'envName2': 'env2',
            'envName3': 'env3',
            'envName4': 'env4',
            'envName5': 'env5',
        },
        {
            'node1': 'value1',
            'node2': 'value2',
            'node3': 'value3',
            'node4': 'value4',
            'node5': 'value5',
        },
        ['key1', 'key2', 'key3'],
        [1, 2, 3],
        ['group1', 'group2', 'group3'],
    )
    client._get.assert_called_once_with(
        'CreateEnvironment',
        params={
            'env': {
                'envName1': 'env1',
                'envName2': 'env2',
                'envName3': 'env3',
                'envName4': 'env4',
                'envName5': 'env5',
            },
            'nodes': {
                'node1': 'value1',
                'node2': 'value2',
                'node3': 'value3',
                'node4': 'value4',
                'node5': 'value5',
            },
            'actionKey': ['key1', 'key2', 'key3'],
            'ownerUid': [1, 2, 3],
            'envGroups': ['group1', 'group2', 'group3'],
        },
        delimiter=",",
    )
    assert response == success_response

def test_delete_env(client):
    client._get.return_value = success_response
    response = client.Control.DeleteEnv(
        'env',
        ['password1', 'password2', 'password3'],
    )
    client._get.assert_called_once_with(
            'DeleteEnv',
            params={
                'envName': 'env',
                'password': ['password1', 'password2', 'password3'],
            },
            delimiter=",",
        )
    assert response == success_response

def test_delete_exported_files(client):
    client._get.return_value = success_response
    response = client.Control.DeleteExportedFiles(
        'env',
        'file',
    )
    client._get.assert_called_once_with(
            'DeleteExportedFiles',
            params={
                'envName': 'env',
                'fileName': 'file',
            }
        )
    assert response == success_response

def test_deploy_app(client):
    client._get.return_value = success_response
    response = client.Control.DeployApp(
        'env',
        'file url',
        'file name',
        ['context1', 'context2', 'context3'],
        [True, False, True],
        [1,2,3],
        ['group1', 'group2', 'group3'],
        ['hook1', 'hook2', 'hook3'],
        [True, False, True],
    )
    client._get.assert_called_once_with(
            'DeployApp',
            params={
                'envName': 'env',
                'fileUrl': 'file url',
                'fileName': 'file name',
                'context': ['context1', 'context2', 'context3'],
                'atomicDeploy': [True, False, True],
                'delay': [1,2,3],
                'nodeGroup': ['group1', 'group2', 'group3'],
                'hooks': ['hook1', 'hook2', 'hook3'],
                'isSequential': [True, False, True],
            },
            delimiter=",",
        )
    assert response == success_response

def test_detach_env_group(client):
    client._get.return_value = success_response
    response = client.Control.DetachEnvGroup(
        'env',
        'group',
    )
    client._get.assert_called_once_with(
            'DetachEnvGroup',
            params={
                'envName': 'env',
                'envGroup': 'group',
            }
        )
    assert response == success_response

def test_disable_replication(client):
    client._get.return_value = success_response
    response = client.Control.DisableReplication(
        'env',
        'group',
    )
    client._get.assert_called_once_with(
            'DisableReplication',
            params={
                'envName': 'env',
                'nodeGroup': 'group',
            }
        )
    assert response == success_response

def test_edit_endpoint(client):
    client._get.return_value = success_response
    response = client.Control.EditEndpoint(
        'env',
        1,
        'name',
        8000,
        'tcp',
    )
    client._get.assert_called_once_with(

        'EditEndpoint',
        params={
            'envName': 'env',
            'id': 1,
            'name': 'name',
            'privatePort': 8000,
            'protocol': 'tcp',
        }
    )
    assert response == success_response