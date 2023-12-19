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
