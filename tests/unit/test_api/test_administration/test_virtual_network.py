from . import *


def test_add_virtual_network(client):
    client._get.return_value = success_response
    response = client.VirtualNetwork.AddVirtualNetwork(
        {
            "networkName1": "name1",
            "networkName2": "name2",
            "networkName3": "name3",
            "networkName4": "name4",
            "networkName5": "name5",
        },
    )
    client._get.assert_called_with(
        "AddVirtualNetwork",
        params={
            "virtualNetwork": {
                "networkName1": "name1",
                "networkName2": "name2",
                "networkName3": "name3",
                "networkName4": "name4",
                "networkName5": "name5",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_apply_virtual_networks(client):
    client._get.return_value = success_response
    response = client.VirtualNetwork.ApplyVirtualNetworks(
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "ApplyVirtualNetworks",
        params={
            "hostId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_virtual_networks(client):
    client._get.return_value = success_response
    response = client.VirtualNetwork.DeleteVirtualNetworks(1)
    client._get.assert_called_with(
        "DeleteVirtualNetworks",
        params={
            "ids": 1,
        },
    )
    assert response == success_response


def test_get_virtual_networks(client):
    client._get.return_value = success_response
    response = client.VirtualNetwork.GetVirtualNetworks(
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "GetVirtualNetworks",
        params={
            "ids": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response
