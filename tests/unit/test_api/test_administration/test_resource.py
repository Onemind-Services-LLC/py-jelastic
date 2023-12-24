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


def test_add_statistics(client):
    client._get.return_value = success_response
    response = client.Resource.AddStatistics(
        "resource 1",
        1,
        1234,
        [CURRENT_DATETIME.date().today(), CURRENT_DATETIME.date().today()],
        [datetime.date(2025, 11, 11), datetime.date(2025, 11, 12)],
        ["env 1", "env 2", "env 3"],
        [1, 2, 3],
        ["note 1", "note 2", "note 3"],
        ["value 1", "value 2", "value 3"],
    )
    client._get.assert_called_with(
        "AddStatistics",
        params={
            "resourceName": "resource 1",
            "uid": 1,
            "value": 1234,
            "startDate": [
                CURRENT_DATETIME.date().today(),
                CURRENT_DATETIME.date().today(),
            ],
            "endDate": [datetime.date(2025, 11, 11), datetime.date(2025, 11, 12)],
            "envName": ["env 1", "env 2", "env 3"],
            "nodeId": [1, 2, 3],
            "note": ["note 1", "note 2", "note 3"],
            "valueGroup": ["value 1", "value 2", "value 3"],
        },
        delimiter=",",
    )
    assert response == success_response
