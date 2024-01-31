from . import *


def test_node_send_event(client):
    client._get.return_value = success_response
    response = client.Node.SendEvent(
        {"key": "value"},
        "OOM_KILLER",
        "ruk",
    )
    client._get.assert_called_with(
        "SendEvent",
        params={
            "params": '{"key": "value"}',
            "eventName": "OOM_KILLER",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_node_send_notification(client):
    client._get.return_value = success_response
    response = client.Node.SendNotification(
        "message",
        "title",
        "ruk",
    )
    client._get.assert_called_with(
        "SendNotification",
        params={
            "message": "message",
            "name": "title",
            "ruk": "ruk",
        },
    )
    assert response == success_response
