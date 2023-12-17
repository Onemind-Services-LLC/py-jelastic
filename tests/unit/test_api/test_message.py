from unittest.mock import patch, Mock

import pytest

from jelastic.api import Message

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        message = Message(session=Mock(), token="token")
        message._get = mock_get
        yield message


def test_send(client):
    client._get.return_value = success_response
    response = client.Email.Send(
        "to@example.com",
        "Subject",
        "This is a body",
        "from@example.com",
        "reply-to@example.com",
        "plain",
        1,
    )
    client._get.assert_called_with(
        "Send",
        params={
            "to": "to@example.com",
            "subject": "Subject",
            "body": "This is a body",
            "from": "from@example.com",
            "replyTo": "reply-to@example.com",
            "type": "plain",
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_send_to_user(client):
    client._get.return_value = success_response
    response = client.Email.SendToUser(
        "user@example.com", "Subject", "This is a body", "from@example.com", 1
    )
    client._get.assert_called_with(
        "SendToUser",
        params={
            "login": "user@example.com",
            "subject": "Subject",
            "body": "This is a body",
            "from": "from@example.com",
            "resellerId": 1,
        },
    )
    assert response == success_response
