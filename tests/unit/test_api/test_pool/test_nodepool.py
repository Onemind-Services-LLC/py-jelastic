from . import *


def test_clear_os_pool(client):
    client._get.return_value = success_response
    response = client.NodePool.ClearOsPool(
        "checksum",
        ["type1", "type2"],
    )
    client._get.assert_called_with(
        "ClearOsPool",
        params={"checksum": "checksum", "type": ["type1", "type2"]},
        delimiter=",",
    )
    assert response == success_response


def test_clear_pool(client):
    client._get.return_value = success_response
    response = client.NodePool.ClearPool(
        1,
        ["type1", "type2"],
    )
    client._get.assert_called_with(
        "ClearPool",
        params={"hnid": 1, "type": ["type1", "type2"]},
        delimiter=",",
    )
    assert response == success_response


def test_generate_pool(client):
    client._get.return_value = success_response
    response = client.NodePool.GeneratePool(123, ["type1", "type2"], [1, 1])
    client._get.assert_called_with(
        "GeneratePool",
        params={
            "checksum": 123,
            "type": ["type1", "type2"],
            "hnid": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_nodepool_get(client):
    client._get.return_value = success_response
    response = client.NodePool.Get(
        "type",
        "hn_id",
        "checksum",
        ["os_template1", "os_template2"],
        ["ct_id1", "ct_id2"],
    )
    client._get.assert_called_with(
        "Get",
        params={
            "type": "type",
            "hnid": "hn_id",
            "checksum": "checksum",
            "osTemplate": ["os_template1", "os_template2"],
            "ctid": ["ct_id1", "ct_id2"],
        },
        delimiter=",",
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
        delimiter=",",
    )
    assert response == success_response


def test_nodepool_clear_os_pool(client):
    client._get.return_value = success_response
    response = client.NodePool.ClearOsPool(
        "checksum",
        ["type1", "type2"],
    )
    client._get.assert_called_with(
        "ClearOsPool",
        params={"checksum": "checksum", "type": ["type1", "type2"]},
        delimiter=",",
    )
    assert response == success_response


def test_nodepool_clear_pool(client):
    client._get.return_value = success_response
    response = client.NodePool.ClearPool(
        1,
        ["type1", "type2"],
    )
    client._get.assert_called_with(
        "ClearPool",
        params={"hnid": 1, "type": ["type1", "type2"]},
        delimiter=",",
    )
    assert response == success_response


def test_nodepool_generate_pool(client):
    client._get.return_value = success_response
    response = client.NodePool.GeneratePool(123, ["type1", "type2"], [1, 1])
    client._get.assert_called_with(
        "GeneratePool",
        params={
            "checksum": 123,
            "type": ["type1", "type2"],
            "hnid": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_nodepool_get(client):
    client._get.return_value = success_response
    response = client.NodePool.Get(
        "type",
        "hn_id",
        "checksum",
        ["os_template1", "os_template2"],
        ["ct_id1", "ct_id2"],
    )
    client._get.assert_called_with(
        "Get",
        params={
            "type": "type",
            "hnid": "hn_id",
            "checksum": "checksum",
            "osTemplate": ["os_template1", "os_template2"],
            "ctid": ["ct_id1", "ct_id2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_nodepool_get_status(client):
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


def test_nodepool_regenerate_pool(client):
    client._get.return_value = success_response
    response = client.NodePool.RegeneratePool("type", "checksum")
    client._get.assert_called_with(
        "RegeneratePool",
        params={
            "type": "type",
            "checksum": "checksum",
        },
        delimiter=",",
    )
    assert response == success_response
