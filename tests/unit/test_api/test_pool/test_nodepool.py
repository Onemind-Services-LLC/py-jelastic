from . import *


def test_clear_os_pool(client):
    client._get.return_value = success_response
    response = client.NodePool.ClearOsPool("checksum", "type")
    client._get.assert_called_with(
        "ClearOsPool", params={"checksum": "checksum", "type": "type"}
    )
    assert response == success_response


def test_clear_pool(client):
    client._get.return_value = success_response
    response = client.NodePool.ClearPool(1, "type")
    client._get.assert_called_with("ClearPool", params={"hnid": 1, "type": "type"})
    assert response == success_response


def test_generate_pool(client):
    client._get.return_value = success_response
    response = client.NodePool.GeneratePool(123, "type", 1)
    client._get.assert_called_with(
        "GeneratePool", params={"checksum": 123, "type": "type", "hnid": 1}
    )
    assert response == success_response


def test_nodepool_get(client):
    client._get.return_value = success_response
    response = client.NodePool.Get("type", 11, "checksum", "osTemplate", 11)
    client._get.assert_called_with(
        "Get",
        params={
            "type": "type",
            "hnid": 11,
            "checksum": "checksum",
            "osTemplate": "osTemplate",
            "ctid": 11,
        },
    )
    assert response == success_response


def test_get_status(client):
    client._get.return_value = success_response
    response = client.NodePool.GetStatus(
        "checksum",
    )
    client._get.assert_called_with(
        "GetStatus",
        params={
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_regenerate_pool(client):
    client._get.return_value = success_response
    response = client.NodePool.RegeneratePool("type", "checksum")
    client._get.assert_called_with(
        "RegeneratePool",
        params={
            "type": "type",
            "checksum": "checksum",
        },
    )
    assert response == success_response
