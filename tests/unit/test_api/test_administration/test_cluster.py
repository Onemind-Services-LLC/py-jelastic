from . import *


def test_add_action_to_isolation_queue(client):
    client._get.return_value = success_response
    response = client.Cluster.AddActionToIsolationQueue(1, 2)
    client._get.assert_called_with(
        "AddActionToIsolationQueue",
        params={"count": 1, "delay": 2},
    )
    assert response == success_response


def test_add_cartridge(client):
    client._get.return_value = success_response
    response = client.Cluster.AddCartridge("manifest_url")
    client._get.assert_called_with(
        "AddCartridge",
        params={"manifestUrl": "manifest_url"},
    )
    assert response == success_response


def test_add_certified_templates(client):
    client._get.return_value = success_response
    response = client.Cluster.AddCertifiedTemplates("manifest_url", True)
    client._get.assert_called_with(
        "AddCertifiedTemplates",
        params={
            "repositories": "manifest_url",
            "publish": True,
        },
    )
    assert response == success_response


def test_add_ext_ips(client):
    client._get.return_value = success_response
    response = client.Cluster.AddExtIps("ipfrom", "ipto", "regions")
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
        "hn_id",
        "message_type",
        "process_response_code",
        "percentage",
        "message",
        "custom_data",
    )
    client._get.assert_called_with(
        "AddHardWareNodeMessage",
        params={
            "hnId": "hn_id",
            "messageType": "message_type",
            "processResponseCode": "process_response_code",
            "percentage": "percentage",
            "message": "message",
            "customData": "custom_data",
        },
    )
    assert response == success_response


def test_add_hd_node(client):
    client._get.return_value = success_response
    response = client.Cluster.AddHdNode(
        {"hd_node1": "hd_node1", "hd_node2": "hd_node2"}, True, False
    )
    client._get.assert_called_with(
        "AddHdNode",
        params={
            "hdnode": {"hd_node1": "hd_node1", "hd_node2": "hd_node2"},
            "setAsDockerHost": True,
            "skipConfiguration": False,
        },
    )
    assert response == success_response


def test_add_hd_node_group(client):
    client._get.return_value = success_response
    response = client.Cluster.AddHdNodeGroup({"data1": "data1", "data2": "data2"})
    client._get.assert_called_with(
        "AddHdNodeGroup",
        params={"data": {"data1": "data1", "data2": "data2"}},
    )
    assert response == success_response


def test_add_ips(client):
    client._get.return_value = success_response
    response = client.Cluster.AddIps("ipfrom", "ipto", "regions")
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
    response = client.Cluster.AddIpv6Network("region", "network")
    client._get.assert_called_with(
        "AddIpv6Network",
        params={"region": "region", "network": "network"},
    )
    assert response == success_response


def test_add_nameserver(client):
    client._get.return_value = success_response
    response = client.Cluster.AddNameserver(1, "nameserver")
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
    response = client.Cluster.AddRegion({"data1": "data1", "data2": "data2"}, True)
    client._get.assert_called_with(
        "AddRegion",
        params={
            "data": {"data1": "data1", "data2": "data2"},
            "testAuthentication": True,
        },
    )
    assert response == success_response


def test_add_region_domain(client):
    client._get.return_value = success_response
    response = client.Cluster.AddRegionDomain(1, "domain", True)
    client._get.assert_called_with(
        "AddRegionDomain",
        params={"regionId": 1, "domain": "domain", "primary": True},
    )
    assert response == success_response


def test_add_region_reseller(client):
    client._get.return_value = success_response
    response = client.Cluster.AddRegionReseller(
        1,
        "domain",
        "type",
        True,
        "sslType",
        1,
        "key",
        "intermediate",
        "cert",
        "source502",
    )
    client._get.assert_called_with(
        "AddRegionReseller",
        params={
            "resellerId": 1,
            "domain": "domain",
            "type": "type",
            "generateDns": True,
            "sslType": "sslType",
            "regionId": 1,
            "key": "key",
            "intermediate": "intermediate",
            "cert": "cert",
            "source502": "source502",
        },
    )
    assert response == success_response


def test_add_region_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.AddRegionSsl(
        1, "ssl_type", 1, "cert_key", "intermediate", "cert"
    )
    client._get.assert_called_with(
        "AddRegionSsl",
        params={
            "regionId": 1,
            "sslType": "ssl_type",
            "domainId": 1,
            "cert_key": "cert_key",
            "intermediate": "intermediate",
            "cert": "cert",
        },
    )
    assert response == success_response


def test_add_template(client):
    client._get.return_value = success_response
    response = client.Cluster.AddTemplate(
        1,
        "repository",
        "tags",
        "nodeType",
        "nodeMission",
        "displayName",
        "engineType",
        "imagesData",
        "autoUpdate",
        True,
        False,
        "skipTagsFromAutoUpdate",
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
            "engineType": "engineType",
            "imagesData": "imagesData",
            "autoUpdate": "autoUpdate",
            "keepSelectedTags": True,
            "updateDefaultTag": False,
            "skipTagsFromAutoUpdate": "skipTagsFromAutoUpdate",
        },
    )
    assert response == success_response


def test_add_template_registry(client):
    client._get.return_value = success_response
    response = client.Cluster.AddTemplateRegistry("data")
    client._get.assert_called_with(
        "AddTemplateRegistry",
        params={"data": "data"},
    )
    assert response == success_response


def test_add_user_to_container(client):
    client._get.return_value = success_response
    response = client.Cluster.AddUserToContainer(1, 1, True)
    client._get.assert_called_with(
        "AddUserToContainer",
        params={"nodeId": 1, "containerId": 1, "regenerateKeys": True},
    )
    assert response == success_response


def test_add_users_to_gate(client):
    client._get.return_value = success_response
    response = client.Cluster.AddUsersToGate()
    client._get.assert_called_with(
        "AddUsersToGate",
        params={},
    )
    assert response == success_response


def test_apply_firewall_rules(client):
    client._get.return_value = success_response
    response = client.Cluster.ApplyFirewallRules()
    client._get.assert_called_with(
        "ApplyFirewallRules",
        params={},
    )
    assert response == success_response


def test_check_migration_env_possibility(client):
    client._get.return_value = success_response
    response = client.Cluster.CheckMigrationEnvPossibility(
        "targetAppid", "hardwareNodeGroup"
    )
    client._get.assert_called_with(
        "CheckMigrationEnvPossibility",
        params={"targetAppid": "targetAppid", "hardwareNodeGroup": "hardwareNodeGroup"},
    )
    assert response == success_response


def test_clean_template_manifest_cache(client):
    client._get.return_value = success_response
    response = client.Cluster.CleanTemplateManifestCache()
    client._get.assert_called_with(
        "CleanTemplateManifestCache",
        params={},
    )
    assert response == success_response


def test_clear_pool(client):
    client._get.return_value = success_response
    response = client.Cluster.ClearPool(1)
    client._get.assert_called_with(
        "ClearPool",
        params={"hnid": 1},
    )
    assert response == success_response


def test_convert_passwords(client):
    client._get.return_value = success_response
    response = client.Cluster.ConvertPasswords()
    client._get.assert_called_with(
        "ConvertPasswords",
        params={},
    )
    assert response == success_response


def test_deactivate_region_domain(client):
    client._get.return_value = success_response
    response = client.Cluster.DeactivateRegionDomain(1, 2)
    client._get.assert_called_with(
        "DeactivateRegionDomain",
        params={"regionId": 1, "domainId": 2},
    )
    assert response == success_response


def test_delete_env(client):
    client._get.return_value = success_response
    response = client.Cluster.DeleteEnv("target_appid", "password")
    client._get.assert_called_with(
        "DeleteEnv",
        params={"targetAppid": "target_appid", "password": "password"},
    )
    assert response == success_response


def test_delete_envs_by_checksum(client):
    client._get.return_value = success_response
    response = client.Cluster.DeleteEnvsByChecksum("checksum", 1, "target_appid")
    client._get.assert_called_with(
        "DeleteEnvsByChecksum",
        params={
            "checksum": "checksum",
            "uid": 1,
            "targetAppid": "target_appid",
        },
    )
    assert response == success_response


def test_delete_envs_by_uid_by_checksum(client):
    client._get.return_value = success_response
    response = client.Cluster.DeleteEnvsByUidByChecksum(1)
    client._get.assert_called_with(
        "DeleteEnvsByUidByChecksum",
        params={
            "uid": 1,
        },
    )
    assert response == success_response


def test_delete_hd_node(client):
    client._get.return_value = success_response
    response = client.Cluster.DeleteHDNode(1, True)
    client._get.assert_called_with(
        "DeleteHDNode",
        params={"hdnodeid": 1, "force": True},
    )
    assert response == success_response


def test_edit_hd_node(client):
    client._get.return_value = success_response
    response = client.Cluster.EditHdNode(
        {"hdnode1": "hdnode1", "hdnode2": "hdnode2"}, True
    )
    client._get.assert_called_with(
        "EditHdNode",
        params={
            "hdnode": {"hdnode1": "hdnode1", "hdnode2": "hdnode2"},
            "set_as_docker_host": True,
        },
    )
    assert response == success_response


def test_edit_hd_node_group(client):
    client._get.return_value = success_response
    response = client.Cluster.EditHdNodeGroup({"data1": "data1", "data2": "data2"})
    client._get.assert_called_with(
        "EditHdNodeGroup",
        params={"data": {"data1": "data1", "data2": "data2"}},
    )
    assert response == success_response


def test_edit_region(client):
    client._get.return_value = success_response
    response = client.Cluster.EditRegion({"data1": "data1", "data2": "data2"}, True)
    client._get.assert_called_with(
        "EditRegion",
        params={
            "data": {"data1": "data1", "data2": "data2"},
            "testAuthentication": True,
        },
    )
    assert response == success_response


def test_edit_template(client):
    client._get.return_value = success_response
    response = client.Cluster.EditTemplate(
        "node_type",
        "tags",
        "displayName",
        "engineType",
        "imagesData",
        True,
        False,
        False,
        "skipTagsFromAutoUpdate",
    )
    client._get.assert_called_with(
        "EditTemplate",
        params={
            "nodeType": "node_type",
            "tags": "tags",
            "displayName": "displayName",
            "engineType": "engineType",
            "imagesData": "imagesData",
            "autoUpdate": True,
            "keepSelectedTags": False,
            "updateDefaultTag": False,
            "skipTagsFromAutoUpdate": "skipTagsFromAutoUpdate",
        },
    )
    assert response == success_response


def test_edit_template_registry(client):
    client._get.return_value = success_response
    response = client.Cluster.EditTemplateRegistry("data")
    client._get.assert_called_with(
        "EditTemplateRegistry",
        params={"data": "data"},
    )
    assert response == success_response


def test_evacuate_containers(client):
    client._get.return_value = success_response
    response = client.Cluster.EvacuateContainers(
        "source_hn_id", "possibleTargetNodeIds", True
    )
    client._get.assert_called_with(
        "EvacuateContainers",
        params={
            "sourceHnId": "source_hn_id",
            "possibleTargetNodeIds": "possibleTargetNodeIds",
            "isOnline": True,
        },
    )
    assert response == success_response


def test_exec_hn_cmd(client):
    client._get.return_value = success_response
    response = client.Cluster.ExecHnCMD("cmd", 1, True, True, "vzVersion", True)
    client._get.assert_called_with(
        "ExecHnCMD",
        params={
            "cmd": "cmd",
            "hnId": 1,
            "infraOnly": True,
            "runOnBroken": True,
            "vzVersion": "vzVersion",
            "dockerHostOnly": True,
        },
    )
    assert response == success_response


def test_exec_host_cmd(client):
    client._get.return_value = success_response
    response = client.Cluster.ExecHostCmd("cmd", 1, True, True, "vzVersion", True)
    client._get.assert_called_with(
        "ExecHostCmd",
        params={
            "cmd": "cmd",
            "hostId": 1,
            "infraOnly": True,
            "runOnBroken": True,
            "vzVersion": "vzVersion",
            "dockerHostOnly": True,
        },
    )
    assert response == success_response


def test_generate_pool(client):
    client._get.return_value = success_response
    response = client.Cluster.GeneratePool("nodeType", 1)
    client._get.assert_called_with(
        "GeneratePool",
        params={"nodeType": "nodeType", "hnId": 1},
    )
    assert response == success_response


def test_get_add_hd_node_cmd(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAddHdNodeCmd("hardNodeGroup")
    client._get.assert_called_with(
        "GetAddHdNodeCmd", params={"hardNodeGroup": "hardNodeGroup"}
    )
    assert response == success_response


def test_get_add_host_cmd(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAddHostCmd("host_group")
    client._get.assert_called_with(
        "GetAddHostCmd",
        params={"hostGroup": "host_group"},
    )
    assert response == success_response


def test_get_all_containers(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAllContainers()
    client._get.assert_called_with(
        "GetAllContainers",
        params={},
    )
    assert response == success_response


def test_get_all_resellers(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAllRegionReseller()
    client._get.assert_called_with(
        "GetAllRegionReseller",
        params={},
    )
    assert response == success_response


def test_get_all_sum_stat_by_uid(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAllSumStatByUid(1, CURRENT_DATETIME, 1)
    client._get.assert_called_with(
        "GetAllSumStatByUid",
        params={"duration": 1, "endtime": CURRENT_DATETIME, "uid": 1},
    )
    assert response == success_response


def test_get_appid_by_domain(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAppidByDomain("domain")
    client._get.assert_called_with("GetAppidByDomain", params={"domain": "domain"})
    assert response == success_response


def test_get_billable_items(client):
    client._get.return_value = success_response
    response = client.Cluster.GetBillableItems()
    client._get.assert_called_with(
        "GetBillableItems",
        params={},
    )
    assert response == success_response


def test_get_cluster_load_history(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterLoadHistory(CURRENT_DATETIME, CURRENT_DATETIME)
    client._get.assert_called_with(
        "GetClusterLoadHistory",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_cluster_load_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterLoadInfo()
    client._get.assert_called_with(
        "GetClusterLoadInfo",
        params={},
    )
    assert response == success_response


def test_get_cluster_load_percent(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterLoadPercent("checksum")
    client._get.assert_called_with(
        "GetClusterLoadPercent",
        params={"checksum": "checksum"},
    )
    assert response == success_response


def test_get_cluster_status(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterStatus(True, True)
    client._get.assert_called_with(
        "GetClusterStatus", params={"checkSMTP": True, "cached": True}
    )
    assert response == success_response


def test_get_cluster_usage(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterUsage()
    client._get.assert_called_with(
        "GetClusterUsage",
        params={},
    )
    assert response == success_response


def test_get_container_config(client):
    client._get.return_value = success_response
    response = client.Cluster.GetContainerConfig(10)
    client._get.assert_called_with(
        "GetContainerConfig",
        params={"nodeId": 10},
    )
    assert response == success_response


def test_get_default_region(client):
    client._get.return_value = success_response
    response = client.Cluster.GetDefaultRegion()
    client._get.assert_called_with(
        "GetDefaultRegion",
        params={},
    )
    assert response == success_response


def test_get_default_tag_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetDefaultTagInfo("node_type", "engine")
    client._get.assert_called_with(
        "GetDefaultTagInfo",
        params={"nodeType": "node_type", "engine": "engine"},
    )
    assert response == success_response


def test_get_domain_by_ip(client):
    client._get.return_value = success_response
    response = client.Cluster.GetDomainByIp("ips")
    client._get.assert_called_with(
        "GetDomainByIp",
        params={
            "ips": "ips",
        },
    )
    assert response == success_response


def test_get_engine_types(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEngineTypes()
    client._get.assert_called_with(
        "GetEngineTypes",
        params={},
    )
    assert response == success_response


def test_get_env_groups_by_uid(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvGroupsByUid(1)
    client._get.assert_called_with(
        "GetEnvGroupsByUid",
        params={"uid": 1},
    )
    assert response == success_response


def test_get_env_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvInfo("target_appid")
    client._get.assert_called_with(
        "GetEnvInfo",
        params={"targetAppid": "target_appid"},
    )
    assert response == success_response


def test_get_env_stat(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvStat(
        CURRENT_DATETIME,
        CURRENT_DATETIME,
    )
    client._get.assert_called_with(
        "GetEnvStat",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_environment_group_populations(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvironmentGroupPopulations(
        CURRENT_DATETIME, CURRENT_DATETIME
    )
    client._get.assert_called_with(
        "GetEnvironmentGroupPopulations",
        params={"start": CURRENT_DATETIME, "end": CURRENT_DATETIME},
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_envs(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvs(1, ["rights1", "rights2"], True, 1, True)
    client._get.assert_called_with(
        "GetEnvs",
        params={
            "uid": 1,
            "rights": ["rights1", "rights2"],
            "lazy": True,
            "ownerUid": 1,
            "sshAccessOnly": True,
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_evacuation_state(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEvacuationState(1)
    client._get.assert_called_with(
        "GetEvacuationState",
        params={"hardNodeId": 1},
    )
    assert response == success_response


def test_get_ext_ip_pool_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetExtIpPoolInfo(
        {"search1": "search1", "search2": "search2"}
    )
    client._get.assert_called_with(
        "GetExtIpPoolInfo",
        params={"search": {"search1": "search1", "search2": "search2"}},
    )
    assert response == success_response


def test_get_hd_node_groups(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodeGroups()
    client._get.assert_called_with(
        "GetHdNodeGroups",
        params={},
    )
    assert response == success_response


def test_get_hd_node_status(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodeStatus()
    client._get.assert_called_with(
        "GetHdNodeStatus",
        params={},
    )
    assert response == success_response


def test_get_hd_nodes(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodes("id")
    client._get.assert_called_with(
        "GetHdNodes",
        params={"ids": "id"},
    )
    assert response == success_response


def test_get_hd_nodes_load(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodesLoad(1, "hdnodes")
    client._get.assert_called_with(
        "GetHdNodesLoad",
        params={"duration": 1, "hdnodes": "hdnodes"},
    )
    assert response == success_response


def test_get_hd_load_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodesLoadInfo("id")
    client._get.assert_called_with(
        "GetHdNodesLoadInfo",
        params={"ids": "id"},
    )
    assert response == success_response


def test_get_hosts(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHosts("id")
    client._get.assert_called_with("GetHosts", params={"ids": "id"})
    assert response == success_response


def test_get_ip_pool_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetIpPoolInfo(
        {"search1": "search1", "search2": "search2"}
    )
    client._get.assert_called_with(
        "GetIpPoolInfo", params={"search": {"search1": "search1", "search2": "search2"}}
    )
    assert response == success_response


def test_get_ipv6_networks(client):
    client._get.return_value = success_response
    response = client.Cluster.GetIpv6Networks()
    client._get.assert_called_with(
        "GetIpv6Networks",
        params={},
    )
    assert response == success_response


def test_get_ipv6_subnets_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetIpv6SubnetsInfo("search")
    client._get.assert_called_with("GetIpv6SubnetsInfo", params={"search": "search"})
    assert response == success_response


def test_get_jelastic_appid(client):
    client._get.return_value = success_response
    response = client.Cluster.GetJelasticAppid()
    client._get.assert_called_with(
        "GetJelasticAppid",
        params={},
    )
    assert response == success_response


def test_get_job_names(client):
    client._get.return_value = success_response
    response = client.Cluster.GetJobNames()
    client._get.assert_called_with(
        "GetJobNames",
        params={},
    )
    assert response == success_response


def test_get_last_hard_ware_node_message(client):
    client._get.return_value = success_response
    response = client.Cluster.GetLastHardWareNodeMessage(1)
    client._get.assert_called_with(
        "GetLastHardWareNodeMessage",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_get_node_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodeInfo("target_appid", 1)
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
    response = client.Cluster.GetNodeMissions()
    client._get.assert_called_with(
        "GetNodeMissions",
        params={},
    )
    assert response == success_response


def test_get_node_password(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodePassword(1)
    client._get.assert_called_with("GetNodePassword", params={"nodeid": 1})
    assert response == success_response


def test_get_nodes(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodes(1, "name", 1, 1)
    client._get.assert_called_with(
        "GetNodes",
        params={"hdnodeid": 1, "name": "name", "startRow": 1, "resultCount": 1},
    )
    assert response == success_response


def test_get_oom_killed_processes(client):
    client._get.return_value = success_response
    response = client.Cluster.GetOOMKilledProcesses(
        {"search1": "search1", "search2": "search2"}
    )
    client._get.assert_called_with(
        "GetOOMKilledProcesses",
        params={"search": {"search1": "search1", "search2": "search2"}},
    )
    assert response == success_response


def test_get_pcs_cluster_list(client):
    client._get.return_value = success_response
    response = client.Cluster.GetPcsClusterList()
    client._get.assert_called_with(
        "GetPcsClusterList",
        params={},
    )
    assert response == success_response


def test_get_pool_status(client):
    client._get.return_value = success_response
    response = client.Cluster.GetPoolStatus()
    client._get.assert_called_with(
        "GetPoolStatus",
        params={},
    )
    assert response == success_response


def test_get_region(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegion(1)
    client._get.assert_called_with(
        "GetRegion",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_get_region_dns_records(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegionDnsRecords(1)
    client._get.assert_called_with(
        "GetRegionDnsRecords",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_get_region_domains(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegionDomains(1)
    client._get.assert_called_with(
        "GetRegionDomains",
        params={"regionId": 1},
        delimiter=",",
    )
    assert response == success_response


def test_get_region_reseller_by_reseller_id(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegionResellerByResellerId(1)
    client._get.assert_called_with(
        "GetRegionResellerByResellerId",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_get_regions(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegions()
    client._get.assert_called_with(
        "GetRegions",
        params={},
    )
    assert response == success_response


def test_get_repository_tags(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRepositoryTags("repository", 1)
    client._get.assert_called_with(
        "GetRepositoryTags", params={"repository": "repository", "registryId": 1}
    )
    assert response == success_response


def test_get_soft_node_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetSoftNodeInfo(1)
    client._get.assert_called_with(
        "GetSoftNodeInfo",
        params={"nodeId": 1},
    )
    assert response == success_response


def test_get_stand_by_status(client):
    client._get.return_value = success_response
    response = client.Cluster.GetStandByStatus()
    client._get.assert_called_with(
        "GetStandByStatus",
        params={},
    )
    assert response == success_response


def test_get_stats(client):
    client._get.return_value = success_response
    response = client.Cluster.GetStats(
        1, 1, "target_appid", CURRENT_DATETIME, 1, "nodetype", "nodeGroup"
    )
    client._get.assert_called_with(
        "GetStats",
        params={
            "duration": 1,
            "interval": 1,
            "targetAppid": "target_appid",
            "endtime": CURRENT_DATETIME,
            "nodeid": 1,
            "nodetype": "nodetype",
            "nodeGroup": "nodeGroup",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_sum_stats(client):
    client._get.return_value = success_response
    response = client.Cluster.GetSumStat(1, CURRENT_DATETIME, "target_appid")
    client._get.assert_called_with(
        "GetSumStat",
        params={
            "duration": 1,
            "endtime": CURRENT_DATETIME,
            "targetAppid": "target_appid",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_system_log(client):
    client._get.return_value = success_response
    response = client.Cluster.GetSystemLog("search")
    client._get.assert_called_with(
        "GetSystemLog",
        params={"search": "search"},
    )
    assert response == success_response


def test_get_template_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetTemplateInfo("node_type")
    client._get.assert_called_with(
        "GetTemplateInfo",
        params={"nodeType": "node_type"},
    )
    assert response == success_response


def test_get_template_labels(client):
    client._get.return_value = success_response
    response = client.Cluster.GetTemplateLabels("repository", 1, "tag")
    client._get.assert_called_with(
        "GetTemplateLabels",
        params={"repository": "repository", "registryId": 1, "tag": "tag"},
    )
    assert response == success_response


def test_get_template_registries(client):
    client._get.return_value = success_response
    response = client.Cluster.GetTemplateRegistries()
    client._get.assert_called_with(
        "GetTemplateRegistries",
        params={},
    )
    assert response == success_response


def test_get_templates(client):
    client._get.return_value = success_response
    response = client.Cluster.GetTemplates("type", True, False)
    client._get.assert_called_with(
        "GetTemplates", params={"type": "type", "published": True, "lazy": False}
    )
    assert response == success_response


def test_get_user_activity(client):
    client._get.return_value = success_response
    response = client.Cluster.GetUserActivity(
        1,
        CURRENT_DATETIME,
        CURRENT_DATETIME,
        "targetAppid",
        "startRow",
        1,
        "serviceName",
        "searchText",
        "actionTypes",
        "orderField",
        "orderDirection",
    )
    client._get.assert_called_with(
        "GetUserActivity",
        params={
            "uid": 1,
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "targetAppid": "targetAppid",
            "startRow": "startRow",
            "resultCount": 1,
            "serviceName": "serviceName",
            "searchText": "searchText",
            "actionTypes": "actionTypes",
            "orderField": "orderField",
            "orderDirection": "orderDirection",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_user_activities(client):
    client._get.return_value = success_response
    response = client.Cluster.GetUsersActivities(
        CURRENT_DATETIME, CURRENT_DATETIME, 1, 1
    )
    client._get.assert_called_with(
        "GetUsersActivities",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "startRow": 1,
            "resultCount": 1,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_l2_update(client):
    client._get.return_value = success_response
    response = client.Cluster.L2Update(1)
    client._get.assert_called_with(
        "L2Update",
        params={
            "hnId": 1,
        },
    )
    assert response == success_response


def test_migrate_env(client):
    client._get.return_value = success_response
    response = client.Cluster.MigrateEnv("targetAppid", "hardwareNodeGroup", True)
    client._get.assert_called_with(
        "MigrateEnv",
        params={
            "targetAppid": "targetAppid",
            "hardwareNodeGroup": "hardwareNodeGroup",
            "isOnline": True,
        },
    )
    assert response == success_response


def test_migrate_node(client):
    client._get.return_value = success_response
    response = client.Cluster.MigrateNode(1, 1, True, True)
    client._get.assert_called_with(
        "MigrateNode",
        params={
            "nodeid": 1,
            "hdnodeid": 1,
            "isOnline": True,
            "manageDNSState": True,
        },
    )
    assert response == success_response


def test_redeploy_containers(client):
    client._get.return_value = success_response
    response = client.Cluster.RedeployContainers(
        "target_env_name", "tag", "nodeGroup", 1, True, "login", "password", True
    )
    client._get.assert_called_with(
        "RedeployContainers",
        params={
            "targetEnvName": "target_env_name",
            "tag": "tag",
            "nodeGroup": "nodeGroup",
            "nodeId": 1,
            "useExistingVolumes": True,
            "login": "login",
            "password": "password",
            "skipReinstall": True,
        },
    )
    assert response == success_response


def test_refresh_email_templates(client):
    client._get.return_value = success_response
    response = client.Cluster.RefreshEmailTemplates("modules")
    client._get.assert_called_with(
        "RefreshEmailTemplates",
        params={"modules": "modules"},
    )
    assert response == success_response


def test_refresh_user(client):
    client._get.return_value = success_response
    response = client.Cluster.RefreshUser("language")
    client._get.assert_called_with("RefreshUser", params={"language": "language"})
    assert response == success_response


def test_regenerate_pool(client):
    client._get.return_value = success_response
    response = client.Cluster.RegeneratePool("node_type", "exclude")
    client._get.assert_called_with(
        "RegeneratePool", params={"nodeType": "node_type", "exclude": "exclude"}
    )
    assert response == success_response


def test_register_infa_module(client):
    client._get.return_value = success_response
    response = client.Cluster.RegisterInfaModule("module", "dstEnvName", True)
    client._get.assert_called_with(
        "RegisterInfaModule",
        params={"module": "module", "dstEnvName": "dstEnvName", "dryRun": True},
    )
    assert response == success_response


def test_remove_ext_ips(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveExtIps("ips")
    client._get.assert_called_with("RemoveExtIps", params={"ips": "ips"})
    assert response == success_response


def test_remove_hd_node_group(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveHdNodeGroup(1)
    client._get.assert_called_with(
        "RemoveHdNodeGroup",
        params={"id": 1},
    )
    assert response == success_response


def test_remove_ipv6_network(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveIpv6Network(1)
    client._get.assert_called_with(
        "RemoveIpv6Network",
        params={"id": 1},
    )
    assert response == success_response


def test_remove_region(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveRegion(1)
    client._get.assert_called_with(
        "RemoveRegion",
        params={"id": 1},
    )
    assert response == success_response


def test_remove_region_reseller(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveRegionReseller(1, True, 1)
    client._get.assert_called_with(
        "RemoveRegionReseller",
        params={"resellerId": 1, "dstEnvName": True, "regionId": 1},
    )
    assert response == success_response


def test_remove_region_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveRegionSsl(1, 1, 1)
    client._get.assert_called_with(
        "RemoveRegionSsl",
        params={
            "regionId": 1,
            "domainId": 1,
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_remove_template(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveTemplate("node_type")
    client._get.assert_called_with(
        "RemoveTemplate",
        params={"nodeType": "node_type"},
    )
    assert response == success_response


def test_remove_template_registry(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveTemplateRegistry(1)
    client._get.assert_called_with(
        "RemoveTemplateRegistry",
        params={"id": 1},
    )
    assert response == success_response


def test_replace_node_in_env(client):
    client._get.return_value = success_response
    response = client.Cluster.ReplaceNodeInEnv("dstEnvName", 1, "srcEnvId", 1)
    client._get.assert_called_with(
        "ReplaceNodeInEnv",
        params={
            "dstEnvName": "dstEnvName",
            "dstNodeId": 1,
            "srcEnvId": "srcEnvId",
            "srcHnId": 1,
        },
    )
    assert response == success_response


def test_revive_install_hd_node(client):
    client._get.return_value = success_response
    response = client.Cluster.ReviveInstallHdNode(1)
    client._get.assert_called_with(
        "ReviveInstallHdNode",
        params={"id": 1},
    )
    assert response == success_response


def test_search_envs(client):
    client._get.return_value = success_response
    response = client.Cluster.SearchEnvs({"search1": "search1", "search2": "search2"})
    client._get.assert_called_with(
        "SearchEnvs", params={"search": {"search1": "search1", "search2": "search2"}}
    )
    assert response == success_response


def test_search_nodes(client):
    client._get.return_value = success_response
    response = client.Cluster.SearchNodes({"search1": "search1", "search2": "search2"})
    client._get.assert_called_with(
        "SearchNodes", params={"search": {"search1": "search1", "search2": "search2"}}
    )
    assert response == success_response


def test_set_default_template_tag(client):
    client._get.return_value = success_response
    response = client.Cluster.SetDefaultTemplateTag("node_type", "tag")
    client._get.assert_called_with(
        "SetDefaultTemplateTag",
        params={"nodeType": "node_type", "tag": "tag"},
    )
    assert response == success_response


def test_set_env_note(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvNote("targetAppid", "note")
    client._get.assert_called_with(
        "SetEnvNote",
        params={
            "targetAppid": "targetAppid",
            "note": "note",
        },
    )
    assert response == success_response


def test_set_env_status(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvStatus("target_appid", 1)
    client._get.assert_called_with(
        "SetEnvStatus",
        params={"targetAppid": "target_appid", "status": 1},
    )
    assert response == success_response


def test_set_envs_status(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvsStatus("target_appid", 1)
    client._get.assert_called_with(
        "SetEnvsStatus",
        params={"targetAppid": "target_appid", "status": 1},
    )
    assert response == success_response


def test_set_env_status_by_uid(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvsStatusByUid(1, 1)
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
    response = client.Cluster.SetEnvsStatusByUidByChecksum(1, 1)
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
        1,
        1,
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
    response = client.Cluster.SetRegionPrimaryDomain(1, 1)
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
    response = client.Cluster.SetTemplatePublished("node type", True)
    client._get.assert_called_with(
        "SetTemplatePublished",
        params={"nodeType": "node type", "published": True},
    )
    assert response == success_response


def test_sleep(client):
    client._get.return_value = success_response
    response = client.Cluster.Sleep(CURRENT_DATETIME, CURRENT_DATETIME, 1)
    client._get.assert_called_with(
        "Sleep",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "deactivateAfter": 1,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_start_env(client):
    client._get.return_value = success_response
    response = client.Cluster.StartEnv("target")
    client._get.assert_called_with(
        "StartEnv(",
        params={
            "targetAppid": "target",
        },
    )
    assert response == success_response


def test_stop_balance_resources(client):
    client._get.return_value = success_response
    response = client.Cluster.StopBalanceResources()
    client._get.assert_called_with(
        "StopBalanceResources(",
        params={},
    )
    assert response == success_response


def test_stop_env(client):
    client._get.return_value = success_response
    response = client.Cluster.StopEnv("target")
    client._get.assert_called_with(
        "StopEnv(",
        params={
            "targetAppid": "target",
        },
    )
    assert response == success_response


def test_stop_evacuation(client):
    client._get.return_value = success_response
    response = client.Cluster.StopEvacuation(1)
    client._get.assert_called_with(
        "StopEvacuation",
        params={
            "hardNodeId": 1,
        },
    )
    assert response == success_response


def test_sync_cloud_lets(client):
    client._get.return_value = success_response
    response = client.Cluster.SyncCloudlets(CURRENT_DATETIME, True)
    client._get.assert_called_with(
        "SyncCloudlets(",
        params={
            "starttime": CURRENT_DATETIME,
            "debug": True,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_sync_infa_module(client):
    client._get.return_value = success_response
    response = client.Cluster.SyncInfaModule(
        "node group", "dst env", "components", "targetTag"
    )
    client._get.assert_called_with(
        "SyncInfaModule",
        params={
            "nodeGroup": "node group",
            "dstEnvName": "dst env",
            "components": "components",
            "targetTag": "targetTag",
        },
    )
    assert response == success_response


def test_update_region_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.UpdateRegionSsl(1, 1)
    client._get.assert_called_with(
        "UpdateRegionSsl",
        params={"regionId": 1, "domainId": 1},
    )
    assert response == success_response


def test_update_reseller_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.UpdateResellerSsl(1, 1)
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
    response = client.Cluster.UpdateTemplate(1, True)
    client._get.assert_called_with(
        "UpdateTemplate", params={"nodeType": 1, "iconsOnly": True}
    )
    assert response == success_response


def test_validate(client):
    client._get.return_value = success_response
    response = client.Cluster.Validate()
    client._get.assert_called_with(
        "Validate",
        params={},
    )
    assert response == success_response


def test_validate_all(client):
    client._get.return_value = success_response
    response = client.Cluster.ValidateAll()
    client._get.assert_called_with(
        "ValidateAll",
        params={},
    )
    assert response == success_response


def test_validate_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.ValidateSsl("domain", "key", "intermediate", "cert")
    client._get.assert_called_with(
        "ValidateSsl",
        params={
            "domain": "domain",
            "key": "key",
            "intermediate": "intermediate",
            "cert": "cert",
        },
    )
    assert response == success_response
