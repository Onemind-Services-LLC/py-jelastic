from . import *


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
        "ruk",
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
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_send_to_user(client):
    client._get.return_value = success_response
    response = client.Email.SendToUser(
        "user@example.com", "Subject", "This is a body", "from@example.com", 1, "ruk"
    )
    client._get.assert_called_with(
        "SendToUser",
        params={
            "login": "user@example.com",
            "subject": "Subject",
            "body": "This is a body",
            "from": "from@example.com",
            "resellerId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response
