from . import *


def test_add_trusted_user(client):
    client._get.return_value = success_response
    response = client.Admin.AddTrustedUser("login")
    client._get.assert_called_once_with(
        "AddTrustedUser",
        params={
            "login": "login",
        },
    )
    assert response == success_response


def test_change_email(client):
    client._get.return_value = success_response
    response = client.Admin.ChangeEmail("login", "test@email.com")
    client._get.assert_called_once_with(
        "ChangeEmail",
        params={
            "login": "login",
            "email": "test@email.com",
        },
    )
    assert response == success_response


def test_change_phone_number(client):
    client._get.return_value = success_response
    response = client.Admin.ChangePhoneNumber("login", ["1234", "2345", "3456"])
    client._get.assert_called_once_with(
        "ChangePhoneNumber",
        params={
            "login": "login",
            "number": ["1234", "2345", "3456"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_check_activation_key(client):
    client._get.return_value = success_response
    response = client.Admin.CheckActivationKey("key")
    client._get.assert_called_once_with("CheckActivationKey", params={"key": "key"})
    assert response == success_response


def test_create_account(client):
    client._get.return_value = success_response
    response = client.Admin.CreateAccount(
        "test@email.com",
        "password",
        ["f name", "m name", "l name"],
        [True, True, True],
        ["welcome message 1", "welcome message 2", "welcome message 3"],
        [True, True, True],
        [True, True, True],
        [True, True, True],
        [1, 2, 3],
    )
    client._get.assert_called_once_with(
        "CreateAccount",
        params={
            "email": "test@email.com",
            "password": "password",
            "name": ["f name", "m name", "l name"],
            "checkEmail": [True, True, True],
            "welcome": ["welcome message 1", "welcome message 2", "welcome message 3"],
            "skipSendEmail": [True, True, True],
            "autoActive": [True, True, True],
            "sendCredentials": [True, True, True],
            "resellerId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_app(client):
    client._get.return_value = success_response
    response = client.Admin.DeleteApp("app")
    client._get.assert_called_once_with("DeleteApp", params={"targetAppid": "app"})
    assert response == success_response


def test_disable_2fa(client):
    client._get.return_value = success_response
    response = client.Admin.Disable2FA(
        "login",
        ["password 1", "password 2", "password 3"],
    )
    client._get.assert_called_once_with(
        "Disable2FA",
        params={
            "login": "login",
            "password": ["password 1", "password 2", "password 3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_disable_mandatory2fa(client):
    client._get.return_value = success_response
    response = client.Admin.DisableMandatory2FA()
    client._get.assert_called_once_with(
        "DisableMandatory2FA",
        params={},
        delimiter=",",
    )
    assert response == success_response


def test_enable_mandatory_2fa(client):
    client._get.return_value = success_response
    response = client.Admin.EnableMandatory2FA(
        [1, 2, 3],
        [True, False, True],
        ["user 1", "user 2", "user 3"],
    )
    client._get.assert_called_once_with(
        "EnableMandatory2FA",
        params={
            "period": [1, 2, 3],
            "notify": [True, False, True],
            "trustedUsers": ["user 1", "user 2", "user 3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_activation_key(client):
    client._get.return_value = success_response
    response = client.Admin.GetActivationKey("test@email.com")
    client._get.assert_called_once_with(
        "GetActivationKey", params={"email": "test@email.com"}
    )
    assert response == success_response


def test_get_admin_users_info(client):
    client._get.return_value = success_response
    response = client.Admin.GetAdminUsersInfo()
    client._get.assert_called_once_with("GetAdminUsersInfo", params={})
    assert response == success_response


def test_get_app(client):
    client._get.return_value = success_response
    response = client.Admin.GetApp("app")
    client._get.assert_called_once_with(
        "GetApp",
        params={
            "targetAppid": "app",
        },
    )
    assert response == success_response


def test_get_app_permission(client):
    client._get.return_value = success_response
    response = client.Admin.GetAppPermission("app")
    client._get.assert_called_once_with(
        "GetAppPermission",
        params={
            "targetAppid": "app",
        },
    )
    assert response == success_response


def test_get_user_ids(client):
    client._get.return_value = success_response
    response = client.Admin.GetUserIDs("test@email.com")
    client._get.assert_called_once_with(
        "GetUserIDs",
        params={
            "email": "test@email.com",
        },
    )
    assert response == success_response


def test_get_user_info(client):
    client._get.return_value = success_response
    response = client.Admin.GetUserInfo("login")
    client._get.assert_called_once_with(
        "GetUserInfo",
        params={
            "login": "login",
        },
    )
    assert response == success_response


def test_get_user_ssh_key(client):
    client._get.return_value = success_response
    response = client.Admin.GetUserSSHKeys(
        "login",
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "GetUserSSHKeys",
        params={
            "login": "login",
            "isPrivate": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_users_by_status(client):
    client._get.return_value = success_response
    response = client.Admin.GetUsersByStatus("status")
    client._get.assert_called_once_with(
        "GetUsersByStatus",
        params={
            "status": "status",
        },
    )
    assert response == success_response


def test_get_users_by_uids(client):
    client._get.return_value = success_response
    response = client.Admin.GetUsersByUIDs("uid")
    client._get.assert_called_once_with(
        "GetUsersByUIDs",
        params={
            "uid": "uid",
        },
    )
    assert response == success_response


def test_invalid_auth_key(client):
    client._get.return_value = success_response
    response = client.Admin.InvalidateAuthKey(
        ["rid1", "rid2", "rid3"],
        ["type1", "type2", "type3"],
        ["key1", "key2", "key3"],
    )
    client._get.assert_called_once_with(
        "InvalidateAuthKey",
        params={
            "referenceId": ["rid1", "rid2", "rid3"],
            "referenceType": ["type1", "type2", "type3"],
            "authKey": ["key1", "key2", "key3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_recover_password(client):
    client._get.return_value = success_response
    response = client.Admin.RecoverPassword(
        "test@email.com",
        ["password1", "password2", "password3"],
        [True, False, True],
        ["language 1", "language 2", "language 3"],
    )
    client._get.assert_called_once_with(
        "RecoverPassword",
        params={
            "email": "test@email.com",
            "password": ["password1", "password2", "password3"],
            "skipSendEmail": [True, False, True],
            "lang": ["language 1", "language 2", "language 3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_personal_data(client):
    client._get.return_value = success_response
    response = client.Admin.RemovePersonalData(
        "login",
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "RemovePersonalData",
        params={
            "login": "login",
            "isAnonymize": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_trusted_user(client):
    client._get.return_value = success_response
    response = client.Admin.RemoveTrustedUser("login")
    client._get.assert_called_once_with("RemoveTrustedUser", params={"login": "login"})
    assert response == success_response


def test_reset_persistence_password(client):
    client._get.return_value = success_response
    response = client.Admin.ResetPersistencePasswords()
    client._get.assert_called_once_with("ResetPersistencePasswords", params={})
    assert response == success_response


def test_set_password(client):
    client._get.return_value = success_response
    response = client.Admin.SetPassword(
        "login",
        "password",
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "SetPassword",
        params={
            "login": "login",
            "password": "password",
            "invalidateSessions": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_trusted_users(client):
    client._get.return_value = success_response
    response = client.Admin.SetTrustedUsers("login")
    client._get.assert_called_once_with(
        "SetTrustedUsers",
        params={
            "login": "login",
        },
    )
    assert response == success_response


def test_set_user_status(client):
    client._get.return_value = success_response
    response = client.Admin.SetUserStatus("login", "status")
    client._get.assert_called_once_with(
        "SetUserStatus",
        params={
            "login": "login",
            "status": "status",
        },
    )
    assert response == success_response


def test_signin_as_client(client):
    client._get.return_value = success_response
    response = client.Admin.SigninAsClient("login")
    client._get.assert_called_once_with(
        "SigninAsClient",
        params={
            "login": "login",
        },
    )
    assert response == success_response
