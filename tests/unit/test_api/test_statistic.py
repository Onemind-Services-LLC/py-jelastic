from unittest.mock import patch, Mock
import pytest

from jelastic.api import Statistic

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        statistic = Statistic(session=Mock(), token="token")
        statistic._get = mock_get
        yield statistic


def test_generate_statistics(client):
    client._get.return_value = success_response
    response = client.Utils.GenerateStatistics(1, 1, "stat_json", "checksum")
    client._get.assert_called_with(
        "GenerateStatistics",
        params={
            "durationHours": 1,
            "nodeId": 1,
            "statJSON": "stat_json",
            "checksum": "checksum",
        },
    )
    assert response == success_response
