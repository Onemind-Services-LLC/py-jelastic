from . import *


def test_get_auth_endpoint(client):
    client._get.return_value = success_response
    response = client.SSO.GetAuthEndpoint("redirect_uri")
    client._get.assert_called_with(
        "GetAuthEndpoint",
        params={
            "redirectUri": "redirect_uri",
        },
    )

    assert response == success_response


def test_get_impersonation_data(client):
    client._get.return_value = success_response
    response = client.SSO.GetImpersonationData(1)
    client._get.assert_called_with(
        "GetImpersonationData",
        params={
            "uid": 1,
        },
    )

    assert response == success_response


def test_get_settings(client):
    client._get.return_value = success_response
    response = client.SSO.GetSettings()
    client._get.assert_called_with(
        "GetSettings",
        params={},
    )

    assert response == success_response


def test_reset_password(client):
    client._get.return_value = success_response
    response = client.SSO.ResetPassword()
    client._get.assert_called_with(
        "ResetPassword",
        params={},
    )

    assert response == success_response


def test_sign_in_by_code(client):
    client._get.return_value = success_response
    response = client.SSO.SigninByCode("code", "redirect_uri")
    client._get.assert_called_with(
        "SigninByCode",
        params={
            "code": "code",
            "redirectUri": "redirect_uri",
        },
    )

    assert response == success_response


def test_sign_in_by_token(client):
    client._get.return_value = success_response
    response = client.SSO.SigninByToken("token")
    client._get.assert_called_with(
        "SigninByToken",
        params={
            "token": "token",
        },
    )

    assert response == success_response
