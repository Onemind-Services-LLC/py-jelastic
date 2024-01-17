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
    response = client.Admin.ChangePhoneNumber("login", "1234")
    client._get.assert_called_once_with(
        "ChangePhoneNumber", params={"login": "login", "number": "1234"}
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
        "test@email.com", "password", "name", True, "welcome", True, True, True, 11
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
        },
    )
    assert response == success_response


def test_delete_app(client):
    client._get.return_value = success_response
    response = client.Admin.DeleteApp("app")
    client._get.assert_called_once_with("DeleteApp", params={"targetAppid": "app"})
    assert response == success_response


def test_disable_2fa(client):
    client._get.return_value = success_response
    response = client.Admin.Disable2FA("login", "password")
    client._get.assert_called_once_with(
        "Disable2FA", params={"login": "login", "password": "password"}
    )
    assert response == success_response


def test_disable_mandatory2fa(client):
    client._get.return_value = success_response
    response = client.Admin.DisableMandatory2FA()
    client._get.assert_called_once_with("DisableMandatory2FA", params={})
    assert response == success_response


def test_enable_mandatory_2fa(client):
    client._get.return_value = success_response
    response = client.Admin.EnableMandatory2FA(112, True, "user")
    client._get.assert_called_once_with(
        "EnableMandatory2FA",
        params={"period": 112, "notify": True, "trustedUsers": "user"},
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
    response = client.Admin.GetUserSSHKeys("login", True)
    client._get.assert_called_once_with(
        "GetUserSSHKeys", params={"login": "login", "isPrivate": True}
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
    response = client.Admin.InvalidateAuthKey("rid", "type", "key")
    client._get.assert_called_once_with(
        "InvalidateAuthKey",
        params={"referenceId": "rid", "referenceType": "type", "authKey": "key"},
    )
    assert response == success_response


def test_recover_password(client):
    client._get.return_value = success_response
    response = client.Admin.RecoverPassword("test@email.com", "password", True, "lang")
    client._get.assert_called_once_with(
        "RecoverPassword",
        params={
            "email": "test@email.com",
            "password": "password",
            "skipSendEmail": True,
            "lang": "lang",
        },
    )
    assert response == success_response


def test_remove_personal_data(client):
    client._get.return_value = success_response
    response = client.Admin.RemovePersonalData("login", True)
    client._get.assert_called_once_with(
        "RemovePersonalData", params={"login": "login", "isAnonymize": True}
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
    response = client.Admin.SetPassword("login", "password", True)
    client._get.assert_called_once_with(
        "SetPassword",
        params={"login": "login", "password": "password", "invalidateSessions": True},
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
