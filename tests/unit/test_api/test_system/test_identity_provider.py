from . import *


def test_add_user(client):
    client._get.return_value = success_response
    response = client.IdentityProvider.CreateUser(
        "realm",
        "json",
        "ruk",
    )
    client._get.assert_called_once_with(
        "CreateUser",
        params={"realm": "realm", "userJson": "json", "ruk": "ruk"},
    )
    assert response == success_response
