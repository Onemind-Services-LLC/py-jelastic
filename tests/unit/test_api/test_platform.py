from unittest.mock import patch, Mock

import pytest

from jelastic.api import Platform

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        platform = Platform(session=Mock(), token="token")
        platform._get = mock_get
        yield platform


def test_get(client):
    client._get.return_value = success_response
    response = client.Engine.Get("docker", 77)
    client._get.assert_called_with(
        "Get", params={"engineType": "docker", "ownerUid": 77}
    )
    assert response == success_response


def test_get_entry_point(client):
    client._get.return_value = success_response
    response = client.Engine.GetEntryPoint("COLUMBUS", 1)
    client._get.assert_called_with(
        "GetEntryPoint", params={"hostGroup": "COLUMBUS", "ownerUid": 1}
    )
    assert response == success_response
