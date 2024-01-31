from . import *


def test_update_fix_ext_dns(client):
    client._get.return_value = success_response
    response = client.Update.FixExtDns(1, "target_app_id", "ruk")
    client._get.assert_called_with(
        "FixExtDns", params={"uid": 1, "targetAppIds": "target_app_id", "ruk": "ruk"}
    )
    assert response == success_response


def test_restore_env(client):
    client._get.return_value = success_response
    response = client.Update.RestoreEnv("env", 1, "region", "ruk")
    client._get.assert_called_with(
        "RestoreEnv",
        params={"envName": "env", "uid": 1, "region": "region", "ruk": "ruk"},
    )
    assert response == success_response


def test_sync_infra_env(client):
    client._get.return_value = success_response
    response = client.Update.SyncInfraEnv("domain", "registry", "ruk")
    client._get.assert_called_with(
        "SyncInfraEnv",
        params={"domain": "domain", "registry": "registry", "ruk": "ruk"},
    )
    assert response == success_response
