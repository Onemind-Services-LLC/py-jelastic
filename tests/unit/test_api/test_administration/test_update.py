from . import *


def test_update_fix_ext_dns(client):
    client._get.return_value = success_response
    response = client.Update.FixExtDns(1, "target_app_id")
    client._get.assert_called_with(
        "FixExtDns", params={"uid": 1, "targetAppIds": "target_app_id"}
    )
    assert response == success_response


def test_restore_env(client):
    client._get.return_value = success_response
    response = client.Update.RestoreEnv("env", 1, "region")
    client._get.assert_called_with(
        "RestoreEnv", params={"envName": "env", "uid": 1, "region": "region"}
    )
    assert response == success_response


def test_sync_infra_env(client):
    client._get.return_value = success_response
    response = client.Update.SyncInfraEnv("domain", "registry")
    client._get.assert_called_with(
        "SyncInfraEnv",
        params={
            "domain": "domain",
            "registry": "registry",
        },
    )
    assert response == success_response
