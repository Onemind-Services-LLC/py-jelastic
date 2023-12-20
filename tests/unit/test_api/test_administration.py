import pytest
from unittest.mock import patch, Mock
from jelastic.api import Administration
from datetime import datetime, date
import pytz

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


def test_add_action_to_isolation_queue(client):
    client._get.return_value = success_response
    response = client.Cluster.AddActionToIsolationQueue(
        [1, 2],
        [1, 2],
    )
    client._get.assert_called_with(
        "AddActionToIsolationQueue",
        params={
            "count": [1, 2],
            "delay": [1, 2],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_cartridge(client):
    client._get.return_value = success_response
    response = client.Cluster.AddCartridge(
        "manifest_url"
    )
    client._get.assert_called_with(
        "AddCartridge",
        params={
            "manifestUrl": "manifest_url"
        },
    )
    assert response == success_response


def test_add_certified_templates(client):
    client._get.return_value = success_response
    response = client.Cluster.AddCertifiedTemplates(
        "manifest_url",
        [True, False]
    )
    client._get.assert_called_with(
        "AddCertifiedTemplates",
        params={
            "repositories": "manifest_url",
            "publish": [True, False],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_ext_ips(client):
    client._get.return_value = success_response
    response = client.Cluster.AddExtIps(
        "ipfrom", "ipto", "regions"
    )
    client._get.assert_called_with(
        "AddExtIps",
        params={
            "ipfrom": "ipfrom",
            "ipto": "ipto",
            "regions": "regions",

        },
    )
    assert response == success_response


def test_add_hard_ware_node_message(client):
    client._get.return_value = success_response
    response = client.Cluster.AddHardWareNodeMessage(
        "hn_id", "message_type", "process_response_code", "percentage", "message", "custom_data"
    )
    client._get.assert_called_with(
        "AddHardWareNodeMessage",
        params={
            "hnId": "hn_id",
            "messageType": "message_type",
            "processResponseCode": "process_response_code",
            "percentage": "percentage",
            "message": "message",
            "customData": "custom_data"

        },
    )
    assert response == success_response


def test_add_hd_node(client):
    client._get.return_value = success_response
    response = client.Cluster.AddHdNode(
        {"hd_node1": "hd_node1", "hd_node2": "hd_node2"}, [True, False], [True, False]
    )
    client._get.assert_called_with(
        "AddHdNode",
        params={
            "hdnode": {"hd_node1": "hd_node1", "hd_node2": "hd_node2"},
            "setAsDockerHost": [True, False],
            "setAsDockerHost": [True, False],

        },
        delimiter=",",
    )
    assert response == success_response


def test_add_hd_node_group(client):
    client._get.return_value = success_response
    response = client.Cluster.AddHdNodeGroup(
        {"data1": "data1", "data2": "data2"}
    )
    client._get.assert_called_with(
        "AddHdNodeGroup",
        params={
            "data": {"data1": "data1", "data2": "data2"}
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_ips(client):
    client._get.return_value = success_response
    response = client.Cluster.AddIps(
        "ipfrom", "ipto", "regions"
    )
    client._get.assert_called_with(
        "AddIps",
        params={
            "ipfrom": "ipfrom",
            "ipto": "ipto",
            "region": "regions",
        },
    )
    assert response == success_response


def test_add_ipv6_network(client):
    client._get.return_value = success_response
    response = client.Cluster.AddIpv6Network(
        "region", ["network1", "network2"]
    )
    client._get.assert_called_with(
        "AddIpv6Network",
        params={
            "region": "region",
            "network": ["network1", "network2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_nameserver(client):
    client._get.return_value = success_response
    response = client.Cluster.AddNameserver(
        1, "nameserver"
    )
    client._get.assert_called_with(
        "AddNameserver",
        params={
            "nodeId": 1,
            "nameserver": "nameserver",
        },
    )
    assert response == success_response


def test_add_region(client):
    client._get.return_value = success_response
    response = client.Cluster.AddRegion(
        {"data1": "data1", "data2": "data2"}, [True, False]
    )
    client._get.assert_called_with(
        "AddRegion",
        params={
            "data": {"data1": "data1", "data2": "data2"},
            "testAuthentication": [True, False]
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_region_domain(client):
    client._get.return_value = success_response
    response = client.Cluster.AddRegionDomain(
        1, "domain", [True, False]
    )
    client._get.assert_called_with(
        "AddRegionDomain",
        params={
            "regionId": 1,
            "domain": "domain",
            "primary": [True, False]
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_region_reseller(client):
    client._get.return_value = success_response
    response = client.Cluster.AddRegionReseller(
        1, "domain", "type", True, ["ssl_type1", "ssl_type2"], [1, 2], ["key1", "key2"],
        ["intermediate1", "intermediate2"], ["cert1", "cert2"], ["source5021", "source5022"]
    )
    client._get.assert_called_with(
        "AddRegionReseller",
        params={
            "resellerId": 1,
            "domain": "domain",
            "type": "type",
            "generateDns": True,
            "sslType": ["ssl_type1", "ssl_type2"],
            "regionId": [1, 2],
            "key": ["key1", "key2"],
            "intermediate": ["intermediate1", "intermediate2"],
            "cert": ["cert1", "cert2"],
            "source502": ["source5021", "source5022"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_region_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.AddRegionSsl(
        1, "ssl_type", [1, 2], ["cert_key1", "cert_keyt2"],
        ["intermediate1", "intermediate2"], ["cert1", "cert2"],
    )
    client._get.assert_called_with(
        "AddRegionSsl",
        params={
            "regionId": 1,
            "sslType": "ssl_type",
            "domainId": [1, 2],
            "cert_key": ["cert_key1", "cert_keyt2"],
            "intermediate": ["intermediate1", "intermediate2"],
            "cert": ["cert1", "cert2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_template(client):
    client._get.return_value = success_response
    response = client.Cluster.AddTemplate(
        1, "repository", "tags", "nodeType", "nodeMission", "displayName",
        ["engine_type1", "engine_type2"],
        ["images_data1", "images_data2"], ["auto_update1", "auto_update2"],
        [True, False], [True, False], ["skip_tags_from_auto_update1", "skip_tags_from_auto_update2"],
    )
    client._get.assert_called_with(
        "AddTemplate",
        params={
            "registryId": 1,
            "repository": "repository",
            "tags": "tags",
            "nodeType": "nodeType",
            "nodeMission": "nodeMission",
            "displayName": "displayName",
            "engineType": ["engine_type1", "engine_type2"],
            "imagesData": ["images_data1", "images_data2"],
            "autoUpdate": ["auto_update1", "auto_update2"],
            "keepSelectedTags": [True, False],
            "updateDefaultTag": [True, False],
            "skipTagsFromAutoUpdate": ["skip_tags_from_auto_update1", "skip_tags_from_auto_update2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_template_registry(client):
    client._get.return_value = success_response
    response = client.Cluster.AddTemplateRegistry(
        "data"
    )
    client._get.assert_called_with(
        "AddTemplateRegistry",
        params={
            "data": "data"
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_user_to_container(client):
    client._get.return_value = success_response
    response = client.Cluster.AddUserToContainer(
        ["node_id1", "node_id2"], ["container_id1", "container_id2"], [True, True]
    )
    client._get.assert_called_with(
        "AddUserToContainer",
        params={
            "nodeId": ["node_id1", "node_id2"],
            "containerId": ["container_id1", "container_id2"],
            "regenerateKeys": [True, True]
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_users_to_gate(client):
    client._get.return_value = success_response
    response = client.Cluster.AddUsersToGate(
    )
    client._get.assert_called_with(
        "AddUsersToGate",
        params={
        },
    )
    assert response == success_response


def test_apply_firewall_rules(client):
    client._get.return_value = success_response
    response = client.Cluster.ApplyFirewallRules(
    )
    client._get.assert_called_with(
        "ApplyFirewallRules",
        params={
        },
    )
    assert response == success_response


def test_check_migration_env_possibility(client):
    client._get.return_value = success_response
    response = client.Cluster.CheckMigrationEnvPossibility(
        ["target_appid1", "target_appid2"], ["hardware_node_group1", "hardware_node_group2"]
    )
    client._get.assert_called_with(
        "CheckMigrationEnvPossibility",
        params={
            "targetAppid": ["target_appid1", "target_appid2"],
            "hardwareNodeGroup": ["hardware_node_group1", "hardware_node_group2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_clean_template_manifest_cache(client):
    client._get.return_value = success_response
    response = client.Cluster.CleanTemplateManifestCache(
    )
    client._get.assert_called_with(
        "CleanTemplateManifestCache",
        params={
        },
    )
    assert response == success_response


def test_clear_pool(client):
    client._get.return_value = success_response
    response = client.Cluster.ClearPool(
        [1, 2]
    )
    client._get.assert_called_with(
        "ClearPool",
        params={
            "hnid": [1, 2]
        },
        delimiter=",",
    )
    assert response == success_response


def test_convert_passwords(client):
    client._get.return_value = success_response
    response = client.Cluster.ConvertPasswords(
    )
    client._get.assert_called_with(
        "ConvertPasswords",
        params={
        },
    )
    assert response == success_response


def test_deactivate_region_domain(client):
    client._get.return_value = success_response
    response = client.Cluster.DeactivateRegionDomain(
        1, 2
    )
    client._get.assert_called_with(
        "DeactivateRegionDomain",
        params={
            "regionId": 1,
            "domainId": 2
        },
    )
    assert response == success_response


def test_delete_env(client):
    client._get.return_value = success_response
    response = client.Cluster.DeleteEnv(
        "target_appid", "password"
    )
    client._get.assert_called_with(
        "DeleteEnv",
        params={
            "targetAppid": "target_appid",
            "password": "password"
        },
    )
    assert response == success_response


def test_delete_envs_by_checksum(client):
    client._get.return_value = success_response
    response = client.Cluster.DeleteEnvsByChecksum(
        1, "target_appid"
    )
    client._get.assert_called_with(
        "DeleteEnvsByChecksum",
        params={
            "uid": 1,
            "targetAppid": "target_appid",
        },
    )
    assert response == success_response


def test_delete_envs_by_uid_by_checksum(client):
    client._get.return_value = success_response
    response = client.Cluster.DeleteEnvsByUidByChecksum(
        1
    )
    client._get.assert_called_with(
        "DeleteEnvsByUidByChecksum",
        params={
            "uid": 1,
        },
    )
    assert response == success_response


def test_delete_hd_node(client):
    client._get.return_value = success_response
    response = client.Cluster.DeleteHDNode(
        1, [True, True]
    )
    client._get.assert_called_with(
        "DeleteHDNode",
        params={
            "hdnodeid": 1,
            "force": [True, True]
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_hd_node(client):
    client._get.return_value = success_response
    response = client.Cluster.EditHdNode(
        {"hdnode1": "hdnode1", "hdnode2": "hdnode2"}, [True, True]
    )
    client._get.assert_called_with(
        "EditHdNode",
        params={
            "hdnode": {"hdnode1": "hdnode1", "hdnode2": "hdnode2"},
            "set_as_docker_host": [True, True]
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_hd_node_group(client):
    client._get.return_value = success_response
    response = client.Cluster.EditHdNodeGroup(
        {"data1": "data1", "data2": "data2"}
    )
    client._get.assert_called_with(
        "EditHdNodeGroup",
        params={
            "data": {"data1": "data1", "data2": "data2"}
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_region(client):
    client._get.return_value = success_response
    response = client.Cluster.EditRegion(
        {"data1": "data1", "data2": "data2"}, [True, True]
    )
    client._get.assert_called_with(
        "EditRegion",
        params={
            "data": {"data1": "data1", "data2": "data2"},
            "testAuthentication": [True, True]
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_template(client):
    client._get.return_value = success_response
    response = client.Cluster.EditTemplate(
        "node_type", ["tags1", "tags2"],
        ["display_name1", "display_name2"],
        ["engine_type1", "engine_type2"],
        ["images_data1", "images_data2"], [True, True],
        [True, True], [False, False], ["skip_tags_from_auto_update1", "skip_tags_from_auto_update2"]
    )
    client._get.assert_called_with(
        "EditTemplate",
        params={
            "nodeType": "node_type",
            "tags": ["tags1", "tags2"],
            "displayName": ["display_name1", "display_name2"],
            "engineType": ["engine_type1", "engine_type2"],
            "imagesData": ["images_data1", "images_data2"],
            "autoUpdate": [True, True],
            "keepSelectedTags": [True, True],
            "updateDefaultTag": [False, False],
            "skipTagsFromAutoUpdate": ["skip_tags_from_auto_update1", "skip_tags_from_auto_update2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_template_registry(client):
    client._get.return_value = success_response
    response = client.Cluster.EditTemplateRegistry(
        "data"
    )
    client._get.assert_called_with(
        "EditTemplateRegistry",
        params={
            "data": "data"
        },
    )
    assert response == success_response


def test_evacuate_containers(client):
    client._get.return_value = success_response
    response = client.Cluster.EvacuateContainers(
        "source_hn_id", ["possible_target_node_id1", "possible_target_node_id2"],
        [True, True]

    )
    client._get.assert_called_with(
        "EvacuateContainers",
        params={
            "sourceHnId": "source_hn_id",
            "possibleTargetNodeIds": ["possible_target_node_id1", "possible_target_node_id2"],
            "isOnline": [True, True]
        },
        delimiter=",",
    )
    assert response == success_response


def test_exec_hn_cmd(client):
    client._get.return_value = success_response
    response = client.Cluster.ExecHnCMD(
        "cmd", ["hn_id1", "hn_id2"],
        [True, True], [True, True], ["vz_version1", "vz_version2"], [True, True],

    )
    client._get.assert_called_with(
        "ExecHnCMD",
        params={
            "cmd": "cmd",
            "hnId": ["hn_id1", "hn_id2"],
            "infraOnly": [True, True],
            "runOnBroken": [True, True],
            "vzVersion": ["vz_version1", "vz_version2"],
            "dockerHostOnly": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_exec_host_cmd(client):
    client._get.return_value = success_response
    response = client.Cluster.ExecHostCmd(
        "cmd",
        [1, 2],
        [True, True], [True, True], ["vz_version1", "vz_version2"], [True, True],

    )
    client._get.assert_called_with(
        "ExecHostCmd",
        params={
            "cmd": "cmd",
            "hostId": [1, 2],
            "infraOnly": [True, True],
            "runOnBroken": [True, True],
            "vzVersion": ["vz_version1", "vz_version2"],
            "dockerHostOnly": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_generate_pool(client):
    client._get.return_value = success_response
    response = client.Cluster.GeneratePool(
        ["node_type1", "node_type2"], [1, 1],

    )
    client._get.assert_called_with(
        "GeneratePool",
        params={
            "nodeType": ["node_type1", "node_type2"],
            "hnId": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_add_hd_node_cmd(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAddHdNodeCmd(
        ["hard_node_group1", "hard_node_group2"]
    )
    client._get.assert_called_with(
        "GetAddHdNodeCmd",
        params={
            "hardNodeGroup": ["hard_node_group1", "hard_node_group2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_add_host_cmd(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAddHostCmd(
        ["hostGroup1", "hostGroup2"]
    )
    client._get.assert_called_with(
        "GetAddHostCmd",
        params={
            "hostGroup": ["hostGroup1", "hostGroup2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_all_containers(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAllContainers(
    )
    client._get.assert_called_with(
        "GetAllContainers",
        params={
        },
    )
    assert response == success_response
def test_get_all_resellers(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAllRegionReseller(
    )
    client._get.assert_called_with(
        "GetAllRegionReseller",
        params={
        },
    )
    assert response == success_response

def test_get_all_sum_stat_by_uid(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAllSumStatByUid(
        [1, 2], [datetime(2022, 11, 10, tzinfo=pytz.utc), datetime(2022, 11, 10, tzinfo=pytz.utc)], [1, 1]
    )
    client._get.assert_called_with(
        "GetAllSumStatByUid",
        params={
            "duration": [1, 2],
            "endtime": [datetime(2022, 11, 10, tzinfo=pytz.utc), datetime(2022, 11, 10, tzinfo=pytz.utc)],
            "uid": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_appid_by_domain(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAppidByDomain(
        ["domain1", "domain2"]
    )
    client._get.assert_called_with(
        "GetAppidByDomain",
        params={
            "domain": ["domain1", "domain2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_billable_items(client):
    client._get.return_value = success_response
    response = client.Cluster.GetBillableItems(
    )
    client._get.assert_called_with(
        "GetBillableItems",
        params={
        },
    )
    assert response == success_response


def test_get_cluster_load_history(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterLoadHistory(
        [datetime(2022, 11, 10, tzinfo=pytz.utc), datetime(2022, 11, 10, tzinfo=pytz.utc)],
        [datetime(2022, 9, 10, tzinfo=pytz.utc), datetime(2022, 10, 10, tzinfo=pytz.utc)]
    )
    client._get.assert_called_with(
        "GetClusterLoadHistory",
        params={
            "starttime": [datetime(2022, 11, 10, tzinfo=pytz.utc), datetime(2022, 11, 10, tzinfo=pytz.utc)],
            "endtime": [datetime(2022, 9, 10, tzinfo=pytz.utc), datetime(2022, 10, 10, tzinfo=pytz.utc)]
        },
    )
    assert response == success_response


def test_get_cluster_load_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterLoadInfo(
    )
    client._get.assert_called_with(
        "GetClusterLoadInfo",
        params={
        },
    )
    assert response == success_response


def test_get_cluster_load_percent(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterLoadPercent(
        "checksum"
    )
    client._get.assert_called_with(
        "GetClusterLoadPercent",
        params={
            "checksum": "checksum"
        },
    )
    assert response == success_response


def test_get_cluster_status(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterStatus(
        [True, True], [False, False]
    )
    client._get.assert_called_with(
        "GetClusterStatus",
        params={
            "checkSMTP": [True, True],
            "cached": [False, False]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_cluster_usage(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterUsage(
    )
    client._get.assert_called_with(
        "GetClusterUsage",
        params={
        },
    )
    assert response == success_response


def test_get_container_config(client):
    client._get.return_value = success_response
    response = client.Cluster.GetContainerConfig(
        10
    )
    client._get.assert_called_with(
        "GetContainerConfig",
        params={
            "nodeId": 10
        },
    )
    assert response == success_response


def test_get_default_region(client):
    client._get.return_value = success_response
    response = client.Cluster.GetDefaultRegion(
    )
    client._get.assert_called_with(
        "GetDefaultRegion",
        params={
        },
    )
    assert response == success_response


def test_get_default_tag_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetDefaultTagInfo(
        "node_type", ["engine1", "engine2"]
    )
    client._get.assert_called_with(
        "GetDefaultTagInfo",
        params={
            "nodeType": "node_type",
            "engine": ["engine1", "engine2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_default_tag_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetDomainByIp(
        "ips"
    )
    client._get.assert_called_with(
        "GetDomainByIp",
        params={
            "ips": "ips",
        },
    )
    assert response == success_response


def test_get_engine_types(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEngineTypes(
    )
    client._get.assert_called_with(
        "GetEngineTypes",
        params={
        },
    )
    assert response == success_response


def test_get_env_groups_by_uid(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvGroupsByUid(
        1
    )
    client._get.assert_called_with(
        "GetEnvGroupsByUid",
        params={
            "uid": 1
        },
    )
    assert response == success_response


def test_get_env_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvInfo(
        "target_appid"
    )
    client._get.assert_called_with(
        "GetEnvInfo",
        params={
            "targetAppid": "target_appid"
        },
    )
    assert response == success_response


def test_get_env_stat(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvStat(
        datetime(2022, 11, 10, tzinfo=pytz.utc), datetime(2022, 9, 10, tzinfo=pytz.utc)
    )
    client._get.assert_called_with(
        "GetEnvStat",
        params={
            "starttime": datetime(2022, 11, 10, tzinfo=pytz.utc),
            "endtime": datetime(2022, 9, 10, tzinfo=pytz.utc)
        },
    )
    assert response == success_response


def test_get_environment_group_populations(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvironmentGroupPopulations(
        datetime(2022, 11, 10, tzinfo=pytz.utc), datetime(2022, 9, 10, tzinfo=pytz.utc)
    )
    client._get.assert_called_with(
        "GetEnvironmentGroupPopulations",
        params={
            "start": datetime(2022, 11, 10, tzinfo=pytz.utc),
            "end": datetime(2022, 9, 10, tzinfo=pytz.utc)
        },
    )
    assert response == success_response


def test_get_envs(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvs(
        1, ["rights1", "rights2"], [True, True], [1, 2], [True, True]
    )
    client._get.assert_called_with(
        "GetEnvs",
        params={
            "uid": 1,
            "rights": ["rights1", "rights2"],
            "lazy": [True, True],
            "ownerUid": [1, 2],
            "sshAccessOnly": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_evacuation_state(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEvacuationState(
        1
    )
    client._get.assert_called_with(
        "GetEvacuationState",
        params={
            "hardNodeId": 1
        },
    )
    assert response == success_response


def test_get_ext_ip_pool_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetExtIpPoolInfo(
        {"search1": "search1", "search2": "search2"}
    )
    client._get.assert_called_with(
        "GetExtIpPoolInfo",
        params={
            "search": {"search1": "search1", "search2": "search2"}
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_hd_node_groups(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodeGroups(
    )
    client._get.assert_called_with(
        "GetHdNodeGroups",
        params={
        },
    )
    assert response == success_response


def test_get_hd_node_status(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodeStatus(
    )
    client._get.assert_called_with(
        "GetHdNodeStatus",
        params={
        },
    )
    assert response == success_response


def test_get_hd_nodes(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodes(
        ["id1", "id2"]
    )
    client._get.assert_called_with(
        "GetHdNodes",
        params={
            "ids": ["id1", "id2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_hd_nodes_load(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodesLoad(
        1, ["hdnodes1", "hdnodes2"]
    )
    client._get.assert_called_with(
        "GetHdNodesLoad",
        params={
            "duration": 1,
            "hdnodes": ["hdnodes1", "hdnodes2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_hd_load_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodesLoadInfo(
        ["id1", "id2"]
    )
    client._get.assert_called_with(
        "GetHdNodesLoadInfo",
        params={
            "ids": ["id1", "id2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_hosts(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHosts(
        ["id1", "id2"]
    )
    client._get.assert_called_with(
        "GetHosts",
        params={
            "ids": ["id1", "id2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_ip_pool_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetIpPoolInfo(
        {"search1": "search1", "search2": "search2"}
    )
    client._get.assert_called_with(
        "GetIpPoolInfo",
        params={
            "search": {"search1": "search1", "search2": "search2"}
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_ipv6_networks(client):
    client._get.return_value = success_response
    response = client.Cluster.GetIpv6Networks(
    )
    client._get.assert_called_with(
        "GetIpv6Networks",
        params={
        },
    )
    assert response == success_response


def test_get_ipv6_subnets_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetIpv6SubnetsInfo(
        ["search1", "search2"]
    )
    client._get.assert_called_with(
        "GetIpv6SubnetsInfo",
        params={
            "search": ["search1", "search2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_jelastic_appid(client):
    client._get.return_value = success_response
    response = client.Cluster.GetJelasticAppid(
    )
    client._get.assert_called_with(
        "GetJelasticAppid",
        params={
        },
    )
    assert response == success_response


def test_get_job_names(client):
    client._get.return_value = success_response
    response = client.Cluster.GetJobNames(
    )
    client._get.assert_called_with(
        "GetJobNames",
        params={
        },
    )
    assert response == success_response


def test_get_last_hard_ware_node_message(client):
    client._get.return_value = success_response
    response = client.Cluster.GetLastHardWareNodeMessage(
        1
    )
    client._get.assert_called_with(
        "GetLastHardWareNodeMessage",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_get_node_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodeInfo(
        "target_appid", 1
    )
    client._get.assert_called_with(
        "GetNodeInfo",
        params={
            "targetAppid": "target_appid",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_node_missions(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodeMissions(
    )
    client._get.assert_called_with(
        "GetNodeMissions",
        params={
        },
    )
    assert response == success_response


def test_get_node_password(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodePassword(
        [1, 2]
    )
    client._get.assert_called_with(
        "GetNodePassword",
        params={
            "nodeid": [1, 2]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_nodes(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodes(
        1, ["name1", "name2"], [1, 2], [1, 1]
    )
    client._get.assert_called_with(
        "GetNodes",
        params={
            "hdnodeid": 1,
            "name": ["name1", "name2"],
            "startRow": [1, 2],
            "resultCount": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_oom_killed_processes(client):
    client._get.return_value = success_response
    response = client.Cluster.GetOOMKilledProcesses(
        {"search1": "search1", "search2": "search2"}
    )
    client._get.assert_called_with(
        "GetOOMKilledProcesses",
        params={
            "search": {"search1": "search1", "search2": "search2"}
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_pcs_cluster_list(client):
    client._get.return_value = success_response
    response = client.Cluster.GetPcsClusterList(
    )
    client._get.assert_called_with(
        "GetPcsClusterList",
        params={
        },
    )
    assert response == success_response


def test_get_pool_status(client):
    client._get.return_value = success_response
    response = client.Cluster.GetPoolStatus(
    )
    client._get.assert_called_with(
        "GetPoolStatus",
        params={
        },
    )
    assert response == success_response


def test_get_region(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegion(
        1
    )
    client._get.assert_called_with(
        "GetRegion",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_get_region_dns_records(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegionDnsRecords(
        1
    )
    client._get.assert_called_with(
        "GetRegionDnsRecords",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_get_region_domains(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegionDomains(
        [1, 2]
    )
    client._get.assert_called_with(
        "GetRegionDomains",
        params={
            "regionId": [1, 2]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_region_reseller_by_reseller_id(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegionResellerByResellerId(
        1
    )
    client._get.assert_called_with(
        "GetRegionResellerByResellerId",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_get_region(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegions(
    )
    client._get.assert_called_with(
        "GetRegions",
        params={
        },
    )
    assert response == success_response


def test_get_repository_tags(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRepositoryTags(
        [1, 2], ["repository1", "repository2"]
    )
    client._get.assert_called_with(
        "GetRepositoryTags",
        params={
            "registryId": [1, 2],
            "repository": ["repository1", "repository2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_soft_node_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetSoftNodeInfo(
        1
    )
    client._get.assert_called_with(
        "GetSoftNodeInfo",
        params={
            "nodeId": 1
        },
    )
    assert response == success_response


def test_get_stand_by_status(client):
    client._get.return_value = success_response
    response = client.Cluster.GetStandByStatus(
    )
    client._get.assert_called_with(
        "GetStandByStatus",
        params={
        },
    )
    assert response == success_response


def test_get_stats(client):
    client._get.return_value = success_response
    response = client.Cluster.GetStats(
        1, 1, "target_appid",
        [datetime(2022, 11, 10, tzinfo=pytz.utc), datetime(2022, 9, 10, tzinfo=pytz.utc)
         ], [1, 2], ["nodetype1", "nodetype2"], ["node_group1", "node_group2"]

    )
    client._get.assert_called_with(
        "GetStats",
        params={
            "duration": 1,
            "interval": 1,
            "targetAppid": "target_appid",
            "endtime": [datetime(2022, 11, 10, tzinfo=pytz.utc), datetime(2022, 9, 10, tzinfo=pytz.utc)
                        ],
            "nodeid": [1, 2],
            "nodetype": ["nodetype1", "nodetype2"],
            "nodeGroup": ["node_group1", "node_group2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_sum_stats(client):
    client._get.return_value = success_response
    response = client.Cluster.GetSumStat(
        [1, 2],
        [datetime(2022, 11, 10, tzinfo=pytz.utc), datetime(2022, 9, 10, tzinfo=pytz.utc)
         ], ["target_appid1", "target_appid2"]

    )
    client._get.assert_called_with(
        "GetSumStat",
        params={
            "duration": [1, 2],
            "endtime": [datetime(2022, 11, 10, tzinfo=pytz.utc), datetime(2022, 9, 10, tzinfo=pytz.utc)
                        ],
            "targetAppid": ["target_appid1", "target_appid2"]

        },
        delimiter=",",
    )
    assert response == success_response


def test_get_system_log(client):
    client._get.return_value = success_response
    response = client.Cluster.GetSystemLog(
        "search"
    )
    client._get.assert_called_with(
        "GetSystemLog",
        params={
            "search": "search"
        },
    )
    assert response == success_response


def test_get_template_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetTemplateInfo(
        "node_type"
    )
    client._get.assert_called_with(
        "GetTemplateInfo",
        params={
            "nodeType": "node_type"
        },
    )
    assert response == success_response


def test_get_template_labels(client):
    client._get.return_value = success_response
    response = client.Cluster.GetTemplateLabels(
        "repository", [1, 2], ["tag1", "tag2"]
    )
    client._get.assert_called_with(
        "GetTemplateLabels",
        params={
            "repository": "repository",
            "registryId": [1, 2],
            "tag": ["tag1", "tag2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_template_registries(client):
    client._get.return_value = success_response
    response = client.Cluster.GetTemplateRegistries(
    )
    client._get.assert_called_with(
        "GetTemplateRegistries",
        params={
        },
    )
    assert response == success_response


def test_get_templates(client):
    client._get.return_value = success_response
    response = client.Cluster.GetTemplates(
        ["type1", "type2"], [True, True], [False, False]
    )
    client._get.assert_called_with(
        "GetTemplates",
        params={
            "type": ["type1", "type2"],
            "published": [True, True],
            "lazy": [False, False]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_user_activity(client):
    client._get.return_value = success_response
    response = client.Cluster.GetUserActivity(
        1, datetime(2022, 11, 10, tzinfo=pytz.utc), datetime(2022, 9, 10, tzinfo=pytz.utc),
        ["target_appid1", "target_appid2"], ["start_row1", "start_row2"], [1, 2],
        ["service_name1", "service_name2"], ["search_text1", "search_text2"],
        ["action_types1", "action_types2"], ["order_field1", "order_field2"],
        ["order_direction1", "order_direction2"]
    )
    client._get.assert_called_with(
        "GetUserActivity",
        params={
            "uid": 1,
            "starttime": datetime(2022, 11, 10, tzinfo=pytz.utc),
            "endtime": datetime(2022, 9, 10, tzinfo=pytz.utc),
            "targetAppid": ["target_appid1", "target_appid2"],
            "startRow": ["start_row1", "start_row2"],
            "resultCount": [1, 2],
            "serviceName": ["service_name1", "service_name2"],
            "searchText": ["search_text1", "search_text2"],
            "actionTypes": ["action_types1", "action_types2"],
            "orderField": ["order_field1", "order_field2"],
            "orderDirection": ["order_direction1", "order_direction2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_user_activities(client):
    client._get.return_value = success_response
    response = client.Cluster.GetUsersActivities(
        datetime(2022, 11, 10, tzinfo=pytz.utc),
        datetime(2022, 9, 10, tzinfo=pytz.utc),
        [1, 2], [1, 2]
    )
    client._get.assert_called_with(
        "GetUsersActivities",
        params={
            "starttime": datetime(2022, 11, 10, tzinfo=pytz.utc),
            "endtime": datetime(2022, 9, 10, tzinfo=pytz.utc),
            "startRow": [1, 2],
            "resultCount": [1, 2],
        },
        delimiter=",",
    )
    assert response == success_response


def test_l2_update(client):
    client._get.return_value = success_response
    response = client.Cluster.L2Update(
        1
    )
    client._get.assert_called_with(
        "L2Update",
        params={
            "hnId": 1,
        },
    )
    assert response == success_response


def test_migrate_env(client):
    client._get.return_value = success_response
    response = client.Cluster.MigrateEnv(
        ["target_appid1", "target_appid2"], ["hardware_node_group1", "hardware_node_group2"],
        [True, True]
    )
    client._get.assert_called_with(
        "MigrateEnv",
        params={
            "targetAppid": ["target_appid1", "target_appid2"],
            "hardwareNodeGroup": ["hardware_node_group1", "hardware_node_group2"],
            "isOnline": [True, True]
        },
        delimiter=",",
    )
    assert response == success_response


def test_migrate_node(client):
    client._get.return_value = success_response
    response = client.Cluster.MigrateNode(
        1, 1, [True, True], [True, True]
    )
    client._get.assert_called_with(
        "MigrateNode",
        params={
            "nodeid": 1,
            "hdnodeid": 1,
            "isOnline": [True, True],
            "manageDNSState": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_redeploy_containers(client):
    client._get.return_value = success_response
    response = client.Cluster.RedeployContainers(
        "target_env_name", "tag", ["node_group1", "node_group2"],
        [1, 2], [True, True], ["login1", "login2"], ["password1", "password2"],
        [True, True]
    )
    client._get.assert_called_with(
        "RedeployContainers",
        params={
            "targetEnvName": "target_env_name",
            "tag": "tag",
            "nodeGroup": ["node_group1", "node_group2"],
            "nodeId": [1, 2],
            "useExistingVolumes": [True, True],
            "login": ["login1", "login2"],
            "password": ["password1", "password2"],
            "skipReinstall": [True, True]
        },
        delimiter=",",
    )
    assert response == success_response


def test_refresh_email_templates(client):
    client._get.return_value = success_response
    response = client.Cluster.RefreshEmailTemplates(
        "modules"
    )
    client._get.assert_called_with(
        "RefreshEmailTemplates",
        params={
            "modules": "modules"
        },
    )
    assert response == success_response


def test_refresh_user(client):
    client._get.return_value = success_response
    response = client.Cluster.RefreshUser(
        ["language1", "language2"]
    )
    client._get.assert_called_with(
        "RefreshUser",
        params={
            "language": ["language1", "language2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_regenerate_pool(client):
    client._get.return_value = success_response
    response = client.Cluster.RegeneratePool(
        "node_type", ["exclude1", "exclude2"]
    )
    client._get.assert_called_with(
        "RegeneratePool",
        params={
            "nodeType": "node_type",
            "exclude": ["exclude1", "exclude2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_register_infa_module(client):
    client._get.return_value = success_response
    response = client.Cluster.RegisterInfaModule(
        ["module1", "module2"], ["dst_env_name1", "dst_env_name2"], [True, True]
    )
    client._get.assert_called_with(
        "RegisterInfaModule",
        params={
            "module": ["module1", "module2"],
            "dstEnvName": ["dst_env_name1", "dst_env_name2"],
            "dryRun": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_ext_ips(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveExtIps(
        ["ips1", "ips2"]
    )
    client._get.assert_called_with(
        "RemoveExtIps",
        params={
            "ips": ["ips1", "ips2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_hd_node_group(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveHdNodeGroup(
        1
    )
    client._get.assert_called_with(
        "RemoveHdNodeGroup",
        params={
            "id": 1
        },
    )
    assert response == success_response


def test_remove_ipv6_network(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveIpv6Network(
        1
    )
    client._get.assert_called_with(
        "RemoveIpv6Network",
        params={
            "id": 1
        },
    )
    assert response == success_response


def test_remove_region(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveRegion(
        1
    )
    client._get.assert_called_with(
        "RemoveRegion",
        params={
            "id": 1
        },
    )
    assert response == success_response


def test_remove_region_reseller(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveRegionReseller(
        1, True, [1, 2]
    )
    client._get.assert_called_with(
        "RemoveRegionReseller",
        params={
            "resellerId": 1,
            "dstEnvName": True,
            "regionId": [1, 2]
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_region_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveRegionSsl(
        [1, 2], [1, 2], 1
    )
    client._get.assert_called_with(
        "RemoveRegionSsl",
        params={
            "regionId": [1, 2],
            "domainId": [1, 2],
            "resellerId": 1,

        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_region(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveTemplate(
        "node_type"
    )
    client._get.assert_called_with(
        "RemoveTemplate",
        params={
            "nodeType": "node_type"
        },
    )
    assert response == success_response


def test_remove_template_registry(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveTemplateRegistry(
        1
    )
    client._get.assert_called_with(
        "RemoveTemplateRegistry",
        params={
            "id": 1
        },
    )
    assert response == success_response


def test_replace_node_in_env(client):
    client._get.return_value = success_response
    response = client.Cluster.ReplaceNodeInEnv(
        ["dst_env_name1", "dst_env_name2"], [1, 2], ["src_env_id1", "src_env_id2"], [1, 2]
    )
    client._get.assert_called_with(
        "ReplaceNodeInEnv",
        params={
            "dstEnvName": ["dst_env_name1", "dst_env_name2"],
            "dstNodeId": [1, 2],
            "srcEnvId": ["src_env_id1", "src_env_id2"],
            "srcHnId": [1, 2]
        },
        delimiter=",",
    )
    assert response == success_response


def test_revive_install_hd_node(client):
    client._get.return_value = success_response
    response = client.Cluster.ReviveInstallHdNode(
        1
    )
    client._get.assert_called_with(
        "ReviveInstallHdNode",
        params={
            "id": 1
        },
    )
    assert response == success_response


def test_search_envs(client):
    client._get.return_value = success_response
    response = client.Cluster.SearchEnvs(
        {"search1": "search1", "search2": "search2"}
    )
    client._get.assert_called_with(
        "SearchEnvs",
        params={
            "search": {"search1": "search1", "search2": "search2"}
        },
        delimiter=",",
    )
    assert response == success_response


def test_search_nodes(client):
    client._get.return_value = success_response
    response = client.Cluster.SearchNodes(
        {"search1": "search1", "search2": "search2"}
    )
    client._get.assert_called_with(
        "SearchNodes",
        params={
            "search": {"search1": "search1", "search2": "search2"}
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_default_template_tag(client):
    client._get.return_value = success_response
    response = client.Cluster.SetDefaultTemplateTag(
        "node_type", "tag"
    )
    client._get.assert_called_with(
        "SetDefaultTemplateTag",
        params={
            "nodeType": "node_type",
            "tag": "tag"
        },
    )
    assert response == success_response


def test_set_env_note(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvNote(
        ["target_appid1", "target_appid2"], ["note1", "note2"]
    )
    client._get.assert_called_with(
        "SetEnvNote",
        params={
            "targetAppid": ["target_appid1", "target_appid2"],
            "note": ["note1", "note2"]
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_env_status(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvStatus(
        "target_appid", 1
    )
    client._get.assert_called_with(
        "SetEnvStatus",
        params={
            "targetAppid": "target_appid",
            "status": 1
        },

    )
    assert response == success_response


def test_set_env_status(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvsStatus(
        "target_appid", 1
    )
    client._get.assert_called_with(
        "SetEnvsStatus",
        params={
            "targetAppid": "target_appid",
            "status": 1
        },

    )
    assert response == success_response


def test_set_env_status(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvsStatusByUid(
        1, 1
    )
    client._get.assert_called_with(
        "SetEnvsStatusByUid",
        params={
            "uid": 1,
            "status": 1,
        },

    )
    assert response == success_response


def test_set_envs_status_by_uid_by_checksum(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvsStatusByUidByChecksum(
        1, 1
    )
    client._get.assert_called_with(
        "SetEnvsStatusByUidByChecksum",
        params={
            "uid": 1,
            "status": 1,
        },
    )
    assert response == success_response


def test_set_region_dns_records(client):
    client._get.return_value = success_response
    response = client.Cluster.SetRegionDnsRecords(
        1, 1,
    )
    client._get.assert_called_with(
        "SetRegionDnsRecords",
        params={
            "id": 1,
            "data": 1,
        },
    )
    assert response == success_response


def test_set_region_primary_domain(client):
    client._get.return_value = success_response
    response = client.Cluster.SetRegionPrimaryDomain(
        1, 1
    )
    client._get.assert_called_with(
        "SetRegionPrimaryDomain",
        params={
            "regionId": 1,
            "domainId": 1,
        },
    )
    assert response == success_response


def test_set_stand_by_mode(client):
    client._get.return_value = success_response
    response = client.Cluster.SetStandbyMode(True)
    client._get.assert_called_with(
        "SetStandbyMode",
        params={
            "enabled": True,
        },
    )
    assert response == success_response


def test_set_template_published(client):
    client._get.return_value = success_response
    response = client.Cluster.SetTemplatePublished(
        'node type', True
    )
    client._get.assert_called_with(
        "SetTemplatePublished",
        params={
            "nodeType": 'node type',
            "published": True
        },
    )
    assert response == success_response


def test_sleep(client):
    client._get.return_value = success_response
    response = client.Cluster.Sleep(
        [datetime(2022, 11, 11, tzinfo=pytz.utc), datetime(2022, 11, 11, tzinfo=pytz.utc)],
        [datetime(2024, 11, 11, tzinfo=pytz.utc), datetime(2024, 11, 11, tzinfo=pytz.utc)],
        [1, 2, 3]
    )
    client._get.assert_called_with(
        "Sleep",
        params={
            "starttime": [datetime(2022, 11, 11, tzinfo=pytz.utc), datetime(2022, 11, 11, tzinfo=pytz.utc)],
            "endtime": [datetime(2024, 11, 11, tzinfo=pytz.utc), datetime(2024, 11, 11, tzinfo=pytz.utc)],
            "deactivateAfter": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_start_env(client):
    client._get.return_value = success_response
    response = client.Cluster.StartEnv(
        'target'
    )
    client._get.assert_called_with(
        "StartEnv(",
        params={
            "targetAppid": 'target',
        },
    )
    assert response == success_response


def test_stop_balance_resources(client):
    client._get.return_value = success_response
    response = client.Cluster.StopBalanceResources()
    client._get.assert_called_with(
        "StopBalanceResources(",
        params={
        },
    )
    assert response == success_response


def test_stop_env(client):
    client._get.return_value = success_response
    response = client.Cluster.StopEnv(
        'target'
    )
    client._get.assert_called_with(
        "StopEnv(",
        params={
            "targetAppid": 'target',
        },
    )
    assert response == success_response


def test_stop_evacuation(client):
    client._get.return_value = success_response
    response = client.Cluster.StopEvacuation(
        'hard node'
    )
    client._get.assert_called_with(
        "StopEvacuation",
        params={
            "hardNodeId": 'hard node',
        },
    )
    assert response == success_response


def test_sync_cloud_lets(client):
    client._get.return_value = success_response
    response = client.Cluster.SyncCloudlets(
        datetime(2022, 11, 11, tzinfo=pytz.utc),
        [True, False, True],
    )
    client._get.assert_called_with(
        "SyncCloudlets(",
        params={
            "starttime": datetime(2022, 11, 11, tzinfo=pytz.utc),
            "debug": [True, False, True],
        },
    )
    assert response == success_response


def test_sync_infa_module(client):
    client._get.return_value = success_response
    response = client.Cluster.SyncInfaModule(
        'node group',
        'dst env',
        'components',
        ['tag1', 'tag2', 'tag3'],
    )
    client._get.assert_called_with(
        "SyncInfaModule",
        params={
            "nodeGroup": 'node group',
            "dstEnvName": 'dst env',
            "components": 'components',
            "targetTag": ['tag1', 'tag2', 'tag3'],
        },
        delimiter=",",
    )
    assert response == success_response


def test_update_region_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.UpdateRegionSsl(
        1,
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "UpdateRegionSsl",
        params={
            "regionId": 1,
            "domainId": [1, 2, 3, 4],
        },
    )
    assert response == success_response


def test_update_reseller_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.UpdateResellerSsl(
        1, 1
    )
    client._get.assert_called_with(
        "UpdateResellerSsl",
        params={
            "regionId": 1,
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_update_template(client):
    client._get.return_value = success_response
    response = client.Cluster.UpdateTemplate(
        1,
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "UpdateTemplate",
        params={
            "nodeType": 1,
            "iconsOnly": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_validate(client):
    client._get.return_value = success_response
    response = client.Cluster.Validate(
    )
    client._get.assert_called_with(
        "Validate",
        params={
        },
    )
    assert response == success_response


def test_velidate_all(client):
    client._get.return_value = success_response
    response = client.Cluster.ValidateAll()
    client._get.assert_called_with(
        "ValidateAll",
        params={
        },
    )
    assert response == success_response


def test_validate_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.ValidateSsl(
        'domain',
        ['key1', 'key2', 'key3'],
        ['intermediate1', 'intermediate2', 'intermediate3'],
        ['certificate1', 'certificate2', 'certificate3'],
    )
    client._get.assert_called_with(
        "ValidateSsl",
        params={
            "domain": 'domain',
            "key": ['key1', 'key2', 'key3'],
            "intermediate": ['intermediate1', 'intermediate2', 'intermediate3'],
            "cert": ['certificate1', 'certificate2', 'certificate3'],
        },
        delimiter=",",
    )
    assert response == success_response
