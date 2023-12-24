from . import *


def test_change_session(client):
    client._get.return_value = success_response
    response = client.Authentication.ChangeSession()
    client._get.assert_called_with("ChangeSession", params={})

    assert response == success_response


def test_check_auth_key(client):
    client._get.return_value = success_response
    response = client.Authentication.CheckAuthKey("auth_key")
    client._get.assert_called_with("CheckAuthKey", params={"authKey": "auth_key"})
    assert response == success_response


def test_check_password(client):
    client._get.return_value = success_response
    response = client.Authentication.CheckPassword("password")
    client._get.assert_called_with("CheckPassword", params={"password": "password"})
    assert response == success_response


def test_check_sign(client):
    client._get.return_value = success_response
    response = client.Authentication.CheckSign()
    client._get.assert_called_with("CheckSign", params={})
    assert response == success_response


def test_check_user(client):
    client._get.return_value = success_response
    response = client.Authentication.CheckUser("login")
    client._get.assert_called_with("CheckUser", params={"login": "login"})
    assert response == success_response


def test_clear_api_list_data(client):
    client._get.return_value = success_response
    response = client.Authentication.ClearApiListData()
    client._get.assert_called_with("ClearApiListData", params={})
    assert response == success_response


def test_clear_api_list_data_inner(client):
    client._get.return_value = success_response
    response = client.Authentication.ClearApiListDataInner()
    client._get.assert_called_with("ClearApiListDataInner", params={})
    assert response == success_response


def test_create_token(client):
    client._get.return_value = success_response
    response = client.Authentication.CreateToken(
        "description",
        ["password1", "password2"],
        ["token_template1", "token_template2"],
        ["api_list1", "api_list2"],
        [CURRENT_DATETIME, CURRENT_DATETIME],
    )
    client._get.assert_called_with(
        "CreateToken",
        params={
            "description": "description",
            "password": ["password1", "password2"],
            "tokenTemplate": ["token_template1", "token_template2"],
            "apiList": ["api_list1", "api_list2"],
            "expiresAt": [CURRENT_DATETIME, CURRENT_DATETIME],
        },
        delimiter=",",
    )
    assert response == success_response


def test_create_token_inner(client):
    client._get.return_value = success_response
    response = client.Authentication.CreateTokenInner(
        "login",
        "description",
        ["token_template1", "token_template2"],
        ["api_list1", "api_list2"],
        [CURRENT_DATETIME, CURRENT_DATETIME],
        [True, True],
        [True, True],
    )
    client._get.assert_called_with(
        "CreateTokenInner",
        params={
            "login": "login",
            "description": "description",
            "tokenTemplate": ["token_template1", "token_template2"],
            "apiList": ["api_list1", "api_list2"],
            "expiresAt": [CURRENT_DATETIME, CURRENT_DATETIME],
            "isProtected": [True, True],
            "skipNotification": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_token(client):
    client._get.return_value = success_response
    response = client.Authentication.DeleteTokens("ids", ["password1", "password2"])
    client._get.assert_called_with(
        "DeleteTokens",
        params={
            "ids": "ids",
            "password": ["password1", "password2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_token(client):
    client._get.return_value = success_response
    response = client.Authentication.EditToken(
        1,
        ["password1", "password2"],
        ["description1", "description2"],
        ["token_template1", "token_template2"],
        ["api_list1", "api_list2"],
        [CURRENT_DATETIME, CURRENT_DATETIME],
    )
    client._get.assert_called_with(
        "EditToken",
        params={
            "id": 1,
            "password": ["password1", "password2"],
            "description": ["description1", "description2"],
            "tokenTemplate": ["token_template1", "token_template2"],
            "apiList": ["api_list1", "api_list2"],
            "expiresAt": [CURRENT_DATETIME, CURRENT_DATETIME],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_auth_key(client):
    client._get.return_value = success_response
    response = client.Authentication.GetAuthKey("auth_key")
    client._get.assert_called_with("GetAuthKey", params={"authKey": "auth_key"})
    assert response == success_response


def test_get_description_by_token(client):
    client._get.return_value = success_response
    response = client.Authentication.GetDescriptionByToken("checksum")
    client._get.assert_called_with(
        "GetDescriptionByToken", params={"checksum": "checksum"}
    )
    assert response == success_response


def test_get_device_signature(client):
    client._get.return_value = success_response
    response = client.Authentication.GetDeviceSignature()
    client._get.assert_called_with("GetDeviceSignature", params={})
    assert response == success_response


def test_get_policy_methods(client):
    client._get.return_value = success_response
    response = client.Authentication.GetPolicyMethods(["unique_name1", "unique_name2"])
    client._get.assert_called_with(
        "GetPolicyMethods",
        params={"uniqueName": ["unique_name1", "unique_name2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_session(client):
    client._get.return_value = success_response
    response = client.Authentication.GetSessions()
    client._get.assert_called_with("GetSessions", params={})
    assert response == success_response


def test_get_sign_in_attempts(client):
    client._get.return_value = success_response
    response = client.Authentication.GetSigninAttempts(["search1", "search2"])
    client._get.assert_called_with(
        "GetSigninAttempts",
        params={"search": ["search1", "search2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_token_api_list(client):
    client._get.return_value = success_response
    response = client.Authentication.GetTokenApiList(
        ["show_private1", "show_private2"], ["sort_param1", "sort_param2"]
    )
    client._get.assert_called_with(
        "GetTokenApiList",
        params={
            "showPrivate": ["show_private1", "show_private2"],
            "sortParam": ["sort_param1", "sort_param2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_token_templates(client):
    client._get.return_value = success_response
    response = client.Authentication.GetTokenTemplates()
    client._get.assert_called_with("GetTokenTemplates", params={})
    assert response == success_response


def test_get_tokens(client):
    client._get.return_value = success_response
    response = client.Authentication.GetTokens(["ids1", "ids2"])
    client._get.assert_called_with(
        "GetTokens",
        params={"ids": ["ids1", "ids2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_uid_by_token(client):
    client._get.return_value = success_response
    response = client.Authentication.GetUidByToken("checksum")
    client._get.assert_called_with("GetUidByToken", params={"checksum": "checksum"})
    assert response == success_response


def test_regenerate_token(client):
    client._get.return_value = success_response
    response = client.Authentication.RegenerateToken("ids", ["password1", "password2"])
    client._get.assert_called_with(
        "RegenerateToken",
        params={
            "ids": "ids",
            "password": ["password1", "password2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_reset_sign_in_attempts(client):
    client._get.return_value = success_response
    response = client.Authentication.ResetSigninAttempts(
        ["login1", "login2"], ["ip_address1", "ip_address2"]
    )
    client._get.assert_called_with(
        "ResetSigninAttempts",
        params={
            "login": ["login1", "login2"],
            "ipAddress": ["ip_address1", "ip_address2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_sign_in(client):
    client._get.return_value = success_response
    response = client.Authentication.Signin("login", "password")
    client._get.assert_called_with(
        "Signin", params={"login": "login", "password": "password"}
    )
    assert response == success_response


def test_sign_in_by_auth_key(client):
    client._get.return_value = success_response
    response = client.Authentication.SigninByAuthKey("auth_key")
    client._get.assert_called_with("SigninByAuthKey", params={"authKey": "auth_key"})
    assert response == success_response


def test_sign_in_by_token(client):
    client._get.return_value = success_response
    response = client.Authentication.SigninByToken("token", "user_headers")
    client._get.assert_called_with(
        "SigninByToken", params={"token": "token", "userHeaders": "user_headers"}
    )
    assert response == success_response


def test_sign_out(client):
    client._get.return_value = success_response
    response = client.Authentication.Signout()
    client._get.assert_called_with("Signout", params={})
    assert response == success_response


def test_sign_out_sessions(client):
    client._get.return_value = success_response
    response = client.Authentication.SignoutSessions("ids")
    client._get.assert_called_with("SignoutSessions", params={"ids": "ids"})
    assert response == success_response


def test_validate_captcha(client):
    client._get.return_value = success_response
    response = client.Authentication.ValidateCaptcha("code")
    client._get.assert_called_with("ValidateCaptcha", params={"code": "code"})
    assert response == success_response


def test_verify_2_fa_code(client):
    client._get.return_value = success_response
    response = client.Authentication.Verify2FACode("code")
    client._get.assert_called_with("Verify2FACode", params={"code": "code"})
    assert response == success_response
