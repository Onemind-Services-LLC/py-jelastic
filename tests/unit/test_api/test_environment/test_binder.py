from . import *


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


def test_add_auto_scaling_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.AddAutoScalingTrigger(
        "env_name",
        {"data1": "data1", "data2": "data2"},
    )
    client._get.assert_called_with(
        "AddAutoScalingTrigger",
        params={
            "envName": "env_name",
            "data": {"data1": "data1", "data2": "data2"},
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_load_alert_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.AddLoadAlertTrigger(
        "env_name",
        {"data1": "data1", "data2": "data2"},
    )
    client._get.assert_called_with(
        "AddLoadAlertTrigger",
        params={
            "envName": "env_name",
            "data": {"data1": "data1", "data2": "data2"},
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.AddTrigger(
        "env_name",
        {"data1": "data1", "data2": "data2"},
    )
    client._get.assert_called_with(
        "AddTrigger",
        params={
            "envName": "env_name",
            "data": {"data1": "data1", "data2": "data2"},
        },
        delimiter=",",
    )
    assert response == success_response


def test_auto_scaling_history(client):
    client._get.return_value = success_response
    response = client.Trigger.AutoScalingHistory(
        "env_name",
        1,
        1,
        [1, 1],
        ["action_types1", "action_types2"],
        [CURRENT_DATETIME, CURRENT_DATETIME],
        [CURRENT_DATETIME, CURRENT_DATETIME],
        ["order_field1", "order_field2"],
        ["order_direction1", "order_direction2"],
        ["skip_results1", "skip_results2"],
        ["node_group1", "node_group2"],
        ["resource_types1", "resource_types2"],
        [1, 2],
    )
    client._get.assert_called_with(
        "AutoScalingHistory",
        params={
            "envName": "env_name",
            "startRow": 1,
            "resultCount": 1,
            "triggerId": [1, 1],
            "actionTypes": ["action_types1", "action_types2"],
            "startTime": [CURRENT_DATETIME, CURRENT_DATETIME],
            "endTime": [CURRENT_DATETIME, CURRENT_DATETIME],
            "orderField": ["order_field1", "order_field2"],
            "orderDirection": ["order_direction1", "order_direction2"],
            "skipResults": ["skip_results1", "skip_results2"],
            "nodeGroup": ["node_group1", "node_group2"],
            "resourceTypes": ["resource_types1", "resource_types2"],
            "triggerLogId": [1, 2],
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_delete_auto_scaling_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.DeleteAutoScalingTrigger("env_name", 1)
    client._get.assert_called_with(
        "DeleteAutoScalingTrigger",
        params={"envName": "env_name", "id": 1},
    )
    assert response == success_response


def test_delete_load_alert_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.DeleteLoadAlertTrigger("env_name", 1)
    client._get.assert_called_with(
        "DeleteLoadAlertTrigger",
        params={"envName": "env_name", "id": 1},
    )
    assert response == success_response


def test_delete_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.DeleteTrigger("env_name", 1)
    client._get.assert_called_with(
        "DeleteTrigger",
        params={"envName": "env_name", "id": 1},
    )
    assert response == success_response


def test_edit_auto_scaling_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.EditAutoScalingTrigger("env_name", 1, "data")
    client._get.assert_called_with(
        "EditAutoScalingTrigger",
        params={"envName": "env_name", "id": 1, "data": "data"},
    )
    assert response == success_response


def test_edit_load_alert_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.EditLoadAlertTrigger("env_name", 1, "data")
    client._get.assert_called_with(
        "EditLoadAlertTrigger",
        params={"envName": "env_name", "id": 1, "data": "data"},
    )
    assert response == success_response


def test_edit_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.EditTrigger("env_name", 1, "data")
    client._get.assert_called_with(
        "EditTrigger",
        params={"envName": "env_name", "id": 1, "data": "data"},
    )
    assert response == success_response


def test_get_auto_scaling_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.GetAutoScalingTriggers(
        "env_name", ["action_types1", "action_types2"]
    )
    client._get.assert_called_with(
        "GetAutoScalingTriggers",
        params={
            "envName": "env_name",
            "actionTypes": ["action_types1", "action_types2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_load_alert_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.GetAutoScalingTriggers(
        "env_name", ["action_types1", "action_types2"]
    )
    client._get.assert_called_with(
        "GetAutoScalingTriggers",
        params={
            "envName": "env_name",
            "actionTypes": ["action_types1", "action_types2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_trigger_logs(client):
    client._get.return_value = success_response
    response = client.Trigger.GetTriggerLogs(
        "env_name",
        1,
        1,
        [1, 1],
        ["action_types1", "action_types2"],
        [CURRENT_DATETIME, CURRENT_DATETIME],
        [CURRENT_DATETIME, CURRENT_DATETIME],
        ["order_field1", "order_field2"],
        ["order_direction1", "order_direction2"],
        ["skip_results1", "skip_results2"],
        ["node_group1", "node_group2"],
        ["resource_types1", "resource_types2"],
        [1, 2],
    )
    client._get.assert_called_with(
        "GetTriggerLogs",
        params={
            "envName": "env_name",
            "startRow": 1,
            "resultCount": 1,
            "triggerId": [1, 1],
            "actionTypes": ["action_types1", "action_types2"],
            "startTime": [CURRENT_DATETIME, CURRENT_DATETIME],
            "endTime": [CURRENT_DATETIME, CURRENT_DATETIME],
            "orderField": ["order_field1", "order_field2"],
            "orderDirection": ["order_direction1", "order_direction2"],
            "skipResults": ["skip_results1", "skip_results2"],
            "nodeGroup": ["node_group1", "node_group2"],
            "resourceTypes": ["resource_types1", "resource_types2"],
            "triggerLogId": [1, 2],
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.GetTriggers(
        "env_name", ["action_types1", "action_types2"]
    )
    client._get.assert_called_with(
        "GetTriggers",
        params={
            "envName": "env_name",
            "actionTypes": ["action_types1", "action_types2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_load_alert_history(client):
    client._get.return_value = success_response
    response = client.Trigger.LoadAlertHistory(
        "env_name",
        1,
        1,
        [1, 1],
        ["action_types1", "action_types2"],
        [CURRENT_DATETIME, CURRENT_DATETIME],
        [CURRENT_DATETIME, CURRENT_DATETIME],
        ["order_field1", "order_field2"],
        ["order_direction1", "order_direction2"],
        ["skip_results1", "skip_results2"],
        ["node_group1", "node_group2"],
        ["resource_types1", "resource_types2"],
        [1, 2],
    )
    client._get.assert_called_with(
        "LoadAlertHistory",
        params={
            "envName": "env_name",
            "startRow": 1,
            "resultCount": 1,
            "triggerId": [1, 1],
            "actionTypes": ["action_types1", "action_types2"],
            "startTime": [CURRENT_DATETIME, CURRENT_DATETIME],
            "endTime": [CURRENT_DATETIME, CURRENT_DATETIME],
            "orderField": ["order_field1", "order_field2"],
            "orderDirection": ["order_direction1", "order_direction2"],
            "skipResults": ["skip_results1", "skip_results2"],
            "nodeGroup": ["node_group1", "node_group2"],
            "resourceTypes": ["resource_types1", "resource_types2"],
            "triggerLogId": [1, 2],
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_set_auto_scaling_trigger_enabled(client):
    client._get.return_value = success_response
    response = client.Trigger.SetAutoScalingTriggerEnabled("env_name", 1, True)
    client._get.assert_called_with(
        "SetAutoScalingTriggerEnabled",
        params={"envName": "env_name", "id": 1, "enabled": True},
    )
    assert response == success_response


def test_set_load_alert_trigger_enabled(client):
    client._get.return_value = success_response
    response = client.Trigger.SetLoadAlertTriggerEnabled("env_name", 1, True)
    client._get.assert_called_with(
        "SetLoadAlertTriggerEnabled",
        params={"envName": "env_name", "id": 1, "enabled": True},
    )
    assert response == success_response


def test_set_trigger_enabled(client):
    client._get.return_value = success_response
    response = client.Trigger.SetTriggerEnabled("env_name", 1, True)
    client._get.assert_called_with(
        "SetTriggerEnabled",
        params={"envName": "env_name", "id": 1, "enabled": True},
    )
    assert response == success_response
