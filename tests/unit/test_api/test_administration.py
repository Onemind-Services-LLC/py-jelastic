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


def test_set_default_registry(client):
    client._get.return_value = success_response
    response = client.Template.SetDefaultRegistry(
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "SetDefaultRegistry",
        params={"id": [1, 2, 3, 4], },
        delimiter=",",
    )
    assert response == success_response


def test_set_distribution(client):
    client._get.return_value = success_response
    response = client.Template.SetDistribution(
        'node type',
        ['distribution1', 'distribution2'],
    )
    client._get.assert_called_with(
        "SetDistribution",
        params={
            'nodeTypes': 'node type',
            'distribution': ['distribution1', 'distribution2'],
        },
        delimiter=",",
    )
    assert response == success_response
