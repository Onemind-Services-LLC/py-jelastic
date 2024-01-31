from . import *


def test_generate_statistics(client):
    client._get.return_value = success_response
    response = client.Utils.GenerateStatistics(
        1,
        1,
        "stat_json",
        "checksum",
        "ruk",
    )
    client._get.assert_called_with(
        "GenerateStatistics",
        params={
            "durationHours": 1,
            "nodeId": 1,
            "statJSON": "stat_json",
            "checksum": "checksum",
            "ruk": "ruk",
        },
    )
    assert response == success_response
