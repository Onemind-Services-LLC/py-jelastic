import datetime
from unittest.mock import patch, Mock

import pytest

from jelastic.api import Administration

CURRENT_DATETIME = datetime.datetime.now()
success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        jc = Administration(session=Mock(), token="token")
        jc._get = mock_get
        yield jc


def test_update_fix_ext_dns(client):
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
    assert response == success_response
