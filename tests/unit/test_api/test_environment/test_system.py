from . import *


def test_check_db_connection(client):
    client._get.return_value = success_response
    response = client.System.CheckDBConnection("checksum")
    client._get.assert_called_with(
        "CheckDBConnection",
        params={
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_check_error(client):
    client._get.return_value = success_response
    response = client.System.CheckError(1)
    client._get.assert_called_with("CheckError", params={"code": 1})
    assert response == success_response


def test_clean_check_request_cache(client):
    client._get.return_value = success_response
    response = client.System.CleanCheckRequestCache(1)
    client._get.assert_called_with("CleanCheckRequestCache", params={"uid": 1})
    assert response == success_response


def test_clean_check_request_cache_inner(client):
    client._get.return_value = success_response
    response = client.System.CleanCheckRequestCacheInner(1)
    client._get.assert_called_with("CleanCheckRequestCacheInner", params={"uid": 1})
    assert response == success_response


def test_clean_template_manifest_cache(client):
    client._get.return_value = success_response
    response = client.System.CleanTemplateManifestCache()
    client._get.assert_called_with(
        "CleanTemplateManifestCache",
        params={},
    )
    assert response == success_response


def test_delete_old_envs(client):
    client._get.return_value = success_response
    response = client.System.DeleteOldEnvs("updatedon", 1, True, "checksum")
    client._get.assert_called_with(
        "DeleteOldEnvs",
        params={
            "updatedon": "updatedon",
            "status": 1,
            "debug": True,
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_event(client):
    client._get.return_value = success_response
    response = client.System.Event("message", True)
    client._get.assert_called_with(
        "Event", params={"message": "message", "publishLocal": True}
    )
    assert response == success_response


def test_fix_duplicates(client):
    client._get.return_value = success_response
    response = client.System.FixDuplicates(True)
    client._get.assert_called_with("FixDuplicates", params={"debug": True})
    assert response == success_response


def test_fix_stuck_envs(client):
    client._get.return_value = success_response
    response = client.System.FixStuckEnvs("checksum")
    client._get.assert_called_with(
        "FixStuckEnvs",
        params={"checksum": "checksum"},
    )
    assert response == success_response


def test_get_api_descriptions(client):
    client._get.return_value = success_response
    response = client.System.GetAPIDescriptions(True, True)
    client._get.assert_called_with(
        "GetAPIDescriptions", params={"isPublicOnly": True, "isToken": True}
    )
    assert response == success_response


def test_get_all_api_descriptions(client):
    client._get.return_value = success_response
    response = client.System.GetAllAPIDescriptions(True, True)
    client._get.assert_called_with(
        "GetAllAPIDescriptions", params={"isPublicOnly": True, "isToken": True}
    )
    assert response == success_response


def test_get_billable_items(client):
    client._get.return_value = success_response
    response = client.System.GetBillableItems()
    client._get.assert_called_with(
        "GetBillableItems",
        params={},
    )
    assert response == success_response


def test_get_cache_stats(client):
    client._get.return_value = success_response
    response = client.System.GetCacheStats()
    client._get.assert_called_with(
        "GetCacheStats",
        params={},
    )
    assert response == success_response


def test_get_cache_status(client):
    client._get.return_value = success_response
    response = client.System.GetCacheStatus()
    client._get.assert_called_with(
        "GetCacheStatus",
        params={},
    )
    assert response == success_response


def test_get_cont_count_status(client):
    client._get.return_value = success_response
    response = client.System.GetContCountStatus(CURRENT_DATETIME, CURRENT_DATETIME)
    client._get.assert_called_with(
        "GetContCountStatus",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_instance_cache_status(client):
    client._get.return_value = success_response
    response = client.System.GetInstanceCacheStatus()
    client._get.assert_called_with(
        "GetInstanceCacheStatus",
        params={},
    )
    assert response == success_response


def test_get_ips_by_type(client):
    client._get.return_value = success_response
    response = client.System.GetIpsByType("checksum", "node_type", "hnip")
    client._get.assert_called_with(
        "GetIpsByType",
        params={"checksum": "checksum", "nodeType": "node_type", "hnip": "hnip"},
    )
    assert response == success_response


def test_get_keyword(client):
    client._get.return_value = success_response
    response = client.System.GetKeyword("checksum")
    client._get.assert_called_with(
        "GetKeyword",
        params={"checksum": "checksum"},
    )
    assert response == success_response


def test_get_platform_status(client):
    client._get.return_value = success_response
    response = client.System.GetPlatformStatus("checksum", True)
    client._get.assert_called_with(
        "GetPlatformStatus",
        params={"checksum": "checksum", "checkSMTP": True},
    )
    assert response == success_response


def test_get_stat_collector_status(client):
    client._get.return_value = success_response
    response = client.System.GetStatCollectorStatus()
    client._get.assert_called_with(
        "GetStatCollectorStatus",
        params={},
    )
    assert response == success_response


def test_get_version(client):
    client._get.return_value = success_response
    response = client.System.GetVersion()
    client._get.assert_called_with(
        "GetVersion",
        params={},
    )
    assert response == success_response


def test_refresh_email_templates(client):
    client._get.return_value = success_response
    response = client.System.RefreshEmailTemplates()
    client._get.assert_called_with(
        "RefreshEmailTemplates",
        params={},
    )
    assert response == success_response


def test_refresh_user(client):
    client._get.return_value = success_response
    response = client.System.RefreshUser("language")
    client._get.assert_called_with("RefreshUser", params={"language": "language"})
    assert response == success_response


def test_register_env_container(client):
    client._get.return_value = success_response
    response = client.System.RegisterEnvContainer(
        "env_name",
        "node_type",
        "ip_address",
        "env_id",
        "ct_id",
        "passwd",
        "hn_ip_address",
    )
    client._get.assert_called_with(
        "RegisterEnvContainer",
        params={
            "envName": "env_name",
            "nodeType": "node_type",
            "ipAddress": "ip_address",
            "envId": "env_id",
            "ctId": "ct_id",
            "passwd": "passwd",
            "hnIpAddress": "hn_ip_address",
        },
    )
    assert response == success_response


def test_reload_configuration(client):
    client._get.return_value = success_response
    response = client.System.ReloadConfiguration(1, "changedPlaceholders")
    client._get.assert_called_with(
        "ReloadConfiguration",
        params={"resellerId": 1, "changedPlaceholders": "changedPlaceholders"},
    )
    assert response == success_response


def test_send_email(client):
    client._get.return_value = success_response
    response = client.System.SendEmail("templates", "abc@gmail.com", "language", 1)
    client._get.assert_called_with(
        "SendEmail",
        params={
            "templates": "templates",
            "email": "abc@gmail.com",
            "language": "language",
            "timeout": 1,
        },
    )
    assert response == success_response


def test_surcharge_billable_items(client):
    client._get.return_value = success_response
    response = client.System.SurchargeBillableItems(CURRENT_DATETIME, CURRENT_DATETIME)
    client._get.assert_called_with(
        "SurchargeBillableItems",
        params={
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_synch_envs(client):
    client._get.return_value = success_response
    response = client.System.SynchEnvs("checksum")
    client._get.assert_called_with(
        "SynchEnvs",
        params={"checksum": "checksum"},
    )
    assert response == success_response
