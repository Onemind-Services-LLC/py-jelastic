from . import *


def test_add_domain(client):
    client._get.return_value = success_response
    response = client.Windows.AddDomain(
        "name", "username", "password", ["dns_server1", "dns_server2"]
    )
    client._get.assert_called_with(
        "AddDomain",
        params={
            "name": "name",
            "username": "username",
            "password": "password",
            "dnsServer": ["dns_server1", "dns_server2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_domain(client):
    client._get.return_value = success_response
    response = client.Windows.EditDomain(
        1,
        ["name1", "name2"],
        ["username", "username2"],
        ["old_password1", "old_password2"],
        ["password1", "password2"],
        ["dns_server1", "dns_server2"],
    )
    client._get.assert_called_with(
        "EditDomain",
        params={
            "id": 1,
            "name": ["name1", "name2"],
            "username": ["username", "username2"],
            "oldPassword": ["old_password1", "old_password2"],
            "password": ["password1", "password2"],
            "dnsServer": ["dns_server1", "dns_server2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_list(client):
    client._get.return_value = success_response
    response = client.Windows.GetList()
    client._get.assert_called_with(
        "GetList",
        params={},
    )
    assert response == success_response


def test_is_domain_exists(client):
    client._get.return_value = success_response
    response = client.Windows.IsDomainExists(1, "checksum")
    client._get.assert_called_with(
        "IsDomainExists",
        params={"id": 1, "checksum": "checksum"},
        delimiter=",",
    )
    assert response == success_response


def test_remove_domain(client):
    client._get.return_value = success_response
    response = client.Windows.RemoveDomain(1)
    client._get.assert_called_with("RemoveDomain", params={"id": 1})
    assert response == success_response
