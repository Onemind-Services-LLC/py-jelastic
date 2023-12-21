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


def test_check_db_connection(client):
    client._get.return_value = success_response
    response = client.System.CheckDBConnection(
        "checksum"
    )
    client._get.assert_called_with(
        "CheckDBConnection",
        params={
            "checksum": "checksum",

        },
    )
    assert response == success_response


def test_check_error(client):
    client._get.return_value = success_response
    response = client.System.CheckError(
        [1, 1]
    )
    client._get.assert_called_with(
        "CheckError",
        params={
            "code": [1, 1]

        },
        delimiter=",",
    )
    assert response == success_response


def test_clean_check_request_cache(client):
    client._get.return_value = success_response
    response = client.System.CleanCheckRequestCache(
        [1, 1]
    )
    client._get.assert_called_with(
        "CleanCheckRequestCache",
        params={
            "uid": [1, 1]
        },
        delimiter=",",
    )
    assert response == success_response


def test_clean_check_request_cache_inner(client):
    client._get.return_value = success_response
    response = client.System.CleanCheckRequestCacheInner(
        [1, 1]
    )
    client._get.assert_called_with(
        "CleanCheckRequestCacheInner",
        params={
            "uid": [1, 1]
        },
        delimiter=",",
    )
    assert response == success_response


def test_clean_template_manifest_cache(client):
    client._get.return_value = success_response
    response = client.System.CleanTemplateManifestCache(
    )
    client._get.assert_called_with(
        "CleanTemplateManifestCache",
        params={
        },
    )
    assert response == success_response


def test_delete_old_envs(client):
    client._get.return_value = success_response
    response = client.System.DeleteOldEnvs(
        "updatedon", 1, True, "checksum"
    )
    client._get.assert_called_with(
        "DeleteOldEnvs",
        params={
            "updatedon": "updatedon",
            "status": 1,
            "debug": True,
            "checksum": "checksum"

        },
    )
    assert response == success_response


def test_event(client):
    client._get.return_value = success_response
    response = client.System.Event(
        "message", [True, False],
    )
    client._get.assert_called_with(
        "Event",
        params={
            "message": "message",
            "publishLocal": [True, False],
        },
        delimiter=",",
    )
    assert response == success_response


def test_fix_duplicates(client):
    client._get.return_value = success_response
    response = client.System.FixDuplicates(
        [True, False],
    )
    client._get.assert_called_with(
        "FixDuplicates",
        params={
            "debug": [True, False],
        },
        delimiter=",",
    )
    assert response == success_response


def test_fix_stuck_envs(client):
    client._get.return_value = success_response
    response = client.System.FixStuckEnvs(
        "checksum"
    )
    client._get.assert_called_with(
        "FixStuckEnvs",
        params={
            "checksum": "checksum"
        },
    )
    assert response == success_response


def test_get_api_descriptions(client):
    client._get.return_value = success_response
    response = client.System.GetAPIDescriptions(
        [True, True], [True, True]
    )
    client._get.assert_called_with(
        "GetAPIDescriptions",
        params={
            "isPublicOnly": [True, True],
            "isToken": [True, True]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_all_api_descriptions(client):
    client._get.return_value = success_response
    response = client.System.GetAllAPIDescriptions(
        [True, True], [True, True]
    )
    client._get.assert_called_with(
        "GetAllAPIDescriptions",
        params={
            "isPublicOnly": [True, True],
            "isToken": [True, True]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_billable_items(client):
    client._get.return_value = success_response
    response = client.System.GetBillableItems(
    )
    client._get.assert_called_with(
        "GetBillableItems",
        params={
        },
    )
    assert response == success_response


def test_get_cache_stats(client):
    client._get.return_value = success_response
    response = client.System.GetCacheStats(
    )
    client._get.assert_called_with(
        "GetCacheStats",
        params={
        },
    )
    assert response == success_response


def test_get_cache_status(client):
    client._get.return_value = success_response
    response = client.System.GetCacheStatus(
    )
    client._get.assert_called_with(
        "GetCacheStatus",
        params={
        },
    )
    assert response == success_response


def test_get_cont_count_status(client):
    client._get.return_value = success_response
    response = client.System.GetContCountStatus(CURRENT_DATETIME, CURRENT_DATETIME)
    client._get.assert_called_with(
        "GetContCountStatus",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_instance_cache_status(client):
    client._get.return_value = success_response
    response = client.System.GetInstanceCacheStatus(
    )
    client._get.assert_called_with(
        "GetInstanceCacheStatus",
        params={
        },
    )
    assert response == success_response


def test_get_ips_by_type(client):
    client._get.return_value = success_response
    response = client.System.GetIpsByType("checksum", "node_type", ['hnip1', "hnip2"]
                                          )
    client._get.assert_called_with(
        "GetIpsByType",
        params={
            "checksum": "checksum",
            "nodeType": "node_type",
            "hnip": ['hnip1', "hnip2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_keyword(client):
    client._get.return_value = success_response
    response = client.System.GetKeyword(
        "checksum"
    )
    client._get.assert_called_with(
        "GetKeyword",
        params={
            "checksum": "checksum"
        },
    )
    assert response == success_response


def test_get_platform_status(client):
    client._get.return_value = success_response
    response = client.System.GetPlatformStatus(
        "checksum", [True, True]
    )
    client._get.assert_called_with(
        "GetPlatformStatus",
        params={
            "checksum": "checksum",
            "checkSMTP": [True, True]
        },
    )
    assert response == success_response


def test_get_stat_collector_status(client):
    client._get.return_value = success_response
    response = client.System.GetStatCollectorStatus(
    )
    client._get.assert_called_with(
        "GetStatCollectorStatus",
        params={
        },
    )
    assert response == success_response


def test_get_version(client):
    client._get.return_value = success_response
    response = client.System.GetVersion(
    )
    client._get.assert_called_with(
        "GetVersion",
        params={
        },
    )
    assert response == success_response


def test_refresh_email_templates(client):
    client._get.return_value = success_response
    response = client.System.RefreshEmailTemplates(
    )
    client._get.assert_called_with(
        "RefreshEmailTemplates",
        params={
        },
    )
    assert response == success_response


def test_refresh_user(client):
    client._get.return_value = success_response
    response = client.System.RefreshUser(
        ["language1", "language2"]
    )
    client._get.assert_called_with(
        "RefreshUser",
        params={
            "language": ["language1", "language2"]
        }, delimiter=",",
    )
    assert response == success_response


def test_register_env_container(client):
    client._get.return_value = success_response
    response = client.System.RegisterEnvContainer(
        "env_name", "node_type", "ip_address", "env_id", "ct_id", "passwd", "hn_ip_address"
    )
    client._get.assert_called_with(
        "RegisterEnvContainer",
        params={
            "envName": "env_name",
            "nodeType": "node_type",
            "ipAddress": "ip_address",
            "envId": "env_id",
            "ctId": "ct_id",
            "passwd": "passwd",
            "hnIpAddress": "hn_ip_address"
        }
    )
    assert response == success_response


def test_reload_configuration(client):
    client._get.return_value = success_response
    response = client.System.ReloadConfiguration(
        [1, 1], ["changed_placeholders1", "changed_placeholders2"]
    )
    client._get.assert_called_with(
        "ReloadConfiguration",
        params={
            "resellerId": [1, 1],
            "changedPlaceholders": ["changed_placeholders1", "changed_placeholders2"]
        }, delimiter=",",
    )
    assert response == success_response


def test_send_email(client):
    client._get.return_value = success_response
    response = client.System.SendEmail(
        "templates", ["email1", "email2"], ["language1", "language2"], [1, 3]
    )
    client._get.assert_called_with(
        "SendEmail",
        params={
            "templates": "templates",
            "email": ["email1", "email2"],
            "language": ["language1", "language2"],
            "timeout": [1, 3]
        }, delimiter=",",
    )
    assert response == success_response


def test_surcharge_billable_items(client):
    client._get.return_value = success_response
    response = client.System.SurchargeBillableItems(CURRENT_DATETIME, CURRENT_DATETIME)
    client._get.assert_called_with(
        "SurchargeBillableItems",
        params={
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_synch_envs(client):
    client._get.return_value = success_response
    response = client.System.SynchEnvs(
        "checksum"
    )
    client._get.assert_called_with(
        "SynchEnvs",
        params={
            "checksum": "checksum"
        },
    )
    assert response == success_response
