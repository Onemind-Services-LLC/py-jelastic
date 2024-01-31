from . import *


def test_clear_log(client):
    client._get.return_value = success_response
    response = client.Console.ClearLog("ruk")
    client._get.assert_called_with(
        "ClearLog",
        params={"ruk":"ruk"},
    )
    assert response == success_response


def test_read_log(client):
    client._get.return_value = success_response
    response = client.Console.ReadLog("ruk")
    client._get.assert_called_with(
        "ReadLog",
        params={"ruk":"ruk"},
    )
    assert response == success_response


def test_write_log(client):
    client._get.return_value = success_response
    response = client.Console.WriteLog("message", "ruk")
    client._get.assert_called_with(
        "WriteLog",
        params={"message": "message", "ruk":"ruk"},
    )
    assert response == success_response
