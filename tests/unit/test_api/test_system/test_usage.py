from . import *


def test_get_cpu_hours(client):
    client._get.return_value = success_response
    response = client.Usage.GetCPUHours(
        ["start1", "start2", "start3"],
        ["period1", "period2", "period3"],
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "GetCPUHours",
        params={
            "start": ["start1", "start2", "start3"],
            "period": ["period1", "period2", "period3"],
            "series": [True, False, True],
        },
        delimiter=",",
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
