from . import *


def test_add_group(client):
    client._get.return_value = success_response
    response = client.Groups.AddGroup(
        "login",
        "group",
        "ruk",
    )
    client._get.assert_called_once_with(
        "AddGroup",
        params={"login": "login", "group": "group", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_groups(client):
    client._get.return_value = success_response
    response = client.Groups.GetGroups(
        "login",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetGroups",
        params={"login": "login", "ruk": "ruk"},
    )
    assert response == success_response


def test_remove_group(client):
    client._get.return_value = success_response
    response = client.Groups.RemoveGroup(
        "login",
        "group",
        "ruk",
    )
    client._get.assert_called_once_with(
        "RemoveGroup",
        params={"login": "login", "group": "group", "ruk": "ruk"},
    )
    assert response == success_response
