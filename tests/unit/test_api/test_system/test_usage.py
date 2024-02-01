from . import *


def test_get_cpu_hours(client):
    client._get.return_value = success_response
    response = client.Usage.GetCPUHours(
        "start",
        "period",
        True,
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetCPUHours",
        params={"start": "start", "period": "period", "series": True, "ruk": "ruk"},
    )
    assert response == success_response


def test_get_platform_stats(client):
    client._get.return_value = success_response
    response = client.Usage.GetPlatformStats(
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetPlatformStats",
        params={"ruk": "ruk"},
    )
    assert response == success_response
