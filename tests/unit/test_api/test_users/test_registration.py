from . import *


def test_activate(client):
    client._get.return_value = success_response
    response = client.Registration.Activate(
        "key",
        "password",
        True,
        "code",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "Activate",
        params={
            "key": "key",
            "password": "password",
            "skipSendEmail": True,
            "code": "code",
            "resellerId": 1,
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_check_email_exist(client):
    client._get.return_value = success_response
    response = client.Registration.CheckEmailExist(
        "email",
        "ruk",
    )
    client._get.assert_called_with(
        "CheckEmailExist", params={"email": "email", "ruk": "ruk"}
    )

    assert response == success_response


def test_check_email_registration(client):
    client._get.return_value = success_response
    response = client.Registration.CheckEmailRegistration(
        "email",
        "ruk",
    )
    client._get.assert_called_with(
        "CheckEmailRegistration", params={"email": "email", "ruk": "ruk"}
    )

    assert response == success_response


def test_check_password(client):
    client._get.return_value = success_response
    response = client.Registration.CheckPassword(
        "password",
        "ruk",
    )
    client._get.assert_called_with(
        "CheckPassword", params={"password": "password", "ruk": "ruk"}
    )

    assert response == success_response


def test_clear_sms_list_data(client):
    client._get.return_value = success_response
    response = client.Registration.ClearSmsListData(
        "email",
        "ruk",
    )
    client._get.assert_called_with(
        "ClearSmsListData", params={"email": "email", "ruk": "ruk"}
    )
    assert response == success_response


def test_create_account(client):
    client._get.return_value = success_response
    response = client.Registration.CreateAccount(
        "email",
        "password",
        "name",
        True,
        "welcome",
        True,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "CreateAccount",
        params={
            "email": "email",
            "password": "password",
            "name": "name",
            "checkEmail": True,
            "welcome": "welcome",
            "skipSendEmail": True,
            "resellerId": 1,
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_create_auth_key(client):
    client._get.return_value = success_response
    response = client.Registration.CreateAuthKey(
        "login",
        "solution",
        "authType",
        CURRENT_DATETIME,
        "type",
        "ruk",
    )
    client._get.assert_called_with(
        "CreateAuthKey",
        params={
            "login": "login",
            "solution": "solution",
            "authType": "authType",
            "expiresAt": CURRENT_DATETIME,
            "type": "type",
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )

    assert response == success_response


def test_create_confirm_link_user_key(client):
    client._get.return_value = success_response
    response = client.Registration.CreateConfirmLinkUserKey(
        "email",
        "role",
        "targetAppid",
        "applicationRight",
        "ruk",
    )
    client._get.assert_called_with(
        "CreateConfirmLinkUserKey",
        params={
            "email": "email",
            "role": "role",
            "targetAppid": "targetAppid",
            "applicationRight": "applicationRight",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_generate_password(client):
    client._get.return_value = success_response
    response = client.Registration.GeneratePassword(
        11111,
        "ruk",
    )
    client._get.assert_called_with(
        "GeneratePassword", params={"length": 11111, "ruk": "ruk"}
    )
    assert response == success_response


def test_get_sms_list_data(client):
    client._get.return_value = success_response
    response = client.Registration.GetSmsListData(
        "ruk",
    )
    client._get.assert_called_with("GetSmsListData", params={"ruk": "ruk"})
    assert response == success_response


def test_resend_invitation(client):
    client._get.return_value = success_response
    response = client.Registration.ResendInvitation(
        "welcome",
        "ruk",
    )
    client._get.assert_called_with(
        "ResendInvitation", params={"welcome": "welcome", "ruk": "ruk"}
    )
    assert response == success_response


def test_send_sms(client):
    client._get.return_value = success_response
    response = client.Registration.SendSms(
        "activation_key",
        "email",
        "phone",
        "lang",
        "ruk",
    )
    client._get.assert_called_with(
        "SendSms",
        params={
            "activationKey ": "activation_key",
            "email": "email",
            "phone": "phone",
            "lang": "lang",
            "ruk": "ruk",
        },
    )
    assert response == success_response
