from . import *


def test_activate(client):
    client._get.return_value = success_response
    response = client.Registration.Activate(
        "key", ["password1", "password2"], [True, True], ["code1", "code2"], [1, 1]
    )
    client._get.assert_called_with(
        "Activate",
        params={
            "key": "key",
            "password": ["password1", "password2"],
            "skipSendEmail": [True, True],
            "code": ["code1", "code2"],
            "resellerId": [1, 1],
        },
        delimiter=",",
    )

    assert response == success_response


def test_check_email_exist(client):
    client._get.return_value = success_response
    response = client.Registration.CheckEmailExist("email")
    client._get.assert_called_with("CheckEmailExist", params={"email": "email"})

    assert response == success_response


def test_check_email_registration(client):
    client._get.return_value = success_response
    response = client.Registration.CheckEmailRegistration("email")
    client._get.assert_called_with("CheckEmailRegistration", params={"email": "email"})

    assert response == success_response


def test_check_password(client):
    client._get.return_value = success_response
    response = client.Registration.CheckPassword("password")
    client._get.assert_called_with("CheckPassword", params={"password": "password"})

    assert response == success_response


def test_clear_sms_list_data(client):
    client._get.return_value = success_response
    response = client.Registration.ClearSmsListData("email")
    client._get.assert_called_with("ClearSmsListData", params={"email": "email"})
    assert response == success_response


def test_create_account(client):
    client._get.return_value = success_response
    response = client.Registration.CreateAccount(
        "email",
        "password",
        ["name1", "name2"],
        [True, True],
        ["welcome1", "welcome2"],
        [True, True],
        [1, 1],
    )
    client._get.assert_called_with(
        "CreateAccount",
        params={
            "email": "email",
            "password": "password",
            "name": ["name1", "name2"],
            "checkEmail": [True, True],
            "welcome": ["welcome1", "welcome2"],
            "skipSendEmail": [True, True],
            "resellerId": [1, 1],
        },
        delimiter=",",
    )

    assert response == success_response


def test_create_auth_key(client):
    client._get.return_value = success_response
    response = client.Registration.CreateAuthKey(
        "login",
        "solution",
        ["auth_type1", "auth_type2"],
        [CURRENT_DATETIME, CURRENT_DATETIME],
        ["type1", "type2"],
    )
    client._get.assert_called_with(
        "CreateAuthKey",
        params={
            "login": "login",
            "solution": "solution",
            "authType": ["auth_type1", "auth_type2"],
            "expiresAt": [CURRENT_DATETIME, CURRENT_DATETIME],
            "type": ["type1", "type2"],
        },
        delimiter=",",
    )

    assert response == success_response


def test_create_confirm_link_user_key(client):
    client._get.return_value = success_response
    response = client.Registration.CreateConfirmLinkUserKey(
        "email",
        "role",
        ["target_app_id1", "target_app_id2"],
        ["application_right1", "application_right2"],
    )
    client._get.assert_called_with(
        "CreateConfirmLinkUserKey",
        params={
            "email": "email",
            "role": "role",
            "targetAppid": ["target_app_id1", "target_app_id2"],
            "applicationRight": ["application_right1", "application_right2"],
        },
        delimiter=",",
    )

    assert response == success_response


def test_generate_password(client):
    client._get.return_value = success_response
    response = client.Registration.GeneratePassword([1, 1])
    client._get.assert_called_with("GeneratePassword", params={"length": [1, 1]})
    assert response == success_response


def test_get_sms_list_data(client):
    client._get.return_value = success_response
    response = client.Registration.GetSmsListData()
    client._get.assert_called_with("GetSmsListData", params={})
    assert response == success_response


def test_resend_invitation(client):
    client._get.return_value = success_response
    response = client.Registration.ResendInvitation("welcome")
    client._get.assert_called_with("ResendInvitation", params={"welcome": "welcome"})
    assert response == success_response


def test_send_sms(client):
    client._get.return_value = success_response
    response = client.Registration.SendSms(
        "activation_key", "email", "phone", ["lang1", "lang2"]
    )
    client._get.assert_called_with(
        "SendSms",
        params={
            "activationKey ": "activation_key",
            "email ": "email",
            "phone ": "phone",
            "lang ": ["lang1", "lang2"],
        },
    )
    assert response == success_response
