import pytest
from unittest.mock import patch, Mock
from jelastic.api import Administration

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        admin = Administration(session=Mock(), token="token")
        admin._get = mock_get
        yield admin


def test_get_nodes_affinity_suggestion(client):
    client._get.return_value = success_response
    response = client.Analytics.GetNodesAffinitySuggestion(
        ["app_id1", "app_id2"], ["node_group1", "node_group2"], ["uid1", "uid2"], 10
    )
    client._get.assert_called_with(
        "GetNodesAffinitySuggestion",
        params={
            "targetAppIds": ["app_id1", "app_id2"],
            "nodeGroups": ["node_group1", "node_group2"],
            "uids": ["uid1", "uid2"],
            "threadCount": 10,
        },
        delimiter=",",
    )

    assert response == success_response


def test_get_nodes_anti_affinity_suggestion(client):
    client._get.return_value = success_response
    response = client.Analytics.GetNodesAntiAffinitySuggestion(
        ["app_id1", "app_id2"],
        "STRONG",
        ["node_group1", "node_group2"],
        ["uid1", "uid2"],
        10,
    )
    client._get.assert_called_with(
        "GetNodesAntiAffinitySuggestion",
        params={
            "targetAppIds": ["app_id1", "app_id2"],
            "mode": "STRONG",
            "nodeGroups": ["node_group1", "node_group2"],
            "uids": ["uid1", "uid2"],
            "threadCount": 10,
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_default_registry(client):
    client._get.return_value = success_response
    response = client.Template.SetDefaultRegistry(
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "SetDefaultRegistry",
        params={
            "id": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_distribution(client):
    client._get.return_value = success_response
    response = client.Template.SetDistribution(
        "node type",
        ["distribution1", "distribution2"],
    )
    client._get.assert_called_with(
        "SetDistribution",
        params={
            "nodeTypes": "node type",
            "distribution": ["distribution1", "distribution2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_system_external_dns_records(client):
    client._get.return_value = success_response
    response = client.Utils.AddSystemExternalDNSRecord(
        "record1",
        "name1",
        1,
        "data type 1",
        [True, False, True],
        [True, False, True],
    )
    client._get.assert_called_with(
        "AddSystemExternalDNSRecord",
        params={
            "recordData": "record1",
            "name": "name1",
            "ttl": 1,
            "recordDataType": "data type 1",
            "sslEnabled": [True, False, True],
            "enabled": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_analize_env(client):
    client._get.return_value = success_response
    response = client.Utils.AnalizeEnv(
        "domain",
    )
    client._get.assert_called_with(
        "AnalizeEnv",
        params={
            "domain": "domain",
        },
    )
    assert response == success_response


def test_balance_resources(client):
    client._get.return_value = success_response
    response = client.Utils.BalanceResources(
        1,
    )
    client._get.assert_called_with("BalanceResources", params={"domain": 1})
    assert response == success_response


def test_clear_envs(client):
    client._get.return_value = success_response
    response = client.Utils.ClearEnvs()
    client._get.assert_called_with("ClearEnvs", params={})
    assert response == success_response


def test_delete_broken_envs(client):
    client._get.return_value = success_response
    response = client.Utils.DeleteBrokenEnvs(
        ["app1", "app2", "app3"],
    )
    client._get.assert_called_with(
        "DeleteBrokenEnvs",
        params={
            "targetAppIds": ["app1", "app2", "app3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_system_external_dns_record(client):
    client._get.return_value = success_response
    response = client.Utils.EditSystemExternalDNSRecord(
        1,
        ["record1", "record2", "record2"],
        ["name1", "name2", "name3"],
        [1, 2, 3],
        ["datatype1", "datatype2", "datatype3"],
        [True, False, True],
        [True, False, True],
    )
    client._get.assert_called_with(
        "EditSystemExternalDNSRecord",
        params={
            "id": 1,
            "recordData": ["record1", "record2", "record2"],
            "name": ["name1", "name2", "name3"],
            "ttl": [1, 2, 3],
            "recordDataType": ["datatype1", "datatype2", "datatype3"],
            "sslEnabled": [True, False, True],
            "enabled": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_export_env(client):
    client._get.return_value = success_response
    response = client.Utils.ExportEnv(
        "app id 1",
    )
    client._get.assert_called_with(
        "ExportEnv",
        params={
            "targetAppId": "app id 1",
        },
    )
    assert response == success_response


def test_fix_ext_dns(client):
    client._get.return_value = success_response
    response = client.Utils.FixExtDns(
        [1, 2, 3],
        ["app id 1", "app id 2", "app id"],
    )
    client._get.assert_called_with(
        "FixExtDns",
        params={
            "uid": [1, 2, 3],
            "targetAppId": ["app id 1", "app id 2", "app id"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_fix_launching(client):
    client._get.return_value = success_response
    response = client.Utils.FixLaunching()
    client._get.assert_called_with("FixLaunching", params={})
    assert response == success_response


def test_generate_zone(client):
    client._get.return_value = success_response
    response = client.Utils.GenerateZone(
        True,
    )
    client._get.assert_called_with(
        "GenerateZone",
        params={
            "generateSlept": True,
        },
    )
    assert response == success_response


def test_get_avgs(client):
    client._get.return_value = success_response
    response = client.Utils.GetAvgs()
    client._get.assert_called_with("GetAvgs", params={})
    assert response == success_response


def test_get_avgs2(client):
    client._get.return_value = success_response
    response = client.Utils.GetAvgs2()
    client._get.assert_called_with("GetAvgs2", params={})
    assert response == success_response


def test_get_balance_stat(client):
    client._get.return_value = success_response
    response = client.Utils.GetBalancerStat(
        "2022-11-11",
        "2024-11-11",
    )
    client._get.assert_called_with(
        "GetBalancerStat",
        params={
            "starttime": "2022-11-11",
            "endtime": "2024-11-11",
        },
    )
    assert response == success_response


def test_get_cloud_lets_usage(client):
    client._get.return_value = success_response
    response = client.Utils.GetCloudletsUsage()
    client._get.assert_called_with("GetCloudletsUsage", params={})
    assert response == success_response


def test_get_db_creation_stat(client):
    client._get.return_value = success_response
    response = client.Utils.GetDBCreationStat(
        "2022-11-11",
        "2024-11-11",
    )
    client._get.assert_called_with(
        "GetDBCreationStat",
        params={
            "startTime": "2022-11-11",
            "endTime": "2024-11-11",
        },
    )
    assert response == success_response


def test_get_errors(client):
    client._get.return_value = success_response
    response = client.Utils.GetErrors(
        "2022-11-11",
        "2024-11-11",
        1,
        1,
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "GerErrors",
        params={
            "starttime": "2022-11-11",
            "endtime": "2024-11-11",
            "startrow": 1,
            "resultCount": 1,
            "filter": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_errors_by_date(client):
    client._get.return_value = success_response
    response = client.Utils.GetErrorsByDate(
        "2022-11-11",
        "2024-11-11",
        1,
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "GetErrorsByDate",
        params={
            "starttime": "2022-11-11",
            "endtime": "2024-11-11",
            "interval": 1,
            "filter": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_system_external_dns_records(client):
    client._get.return_value = success_response
    response = client.Utils.GetSystemExternalDNSRecords()
    client._get.assert_called_with("GetSystemExternalDNSRecords", params={})
    assert response == success_response


def test_get_zone(client):
    client._get.return_value = success_response
    response = client.Utils.GetZone()
    client._get.assert_called_with("GetZone", params={})
    assert response == success_response


def test_import_env(client):
    client._get.return_value = success_response
    response = client.Utils.ImportEnv(
        "env1",
        ["name1", "name2", "name3"],
        [True, False, True],
    )
    client._get.assert_called_with(
        "ImportEnv",
        params={
            "envInfo": "env1",
            "envName": ["name1", "name2", "name3"],
            "enableFirewall": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_inspect_envs(client):
    client._get.return_value = success_response
    response = client.Utils.InspectEnvs(
        [True, False, True],
    )
    client._get.assert_called_with(
        "InspectEnvs",
        params={
            "remove": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_manage_service(client):
    client._get.return_value = success_response
    response = client.Utils.ManageService(
        1,
        "command",
        "service 1",
    )
    client._get.assert_called_with(
        "ManageServices",
        params={
            "nodeid": 1,
            "command": "command",
            "servicename": "service 1",
        },
    )
    assert response == success_response


def test_remove_system_external_dns_record(client):
    client._get.return_value = success_response
    response = client.Utils.RemoveSystemExternalDNSRecord(1)
    client._get.assert_called_with(
        "RemoveSystemExternalDNSRecord",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_update_env(client):
    client._get.return_value = success_response
    response = client.Utils.UpdateEnv("app 1")
    client._get.assert_called_with(
        "UpdateEnv",
        params={
            "targetAppId": "app 1",
        },
    )
    assert response == success_response


def test_update_inv_in_thread(client):
    client._get.return_value = success_response
    response = client.Utils.UpdateEnvInThread(
        "thread app 1",
    )
    client._get.assert_called_with(
        "UpdateEnvInThread",
        params={
            "targetAppId": "thread app 1",
        },
    )
    assert response == success_response


def test_update_nodes(client):
    client._get.return_value = success_response
    response = client.Utils.UpdateNodes()
    client._get.assert_called_with("UpdateNodes", params={})
    assert response == success_response


def test_add_labels(client):
    client._get.return_value = success_response
    response = client.Host.AddLabels("app_id1", "app_label1")
    client._get.assert_called_with(
        "AddLabels",
        params={
            "ids": "app_id1",
            "labels": "app_label1",
        },
    )
    assert response == success_response


def test_check_host_connection(client):
    client._get.return_value = success_response
    response = client.Host.CheckHostConnection(
        "host_id1", [8000, 8001, 8002], [True, False, True]
    )
    client._get.assert_called_with(
        "CheckHostConnection",
        params={
            "hostId": "host_id1",
            "port": [8000, 8001, 8002],
            "checkExternalIp": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_host_firewall_sets(client):
    client._get.return_value = success_response
    response = client.Host.GetHostFirewallSets()
    client._get.assert_called_with("GetHostFirewallSets", params={})
    assert response == success_response


def test_remove_labels(client):
    client._get.return_value = success_response
    response = client.Host.RemoveLabels("app_id1", "app_label1")
    client._get.assert_called_with(
        "RemoveLabels", params={"ids": "app_id1", "labels": "app_label1"}
    )
    assert response == success_response


def test_set_label(client):
    client._get.return_value = success_response
    response = client.Host.SetLabels(
        "app_id1",
        "app_label1",
    )
    client._get.assert_called_with(
        "SetLabels", params={"ids": "app_id1", "labels": "app_label1"}
    )
    assert response == success_response


def test_update_host_firewall(client):
    client._get.return_value = success_response
    response = client.Host.UpdateHostFirewall(
        [1, 2, 3], [True, False, True], [True, False, True]
    )
    client._get.assert_called_with(
        "UpdateHostFirewall",
        params={
            "hostId": [1, 2, 3],
            "force": [True, False, True],
            "checkExternalIp": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_labels(client):
    client._get.return_value = success_response
    response = client.Host.AddLabels("app_id1", "app_label1")
    client._get.assert_called_with(
        "AddLabels",
        params={
            "ids": "app_id1",
            "labels": "app_label1",
        },
    )
    assert response == success_response


def test_check_host_connection(client):
    client._get.return_value = success_response
    response = client.Host.CheckHostConnection(
        "host_id1", [8000, 8001, 8002], [True, False, True]
    )
    client._get.assert_called_with(
        "CheckHostConnection",
        params={
            "hostId": "host_id1",
            "port": [8000, 8001, 8002],
            "checkExternalIp": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_host_firewall_sets(client):
    client._get.return_value = success_response
    response = client.Host.GetHostFirewallSets()
    client._get.assert_called_with("GetHostFirewallSets", params={})
    assert response == success_response


def test_remove_labels(client):
    client._get.return_value = success_response
    response = client.Host.RemoveLabels("app_id1", "app_label1")
    client._get.assert_called_with(
        "RemoveLabels", params={"ids": "app_id1", "labels": "app_label1"}
    )
    assert response == success_response


def test_set_label(client):
    client._get.return_value = success_response
    response = client.Host.SetLabels(
        "app_id1",
        "app_label1",
    )
    client._get.assert_called_with(
        "SetLabels", params={"ids": "app_id1", "labels": "app_label1"}
    )
    assert response == success_response


def test_update_host_firewall(client):
    client._get.return_value = success_response
    response = client.Host.UpdateHostFirewall(
        [1, 2, 3], [True, False, True], [True, False, True]
    )
    client._get.assert_called_with(
        "UpdateHostFirewall",
        params={
            "hostId": [1, 2, 3],
            "force": [True, False, True],
            "checkExternalIp": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add(client):
    client._get.return_value = success_response
    response = client.HostGroup.Add(
        {
            "add1": "val1",
            "add2": "val2",
            "add3": "val3",
            "add4": "val4",
        }
    )
    client._get.assert_called_with(
        "Add",
        params={
            "data": {
                "add1": "val1",
                "add2": "val2",
                "add3": "val3",
                "add4": "val4",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_end_points(client):
    client._get.return_value = success_response
    response = client.HostGroup.AddEndpoints(
        "host group",
        {
            "endpoint1": "val1",
            "endpoint2": "val2",
            "endpoint3": "val3",
            "endpoint4": "val4",
        },
    )
    client._get.assert_called_with(
        "AddEndpoints",
        params={
            "hostGroup": "host group",
            "endpoints": {
                "endpoint1": "val1",
                "endpoint2": "val2",
                "endpoint3": "val3",
                "endpoint4": "val4",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit(client):
    client._get.return_value = success_response
    response = client.HostGroup.Edit(
        {
            "edit1": "data1",
            "edit2": "data2",
            "edit3": "data3",
            "edit4": "data4",
        }
    )
    client._get.assert_called_with(
        "Edit",
        params={
            "data": {
                "edit1": "data1",
                "edit2": "data2",
                "edit3": "data3",
                "edit4": "data4",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_end_points(client):
    client._get.return_value = success_response
    response = client.HostGroup.EditEndpoints(
        "host group",
        {
            "endpoint1": "val1",
            "endpoint2": "val2",
            "endpoint3": "val3",
            "endpoint4": "val4",
        },
    )
    client._get.assert_called_with(
        "EditEndpoints",
        params={
            "hostGroup": "host group",
            "endpoints": {
                "endpoint1": "val1",
                "endpoint2": "val2",
                "endpoint3": "val3",
                "endpoint4": "val4",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_get(client):
    client._get.return_value = success_response
    response = client.HostGroup.Get()
    client._get.assert_called_with("Get", params={})
    assert response == success_response


def test_get_end_points(client):
    client._get.return_value = success_response
    response = client.HostGroup.GetEndpoints("host group")
    client._get.assert_called_with(
        "GetEndpoints",
        params={
            "hostGroup": "host group",
        },
    )
    assert response == success_response


def test_remove(client):
    client._get.return_value = success_response
    response = client.HostGroup.Remove(1)
    client._get.assert_called_with(
        "Remove",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_remove_end_points(client):
    client._get.return_value = success_response
    response = client.HostGroup.RemoveEndpoints(1)
    client._get.assert_called_with(
        "RemoveEndpoints",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_rename_remote_user(client):
    client._get.return_value = success_response
    response = client.HostGroup.RenameRemoteUser(1, "remoteuser@.email.com")
    client._get.assert_called_with(
        "RenameRemoteUser",
        params={
            "uid": 1,
            "email": "remoteuser@.email.com",
        },
    )
    assert response == success_response


def test_test_end_points(client):
    client._get.return_value = success_response
    response = client.HostGroup.TestEndpoints(
        {
            "endpoint1": "val1",
            "endpoint2": "val2",
            "endpoint3": "val3",
            "endpoint4": "val4",
        }
    )
    client._get.assert_called_with(
        "TestEndpoints",
        params={
            "endPoints": {
                "endpoint1": "val1",
                "endpoint2": "val2",
                "endpoint3": "val3",
                "endpoint4": "val4",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_labels(client):
    client._get.return_value = success_response
    response = client.Host.AddLabels("app_id1", "app_label1")
    client._get.assert_called_with(
        "AddLabels",
        params={
            "ids": "app_id1",
            "labels": "app_label1",
        },
    )
    assert response == success_response


def test_check_host_connection(client):
    client._get.return_value = success_response
    response = client.Host.CheckHostConnection(
        "host_id1", [8000, 8001, 8002], [True, False, True]
    )
    client._get.assert_called_with(
        "CheckHostConnection",
        params={
            "hostId": "host_id1",
            "port": [8000, 8001, 8002],
            "checkExternalIp": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_host_firewall_sets(client):
    client._get.return_value = success_response
    response = client.Host.GetHostFirewallSets()
    client._get.assert_called_with("GetHostFirewallSets", params={})
    assert response == success_response


def test_remove_labels(client):
    client._get.return_value = success_response
    response = client.Host.RemoveLabels("app_id1", "app_label1")
    client._get.assert_called_with(
        "RemoveLabels", params={"ids": "app_id1", "labels": "app_label1"}
    )
    assert response == success_response


def test_set_label(client):
    client._get.return_value = success_response
    response = client.Host.SetLabels(
        "app_id1",
        "app_label1",
    )
    client._get.assert_called_with(
        "SetLabels", params={"ids": "app_id1", "labels": "app_label1"}
    )
    assert response == success_response


def test_update_host_firewall(client):
    client._get.return_value = success_response
    response = client.Host.UpdateHostFirewall(
        [1, 2, 3], [True, False, True], [True, False, True]
    )
    client._get.assert_called_with(
        "UpdateHostFirewall",
        params={
            "hostId": [1, 2, 3],
            "force": [True, False, True],
            "checkExternalIp": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response
