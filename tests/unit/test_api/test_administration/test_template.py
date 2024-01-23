from . import *


def test_set_default_registry(client):
    client._get.return_value = success_response
    response = client.Template.SetDefaultRegistry(1)
    client._get.assert_called_with(
        "SetDefaultRegistry",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_set_distribution(client):
    client._get.return_value = success_response
    response = client.Template.SetDistribution("node type", "distribution")
    client._get.assert_called_with(
        "SetDistribution",
        params={"nodeTypes": "node type", "distribution": "distribution"},
    )
    assert response == success_response
