from . import *


def test_change_session(client):
    client._get.return_value = success_response
    response = client.Authentication.ChangeSession(
        "ruk",
    )
    client._get.assert_called_with("ChangeSession", params={"ruk": "ruk"})

    assert response == success_response


def test_check_auth_key(client):
    client._get.return_value = success_response
    response = client.Authentication.CheckAuthKey(
        "auth_key",
        "ruk",
    )
    client._get.assert_called_with(
        "CheckAuthKey", params={"authKey": "auth_key", "ruk": "ruk"}
    )
    assert response == success_response


def test_check_password(client):
    client._get.return_value = success_response
    response = client.Authentication.CheckPassword(
        "password",
        "ruk",
    )
    client._get.assert_called_with(
        "CheckPassword", params={"password": "password", "ruk": "ruk"}
    )
    assert response == success_response


def test_check_sign(client):
    client._get.return_value = success_response
    response = client.Authentication.CheckSign(
        "ruk",
    )
    client._get.assert_called_with("CheckSign", params={"ruk": "ruk"})
    assert response == success_response


def test_check_user(client):
    client._get.return_value = success_response
    response = client.Authentication.CheckUser(
        "login",
        "ruk",
    )
    client._get.assert_called_with("CheckUser", params={"login": "login", "ruk": "ruk"})
    assert response == success_response


def test_clear_api_list_data(client):
    client._get.return_value = success_response
    response = client.Authentication.ClearApiListData(
        "ruk",
    )
    client._get.assert_called_with("ClearApiListData", params={"ruk": "ruk"})
    assert response == success_response


def test_clear_api_list_data_inner(client):
    client._get.return_value = success_response
    response = client.Authentication.ClearApiListDataInner(
        "ruk",
    )
    client._get.assert_called_with("ClearApiListDataInner", params={"ruk": "ruk"})
    assert response == success_response


def test_create_token(client):
    client._get.return_value = success_response
    response = client.Authentication.CreateToken(
        "description",
        "password",
        "tokenTemplate",
        ["api_list1", "api_list2"],
        CURRENT_DATETIME,
        "ruk",
    )
    client._get.assert_called_with(
        "CreateToken",
        params={
            "description": "description",
            "password": "password",
            "tokenTemplate": "tokenTemplate",
            "apiList": ["api_list1", "api_list2"],
            "expiresAt": CURRENT_DATETIME,
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_create_token_inner(client):
    client._get.return_value = success_response
    response = client.Authentication.CreateTokenInner(
        "login",
        "description",
        "tokenTemplate",
        ["api_list1", "api_list2"],
        CURRENT_DATETIME,
        True,
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "CreateTokenInner",
        params={
            "login": "login",
            "description": "description",
            "tokenTemplate": "tokenTemplate",
            "apiList": ["api_list1", "api_list2"],
            "expiresAt": CURRENT_DATETIME,
            "isProtected": True,
            "skipNotification": True,
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_delete_token(client):
    client._get.return_value = success_response
    response = client.Authentication.DeleteTokens(
        "ids",
        "password",
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteTokens", params={"ids": "ids", "password": "password", "ruk": "ruk"}
    )
    assert response == success_response


def test_edit_token(client):
    client._get.return_value = success_response
    response = client.Authentication.EditToken(
        1,
        "password",
        "description",
        "tokenTemplate",
        ["api_list1", "api_list2"],
        CURRENT_DATETIME,
        "ruk",
    )
    client._get.assert_called_with(
        "EditToken",
        params={
            "id": 1,
            "password": "password",
            "description": "description",
            "tokenTemplate": "tokenTemplate",
            "apiList": ["api_list1", "api_list2"],
            "expiresAt": CURRENT_DATETIME,
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_auth_key(client):
    client._get.return_value = success_response
    response = client.Authentication.GetAuthKey(
        "auth_key",
        "ruk",
    )
    client._get.assert_called_with(
        "GetAuthKey", params={"authKey": "auth_key", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_description_by_token(client):
    client._get.return_value = success_response
    response = client.Authentication.GetDescriptionByToken(
        "checksum",
        "ruk",
    )
    client._get.assert_called_with(
        "GetDescriptionByToken", params={"checksum": "checksum", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_device_signature(client):
    client._get.return_value = success_response
    response = client.Authentication.GetDeviceSignature(
        "ruk",
    )
    client._get.assert_called_with("GetDeviceSignature", params={"ruk": "ruk"})
    assert response == success_response


def test_get_policy_methods(client):
    client._get.return_value = success_response
    response = client.Authentication.GetPolicyMethods(
        "uniqueName",
        "ruk",
    )
    client._get.assert_called_with(
        "GetPolicyMethods", params={"uniqueName": "uniqueName", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_session(client):
    client._get.return_value = success_response
    response = client.Authentication.GetSessions(
        "ruk",
    )
    client._get.assert_called_with("GetSessions", params={"ruk": "ruk"})
    assert response == success_response


def test_get_sign_in_attempts(client):
    client._get.return_value = success_response
    response = client.Authentication.GetSigninAttempts(
        "search",
        "ruk",
    )
    client._get.assert_called_with(
        "GetSigninAttempts", params={"search": "search", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_token_api_list(client):
    client._get.return_value = success_response
    response = client.Authentication.GetTokenApiList(
        "showPrivate",
        "sortParam",
        "ruk",
    )
    client._get.assert_called_with(
        "GetTokenApiList",
        params={"showPrivate": "showPrivate", "sortParam": "sortParam", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_token_templates(client):
    client._get.return_value = success_response
    response = client.Authentication.GetTokenTemplates(
        "ruk",
    )
    client._get.assert_called_with("GetTokenTemplates", params={"ruk": "ruk"})
    assert response == success_response


def test_get_tokens(client):
    client._get.return_value = success_response
    response = client.Authentication.GetTokens(
        [
            "ids1",
            "ids2",
        ],
        "ruk",
    )
    client._get.assert_called_with(
        "GetTokens",
        params={"ids": ["ids1", "ids2"], "ruk": "ruk"},
        delimiter=",",
    )
    assert response == success_response


def test_get_uid_by_token(client):
    client._get.return_value = success_response
    response = client.Authentication.GetUidByToken(
        "checksum",
        "ruk",
    )
    client._get.assert_called_with(
        "GetUidByToken", params={"checksum": "checksum", "ruk": "ruk"}
    )
    assert response == success_response


def test_regenerate_token(client):
    client._get.return_value = success_response
    response = client.Authentication.RegenerateToken(
        "ids",
        "password",
        "ruk",
    )
    client._get.assert_called_with(
        "RegenerateToken", params={"ids": "ids", "password": "password", "ruk": "ruk"}
    )
    assert response == success_response


def test_reset_sign_in_attempts(client):
    client._get.return_value = success_response
    response = client.Authentication.ResetSigninAttempts(
        "login",
        "ipAddress",
        "ruk",
    )
    client._get.assert_called_with(
        "ResetSigninAttempts",
        params={"login": "login", "ipAddress": "ipAddress", "ruk": "ruk"},
    )
    assert response == success_response


def test_sign_in(client):
    client._get.return_value = success_response
    response = client.Authentication.Signin(
        "login",
        "password",
        "ruk",
    )
    client._get.assert_called_with(
        "Signin", params={"login": "login", "password": "password", "ruk": "ruk"}
    )
    assert response == success_response


def test_sign_in_by_auth_key(client):
    client._get.return_value = success_response
    response = client.Authentication.SigninByAuthKey(
        "auth_key",
        "ruk",
    )
    client._get.assert_called_with(
        "SigninByAuthKey", params={"authKey": "auth_key", "ruk": "ruk"}
    )
    assert response == success_response


def test_sign_in_by_token(client):
    client._get.return_value = success_response
    response = client.Authentication.SigninByToken(
        "token",
        "user_headers",
        "ruk",
    )
    client._get.assert_called_with(
        "SigninByToken",
        params={"token": "token", "userHeaders": "user_headers", "ruk": "ruk"},
    )
    assert response == success_response


def test_sign_out(client):
    client._get.return_value = success_response
    response = client.Authentication.Signout(
        "ruk",
    )
    client._get.assert_called_with("Signout", params={"ruk": "ruk"})
    assert response == success_response


def test_sign_out_sessions(client):
    client._get.return_value = success_response
    response = client.Authentication.SignoutSessions(
        "ids",
        "ruk",
    )
    client._get.assert_called_with(
        "SignoutSessions", params={"ids": "ids", "ruk": "ruk"}
    )
    assert response == success_response


def test_validate_captcha(client):
    client._get.return_value = success_response
    response = client.Authentication.ValidateCaptcha(
        "code",
        "ruk",
    )
    client._get.assert_called_with(
        "ValidateCaptcha", params={"code": "code", "ruk": "ruk"}
    )
    assert response == success_response


def test_verify_2_fa_code(client):
    client._get.return_value = success_response
    response = client.Authentication.Verify2FACode(
        "code",
        "ruk",
    )
    client._get.assert_called_with(
        "Verify2FACode", params={"code": "code", "ruk": "ruk"}
    )
    assert response == success_response
