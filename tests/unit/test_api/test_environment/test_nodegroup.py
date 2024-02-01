from . import *


def test_apply_data(client):
    client._get.return_value = success_response
    response = client.NodeGroup.ApplyData(
        "env_name",
        "node_group",
        {"key": "value"},
        "ruk",
    )
    client._get.assert_called_with(
        "ApplyData",
        params={
            "envName": "env_name",
            "nodeGroup": "node_group",
            "data": {"key": "value"},
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get(client):
    client._get.return_value = success_response
    response = client.NodeGroup.Get(
        "env_name",
        "node_group",
        "ruk",
    )
    client._get.assert_called_with(
        "Get",
        params={
            "envName": "env_name",
            "nodeGroup": "node_group",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_set_slb_access_enabled(client):
    client._get.return_value = success_response
    response = client.NodeGroup.SetSLBAccessEnabled(
        "env_name",
        "node_group",
        "enabled",
        "ruk",
    )
    client._get.assert_called_with(
        "SetSLBAccessEnabled",
        params={
            "envName": "env_name",
            "nodeGroup": "node_group",
            "enabled": "enabled",
            "ruk": "ruk",
        },
    )
    assert response == success_response
