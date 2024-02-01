from . import *


def test_get_docker_pull_status(client):
    client._get.return_value = success_response
    response = client.Monitoring.GetDockerPullStatus("ruk")
    client._get.assert_called_with("GetDockerPullStatus", params={"ruk": "ruk"})
    assert response == success_response


def test_get_host_firewall_status(client):
    client._get.return_value = success_response
    response = client.Monitoring.GetHostFirewallStatus("ruk")
    client._get.assert_called_with("GetHostFirewallStatus", params={"ruk": "ruk"})
    assert response == success_response
