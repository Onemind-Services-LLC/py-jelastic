from . import *


def test_add_private_ssh_key(client):
    client._get.return_value = success_response
    response = client.Account.AddPrivateSSHKey("title", "ssh_key", "ruk")
    client._get.assert_called_with(
        "AddPrivateSSHKey",
        params={"title": "title", "sshKey": "ssh_key", "ruk": "ruk", "ruk": "ruk"},
    )
    assert response == success_response


def test_add_public_ssh_key(client):
    client._get.return_value = success_response
    response = client.Account.AddPublicSSHKey("title", "ssh_key", "ruk")
    client._get.assert_called_with(
        "AddPublicSSHKey",
        params={"title": "title", "sshKey": "ssh_key", "ruk": "ruk"},
    )
    assert response == success_response


def test_add_ssh_key(client):
    client._get.return_value = success_response
    response = client.Account.AddSSHKey("title", "ssh_key", False, "ruk")
    client._get.assert_called_with(
        "AddSSHKey",
        params={
            "title": "title",
            "sshKey": "ssh_key",
            "isPrivate": False,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_adjust_containers_limits_or_all_users(client):
    client._get.return_value = success_response
    response = client.Account.AdjustContainersLimitsForAllUsers("ruk")
    client._get.AdjustContainersLimitsForAllUsers(
        "AddSSHKey",
        params={"ruk": "ruk"},
    )
    assert response == success_response


def test_clean_quotas_cache(client):
    client._get.return_value = success_response
    response = client.Account.CleanQuotasCache(1, "ruk")
    client._get.assert_called_with(
        "CleanQuotasCache",
        params={"uid": 1, "ruk": "ruk"},
    )
    assert response == success_response


def test_delete_ssh_key(client):
    client._get.return_value = success_response
    response = client.Account.DeleteSSHKey(1, "ruk")
    client._get.assert_called_with(
        "DeleteSSHKey",
        params={"id": 1, "ruk": "ruk"},
    )
    assert response == success_response


def test_get_quotas_by_ip_address(client):
    client._get.return_value = success_response
    response = client.Account.GetQuotasByIpAddress("address", "quotas_names", "ruk")
    client._get.assert_called_with(
        "GetQuotasByIpAddress",
        params={"ipAddress": "address", "quotasnames": "quotas_names", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_ssh_keys(client):
    client._get.return_value = success_response
    response = client.Account.GetSSHKeys(False, "ruk")
    client._get.assert_called_with(
        "GetSSHKeys",
        params={"isPrivate": False, "ruk": "ruk"},
    )
    assert response == success_response


def test_get_ssh_keys_inner(client):
    client._get.return_value = success_response
    response = client.Account.GetSSHKeysInner(1, "ruk")
    client._get.assert_called_with(
        "GetSSHKeysInner",
        params={"uid": 1, "ruk": "ruk"},
    )
    assert response == success_response
