from . import *


def test_clear_log(client):
    client._get.return_value = success_response
    response = client.Console.ClearLog()
    client._get.assert_called_with(
        "ClearLog",
        params={},
    )
    assert response == success_response


def test_read_log(client):
    client._get.return_value = success_response
    response = client.Console.ReadLog()
    client._get.assert_called_with(
        "ReadLog",
        params={},
    )
    assert response == success_response


def test_write_log(client):
    client._get.return_value = success_response
    response = client.Console.WriteLog("message")
    client._get.assert_called_with(
        "WriteLog",
        params={"message": "message"},
    )
    assert response == success_response
