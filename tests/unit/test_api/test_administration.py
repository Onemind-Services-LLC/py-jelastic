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


def test_fix_ext_dns(client):
    client._get.return_value = success_response
    response = client.Update.FixExtDns(
        [1, 2, 3, 4],
        ["target_app_id1", "target_app_id2", "target_app_id3"],
    )
    client._get.assert_called_with(
        "FixExtDns",
        params={
            "uid": [1, 2, 3, 4],
            "targetAppIds": ["target_app_id1", "target_app_id2", "target_app_id3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_restore_env(client):
    client._get.return_value = success_response
    response = client.Update.RestoreEnv(
        ["env1", "env2", "env3"],
        [1, 2, 3],
        ["region1", "region2", "region3"],
    )
    client._get.assert_called_with(
        "RestoreEnv",
        params={
            "envName": ["env1", "env2", "env3"],
            "uid": [1, 2, 3],
            "region": ["region1", "region2", "region3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_sync_infra_env(client):
    client._get.return_value = success_response
    response = client.Update.SyncInfraEnv(
        ["domain1", "domain2", "domain3"],
        ["registry1", "registry2", "registry3"],
    )
    client._get.assert_called_with(
        "SyncInfraEnv",
        params={
            "domain": ["domain1", "domain2", "domain3"],
            "registry": ["registry1", "registry2", "registry3"],
        },
        delimiter=",",
    )
