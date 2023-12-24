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


def test_get_docker_pull_status(client):
    client._get.return_value = success_response
    response = client.Monitoring.GetDockerPullStatus()
    client._get.assert_called_with("GetDockerPullStatus", params={})
    assert response == success_response


def test_get_host_firewall_status(client):
    client._get.return_value = success_response
    response = client.Monitoring.GetHostFirewallStatus()
    client._get.assert_called_with("GetHostFirewallStatus", params={})
    assert response == success_response
