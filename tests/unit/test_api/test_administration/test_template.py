from . import *


def test_set_default_registry(client):
    client._get.return_value = success_response
    response = client.Template.SetDefaultRegistry(
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "SetDefaultRegistry",
        params={
            "id": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_distribution(client):
    client._get.return_value = success_response
    response = client.Template.SetDistribution(
        "node type",
        ["distribution1", "distribution2"],
    )
    client._get.assert_called_with(
        "SetDistribution",
        params={
            "nodeTypes": "node type",
            "distribution": ["distribution1", "distribution2"],
        },
        delimiter=",",
    )
    assert response == success_response
