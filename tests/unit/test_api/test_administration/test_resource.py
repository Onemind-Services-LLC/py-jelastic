from . import *


def test_add_statistics(client):
    client._get.return_value = success_response
    response = client.Resource.AddStatistics(
        "resource 1",
        1,
        1234,
        [CURRENT_DATETIME.date().today(), CURRENT_DATETIME.date().today()],
        [CURRENT_DATETIME.date().today(), CURRENT_DATETIME.date().today()],
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
            "endDate": [
                CURRENT_DATETIME.date().today(),
                CURRENT_DATETIME.date().today(),
            ],
            "envName": ["env 1", "env 2", "env 3"],
            "nodeId": [1, 2, 3],
            "note": ["note 1", "note 2", "note 3"],
            "valueGroup": ["value 1", "value 2", "value 3"],
        },
        delimiter=",",
    )
    assert response == success_response
