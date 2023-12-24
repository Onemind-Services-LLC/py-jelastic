from . import *


def test_add_private_ssh_key(client):
    client._get.return_value = success_response
    response = client.Account.AddPrivateSSHKey("title", "ssh_key")
    client._get.assert_called_with(
        "AddPrivateSSHKey",
        params={"title": "title", "sshKey": "ssh_key"},
    )
    assert response == success_response


def test_add_public_ssh_key(client):
    client._get.return_value = success_response
    response = client.Account.AddPublicSSHKey("title", "ssh_key")
    client._get.assert_called_with(
        "AddPublicSSHKey",
        params={"title": "title", "sshKey": "ssh_key"},
    )
    assert response == success_response


def test_add_ssh_key(client):
    client._get.return_value = success_response
    response = client.Account.AddSSHKey("title", "ssh_key", False)
    client._get.assert_called_with(
        "AddSSHKey",
        params={"title": "title", "sshKey": "ssh_key", "isPrivate": False},
    )
    assert response == success_response


def test_adjust_containers_limits_or_all_users(client):
    client._get.return_value = success_response
    response = client.Account.AdjustContainersLimitsForAllUsers()
    client._get.AdjustContainersLimitsForAllUsers(
        "AddSSHKey",
        params={},
    )
    assert response == success_response


def test_clean_quotas_cache(client):
    client._get.return_value = success_response
    response = client.Account.CleanQuotasCache(1)
    client._get.assert_called_with(
        "CleanQuotasCache",
        params={
            "uid": 1,
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


def test_get_quotas_by_ip_address(client):
    client._get.return_value = success_response
    response = client.Account.GetQuotasByIpAddress(
        "address",
        "quotas_names",
    )
    client._get.assert_called_with(
        "GetQuotasByIpAddress",
        params={
            "ipAddress": "address",
            "quotasnames": "quotas_names",
        },
    )
    assert response == success_response


def test_get_ssh_keys(client):
    client._get.return_value = success_response
    response = client.Account.GetSSHKeys(False)
    client._get.assert_called_with(
        "GetSSHKeys",
        params={"isPrivate": False},
    )
    assert response == success_response


def test_get_ssh_keys_inner(client):
    client._get.return_value = success_response
    response = client.Account.GetSSHKeysInner(1)
    client._get.assert_called_with(
        "GetSSHKeysInner",
        params={
            "uid": 1,
        },
    )
    assert response == success_response
