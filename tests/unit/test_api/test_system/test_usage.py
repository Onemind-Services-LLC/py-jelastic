from . import *


def test_get_cpu_hours(client):
    client._get.return_value = success_response
    response = client.Usage.GetCPUHours("start", "period", True)
    client._get.assert_called_once_with(
        "GetCPUHours", params={"start": "start", "period": "period", "series": True}
    )
    assert response == success_response


def test_get_platform_stats(client):
    client._get.return_value = success_response
    response = client.Usage.GetPlatformStats()
    client._get.assert_called_once_with(
        "GetPlatformStats",
        params={},
    )
    assert response == success_response
