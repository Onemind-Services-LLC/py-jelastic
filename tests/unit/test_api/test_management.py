from datetime import datetime
from unittest.mock import patch, Mock

import pytest

from jelastic.api import Marketplace

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}
CURRENT_DATETIME = datetime.now()


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        marketplace = Marketplace(session=Mock(), token="token")
        marketplace._get = mock_get
        yield marketplace


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
