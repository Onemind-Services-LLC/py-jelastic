from . import *


def test_get_auth_endpoint(client):
    client._get.return_value = success_response
    response = client.SSO.GetAuthEndpoint(
        "redirect_uri",
        "ruk",
    )
    client._get.assert_called_with(
        "GetAuthEndpoint",
        params={"redirectUri": "redirect_uri", "ruk": "ruk"},
    )

    assert response == success_response


def test_get_impersonation_data(client):
    client._get.return_value = success_response
    response = client.SSO.GetImpersonationData(
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "GetImpersonationData",
        params={"uid": 1, "ruk": "ruk"},
    )

    assert response == success_response


def test_get_settings(client):
    client._get.return_value = success_response
    response = client.SSO.GetSettings(
        "ruk",
    )
    client._get.assert_called_with(
        "GetSettings",
        params={"ruk": "ruk"},
    )

    assert response == success_response


def test_reset_password(client):
    client._get.return_value = success_response
    response = client.SSO.ResetPassword(
        "ruk",
    )
    client._get.assert_called_with(
        "ResetPassword",
        params={"ruk": "ruk"},
    )

    assert response == success_response


def test_sign_in_by_code(client):
    client._get.return_value = success_response
    response = client.SSO.SigninByCode(
        "code",
        "redirect_uri",
        "ruk",
    )
    client._get.assert_called_with(
        "SigninByCode",
        params={"code": "code", "redirectUri": "redirect_uri", "ruk": "ruk"},
    )

    assert response == success_response


def test_sign_in_by_token(client):
    client._get.return_value = success_response
    response = client.SSO.SigninByToken(
        "token",
        "ruk",
    )
    client._get.assert_called_with(
        "SigninByToken",
        params={"token": "token", "ruk": "ruk"},
    )

    assert response == success_response
