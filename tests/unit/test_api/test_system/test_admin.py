from . import *


def test_add_trusted_user(client):
    client._get.return_value = success_response
    response = client.Admin.AddTrustedUser(
        "login",
        "ruk",
    )
    client._get.assert_called_once_with(
        "AddTrustedUser",
        params={"login": "login", "ruk": "ruk"},
    )
    assert response == success_response


def test_change_email(client):
    client._get.return_value = success_response
    response = client.Admin.ChangeEmail(
        "login",
        "test@email.com",
        "ruk",
    )
    client._get.assert_called_once_with(
        "ChangeEmail",
        params={"login": "login", "email": "test@email.com", "ruk": "ruk"},
    )
    assert response == success_response


def test_change_phone_number(client):
    client._get.return_value = success_response
    response = client.Admin.ChangePhoneNumber(
        "login",
        "1234",
        "ruk",
    )
    client._get.assert_called_once_with(
        "ChangePhoneNumber", params={"login": "login", "number": "1234", "ruk": "ruk"}
    )
    assert response == success_response


def test_check_activation_key(client):
    client._get.return_value = success_response
    response = client.Admin.CheckActivationKey(
        "key",
        "ruk",
    )
    client._get.assert_called_once_with(
        "CheckActivationKey", params={"key": "key", "ruk": "ruk"}
    )
    assert response == success_response


def test_create_account(client):
    client._get.return_value = success_response
    response = client.Admin.CreateAccount(
        "test@email.com",
        "password",
        "name",
        True,
        "welcome",
        True,
        True,
        True,
        11,
        "ruk",
    )
    client._get.assert_called_once_with(
        "CreateAccount",
        params={
            "email": "test@email.com",
            "password": "password",
            "name": "name",
            "checkEmail": True,
            "welcome": "welcome",
            "skipSendEmail": True,
            "autoActive": True,
            "sendCredentials": True,
            "resellerId": 11,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_delete_app(client):
    client._get.return_value = success_response
    response = client.Admin.DeleteApp(
        "app",
        "ruk",
    )
    client._get.assert_called_once_with(
        "DeleteApp", params={"targetAppid": "app", "ruk": "ruk"}
    )
    assert response == success_response


def test_disable_2fa(client):
    client._get.return_value = success_response
    response = client.Admin.Disable2FA(
        "login",
        "password",
        "ruk",
    )
    client._get.assert_called_once_with(
        "Disable2FA", params={"login": "login", "password": "password", "ruk": "ruk"}
    )
    assert response == success_response


def test_disable_mandatory2fa(client):
    client._get.return_value = success_response
    response = client.Admin.DisableMandatory2FA(
        "ruk",
    )
    client._get.assert_called_once_with("DisableMandatory2FA", params={"ruk": "ruk"})
    assert response == success_response


def test_enable_mandatory_2fa(client):
    client._get.return_value = success_response
    response = client.Admin.EnableMandatory2FA(
        112,
        True,
        "user",
        "ruk",
    )
    client._get.assert_called_once_with(
        "EnableMandatory2FA",
        params={"period": 112, "notify": True, "trustedUsers": "user", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_activation_key(client):
    client._get.return_value = success_response
    response = client.Admin.GetActivationKey(
        "test@email.com",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetActivationKey", params={"email": "test@email.com", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_admin_users_info(client):
    client._get.return_value = success_response
    response = client.Admin.GetAdminUsersInfo(
        "ruk",
    )
    client._get.assert_called_once_with("GetAdminUsersInfo", params={"ruk": "ruk"})
    assert response == success_response


def test_get_app(client):
    client._get.return_value = success_response
    response = client.Admin.GetApp(
        "app",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetApp",
        params={"targetAppid": "app", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_app_permission(client):
    client._get.return_value = success_response
    response = client.Admin.GetAppPermission(
        "app",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetAppPermission",
        params={"targetAppid": "app", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_user_ids(client):
    client._get.return_value = success_response
    response = client.Admin.GetUserIDs(
        "test@email.com",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetUserIDs",
        params={"email": "test@email.com", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_user_info(client):
    client._get.return_value = success_response
    response = client.Admin.GetUserInfo(
        "login",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetUserInfo",
        params={"login": "login", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_user_ssh_key(client):
    client._get.return_value = success_response
    response = client.Admin.GetUserSSHKeys(
        "login",
        True,
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetUserSSHKeys", params={"login": "login", "isPrivate": True, "ruk": "ruk"}
    )
    assert response == success_response


def test_get_users_by_status(client):
    client._get.return_value = success_response
    response = client.Admin.GetUsersByStatus(
        "status",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetUsersByStatus",
        params={"status": "status", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_users_by_uids(client):
    client._get.return_value = success_response
    response = client.Admin.GetUsersByUIDs(
        "uid",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetUsersByUIDs",
        params={"uid": "uid", "ruk": "ruk"},
    )
    assert response == success_response


def test_invalid_auth_key(client):
    client._get.return_value = success_response
    response = client.Admin.InvalidateAuthKey("rid", "type", "key", "ruk")
    client._get.assert_called_once_with(
        "InvalidateAuthKey",
        params={
            "referenceId": "rid",
            "referenceType": "type",
            "authKey": "key",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_recover_password(client):
    client._get.return_value = success_response
    response = client.Admin.RecoverPassword(
        "test@email.com",
        "password",
        True,
        "lang",
        "ruk",
    )
    client._get.assert_called_once_with(
        "RecoverPassword",
        params={
            "email": "test@email.com",
            "password": "password",
            "skipSendEmail": True,
            "lang": "lang",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_remove_personal_data(client):
    client._get.return_value = success_response
    response = client.Admin.RemovePersonalData(
        "login",
        True,
        "ruk",
    )
    client._get.assert_called_once_with(
        "RemovePersonalData",
        params={"login": "login", "isAnonymize": True, "ruk": "ruk"},
    )
    assert response == success_response


def test_remove_trusted_user(client):
    client._get.return_value = success_response
    response = client.Admin.RemoveTrustedUser(
        "login",
        "ruk",
    )
    client._get.assert_called_once_with(
        "RemoveTrustedUser", params={"login": "login", "ruk": "ruk"}
    )
    assert response == success_response


def test_reset_persistence_password(client):
    client._get.return_value = success_response
    response = client.Admin.ResetPersistencePasswords(
        "ruk",
    )
    client._get.assert_called_once_with(
        "ResetPersistencePasswords", params={"ruk": "ruk"}
    )
    assert response == success_response


def test_set_password(client):
    client._get.return_value = success_response
    response = client.Admin.SetPassword(
        "login",
        "password",
        True,
        "ruk",
    )
    client._get.assert_called_once_with(
        "SetPassword",
        params={
            "login": "login",
            "password": "password",
            "invalidateSessions": True,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_set_trusted_users(client):
    client._get.return_value = success_response
    response = client.Admin.SetTrustedUsers(
        "login",
        "ruk",
    )
    client._get.assert_called_once_with(
        "SetTrustedUsers",
        params={"login": "login", "ruk": "ruk"},
    )
    assert response == success_response


def test_set_user_status(client):
    client._get.return_value = success_response
    response = client.Admin.SetUserStatus(
        "login",
        "status",
        "ruk",
    )
    client._get.assert_called_once_with(
        "SetUserStatus",
        params={"login": "login", "status": "status", "ruk": "ruk"},
    )
    assert response == success_response


def test_signin_as_client(client):
    client._get.return_value = success_response
    response = client.Admin.SigninAsClient(
        "login",
        "ruk",
    )
    client._get.assert_called_once_with(
        "SigninAsClient",
        params={"login": "login", "ruk": "ruk"},
    )
    assert response == success_response
