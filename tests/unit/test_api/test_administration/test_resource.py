from . import *


def test_add_statistics(client):
    client._get.return_value = success_response
    response = client.Resource.AddStatistics(
        "resource 1",
        1,
        1234,
        CURRENT_DATETIME.date().today(),
        CURRENT_DATETIME.date().today(),
        "envName",
        1,
        "note",
        "value",
        "ruk",
    )
    client._get.assert_called_with(
        "AddStatistics",
        params={
            "resourceName": "resource 1",
            "uid": 1,
            "value": 1234,
            "startDate": CURRENT_DATETIME.date().today(),
            "endDate": CURRENT_DATETIME.date().today(),
            "envName": "envName",
            "nodeId": 1,
            "note": "note",
            "valueGroup": "value",
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d",
    )
    assert response == success_response
