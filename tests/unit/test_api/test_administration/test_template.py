from . import *


def test_set_default_registry(client):
    client._get.return_value = success_response
    response = client.Template.SetDefaultRegistry(1, "ruk")
    client._get.assert_called_with(
        "SetDefaultRegistry",
        params={"id": 1, "ruk": "ruk"},
    )
    assert response == success_response


def test_set_distribution(client):
    client._get.return_value = success_response
    response = client.Template.SetDistribution("node type", "distribution", "ruk")
    client._get.assert_called_with(
        "SetDistribution",
        params={"nodeTypes": "node type", "distribution": "distribution", "ruk": "ruk"},
    )
    assert response == success_response
