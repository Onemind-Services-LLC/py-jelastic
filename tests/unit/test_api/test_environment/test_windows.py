from . import *


def test_add_domain(client):
    client._get.return_value = success_response
    response = client.Windows.AddDomain("name", "username", "password", "dnsServer")
    client._get.assert_called_with(
        "AddDomain",
        params={
            "name": "name",
            "username": "username",
            "password": "password",
            "dnsServer": "dnsServer",
        },
    )
    assert response == success_response


def test_edit_domain(client):
    client._get.return_value = success_response
    response = client.Windows.EditDomain(
        1, "name", "username", "oldPassword", "password", "dnsServer"
    )
    client._get.assert_called_with(
        "EditDomain",
        params={
            "id": 1,
            "name": "name",
            "username": "username",
            "oldPassword": "oldPassword",
            "password": "password",
            "dnsServer": "dnsServer",
        },
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
        "IsDomainExists", params={"id": 1, "checksum": "checksum"}
    )
    assert response == success_response


def test_remove_domain(client):
    client._get.return_value = success_response
    response = client.Windows.RemoveDomain(1)
    client._get.assert_called_with("RemoveDomain", params={"id": 1})
    assert response == success_response
