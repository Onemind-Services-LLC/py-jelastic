from . import *


def test_add_group(client):
    client._get.return_value = success_response
    response = client.Groups.AddGroup("login", "group")
    client._get.assert_called_once_with(
        "AddGroup",
        params={
            "login": "login",
            "group": "group",
        },
    )
    assert response == success_response


def test_get_groups(client):
    client._get.return_value = success_response
    response = client.Groups.GetGroups("login")
    client._get.assert_called_once_with(
        "GetGroups",
        params={
            "login": "login",
        },
    )
    assert response == success_response


def test_remove_group(client):
    client._get.return_value = success_response
    response = client.Groups.RemoveGroup("login", "group")
    client._get.assert_called_once_with(
        "RemoveGroup",
        params={
            "login": "login",
            "group": "group",
        },
    )
    assert response == success_response
