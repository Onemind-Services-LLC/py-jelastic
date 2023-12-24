from . import *


def test_add_account(client):
    client._get.return_value = success_response
    response = client.Account.AddAccount(
        "email", "password", ["name1", "name2"], [True, True], [1, 1]
    )
    client._get.assert_called_with(
        "AddAccount",
        params={
            "email": "email",
            "password": "password",
            "name": ["name1", "name2"],
            "notify": [True, True],
            "resellerId": [1, 1],
        },
        delimiter=",",
    )

    assert response == success_response


def test_add_ssh_key(client):
    client._get.return_value = success_response
    response = client.Account.AddSSHKey(
        "title",
        "ssh_key",
        True,
    )
    client._get.assert_called_with(
        "AddSSHKey",
        params={
            "title": "title",
            "sshKey": "ssh_key",
            "isPrivate": True,
        },
    )
    assert response == success_response


def test_change_email(client):
    client._get.return_value = success_response
    response = client.Account.ChangeEmail("email", ["redirect_url1", "redirect_url2"])
    client._get.assert_called_with(
        "ChangeEmail",
        params={
            "email": "email",
            "redirectUrl": ["redirect_url1", "redirect_url2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_change_name(client):
    client._get.return_value = success_response
    response = client.Account.ChangeName("name")
    client._get.assert_called_with(
        "ChangeName",
        params={
            "name": "name",
        },
    )
    assert response == success_response


def test_change_password(client):
    client._get.return_value = success_response
    response = client.Account.ChangePassword(
        "old_password", "new_password", ["invalidate_sessions1", "invalidate_sessions2"]
    )
    client._get.assert_called_with(
        "ChangePassword",
        params={
            "oldPassword": "old_password",
            "newPassword": "new_password",
            "invalidateSessions": ["invalidate_sessions1", "invalidate_sessions2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_check_user(client):
    client._get.return_value = success_response
    response = client.Account.CheckUser("login")
    client._get.assert_called_with(
        "CheckUser",
        params={
            "login": "login",
        },
    )
    assert response == success_response


def test_delete_ssh_key(client):
    client._get.return_value = success_response
    response = client.Account.DeleteSSHKey(1)
    client._get.assert_called_with(
        "DeleteSSHKey",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_disable_2_fa(client):
    client._get.return_value = success_response
    response = client.Account.Disable2FA(["password1", "password2"])
    client._get.assert_called_with(
        "Disable2FA",
        params={"password": ["password1", "password2"]},
        delimiter=",",
    )
    assert response == success_response


def test_enable_2_fa(client):
    client._get.return_value = success_response
    response = client.Account.Enable2FA("code", ["password1", "password2"])
    client._get.assert_called_with(
        "Enable2FA",
        params={"code": "code", "password": ["password1", "password2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_2_fa_backup_codes(client):
    client._get.return_value = success_response
    response = client.Account.Get2FABackupCodes(["password1", "password2"])
    client._get.assert_called_with(
        "Get2FABackupCodes",
        params={"password": ["password1", "password2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_2_fa_config(client):
    client._get.return_value = success_response
    response = client.Account.Get2FAConfig(["password1", "password2"])
    client._get.assert_called_with(
        "Get2FAConfig",
        params={"password": ["password1", "password2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_ssh_keys(client):
    client._get.return_value = success_response
    response = client.Account.GetSSHKeys(["is_private1", "is_private2"])
    client._get.assert_called_with(
        "GetSSHKeys",
        params={"isPrivate": ["is_private1", "is_private2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_user_info(client):
    client._get.return_value = success_response
    response = client.Account.GetUserInfo()
    client._get.assert_called_with(
        "GetUserInfo",
        params={},
    )
    assert response == success_response


def test_check_user_info_inner(client):
    client._get.return_value = success_response
    response = client.Account.GetUserInfoInner("login")
    client._get.assert_called_with(
        "GetUserInfoInner",
        params={
            "login": "login",
        },
    )
    assert response == success_response


def test_recover_password(client):
    client._get.return_value = success_response
    response = client.Account.RecoverPassword("email", ["lang1", "lang2"])
    client._get.assert_called_with(
        "RecoverPassword",
        params={"email": "email", "lang": ["lang1", "lang2"]},
        delimiter=",",
    )
    assert response == success_response


def test_regenerate_2_fa_backup_codes(client):
    client._get.return_value = success_response
    response = client.Account.Regenerate2FABackupCodes(["password1", "password2"])
    client._get.assert_called_with(
        "Regenerate2FABackupCodes",
        params={"password": ["password1", "password2"]},
        delimiter=",",
    )
    assert response == success_response


def test_set_as_tenant_host(client):
    client._get.return_value = success_response
    response = client.Account.SetAsTenantHost(1, True)
    client._get.assert_called_with(
        "SetAsTenantHost",
        params={
            "uid": 1,
            "forceChange": True,
        },
    )
    assert response == success_response


def test_set_password(client):
    client._get.return_value = success_response
    response = client.Account.SetPassword("auth_key", [True, True])
    client._get.assert_called_with(
        "SetPassword",
        params={
            "authKey": "auth_key",
            "invalidateSessions": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_user_data(client):
    client._get.return_value = success_response
    response = client.Account.SetUserData("data")
    client._get.assert_called_with(
        "SetUserData",
        params={
            "data": "data",
        },
    )
    assert response == success_response
