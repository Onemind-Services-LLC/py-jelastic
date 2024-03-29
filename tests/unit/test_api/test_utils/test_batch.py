from . import *


def test_call(client):
    client._get.return_value = success_response
    response = client.Batch.Call(
        {"key": "value"},
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "Call", params={"request": '{"key": "value"}', "sync": True, "ruk": "ruk"}
    )
    assert response == success_response
