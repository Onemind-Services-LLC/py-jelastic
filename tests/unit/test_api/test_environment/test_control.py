from . import *


def test_add_backend(client):
    client._get.return_value = success_response
    response = client.Control.AddBackend(
        "env",
        1,
        1,
    )
    client._get.assert_called_with(
        "AddBackend",
        params={
            "envName": "env",
            "backendNodeId": 1,
            "balancerNodeId": 1,
        },
    )
    assert response == success_response


def test_add_backends(client):
    client._get.return_value = success_response
    response = client.Control.AddBackends(
        "env",
        1,
        1,
    )
    client._get.assert_called_with(
        "AddBackends",
        params={
            "envName": "env",
            "backendNodeId": 1,
            "balancerNodeId": 1,
        },
    )
    assert response == success_response


def test_add_balancer_node(client):
    client._get.return_value = success_response
    response = client.Control.AddBalancerNode(
        "env",
        "node type",
        [1, 2, 3],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ["name1", "name2", "name3"],
        ["group1", "group2", "group3"],
        [1, 2, 3],
        ["tag1", "tag2", "tag3"],
        ["meta1", "meta2", "meta3"],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ["node group1", "node group2", "node group3"],
    )
    client._get.assert_called_with(
        "AddBalancerNode",
        params={
            "envName": "env",
            "nodeType": "node type",
            "cloudLets": [1, 2, 3],
            "expIp": [True, False, True],
            "flexibleCloudlets": [1, 2, 3],
            "fixedCloudlets": [1, 2, 3],
            "displayName": ["name1", "name2", "name3"],
            "nodeGroup": ["group1", "group2", "group3"],
            "diskLimit": [1, 2, 3],
            "tag": ["tag1", "tag2", "tag3"],
            "metadata": ["meta1", "meta2", "meta3"],
            "startService": [True, False, True],
            "extIpv6Count": [1, 2, 3],
            "extIpCount": [1, 2, 3],
            "nodeGroupData": ["node group1", "node group2", "node group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_build_node(client):
    client._get.return_value = success_response
    response = client.Control.AddBuildNode(
        "env",
        "node type",
        [1, 2, 3],
        [True, False, True],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ["group1", "group2", "group3"],
        ["nodeGroup1", "nodeGroup2", "nodeGroup3"],
        ["tag1", "tag2", "tag3"],
        ["meta1", "meta2", "meta3"],
        [True, False, True],
        ["engine1", "engine2", "engine3"],
        [1, 2, 3],
        [
            1,
            2,
            3,
        ],
        ["data1", "data2", "data3"],
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        "AddBuildNode",
        params={
            "envName": "env",
            "nodeType": "node type",
            "cloudlets": [1, 2, 3],
            "nodeId": [True, False, True],
            "expIp": [True, False, True],
            "flexibleCloudlets": [1, 2, 3],
            "fixedCloudlets": [1, 2, 3],
            "displayName": ["group1", "group2", "group3"],
            "nodeGroup": ["nodeGroup1", "nodeGroup2", "nodeGroup3"],
            "tag": ["tag1", "tag2", "tag3"],
            "metadata": ["meta1", "meta2", "meta3"],
            "startService": [True, False, True],
            "engine": ["engine1", "engine2", "engine3"],
            "extIpv6Count": [1, 2, 3],
            "extIpCount": [
                1,
                2,
                3,
            ],
            "nodeGroupData": ["data1", "data2", "data3"],
            "diskLimit": [1, 2, 3],
        },
        delimiter=",",
    )

    assert response == success_response


def test_add_cache_node(client):
    client._get.return_value = success_response
    response = client.Control.AddCacheNode(
        "env",
        "node type",
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        ["name1", "name2", "name3"],
        ["nodeGroup1", "nodeGroup2", "nodeGroup3"],
        [1, 2, 3],
        ["tag1", "tag2", "tag3"],
        ["meta1", "meta2", "meta3"],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ["data1", "data2", "data3"],
    )
    client._get.assert_called_once_with(
        "AddCacheNode",
        params={
            "envName": "env",
            "nodeType": "node type",
            "cloudlets": [1, 2, 3],
            "flexibleCloudlets": [1, 2, 3],
            "fixedCloudlets": [1, 2, 3],
            "displayName": ["name1", "name2", "name3"],
            "nodeGroup": ["nodeGroup1", "nodeGroup2", "nodeGroup3"],
            "diskLimit": [1, 2, 3],
            "tag": ["tag1", "tag2", "tag3"],
            "metadata": ["meta1", "meta2", "meta3"],
            "startService": [True, False, True],
            "expIpv6Count": [1, 2, 3],
            "expIpCount": [1, 2, 3],
            "nodeGroupData": ["data1", "data2", "data3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_computer_node(client):
    client._get.return_value = success_response
    response = client.Control.AddComputeNode(
        "env",
        "node type",
        [1, 2, 3],
        [1, 2, 3],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ["name1", "name2", "name3"],
        ["group1", "group2", "group3"],
        [1, 2, 3],
        ["tag1", "tag2", "tag3"],
        [True, False, True],
        [True, False, True],
        ["engine1", "engine2", "engine3"],
        [1, 2, 3],
        [1, 2, 3],
        ["data1", "data2", "data3"],
    )
    client._get.assert_called_once_with(
        "AddComputeNode",
        params={
            "envName": "env",
            "nodeType": "node type",
            "cloudlets": [1, 2, 3],
            "isMaster": [1, 2, 3],
            "expIp": [True, False, True],
            "flexibleCloudlets": [1, 2, 3],
            "fixedCloudlets": [1, 2, 3],
            "displayName": ["name1", "name2", "name3"],
            "nodeGroup": ["group1", "group2", "group3"],
            "diskLimit": [1, 2, 3],
            "tag": ["tag1", "tag2", "tag3"],
            "metadata": [True, False, True],
            "startService": [True, False, True],
            "engine": ["engine1", "engine2", "engine3"],
            "expIpv6Count": [1, 2, 3],
            "expIpCount": [1, 2, 3],
            "nodeGroupData": ["data1", "data2", "data3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_container_env_vars(client):
    client._get.return_value = success_response
    response = client.Control.AddContainerEnvVars(
        "env",
        {"key": "value"},
        ["group1", "group2", "group3"],
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        "AddContainerEnvVars",
        params={
            "envName": "env",
            "vars": {"key": "value"},
            "nodeGroup": ["group1", "group2", "group3"],
            "nodeId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_container_volume(client):
    client._get.return_value = success_response
    response = client.Control.AddContainerVolume("env", 1, "path")
    client._get.assert_called_once_with(
        "AddContainerVolume",
        params={
            "envName": "env",
            "nodeId": 1,
            "path": "path",
        },
    )
    assert response == success_response


def test_add_container_volume_by_group(client):
    client._get.return_value = success_response
    response = client.Control.AddContainerVolumeByGroup(
        "env",
        "group",
        "path",
    )
    client._get.assert_called_once_with(
        "AddContainerVolumeByGroup",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "path": "path",
        },
    )
    assert response == success_response


def test_add_container_volumes(client):
    client._get.return_value = success_response
    response = client.Control.AddContainerVolumes(
        "env",
        "volume",
        ["group1", "group2", "group3"],
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        "AddContainerVolumes",
        params={
            "envName": "env",
            "volumes": "volume",
            "nodeGroup": ["group1", "group2", "group3"],
            "nodeId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_context(client):
    client._get.return_value = success_response
    response = client.Control.AddContext(
        "env",
        "name",
        "file name",
        "type",
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_once_with(
        "AddContext",
        params={
            "envName": "env",
            "name": "name",
            "fileName": "file name",
            "type": "type",
            "nodeGroup": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_db_node(client):
    client._get.return_value = success_response
    response = client.Control.AddDBNode(
        "env",
        "type",
        [1, 2, 3],
        [True, False, True],
        ["password1", "password2", "password3"],
        [1, 2, 3],
        [1, 2, 3],
        ["name1", "name2", "name3"],
        ["group1", "group2", "group3"],
        [1, 2, 3],
        ["tag1", "tag2", "tag3"],
        [True, True, True],
        [True, True, True],
        [1, 2, 3],
        [1, 2, 3],
        ["data1", "data2", "data3"],
    )
    client._get.assert_called_once_with(
        "AddDBNode",
        params={
            "envName": "env",
            "nodeType": "type",
            "cloudlets": [1, 2, 3],
            "expIp": [True, False, True],
            "password": ["password1", "password2", "password3"],
            "flexibleCloudlets": [1, 2, 3],
            "fixedCloudlets": [1, 2, 3],
            "displayName": ["name1", "name2", "name3"],
            "nodeGroup": ["group1", "group2", "group3"],
            "diskLimit": [1, 2, 3],
            "tag": ["tag1", "tag2", "tag3"],
            "metadata": [True, True, True],
            "startService": [True, True, True],
            "expIpv6Count": [1, 2, 3],
            "expIpCount": [1, 2, 3],
            "nodeGroupData": ["data1", "data2", "data3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_docker_node(client):
    client._get.return_value = success_response
    response = client.Control.AddDockerNode(
        "env",
        "type",
        {
            "metadata1": "val1",
            "metadata2": "val2",
            "metadata3": "val3",
            "metadata4": "val4",
            "metadata5": "val5",
        },
        [1, 2, 3],
        [True, True, True],
        ["pass1", "pass2", "pass3"],
        [1, 2, 3],
        [1, 2, 3],
        ["name1", "name2", "name3"],
        ["group1", "group2", "group3"],
        [1, 2, 3],
        [True, True, True],
        [1, 2, 3],
        [1, 2, 3],
        ["data1", "data2", "data3"],
    )
    client._get.assert_called_once_with(
        "AddDockerNode",
        params={
            "envName": "env",
            "nodeType": "type",
            "metadata": {
                "metadata1": "val1",
                "metadata2": "val2",
                "metadata3": "val3",
                "metadata4": "val4",
                "metadata5": "val5",
            },
            "cloudlets": [1, 2, 3],
            "expIp": [True, True, True],
            "password": ["pass1", "pass2", "pass3"],
            "flexibleCloudlets": [1, 2, 3],
            "fixedCloudlets": [1, 2, 3],
            "displayName": ["name1", "name2", "name3"],
            "nodeGroup": ["group1", "group2", "group3"],
            "diskLimit": [1, 2, 3],
            "startService": [True, True, True],
            "expIpv6Count": [1, 2, 3],
            "expIpCount": [1, 2, 3],
            "nodeGroupData": ["data1", "data2", "data3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_docker_volume(client):
    client._get.return_value = success_response
    response = client.Control.AddDockerVolume(
        "env",
        1,
        "path",
    )
    client._get.assert_called_once_with(
        "AddDockerVolume", params={"envName": "env", "nodeId": 1, "path": "path"}
    )
    assert response == success_response


def test_add_docker_volume_by_groups(client):
    client._get.return_value = success_response
    response = client.Control.AddDockerVolumeByGroup(
        "env",
        1,
        "path",
    )
    client._get.assert_called_once_with(
        "AddDockerVolumeByGroup",
        params={"envName": "env", "nodeGroup": 1, "path": "path"},
    )
    assert response == success_response


def test_add_endpoint(client):
    client._get.return_value = success_response
    response = client.Control.AddEndpoint(
        "env",
        1,
        8000,
        "protocol",
        "name",
    )
    client._get.assert_called_once_with(
        "AddEndpoint",
        params={
            "envName": "env",
            "nodeId": 1,
            "privatePort": 8000,
            "protocol": "protocol",
            "name": "name",
        },
    )
    assert response == success_response


def test_add_env_policy(client):
    client._get.return_value = success_response
    response = client.Control.AddEnvPolicy(
        "app id",
        "policy",
    )
    client._get.assert_called_once_with(
        "AddEnvPolicy",
        params={
            "targetAppId": "app id",
            "policy": "policy",
        },
    )
    assert response == success_response


def test_aad_env_property(client):
    client._get.return_value = success_response
    response = client.Control.AddEnvProperty("properties")
    client._get.assert_called_once_with(
        "AddEnvProperty",
        params={
            "properties": "properties",
        },
    )
    assert response == success_response


def test_add_extra_node(client):
    client._get.return_value = success_response
    response = client.Control.AddExtraNode(
        "env",
        "type",
        [1, 2, 3],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ["name1", "name2", "name3"],
        ["group1", "group2", "group3"],
        [1, 2, 3],
        ["tag1", "tag2", "tag3"],
        [True, False, True],
        [True, False, True],
        [1, 2, 3],
        [1, 2, 3],
        ["date1", "date2", "date3"],
    )
    client._get.assert_called_once_with(
        "AddExtraNode",
        params={
            "envName": "env",
            "nodeType": "type",
            "cloudlets": [1, 2, 3],
            "expIp": [True, False, True],
            "flexibleCloudlets": [1, 2, 3],
            "fixedCloudlets": [1, 2, 3],
            "displayName": ["name1", "name2", "name3"],
            "nodeGroup": ["group1", "group2", "group3"],
            "diskLimit": [1, 2, 3],
            "tag": ["tag1", "tag2", "tag3"],
            "metadata": [True, False, True],
            "startService": [True, False, True],
            "expIpv6Count": [1, 2, 3],
            "expIpCount": [1, 2, 3],
            "nodeGroupData": ["date1", "date2", "date3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_node(client):
    client._get.return_value = success_response
    response = client.Control.AddNode(
        "env",
        "type",
        [1, 2, 3],
        ["ip1", "ip2", "ip3"],
        ["password1", "password2", "password3"],
        [1, 2, 3],
        [1, 2, 3],
        ["name1", "name2", "name3"],
        ["metadata1", "metadata2", "metadata3"],
        ["group1", "group2", "group3"],
        [True, False, True],
        [1, 2, 3],
        ["tag1", "tag2", "tag3"],
        ["engine1", "engine2", "engine3"],
        [1, 2, 3],
        [1, 2, 3],
        ["data1", "data2", "data3"],
        ["option1", "option2", "option3"],
    )
    client._get.assert_called_once_with(
        "AddNode",
        params={
            "envName": "env",
            "nodeType": "type",
            "cloudLets": [1, 2, 3],
            "extIp": ["ip1", "ip2", "ip3"],
            "password": ["password1", "password2", "password3"],
            "flexibleCloudLets": [1, 2, 3],
            "fixedCloudLets": [1, 2, 3],
            "displayName": ["name1", "name2", "name3"],
            "metadata": ["metadata1", "metadata2", "metadata3"],
            "nodeGroup": ["group1", "group2", "group3"],
            "startService": [True, False, True],
            "diskLimit": [1, 2, 3],
            "tag": ["tag1", "tag2", "tag3"],
            "engine": ["engine1", "engine2", "engine3"],
            "extipv4": [1, 2, 3],
            "extipv6": [1, 2, 3],
            "nodeGroupData": ["data1", "data2", "data3"],
            "options": ["option1", "option2", "option3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_port_redirect(client):
    client._get.return_value = success_response
    response = client.Control.AddPortRedirect(
        "env",
        1,
        8000,
        9000,
        "protocol",
        ["comment1", "comment2", "comment3"],
    )
    client._get.assert_called_once_with(
        "AddPortRedirect",
        params={
            "envName": "env",
            "nodeId": 1,
            "srcPort": 8000,
            "dstPort": 9000,
            "protocol": "protocol",
            "comments": ["comment1", "comment2", "comment3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_storage_node(client):
    client._get.return_value = success_response
    response = client.Control.AddStorageNode(
        "env",
        "type",
        [1, 2, 3],
        ["ip1", "ip2", "ip3"],
        [1, 2, 3],
        [1, 2, 3],
        ["name1", "name2", "name3"],
        ["group1", "group2", "group3"],
        [1, 2, 3],
        ["tag1", "tag2", "tag3"],
        ["metadata1", "metadata2", "metadata3"],
        [True, True, True],
        [1, 2, 3],
        [1, 2, 3],
        ["data1", "data2", "data3"],
    )
    client._get.assert_called_once_with(
        "AddStorageNode",
        params={
            "envName": "env",
            "nodeType": "type",
            "cloudlets": [1, 2, 3],
            "extIp": ["ip1", "ip2", "ip3"],
            "flexibleCloudLets": [1, 2, 3],
            "fixedCloudLets": [1, 2, 3],
            "displayName": ["name1", "name2", "name3"],
            "nodeGroup": ["group1", "group2", "group3"],
            "diskLimit": [1, 2, 3],
            "tag": ["tag1", "tag2", "tag3"],
            "metadata": ["metadata1", "metadata2", "metadata3"],
            "startService": [True, True, True],
            "extIpv6Count": [1, 2, 3],
            "extIpCount": [1, 2, 3],
            "nodeGroupData": ["data1", "data2", "data3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_vds_node(client):
    client._get.return_value = success_response
    response = client.Control.AddVdsNode(
        "env",
        "type",
        [1, 2, 3],
        ["ip1", "ip2", "ip3"],
        ["password1", "password2", "password3"],
        [1, 2, 3],
        [1, 2, 3],
        ["name1", "name2", "name3"],
        ["group1", "group2", "group3"],
        [1, 2, 3],
        ["tag1", "tag2", "tag3"],
        ["data1", "data2", "data3"],
        [True, False, False],
        [1, 2, 3],
        [1, 2, 3],
        ["data1", "data2", "data3"],
    )
    client._get.assert_called_once_with(
        "AddVdsNode",
        params={
            "envName": "env",
            "nodeType": "type",
            "cloudlets": [1, 2, 3],
            "extIp": ["ip1", "ip2", "ip3"],
            "password": ["password1", "password2", "password3"],
            "flexibleCloudLets": [1, 2, 3],
            "fixedCloudLets": [1, 2, 3],
            "displayName": ["name1", "name2", "name3"],
            "nodeGroup": ["group1", "group2", "group3"],
            "diskLimit": [1, 2, 3],
            "tag": ["tag1", "tag2", "tag3"],
            "metadata": ["data1", "data2", "data3"],
            "startService": [True, False, False],
            "extIpv6Count": [1, 2, 3],
            "extIpCount": [1, 2, 3],
            "nodeGroupData": ["data1", "data2", "data3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_vm_node(client):
    client._get.return_value = success_response
    response = client.Control.AddVmNode(
        "env",
        "type",
        "option",
        ["ip1", "ip2", "ip3"],
        ["name", "name2", "name3"],
        ["group1", "group2", "group3"],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        ["data1", "data2", "data3"],
        ["password1", "password2", "password3"],
    )
    client._get.assert_called_once_with(
        "AddVmNode",
        params={
            "envName": "env",
            "nodeType": "type",
            "options": "option",
            "extIp": ["ip1", "ip2", "ip3"],
            "displayName": ["name", "name2", "name3"],
            "nodeGroup": ["group1", "group2", "group3"],
            "diskLimit": [1, 2, 3],
            "extIpv6Count": [1, 2, 3],
            "extIpCount": [1, 2, 3],
            "nodeGroupData": ["data1", "data2", "data3"],
            "password": ["password1", "password2", "password3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_append_nodes(client):
    client._get.return_value = success_response
    response = client.Control.AppendNodes("name", 1, "type")
    client._get.assert_called_once_with(
        "AppendNodes",
        params={
            "envName": "name",
            "count": 1,
            "nodeType": "type",
        },
    )
    assert response == success_response


def test_apply_env_property(client):
    client._get.return_value = success_response
    response = client.Control.ApplyEnvProperty("name", "properties")
    client._get.assert_called_once_with(
        "ApplyEnvProperty",
        params={
            "envName": "name",
            "properties": "properties",
        },
    )
    assert response == success_response


def test_apply_node_group_data(client):
    client._get.return_value = success_response
    response = client.Control.ApplyNodeGroupData("env", "group", "data")
    client._get.assert_called_once_with(
        "ApplyNodeGroupData",
        params={
            "envName": "env",
            "nodeGroupData": "group",
            "data": "data",
        },
    )
    assert response == success_response


def test_apply_software_package_action(client):
    client._get.return_value = success_response
    response = client.Control.ApplySoftwarePackageAction(
        "env",
        "keyword",
        ["type1", "type2", "type3"],
        ["action1", "action2", "action3"],
        ["password1", "password2", "password3"],
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_once_with(
        "ApplySoftwarePackageAction",
        params={
            "envName": "env",
            "keywords": "keyword",
            "nodeType": ["type1", "type2", "type3"],
            "action": ["action1", "action2", "action3"],
            "password": ["password1", "password2", "password3"],
            "nodeGroup": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_attach_env_group(client):
    client._get.return_value = success_response
    response = client.Control.AttachEnvGroup("env", "group")
    client._get.assert_called_once_with(
        "AttachEnvGroup",
        params={
            "envName": "env",
            "envGroup": "group",
        },
    )
    assert response == success_response


def test_build_cluster(client):
    client._get.return_value = success_response
    response = client.Control.BuildCluster("env", "group")
    client._get.assert_called_once_with(
        "BuildCluster", params={"envName": "env", "nodeGroup": "group"}
    )
    assert response == success_response


def test_cancel_transfer_request(client):
    client._get.return_value = success_response
    response = client.Control.CancelTransferRequest()
    client._get.assert_called_once_with("CancelTransferRequest", params={})
    assert response == success_response


def test_change_limits(client):
    client._get.return_value = success_response
    response = client.Control.ChangeLimits("env")
    client._get.assert_called_once_with("ChangeLimits", params={"envName": "env"})
    assert response == success_response


def test_change_limit_inner(client):
    client._get.return_value = success_response
    response = client.Control.ChangeLimitsInner(
        "env",
        1,
        ["type1", "type2", "type3"],
    )
    client._get.assert_called_once_with(
        "ChangeLimitsInner",
        params={
            "envName": "env",
            "uid": 1,
            "limitType": ["type1", "type2", "type3"],
        },
    )
    assert response == success_response


def test_change_topology(client):
    client._get.return_value = success_response
    response = client.Control.ChangeTopology(
        "env",
        {
            "envName1": "value1",
            "envName2": "value2",
            "envName3": "value3",
            "envName4": "value4",
            "envName5": "value5",
        },
        {
            "node1": "value1",
            "node2": "value2",
            "node3": "value3",
            "node4": "value4",
            "node5": "value5",
        },
        ["key1", "key2", "key3"],
    )
    client._get.assert_called_once_with(
        "ChangeTopology",
        params={
            "envName": "env",
            "env": {
                "envName1": "value1",
                "envName2": "value2",
                "envName3": "value3",
                "envName4": "value4",
                "envName5": "value5",
            },
            "nodes": {
                "node1": "value1",
                "node2": "value2",
                "node3": "value3",
                "node4": "value4",
                "node5": "value5",
            },
            "actionkey": ["key1", "key2", "key3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_check_dependencies(client):
    client._get.return_value = success_response
    response = client.Control.CheckDependencies(
        "env",
        [1, 2, 3],
        ["filter1", "filter2", "filter3"],
    )
    client._get.assert_called_once_with(
        "CheckDependencies",
        params={
            "envName": "env",
            "nodeId": [1, 2, 3],
            "filter": ["filter1", "filter2", "filter3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_check_ext_ip_count(client):
    client._get.return_value = success_response
    response = client.Control.CheckExtIpCount(
        1,
        [1, 2, 3],
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_once_with(
        "CheckExtIpCount",
        params={
            "expIpv6": 1,
            "expIpv4": [1, 2, 3],
            "hardwareNodeGroup": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_check_migration_possibility(client):
    client._get.return_value = success_response
    response = client.Control.CheckMigrationPossibility(
        "env",
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_once_with(
        "CheckMigrationPossibility",
        params={
            "envName": "env",
            "hardwareNodeGroup": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_clear_log(client):
    client._get.return_value = success_response
    response = client.Control.ClearLog(
        "env",
        1,
        "path",
    )
    client._get.assert_called_once_with(
        "ClearLog",
        params={
            "envName": "env",
            "nodeId": 1,
            "path": "path",
        },
    )
    assert response == success_response


def test_clone_env(client):
    client._get.return_value = success_response
    response = client.Control.CloneEnv(
        "env",
        "env_name",
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "CloneEnv",
        params={
            "srcEnvName": "env",
            "ditEnvName": "env_name",
            "useExternalMounts": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_clone_node(client):
    client._get.return_value = success_response
    response = client.Control.CloneNode(
        "env",
        1,
        "group",
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        "CloneNode",
        params={
            "envName": "env",
            "count": 1,
            "nodeGroup": "group",
            "nodeId": [1, 2, 3],
        },
    )
    assert response == success_response


def test_confirm_transfer_request(client):
    client._get.return_value = success_response
    response = client.Control.ConfirmTransferRequest("key")
    client._get.assert_called_once_with(
        "ConfirmTransferRequest",
        params={
            "key": "key",
        },
    )
    assert response == success_response


def test_create_env(client):
    client._get.return_value = success_response
    response = client.Control.CreateEnv(
        "env",
        {
            "settings1": "value1",
            "settings2": "value2",
            "settings3": "value3",
            "settings4": "value4",
            "settings5": "value5",
        },
        [1, 2, 3],
        ["group1", "group2", "group3"],
        ["env 1", "env 2", "env 3"],
    )
    client._get.assert_called_once_with(
        "CreateEnv",
        params={
            "envName": "env",
            "settings": {
                "settings1": "value1",
                "settings2": "value2",
                "settings3": "value3",
                "settings4": "value4",
                "settings5": "value5",
            },
            "ownerUid": [1, 2, 3],
            "hardwareNodeGroups": ["group1", "group2", "group3"],
            "envGroups": ["env 1", "env 2", "env 3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_create_environment(client):
    client._get.return_value = success_response
    response = client.Control.CreateEnvironment(
        {
            "envName1": "env1",
            "envName2": "env2",
            "envName3": "env3",
            "envName4": "env4",
            "envName5": "env5",
        },
        {
            "node1": "value1",
            "node2": "value2",
            "node3": "value3",
            "node4": "value4",
            "node5": "value5",
        },
        ["key1", "key2", "key3"],
        [1, 2, 3],
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_once_with(
        "CreateEnvironment",
        params={
            "env": {
                "envName1": "env1",
                "envName2": "env2",
                "envName3": "env3",
                "envName4": "env4",
                "envName5": "env5",
            },
            "nodes": {
                "node1": "value1",
                "node2": "value2",
                "node3": "value3",
                "node4": "value4",
                "node5": "value5",
            },
            "actionKey": ["key1", "key2", "key3"],
            "ownerUid": [1, 2, 3],
            "envGroups": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_env(client):
    client._get.return_value = success_response
    response = client.Control.DeleteEnv(
        "env",
        ["password1", "password2", "password3"],
    )
    client._get.assert_called_once_with(
        "DeleteEnv",
        params={
            "envName": "env",
            "password": ["password1", "password2", "password3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_exported_files(client):
    client._get.return_value = success_response
    response = client.Control.DeleteExportedFiles(
        "env",
        "file",
    )
    client._get.assert_called_once_with(
        "DeleteExportedFiles",
        params={
            "envName": "env",
            "fileName": "file",
        },
    )
    assert response == success_response


def test_deploy_app(client):
    client._get.return_value = success_response
    response = client.Control.DeployApp(
        "env",
        "file url",
        "file name",
        ["context1", "context2", "context3"],
        [True, False, True],
        [1, 2, 3],
        ["group1", "group2", "group3"],
        ["hook1", "hook2", "hook3"],
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "DeployApp",
        params={
            "envName": "env",
            "fileUrl": "file url",
            "fileName": "file name",
            "context": ["context1", "context2", "context3"],
            "atomicDeploy": [True, False, True],
            "delay": [1, 2, 3],
            "nodeGroup": ["group1", "group2", "group3"],
            "hooks": ["hook1", "hook2", "hook3"],
            "isSequential": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_detach_env_group(client):
    client._get.return_value = success_response
    response = client.Control.DetachEnvGroup(
        "env",
        "group",
    )
    client._get.assert_called_once_with(
        "DetachEnvGroup",
        params={
            "envName": "env",
            "envGroup": "group",
        },
    )
    assert response == success_response


def test_disable_replication(client):
    client._get.return_value = success_response
    response = client.Control.DisableReplication(
        "env",
        "group",
    )
    client._get.assert_called_once_with(
        "DisableReplication",
        params={
            "envName": "env",
            "nodeGroup": "group",
        },
    )
    assert response == success_response


def test_edit_endpoint(client):
    client._get.return_value = success_response
    response = client.Control.EditEndpoint(
        "env",
        1,
        "name",
        8000,
        "tcp",
    )
    client._get.assert_called_once_with(
        "EditEndpoint",
        params={
            "envName": "env",
            "id": 1,
            "name": "name",
            "privatePort": 8000,
            "protocol": "tcp",
        },
    )
    assert response == success_response


def test_edit_env_settings(client):
    client._get.return_value = success_response
    response = client.Control.EditEnvSettings(
        "env",
        {
            "setting1": "val1",
            "setting2": "val2",
            "setting3": "val3",
            "setting4": "val4",
            "setting5": "val5",
        },
    )
    client._get.assert_called_once_with(
        "EditEnvSettings",
        params={
            "envName": "env",
            "settings": {
                "setting1": "val1",
                "setting2": "val2",
                "setting3": "val3",
                "setting4": "val4",
                "setting5": "val5",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_node_group(client):
    client._get.return_value = success_response
    response = client.Control.EditNodeGroup(
        "env",
        {
            "group1": "val1",
            "group2": "val2",
            "group3": "val3",
            "group4": "val4",
            "group5": "val5",
        },
    )
    client._get.assert_called_once_with(
        "EditNodeGroup",
        params={
            "envName": "env",
            "nodeGroup": {
                "group1": "val1",
                "group2": "val2",
                "group3": "val3",
                "group4": "val4",
                "group5": "val5",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_registry_credentials(client):
    client._get.return_value = success_response
    response = client.Control.EditRegistryCredentials(
        {
            "filter1": "value1",
            "filter2": "value2",
            "filter3": "value3",
            "filter4": "value4",
            "filter5": "value5",
        },
        ["user1", "user2", "user3"],
        ["password1", "password2", "password3"],
    )
    client._get.assert_called_once_with(
        "EditRegistryCredentials",
        params={
            "filter": {
                "filter1": "value1",
                "filter2": "value2",
                "filter3": "value3",
                "filter4": "value4",
                "filter5": "value5",
            },
            "user": ["user1", "user2", "user3"],
            "password": ["password1", "password2", "password3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_exec_cmd(client):
    client._get.return_value = success_response
    response = client.Control.ExecCmd(
        "env",
        "type",
        [{"key": "value"}],
        True,
    )
    client._get.assert_called_once_with(
        "ExecCmd",
        params={
            "envName": "env",
            "nodeType": "type",
            "commandList": [{"key": "value"}],
            "sayYes": True,
        },
    )
    assert response == success_response


def test_exec_cmd_by_group(client):
    client._get.return_value = success_response
    response = client.Control.ExecCmdByGroup(
        "env",
        "group",
        {
            "command1": "val1",
            "command2": "val2",
            "command3": "val3",
            "command4": "val4",
            "command5": "val5",
        },
        [True, False, True],
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "ExecCmdByGroup",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "commandList": {
                "command1": "val1",
                "command2": "val2",
                "command3": "val3",
                "command4": "val4",
                "command5": "val5",
            },
            "sayYes": [True, False, True],
            "async": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_exec_cmd_by_id(client):
    client._get.return_value = success_response
    response = client.Control.ExecCmdById("env", 1, [{"key": "value"}], True)
    client._get.assert_called_once_with(
        "ExecCmdById",
        params={
            "envName": "env",
            "nodeId": 1,
            "commandList": [{"key": "value"}],
            "sayYes": True,
        },
    )
    assert response == success_response


def test_exec_cmd_by_type(client):
    client._get.return_value = success_response
    response = client.Control.ExecCmdByType("env", "type", [{"key": "value"}], True)
    client._get.assert_called_once_with(
        "ExecCmdByType",
        params={
            "envName": "env",
            "nodeType": "type",
            "commandList": [{"key": "value"}],
            "sayYes": True,
        },
    )
    assert response == success_response


def test_exec_docker_run_cmd(client):
    client._get.return_value = success_response
    response = client.Control.ExecDockerRunCmd("env", 1)
    client._get.assert_called_once_with(
        "ExecDockerRunCmd",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_export_env(client):
    client._get.return_value = success_response
    response = client.Control.ExportEnv("env", "settings")
    client._get.assert_called_once_with(
        "ExportEnv",
        params={
            "envName": "env",
            "settings": "settings",
        },
    )
    assert response == success_response


def test_finish(client):
    client._get.return_value = success_response
    response = client.Control.Finish("env")
    client._get.assert_called_once_with("Finish", params={"envName": "env"})
    assert response == success_response


def test_firewall_status(client):
    client._get.return_value = success_response
    response = client.Control.FireWallStatus("env", 1)
    client._get.assert_called_once_with(
        "FireWallStatus",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_active_envs(client):
    client._get.return_value = success_response
    response = client.Control.GetActiveEnvs(
        "env",
        "domain",
        CURRENT_DATETIME,
        CURRENT_DATETIME,
        "checksum",
    )
    client._get.assert_called_once_with(
        "GetActiveEnvs",
        params={
            "envName": "env",
            "domain": "domain",
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "checksum": "checksum",
        },
        datetime_format="%Y-%m-%d",
    )
    assert response == success_response


def test_get_all_sum_stat_by_uid(client):
    client._get.return_value = success_response
    response = client.Control.GetAllSumStatByUid(
        [1, 2, 3],
        [CURRENT_DATETIME, CURRENT_DATETIME, CURRENT_DATETIME],
    )
    client._get.assert_called_once_with(
        "GetAllSumStatByUid",
        params={
            "duration": [1, 2, 3],
            "endtime": [CURRENT_DATETIME, CURRENT_DATETIME, CURRENT_DATETIME],
        },
        datetime_format="%Y-%m-%d",
        delimiter=",",
    )
    assert response == success_response


def test_get_basic_envs_info(client):
    client._get.return_value = success_response
    response = client.Control.GetBasicEnvsInfo(123)
    client._get.assert_called_once_with(
        "GetBasicEnvsInfo",
        params={
            "ownerUid": 123,
        },
    )
    assert response == success_response


def test_get_container_entry_point(client):
    client._get.return_value = success_response
    response = client.Control.GetContainerEntryPoint("env", 1)
    client._get.assert_called_once_with(
        "GetContainerEntryPoint",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_container_env_vars(client):
    client._get.return_value = success_response
    response = client.Control.GetContainerEnvVars("env", 1)
    client._get.assert_called_once_with(
        "GetContainerEnvVars",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_container_env_vars_by_group(client):
    client._get.return_value = success_response
    response = client.Control.GetContainerEnvVarsByGroup("env", "group")
    client._get.assert_called_once_with(
        "GetContainerEnvVarsByGroup",
        params={
            "envName": "env",
            "nodeGroup": "group",
        },
    )
    assert response == success_response


def test_get_container_manifest(client):
    client._get.return_value = success_response
    response = client.Control.GetContainerManifest(
        "image",
        ["registry1", "registry2", "registry3"],
        ["name1", "name2", "name3"],
        ["password1", "password2", "password3"],
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "GetContainerManifest",
        params={
            "image": "image",
            "registry": ["registry1", "registry2", "registry3"],
            "userName": ["name1", "name2", "name3"],
            "password": ["password1", "password2", "password3"],
            "ignoreFormat": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_container_node_tags(client):
    client._get.return_value = success_response
    response = client.Control.GetContainerNodeTags("env", 1)
    client._get.assert_called_once_with(
        "GetContainerNodeTags",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_container_run_cmd(client):
    client._get.return_value = success_response
    response = client.Control.GetContainerRunCmd("env", 1)
    client._get.assert_called_once_with(
        "GetContainerRunCmd",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_container_run_config(client):
    client._get.return_value = success_response
    response = client.Control.GetContainerRunConfig("env", 1)
    client._get.assert_called_once_with(
        "GetContainerRunConfig",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_container_tags(client):
    client._get.return_value = success_response
    response = client.Control.GetContainerTags(
        "image",
        ["registry1", "registry2", "registry3"],
        ["name1", "name2", "name3"],
        ["password1", "password2", "password3"],
    )
    client._get.assert_called_once_with(
        "GetContainerTags",
        params={
            "image": "image",
            "registry": ["registry1", "registry2", "registry3"],
            "userName": ["name1", "name2", "name3"],
            "password": ["password1", "password2", "password3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_container_volumes_by_group(client):
    client._get.return_value = success_response
    response = client.Control.GetContainerVolumesByGroup("env", "group")
    client._get.assert_called_once_with(
        "GetContainerVolumesByGroup",
        params={
            "envName": "env",
            "nodeGroup": "group",
        },
    )
    assert response == success_response


def test_get_container_volumes_by_id(client):
    client._get.return_value = success_response
    response = client.Control.GetContainerVolumesById("env", 1)
    client._get.assert_called_once_with(
        "GetContainerVolumesById",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_docker_config(client):
    client._get.return_value = success_response
    response = client.Control.GetDockerConfig("env", 1)
    client._get.assert_called_once_with(
        "GetDockerConfig",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_docker_entry_point(client):
    client._get.return_value = success_response
    response = client.Control.GetDockerEntryPoint("env", 1)
    client._get.assert_called_once_with(
        "GetDockerEntryPoint",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_docker_run_cmd(client):
    client._get.return_value = success_response
    response = client.Control.GetDockerRunCmd("env", 1)
    client._get.assert_called_once_with(
        "GetDockerRunCmd",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_domains_list(client):
    client._get.return_value = success_response
    response = client.Control.GetDomainsList("env", "checksum")
    client._get.assert_called_once_with(
        "GetDomainsList",
        params={
            "envName": "env",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_get_endpoints(client):
    client._get.return_value = success_response
    response = client.Control.GetEndpoints("env", [1, 2, 3])
    client._get.assert_called_once_with(
        "GetEndpoints",
        params={
            "envName": "env",
            "nodeId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_engine_list(client):
    client._get.return_value = success_response
    response = client.Control.GetEngineList(["type1", "type2", "type3"])
    client._get.assert_called_once_with(
        "GetEngineList",
        params={
            "type": ["type1", "type2", "type3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_engine_types(client):
    client._get.return_value = success_response
    response = client.Control.GetEngineTypes()
    client._get.assert_called_once_with("GetEngineTypes", params={})
    assert response == success_response


def test_get_env_info(client):
    client._get.return_value = success_response
    response = client.Control.GetEnvInfo("env", [True, False, True])
    client._get.assert_called_once_with(
        "GetEnvInfo",
        params={
            "envName": "env",
            "lazy": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_env_property(client):
    client._get.return_value = success_response
    response = client.Control.GetEnvProperty("env", [True, False, True])
    client._get.assert_called_once_with(
        "GetEnvProperty",
        params={
            "envName": "env",
            "propertyKeys": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_envs(client):
    client._get.return_value = success_response
    response = client.Control.GetEnvs([True, False, True], [1, 2, 3])
    client._get.assert_called_once_with(
        "GetEnvs",
        params={"lazy": [True, False, True], "ownerUid": [1, 2, 3]},
        delimiter=",",
    )
    assert response == success_response


def test_get_envs_by_criteria(client):
    client._get.return_value = success_response
    response = client.Control.GetEnvsByCriteria(
        {
            "criteria1": "value1",
            "criteria2": "value2",
            "criteria3": "value3",
            "criteria4": "value4",
            "criteria5": "value5",
        },
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "GetEnvsByCriteria",
        params={
            "criteria": {
                "criteria1": "value1",
                "criteria2": "value2",
                "criteria3": "value3",
                "criteria4": "value4",
                "criteria5": "value5",
            },
            "lazy": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_envs_info(client):
    client._get.return_value = success_response
    response = client.Control.GetEnvsInfo(
        "env",
        ["app1", "app2", "app3"],
    )
    client._get.assert_called_once_with(
        "GetEnvsInfo",
        params={
            "envName": "env",
            "targetAppid": ["app1", "app2", "app3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_logs(client):
    client._get.return_value = success_response
    response = client.Control.GetLogs(
        "env",
        1,
        ["path1", "path2", "path3"],
    )
    client._get.assert_called_once_with(
        "GetLogs",
        params={
            "envName": "env",
            "nodeId": 1,
            "path": ["path1", "path2", "path3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_logs_list(client):
    client._get.return_value = success_response
    response = client.Control.GetLogsList(
        "env",
        1,
        ["path1", "path2", "path3"],
    )
    client._get.assert_called_once_with(
        "GetLogsList",
        params={
            "envName": "env",
            "nodeId": 1,
            "path": ["path1", "path2", "path3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_node_groups(client):
    client._get.return_value = success_response
    response = client.Control.GetNodeGroups("env")
    client._get.assert_called_once_with(
        "GetNodeGroups",
        params={
            "envName": "env",
        },
    )
    assert response == success_response


def test_get_node_info(client):
    client._get.return_value = success_response
    response = client.Control.GetNodeInfo("node_id")
    client._get.assert_called_once_with(
        "GetNodeInfo",
        params={
            "GetNodeInfo": "node_id",
        },
    )
    assert response == success_response


def test_get_node_missions(client):
    client._get.return_value = success_response
    response = client.Control.GetNodeMissions()
    client._get.assert_called_once_with("GetNodeMissions", params={})
    assert response == success_response


def test_get_node_ssh_key(client):
    client._get.return_value = success_response
    response = client.Control.GetNodeSSHKey(
        "env",
        1,
        1,
        [True, False, False],
    )
    client._get.assert_called_once_with(
        "GetNodeSSHKey",
        params={
            "envName": "env",
            "nodeId": 1,
            "uid": 1,
            "skipNodeTypeCheck": [True, False, False],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_node_tags(client):
    client._get.return_value = success_response
    response = client.Control.GetNodeTags("env", 1)
    client._get.assert_called_once_with(
        "GetNodeTags",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_regions(client):
    client._get.return_value = success_response
    response = client.Control.GetRegions()
    client._get.assert_called_once_with("GetRegions", params={})
    assert response == success_response


def test_get_regions_inner(client):
    client._get.return_value = success_response
    response = client.Control.GetRegionsInner("group", [True, False, True])
    client._get.assert_called_once_with(
        "GetRegionsInner",
        params={
            "groupName": "group",
            "isEnabled": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_registry_info(client):
    client._get.return_value = success_response
    response = client.Control.GetRegistryInfo("env", "group")
    client._get.assert_called_once_with(
        "GetRegistryInfo",
        params={
            "envName": "env",
            "nodeGroup": "group",
        },
    )
    assert response == success_response


def test_get_ssh_access_info(client):
    client._get.return_value = success_response
    response = client.Control.GetSSHAccessInfo(1)
    client._get.assert_called_once_with(
        "GetSSHAccessInfo",
        params={
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_getshared_envs_by_uid(client):
    client._get.return_value = success_response
    response = client.Control.GetSharedEnvsByUid(1)
    client._get.assert_called_once_with(
        "GetSharedEnvsByUid",
        params={
            "uid": 1,
        },
    )
    assert response == success_response


def test_get_software_packages(client):
    client._get.return_value = success_response
    response = client.Control.GetSoftwarePackages(
        "env",
        ["node1", "node2", "node3"],
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_once_with(
        "GetSoftwarePackages",
        params={
            "envName": "env",
            "nodeType": ["node1", "node2", "node3"],
            "nodeGroup": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_stats(client):
    client._get.return_value = success_response
    response = client.Control.GetStats(
        "env",
        10,
        10,
        [CURRENT_DATETIME, CURRENT_DATETIME, CURRENT_DATETIME],
        [1, 2, 3],
        ["node1", "node2", "node3"],
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_once_with(
        "GetStats",
        params={
            "envName": "env",
            "duration": 10,
            "interval": 10,
            "endtime": [CURRENT_DATETIME, CURRENT_DATETIME, CURRENT_DATETIME],
            "nodeid": [1, 2, 3],
            "nodetype": ["node1", "node2", "node3"],
            "nodeGroup": ["group1", "group2", "group3"],
        },
        datetime_format="%Y-%m-%d",
        delimiter=",",
    )
    assert response == success_response


def test_get_sum_stat(client):
    client._get.return_value = success_response
    response = client.Control.GetSumStat(
        "env",
        10,
        [CURRENT_DATETIME, CURRENT_DATETIME, CURRENT_DATETIME],
    )
    client._get.assert_called_once_with(
        "GetSumStat",
        params={
            "envName": "env",
            "duration": 10,
            "endtime": [CURRENT_DATETIME, CURRENT_DATETIME, CURRENT_DATETIME],
        },
        datetime_format="%Y-%m-%d",
        delimiter=",",
    )
    assert response == success_response


def test_get_template_manifest(client):
    client._get.return_value = success_response
    response = client.Control.GetTemplateManifest("node", "tag")
    client._get.assert_called_once_with(
        "GetTemplateManifest",
        params={
            "nodeType": "node",
            "tag": "tag",
        },
    )
    assert response == success_response


def test_get_templates(client):
    client._get.return_value = success_response
    response = client.Control.GetTemplates(
        ["type1", "type2", "type3"],
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        "GetTemplates",
        params={
            "type": ["type1", "type2", "type3"],
            "ownerUid": [1, 2, 3],
        },
    )
    assert response == success_response


def test_get_transfer_request(client):
    client._get.return_value = success_response
    response = client.Control.GetTransferRequest()
    client._get.assert_called_once_with("GetTransferRequest", params={})
    assert response == success_response


def test_install_package_by_group(client):
    client._get.return_value = success_response
    response = client.Control.InstallPackageByGroup(
        "env",
        "node",
        "name",
    )
    client._get.assert_called_once_with(
        "InstallPackageByGroup",
        params={
            "envName": "env",
            "nodeGroup": "node",
            "packageName": "name",
        },
    )
    assert response == success_response


def test_install_package_by_id(client):
    client._get.return_value = success_response
    response = client.Control.InstallPackageById(
        "env",
        "name",
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        "InstallPackageById",
        params={
            "envName": "env",
            "packageName": "name",
            "nodeId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_install_software_package(client):
    client._get.return_value = success_response
    response = client.Control.InstallSoftwarePackage(
        "env",
        "keyword",
        ["type1", "type2", "type3"],
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_once_with(
        "InstallSoftwarePackage",
        params={
            "envName": "env",
            "keyword": "keyword",
            "nodeType": ["type1", "type2", "type3"],
            "nodeGroup": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_link_docker_nodes(client):
    client._get.return_value = success_response
    response = client.Control.LinkDockerNodes(
        "env",
        1,
        1,
        "alias",
        [True, False, True],
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_once_with(
        "LinkDockerNodes",
        params={
            "envName": "env",
            "sourceNodeId": 1,
            "targetNodeId": 1,
            "alias": "alias",
            "isAutoRestart": [True, False, True],
            "groupAlias": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_link_node(client):
    client._get.return_value = success_response
    response = client.Control.LinkNode(
        "env",
        1,
        1,
    )
    client._get.assert_called_once_with(
        "LinkNode",
        params={
            "envName": "env",
            "childNodeId": 1,
            "parentNodeId": 1,
        },
    )
    assert response == success_response


def test_link_nodes(client):
    client._get.return_value = success_response
    response = client.Control.LinkNodes(
        "env",
        "child node",
        "parent node",
    )
    client._get.assert_called_once_with(
        "LinkNodes",
        params={
            "envName": "env",
            "childNode": "child node",
            "parentNode": "parent node",
        },
    )
    assert response == success_response


def test_manage_anv_attributes(client):
    client._get.return_value = success_response
    response = client.Control.ManageEnvAttributes("app id", "attributes")
    client._get.assert_called_once_with(
        "ManageEnvAttributes",
        params={
            "targetAppId": "app id",
            "attributes": "attributes",
        },
    )
    assert response == success_response


def test_migrate(client):
    client._get.return_value = success_response
    response = client.Control.Migrate(
        "env",
        ["group1", "group2", "group3"],
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "Migrate",
        params={
            "envName": "env",
            "hardwareNodeGroup": ["group1", "group2", "group3"],
            "isOnLine": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_read_log(client):
    client._get.return_value = success_response
    response = client.Control.ReadLog(
        "env",
        1,
        "path",
        [1, 2, 3],
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        "ReadLog",
        params={
            "envName": "env",
            "nodeId": 1,
            "path": "path",
            "from": [1, 2, 3],
            "count": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_redeploy_container_by_id(client):
    client._get.return_value = success_response
    response = client.Control.RedeployContainerById(
        "env",
        1,
        "tag",
        [True, False, True],
        ["login1", "login2", "login3"],
        ["password1", "password2", "password3"],
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "RedeployContainerById",
        params={
            "envName": "env",
            "nodeId": 1,
            "tag": "tag",
            "useExistingVolumes": [True, False, True],
            "login": ["login1", "login2", "login3"],
            "password": ["password1", "password2", "password3"],
            "manageDNSState": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_redeploy_containers(client):
    client._get.return_value = success_response
    response = client.Control.RedeployContainers(
        "env",
        "tag",
        ["group1", "group2", "group3"],
        [1, 2, 3],
        [True, False, True],
        ["login1", "login2", "login3"],
        ["password1", "password2", "password3"],
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "RedeployContainers",
        params={
            "envName": "env",
            "tag": "tag",
            "nodeGroup": ["group1", "group2", "group3"],
            "nodeId": [1, 2, 3],
            "useExistingVolumes": [True, False, True],
            "login": ["login1", "login2", "login3"],
            "password": ["password1", "password2", "password3"],
            "manageDNSState": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_redeploy_containers_by_group(client):
    client._get.return_value = success_response
    response = client.Control.RedeployContainersByGroup(
        "env",
        "group",
        "tag",
        True,
        True,
        123,
        "login",
        "password",
        True,
    )
    client._get.assert_called_once_with(
        "RedeployContainersByGroup",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "tag": "tag",
            "isSequential": True,
            "useExistingVolumes": True,
            "delay": 123,
            "login": "login",
            "password": "password",
            "manageDNSState": True,
        },
    )
    assert response == success_response


def test_remove_app(client):
    client._get.return_value = success_response
    response = client.Control.RemoveApp(
        "env",
        "context",
        ["group1", "group2"],
    )
    client._get.assert_called_once_with(
        "RemoveApp",
        params={
            "envName": "env",
            "context": "context",
            "nodeGroup": ["group1", "group2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_container_env_vars(client):
    client._get.return_value = success_response
    response = client.Control.RemoveContainerEnvVars(
        "env",
        ["var1", "var2"],
        ["group1", "group2", "group3"],
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        "RemoveContainerEnvVars",
        params={
            "envName": "env",
            "vars": ["var1", "var2"],
            "nodeGroup": ["group1", "group2", "group3"],
            "nodeId": [1, 2, 3],
        },
    )
    assert response == success_response


def test_remove_container_volume(client):
    client._get.return_value = success_response
    response = client.Control.RemoveContainerVolume(
        "env",
        1,
        "path",
    )
    client._get.assert_called_once_with(
        "RemoveContainerVolume",
        params={
            "envName": "env",
            "nodeId": 1,
            "path": "path",
        },
    )
    assert response == success_response


def test_remove_container_volume_by_group(client):
    client._get.return_value = success_response
    response = client.Control.RemoveContainerVolumeByGroup(
        "env",
        "group",
        "path",
    )
    client._get.assert_called_once_with(
        "RemoveContainerVolumeByGroup",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "path": "path",
        },
    )
    assert response == success_response


def test_remove_container_volumes(client):
    client._get.return_value = success_response
    response = client.Control.RemoveContainerVolumes(
        "env",
        "volumes",
        ["group1", "group2", "group3"],
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        "RemoveContainerVolumes",
        params={
            "envName": "env",
            "volumes": "volumes",
            "nodeGroup": ["group1", "group2", "group3"],
            "nodeId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_docker_volume(client):
    client._get.return_value = success_response
    response = client.Control.RemoveDockerVolume(
        "env",
        1,
        "path",
    )
    client._get.assert_called_once_with(
        "RemoveDockerVolume", params={"envName": "env", "nodeId": 1, "path": "path"}
    )
    assert response == success_response


def test_remove_docker_volume_by_group(client):
    client._get.return_value = success_response
    response = client.Control.RemoveDockerVolumeByGroup(
        "env",
        "group",
        "path",
    )
    client._get.RemoveDockerVolumeByGroup(
        "RemoveDockerVolume",
        params={"envName": "env", "nodeGroup": "group", "path": "path"},
    )
    assert response == success_response


def test_remove_endpoint(client):
    client._get.return_value = success_response
    response = client.Control.RemoveEndpoint("env", 1)
    client._get.assert_called_once_with(
        "RemoveEndpoint",
        params={
            "envName": "env",
            "id": 1,
        },
    )
    assert response == success_response


def test_remove_env_policy(client):
    client._get.return_value = success_response
    response = client.Control.RemoveEnvPolicy("app id", "policy")
    client._get.assert_called_once_with(
        "RemoveEnvPolicy",
        params={
            "targetAppId": "app id",
            "policy": "policy",
        },
    )
    assert response == success_response


def test_remove_env_property(client):
    client._get.return_value = success_response
    response = client.Control.RemoveEnvProperty("env", "key")
    client._get.assert_called_once_with(
        "RemoveEnvProperty",
        params={
            "envName": "env",
            "propertyKeys": "key",
        },
    )
    assert response == success_response


def test_remove_log(client):
    client._get.return_value = success_response
    response = client.Control.RemoveLog("env", 1, "path")
    client._get.assert_called_once_with(
        "RemoveLog",
        params={
            "envName": "env",
            "nodeId": 1,
            "path": "path",
        },
    )
    assert response == success_response


def test_remove_node(client):
    client._get.return_value = success_response
    response = client.Control.RemoveNode("env", 1)
    client._get.assert_called_once_with(
        "RemoveNode",
        params={
            "envName": "env",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_rename_app(client):
    client._get.return_value = success_response
    response = client.Control.RenameApp(
        "env",
        "old context",
        "new context",
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_once_with(
        "RenameApp",
        params={
            "envName": "env",
            "oldContext": "old context",
            "newContext": "new context",
            "nodeGroup": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_replicate_nodes(client):
    client._get.return_value = success_response
    response = client.Control.ReplicateNodes("env", "nodes")
    client._get.assert_called_once_with(
        "ReplicateNodes", params={"envName": "env", "nodes": "nodes"}
    )
    assert response == success_response


def test_reset_container_password(client):
    client._get.return_value = success_response
    response = client.Control.ResetContainerPassword(
        "env", 1, ["password1", "password2", "password3"]
    )
    client._get.assert_called_once_with(
        "ResetContainerPassword",
        params={
            "envName": "env",
            "nodeId": 1,
            "password": ["password1", "password2", "password3"],
        },
        delimiter=",",
    )


def test_reset_container_password_by_id(client):
    client._get.return_value = success_response
    response = client.Control.ResetContainerPasswordById(
        "env", 1, ["password1", "password2", "password3"]
    )
    client._get.assert_called_once_with(
        "ResetContainerPasswordById",
        params={
            "envName": "env",
            "nodeId": 1,
            "password": ["password1", "password2", "password3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_reset_container_password_by_type(client):
    client._get.return_value = success_response
    response = client.Control.ResetContainerPasswordByType(
        "env", "type", ["password1", "password2", "password3"]
    )
    client._get.assert_called_once_with(
        "ResetContainerPasswordByType",
        params={
            "envName": "env",
            "nodeType": "type",
            "password": ["password1", "password2", "password3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_reset_container_password_by_group(client):
    client._get.return_value = success_response
    response = client.Control.ResetContainersPasswordByGroup(
        "env", "type", ["password1", "password2", "password3"]
    )
    client._get.assert_called_once_with(
        "ResetContainersPasswordByGroup",
        params={
            "envName": "env",
            "nodeGroup": "type",
            "password": ["password1", "password2", "password3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_reset_node_password(client):
    client._get.return_value = success_response
    response = client.Control.ResetNodePassword(
        "env",
        ["group1", "group2", "group3"],
        [1, 2, 3],
        ["password1", "password2", "password3"],
    )
    client._get.assert_called_once_with(
        "ResetNodePassword",
        params={
            "envName": "env",
            "nodeGroup": ["group1", "group2", "group3"],
            "nodeId": [1, 2, 3],
            "password": ["password1", "password2", "password3"],
        },
        delimiter=",",
    )
    return response == success_response


def test_reset_node_password_by_id(client):
    client._get.return_value = success_response
    response = client.Control.ResetNodePasswordById(
        "env", 1, ["password1", "password2", "password3"]
    )
    client._get.assert_called_once_with(
        "ResetNodePasswordById",
        params={
            "envName": "env",
            "nodeId": 1,
            "password": ["password1", "password2", "password3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_reset_node_password_by_type(client):
    client._get.return_value = success_response
    response = client.Control.ResetNodePasswordByType(
        "env", "type", ["password1", "password2", "password3"]
    )
    client._get.assert_called_once_with(
        "ResetNodePasswordByType",
        params={
            "envName": "env",
            "nodeType": "type",
            "password": ["password1", "password2", "password3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_reset_service_password(client):
    client._get.return_value = success_response
    response = client.Control.ResetServicePassword(
        "env",
        ["group1", "group2", "group3"],
        [1, 2, 3],
        ["password1", "password2", "password3"],
    )
    client._get.assert_called_once_with(
        "ResetServicePassword",
        params={
            "envName": "env",
            "nodeGroup": ["group1", "group2", "group3"],
            "nodeId": [1, 2, 3],
            "password": ["password1", "password2", "password3"],
        },
        delimiter=",",
    )
    return response == success_response


def test_restart_container(client):
    client._get.return_value = success_response
    response = client.Control.RestartContainer(
        "env",
        1,
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "RestartContainer",
        params={
            "envName": "env",
            "nodeId": 1,
            "manageDNSState": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_restart_container_by_type(client):
    client._get.return_value = success_response
    response = client.Control.RestartContainerByType(
        "env",
        "type",
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "RestartContainerByType",
        params={
            "envName": "env",
            "nodeType": "type",
            "manageDNSState": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_restart_containers_by_group(client):
    client._get.return_value = success_response
    response = client.Control.RestartContainersByGroup(
        "env",
        "group",
        [1, 2, 3],
        [True, False, True],
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "RestartContainersByGroup",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "delay": [1, 2, 3],
            "isSequential": [True, False, True],
            "manageDNSState": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_restart_nodes(client):
    client._get.return_value = success_response
    response = client.Control.RestartNodes(
        "env",
        "group",
        1,
        2,
        True,
        True,
    )
    client._get.assert_called_once_with(
        "RestartNodes",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "nodeId": 1,
            "delay": 2,
            "isSequential": True,
            "manageDNSState": True,
        },
    )
    assert response == success_response


def test_restart_nodes_by_group(client):
    client._get.return_value = success_response
    response = client.Control.RestartNodesByGroup(
        "env",
        "group",
        [1, 2, 3],
        [True, False, True],
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "RestartNodesByGroup",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "delay": [1, 2, 3],
            "isSequential": [True, False, True],
            "manageDNSState": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_restart_nodes_by_type(client):
    client._get.return_value = success_response
    response = client.Control.RestartNodesByType(
        "env",
        "type",
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "RestartNodesByType",
        params={
            "envName": "env",
            "nodeType": "type",
            "manageDNSState": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_restart_services(client):
    client._get.return_value = success_response
    response = client.Control.RestartServices(
        "env",
        "group",
        [1, 2, 3],
        [1, 2, 3],
        [True, False, True],
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "RestartServices",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "nodeId": [1, 2, 3],
            "delay": [1, 2, 3],
            "isSequential": [True, False, True],
            "manageDNSState": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_restore_dump(client):
    client._get.return_value = success_response
    response = client.Control.RestoreDump(
        "env", "type", "dbname", "password", "url", ["user1", "user2", "user3"]
    )
    client._get.assert_called_once_with(
        "RestoreDump",
        params={
            "envName": "env",
            "nodeType": "type",
            "dbName": "dbname",
            "password": "password",
            "dumpUrl": "url",
            "user": ["user1", "user2", "user3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_send_env_created_email(client):
    client._get.return_value = success_response
    response = client.Control.SendEnvCreatedEmail([True, False, True])
    client._get.assert_called_once_with(
        "SendEnvCreatedEmail",
        params={
            "isImport": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_send_transfer_request(client):
    client._get.return_value = success_response
    response = client.Control.SendTransferRequest(
        "env",
        "test@email.com",
    )
    client._get.assert_called_once_with(
        "SendTransferRequest",
        params={
            "envName": "env",
            "email": "test@email.com",
        },
    )
    assert response == success_response


def test_set_cloud_lets_count(client):
    client._get.return_value = success_response
    response = client.Control.SetCloudletsCount(
        "env",
        "type",
        105,
        100,
    )
    client._get.assert_called_once_with(
        "SetCloudletsCount",
        params={
            "envName": "env",
            "nodeType": "type",
            "flexibleCloudlets": 105,
            "fixedCloudlets": 100,
        },
    )
    assert response == success_response


def test_set_cloud_lets_count_by_group(client):
    client._get.return_value = success_response
    response = client.Control.SetCloudletsCountByGroup(
        "env",
        "group",
        105,
        100,
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        "SetCloudletsCountByGroup",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "flexibleCloudlets": 105,
            "fixedCloudlets": 100,
            "delay": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_cloud_lets_count_by_id(client):
    client._get.return_value = success_response
    response = client.Control.SetCloudletsCountById(
        "env",
        1,
        105,
        100,
    )
    client._get.assert_called_once_with(
        "SetCloudletsCountById",
        params={
            "envName": "env",
            "nodeId": 1,
            "flexibleCloudlets": 105,
            "fixedCloudlets": 100,
        },
    )
    assert response == success_response


def test_set_cloud_lets_count_by_type(client):
    client._get.return_value = success_response
    response = client.Control.SetCloudletsCountByType(
        "env",
        "type",
        105,
        100,
    )
    client._get.assert_called_once_with(
        "SetCloudletsCountByType",
        params={
            "envName": "env",
            "nodeType": "type",
            "flexibleCloudlets": 105,
            "fixedCloudlets": 100,
        },
    )
    assert response == success_response


def test_set_container_entry_point(client):
    client._get.return_value = success_response
    response = client.Control.SetContainerEntryPoint(
        "env",
        1,
        ["data1", "data2", "data3"],
    )
    client._get.assert_called_once_with(
        "SetContainerEntryPoint",
        params={
            "envName": "env",
            "nodeId": 1,
            "data": ["data1", "data2", "data3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_container_env_vars(client):
    client._get.return_value = success_response
    response = client.Control.SetContainerEnvVars("env", 1, {"key": "value"})
    client._get.assert_called_once_with(
        "SetContainerEnvVars",
        params={
            "envName": "env",
            "nodeId": 1,
            "vars": '{"key": "value"}',
        },
    )
    assert response == success_response


def test_set_container_env_vars_by_group(client):
    client._get.return_value = success_response
    response = client.Control.SetContainerEnvVarsByGroup(
        "env", "group", {"key": "value"}
    )
    client._get.assert_called_once_with(
        "SetContainerEnvVarsByGroup",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "data": '{"key": "value"}',
        },
    )
    assert response == success_response


def test_set_container_run_cmd(client):
    client._get.return_value = success_response
    response = client.Control.SetContainerRunCmd(
        "env",
        1,
        ["data1", "data2", "data3"],
    )
    client._get.assert_called_once_with(
        "SetContainerRunCmd",
        params={
            "envName": "env",
            "nodeId": 1,
            "data": ["data1", "data2", "data3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_disk_limit_by_group(client):
    client._get.return_value = success_response
    response = client.Control.SetDiskLimitByGroup("env", "group", 1)
    client._get.assert_called_once_with(
        "SetDiskLimitByGroup",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "limit": 1,
        },
    )
    assert response == success_response


def test_set_disk_limit_by_id(client):
    client._get.return_value = success_response
    response = client.Control.SetDiskLimitById("env", 1, 1)
    client._get.assert_called_once_with(
        "SetDiskLimitById",
        params={
            "envName": "env",
            "nodeId": 1,
            "limit": 1,
        },
    )
    assert response == success_response


def test_set_docker_entry_point(client):
    client._get.return_value = success_response
    response = client.Control.SetDockerEntryPoint(
        "env",
        1,
        ["data1", "data2", "data3"],
    )
    client._get.assert_called_once_with(
        "SetDockerEntryPoint",
        params={
            "envName": "env",
            "nodeId": 1,
            "data": ["data1", "data2", "data3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_docker_env_vars(client):
    client._get.return_value = success_response
    response = client.Control.SetDockerEnvVars(
        "env",
        1,
        "data",
    )
    client._get.assert_called_once_with(
        "SetDockerEnvVars",
        params={
            "envName": "env",
            "nodeId": 1,
            "data": "data",
        },
    )
    assert response == success_response


def test_set_docker_run_Cmd(client):
    client._get.return_value = success_response
    response = client.Control.SetDockerRunCmd(
        "env",
        1,
        ["data1", "data2", "data3"],
    )
    client._get.assert_called_once_with(
        "SetDockerRunCmd",
        params={
            "envName": "env",
            "nodeId": 1,
            "data": ["data1", "data2", "data3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_docker_volume_form(client):
    client._get.return_value = success_response
    response = client.Control.SetDockerVolumesFrom(
        "env",
        1,
        "data",
    )
    client._get.assert_called_once_with(
        "SetDockerVolumesFrom",
        params={
            "envName": "env",
            "nodeId": 1,
            "data": "data",
        },
    )
    assert response == success_response


def test_set_engine_by_group(client):
    client._get.return_value = success_response
    response = client.Control.SetEngineByGroup(
        "env",
        "group",
        "engine",
    )
    client._get.assert_called_once_with(
        "SetEngineByGroup",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "engine": "engine",
        },
    )
    assert response == success_response


def test_set_env_display_name(client):
    client._get.return_value = success_response
    response = client.Control.SetEnvDisplayName(
        "env",
        ["name1", "name2", "name3"],
    )
    client._get.assert_called_once_with(
        "SetEnvDisplayName",
        params={
            "envName": "env",
            "dispplayName": ["name1", "name2", "name3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_env_group(client):
    client._get.return_value = success_response
    response = client.Control.SetEnvGroup("env", "group")
    client._get.assert_called_once_with(
        "SetEnvGroup",
        params={
            "envName": "env",
            "envGroup": "group",
        },
    )
    assert response == success_response


def test_set_node_display_name(client):
    client._get.return_value = success_response
    response = client.Control.SetNodeDisplayName(
        "env",
        [1, 2, 3],
        ["name1", "name2", "name3"],
    )
    client._get.assert_called_once_with(
        "SetNodeDisplayName",
        params={
            "envName": "env",
            "nodeId": [1, 2, 3],
            "displayName": ["name1", "name2", "name3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_node_group_display_name(client):
    client._get.return_value = success_response
    response = client.Control.SetNodeGroupDisplayName(
        "env",
        ["group1", "group2", "group3"],
        ["name1", "name2", "name3"],
    )
    client._get.assert_called_once_with(
        "SetNodeGroupDisplayName",
        params={
            "envName": "env",
            "nodeGroup": ["group1", "group2", "group3"],
            "displayName": ["name1", "name2", "name3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_slb_access_enabled(client):
    client._get.return_value = success_response
    response = client.Control.SetSLBAccessEnabled("env", "group", True)
    client._get.assert_called_once_with(
        "SetSLBAccessEnabled",
        params={
            "envName": "env",
            "nodeGroup": "group",
            "enabled": True,
        },
    )
    assert response == success_response


def test_skip_message(client):
    client._get.return_value = success_response
    response = client.Control.SkipMessage("env", 1, 1)
    client._get.assert_called_once_with(
        "SkipMessage",
        params={
            "envName": "env",
            "nodeId": 1,
            "id": 1,
        },
    )
    assert response == success_response


def test_sleep_env(client):
    client._get.return_value = success_response
    response = client.Control.SleepEnv("env")
    client._get.assert_called_once_with(
        "SleepEnv",
        params={
            "envName": "env",
        },
    )
    assert response == success_response


def test_start_env(client):
    client._get.return_value = success_response
    response = client.Control.StartEnv("env")
    client._get.assert_called_once_with(
        "StartEnv",
        params={
            "envName": "env",
        },
    )
    assert response == success_response


def test_stop_env(client):
    client._get.return_value = success_response
    response = client.Control.StopEnv("env")
    client._get.assert_called_once_with(
        "StopEnv",
        params={
            "envName": "env",
        },
    )
    assert response == success_response


def test_uninstall_software_package(client):
    client._get.return_value = success_response
    response = client.Control.UninstallSoftwarePackage(
        "env",
        "keyword",
        ["type1", "type2", "type3"],
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_once_with(
        "UninstallSoftwarePackage",
        params={
            "envName": "env",
            "keyword": "keyword",
            "nodeType": ["type1", "type2", "type3"],
            "nodeGroup": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_unlink_docker_nodes(client):
    client._get.return_value = success_response
    response = client.Control.UnlinkDockerNodes(
        "env",
        1,
        1,
        "alias",
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "UnlinkDockerNodes",
        params={
            "envName": "env",
            "sourceNodeId": 1,
            "targetNodeId": 1,
            "alias": "alias",
            "isAutoRestart": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_unpack_docker(client):
    client._get.return_value = success_response
    response = client.Control.UnpackDocker(
        "env",
        1,
        "folders",
        ["tag1", "tag2", "tag3"],
    )
    client._get.assert_called_once_with(
        "UnpackDocker",
        params={
            "envName": "env",
            "nodeID": 1,
            "folders": "folders",
            "tag": ["tag1", "tag2", "tag3"],
        },
        delimiter=",",
    )
    assert response == success_response
