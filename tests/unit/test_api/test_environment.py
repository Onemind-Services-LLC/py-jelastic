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
         "env_name","domains", ["node_group1","node_group2"],[1,2],["subdomain1","subdomain2"]
    )
    client._get.assert_called_with(
        "AddDomains",
        params={
            "envName": "env_name",
            "domains": "domains",
            "nodeGroup": ["node_group1","node_group2"],
            "nodeId": [1,2],
            "subdomain": ["subdomain1","subdomain2"]
        },
        delimiter=",",
    )
    assert response == success_response
def test_add_ssl_cert(client):
    client._get.return_value = success_response
    response = client.Binder.AddSSLCert(
        "env_name","key","cert" ,["interm1","interm2"]
    )
    client._get.assert_called_with(
        "AddSSLCert",
        params={
            "envName": "env_name",
             "key": "key",
              "cert": "cert",
             "interm":["interm1","interm2"]
    },
        delimiter=",",
    )
    assert response == success_response
def test_attach_ext_ip(client):
    client._get.return_value = success_response
    response = client.Binder.AttachExtIp(
         "env_name","nodeid",["type1","type2"]
    )
    client._get.assert_called_with(
        "AttachExtIp",
        params={
            "envName": "env_name",
              "nodeid": "nodeid",
              "type": ["type1","type2"]
    },
        delimiter=",",
    )
    assert response == success_response
def test_bind_ext_domain(client):
    client._get.return_value = success_response
    response = client.Binder.BindExtDomain(
         "env_name","extdomain",[1,2]
    )
    client._get.assert_called_with(
        "BindExtDomain",
        params={
            "envName": "env_name",
            "extdomain": "extdomain",
            "certId":[1,2]
    },
        delimiter=",",
    )
    assert response == success_response
def test_bind_ext_domains(client):
    client._get.return_value = success_response
    response = client.Binder.BindExtDomains(
    "env_name", "extdomains",[1,2]
    )
    client._get.assert_called_with(
        "BindExtDomains",
        params={
            "envName": "env_name",
            "extdomains": "extdomains",
            "certId":[1,2]
    },
        delimiter=",",
    )
    assert response == success_response
def test_bind_ssl(client):
    client._get.return_value = success_response
    response = client.Binder.BindSSL(
        "env_name","cert_key", "cert", "intermediate"
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
        "env_name",1, ["entry_point1","entry_point2"],["ext_domains1","ext_domains2"]
    )
    client._get.assert_called_with(
        "BindSSLCert",
        params={
            "envName": "env_name",
            "certId": 1,
            "entryPoint":["entry_point1","entry_point2"],
            "extDomains":["ext_domains1","ext_domains2"]
    },
        delimiter=",",
    )
    assert response == success_response
def test_check_domain(client):
    client._get.return_value = success_response
    response = client.Binder.CheckDomain(
        "env_name","domain",["region1","region2"]
    )
    client._get.assert_called_with(
        "CheckDomain",
        params={
            "envName": "env_name",
            "domain": "domain",
            "region": ["region1","region2"]
    },
        delimiter=",",
    )
    assert response == success_response
def test_check_ext_domain(client):
    client._get.return_value = success_response
    response = client.Binder.CheckExtDomain(
        "env_name","extdomains"
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
        "env_name",1,"ip"
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
        1,["key1","key2"],["cert1","cert2"],["interm1","interm2"]
    )
    client._get.assert_called_with(
        "EditSSLCert",
        params={
            "envName": "env_name",
            "id": 1,
            "key": ["key1","key2"],
            "cert": ["cert1","cert2"],
            "interm": ["interm1","interm2"]
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
       "env_name",["node_group1","node_group2"] ,[1,2],[True,True]
    )
    client._get.assert_called_with(
        "GetDomains",
        params={
            "envName": "env_name",
            "nodeGroup":["node_group1","node_group2"],
            "nodeId": [1,2],
            "inShort":[True,True]
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
        "env_name", ["id1","id2"]
    )
    client._get.assert_called_with(
        "GetSSLCerts",
        params={
            "envName": "env_name",
            "ids":["id1","id2"]
        }, delimiter=",",
    )
    assert response == success_response
def test_manage_node_dns_state(client):
    client._get.return_value = success_response
    response = client.Binder.ManageNodeDnsState(
           "env_name",[1,2], [True,True]
    )
    client._get.assert_called_with(
        "ManageNodeDnsState",
        params={
            "envName": "env_name",
            "nodeId": [1,2],
            "enabled": [True,True]
        }, delimiter=",",
    )
    assert response == success_response
def test_move_ext_ips(client):
    client._get.return_value = success_response
    response = client.Binder.MoveExtIps(
        "env_name",1,2,"ips"
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
        "env_name", "domains",["node_group1","node_group2"],[1,2]
    )
    client._get.assert_called_with(
        "RemoveDomains",
        params={
                "envName": "env_name",
                "domains": "domains",
                "nodeGroup": ["node_group1","node_group2"],
                "node_id": [1,2],
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
        "env_name","ids"
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
        "env_name", "type",1,["node_group1","node_group2"],[1,2]
    )
    client._get.assert_called_with(
        "SetExtIpCount",
        params={
                "envName": "env_name",
                "type": "type",
                "count":1,
                "nodeGroup": ["node_group1","node_group2"],
                "node_id": [1,2],
        },
        delimiter=",",
    )
    assert response == success_response
def test_swap_ext_domains(client):
    client._get.return_value = success_response
    response = client.Binder.SwapExtDomains(
        "env_name","targetappid"
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
        "env_name",1,2,["source_ip1","source_ip2"],["target_ip1","target_ip2"]
    )
    client._get.assert_called_with(
        "SwapExtIps",
        params={
                "envName": "env_name",
                "sourceNodeId": 1,
                "targetNodeId": 2,
                "sourceIp":["source_ip1","source_ip2"],
                "targetIp":["target_ip1","target_ip2"]

        },
        delimiter=",",
    )
    assert response == success_response
def test_unbind_ssl_cert(client):
    client._get.return_value = success_response
    response = client.Binder.UnbindSSLCert(
        "env_name",["extdomains1","extdomains2"]
    )
    client._get.assert_called_with(
        "UnbindSSLCert",
        params={"envName": "env_name", "extDomains": ["extdomains1", "extdomains2"]},
        delimiter=",",
    )
    assert response == success_response


def test_add_rule(client):
    client._get.return_value = success_response
    response = client.Security.AddRule(
        "env_name", {"rule1": "rule1", "rule2": "rule2"}, ["node_group1", "node_group2"]
    )
    client._get.assert_called_with(
        "AddRule",
        params={
            "envName": "env_name",
            "rule": {"rule1": "rule1", "rule2": "rule2"},
            "nodeGroup": ["node_group1", "node_group2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_rules(client):
    client._get.return_value = success_response
    response = client.Security.AddRules(
        "env_name", "rule", ["node_group1", "node_group2"]
    )
    client._get.assert_called_with(
        "AddRules",
        params={
            "envName": "env_name",
            "rules": "rule",
            "nodeGroup": ["node_group1", "node_group2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_rule(client):
    client._get.return_value = success_response
    response = client.Security.EditRule(
        "env_name", {"rule1": "rule1", "rule2": "rule2"}
    )
    client._get.assert_called_with(
        "EditRule",
        params={
            "envName": "env_name",
            "rule": {"rule1": "rule1", "rule2": "rule2"},
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_rules(client):
    client._get.return_value = success_response
    response = client.Security.GetRules(
        "env_name", ["node_group1", "node_group2"], ["direction1", "direction2"]
    )
    client._get.assert_called_with(
        "GetRules",
        params={
            "envName": "env_name",
            "nodeGroup": ["node_group1", "node_group2"],
            "direction": ["direction1", "direction2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_regenerate_isolation_sets(client):
    client._get.return_value = success_response
    response = client.Security.RegenerateIsolationSets()
    client._get.assert_called_with(
        "RegenerateIsolationSets",
        params={},
    )
    assert response == success_response


def test_remove_rule(client):
    client._get.return_value = success_response
    response = client.Security.RemoveRule("env_name", 1)
    client._get.assert_called_with(
        "RemoveRule",
        params={"envName": "env_name", "id": 1},
    )
    assert response == success_response


def test_remove_rules(client):
    client._get.return_value = success_response
    response = client.Security.RemoveRules("env_name", [1, 2])
    client._get.assert_called_with(
        "RemoveRules",
        params={"envName": "env_name", "ids": [1, 2]},
        delimiter=",",
    )
    assert response == success_response


def test_set_firewall_enabled(client):
    client._get.return_value = success_response
    response = client.Security.SetFirewallEnabled("env_name", True)
    client._get.assert_called_with(
        "SetFirewallEnabled",
        params={
            "envName": "env_name",
            "enabled": True,
        },
    )
    assert response == success_response


def test_set_rule_enabled(client):
    client._get.return_value = success_response
    response = client.Security.SetRuleEnabled("env_name", 1, True)
    client._get.assert_called_with(
        "SetRuleEnabled",
        params={
            "envName": "env_name",
            "id": 1,
            "enabled": True,
        },
    )
    assert response == success_response


def test_set_rules(client):
    client._get.return_value = success_response
    response = client.Security.SetRules(
        "env_name", "rule", ["node_group1", "node_group2"]
    )
    client._get.assert_called_with(
        "SetRules",
        params={
            "envName": "env_name",
            "rules": "rule",
            "nodeGroup": ["node_group1", "node_group2"],
        },
        params={"envName": "env_name", "extDomains": ["extdomains1", "extdomains2"]},
        delimiter=",",
    )
    assert response == success_response
