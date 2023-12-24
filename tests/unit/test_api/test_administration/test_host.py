from . import *


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
