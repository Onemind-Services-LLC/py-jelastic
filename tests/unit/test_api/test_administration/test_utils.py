from . import *


def test_add_system_external_dns_records(client):
    client._get.return_value = success_response
    response = client.Utils.AddSystemExternalDNSRecord(
        "record1", "name1", 1, "data type 1", True, True, "ruk"
    )
    client._get.assert_called_with(
        "AddSystemExternalDNSRecord",
        params={
            "recordData": "record1",
            "name": "name1",
            "ttl": 1,
            "recordDataType": "data type 1",
            "sslEnabled": True,
            "enabled": True,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_analize_env(client):
    client._get.return_value = success_response
    response = client.Utils.AnalizeEnv("domain", "ruk")
    client._get.assert_called_with(
        "AnalizeEnv",
        params={"domain": "domain", "ruk": "ruk"},
    )
    assert response == success_response


def test_balance_resources(client):
    client._get.return_value = success_response
    response = client.Utils.BalanceResources(1, "ruk")
    client._get.assert_called_with(
        "BalanceResources", params={"domain": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_clear_envs(client):
    client._get.return_value = success_response
    response = client.Utils.ClearEnvs("ruk")
    client._get.assert_called_with("ClearEnvs", params={"ruk": "ruk"})
    assert response == success_response


def test_delete_broken_envs(client):
    client._get.return_value = success_response
    response = client.Utils.DeleteBrokenEnvs("target_app_ids", "ruk")
    client._get.assert_called_with(
        "DeleteBrokenEnvs", params={"targetAppIds": "target_app_ids", "ruk": "ruk"}
    )
    assert response == success_response


def test_edit_system_external_dns_record(client):
    client._get.return_value = success_response
    response = client.Utils.EditSystemExternalDNSRecord(
        1, "record", "name", 1, "datatype", True, True, "ruk"
    )
    client._get.assert_called_with(
        "EditSystemExternalDNSRecord",
        params={
            "id": 1,
            "recordData": "record",
            "name": "name",
            "ttl": 1,
            "recordDataType": "datatype",
            "sslEnabled": True,
            "enabled": True,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_export_env(client):
    client._get.return_value = success_response
    response = client.Utils.ExportEnv("app id 1", "ruk")
    client._get.assert_called_with(
        "ExportEnv",
        params={"targetAppId": "app id 1", "ruk": "ruk"},
    )
    assert response == success_response


def test_utils_fix_ext_dns(client):
    client._get.return_value = success_response
    response = client.Utils.FixExtDns(1, "target_app_id", "ruk")
    client._get.assert_called_with(
        "FixExtDns", params={"uid": 1, "targetAppId": "target_app_id", "ruk": "ruk"}
    )
    assert response == success_response


def test_fix_launching(client):
    client._get.return_value = success_response
    response = client.Utils.FixLaunching("ruk")
    client._get.assert_called_with("FixLaunching", params={"ruk": "ruk"})
    assert response == success_response


def test_generate_zone(client):
    client._get.return_value = success_response
    response = client.Utils.GenerateZone(True, "ruk")
    client._get.assert_called_with(
        "GenerateZone",
        params={"generateSlept": True, "ruk": "ruk"},
    )
    assert response == success_response


def test_get_avgs(client):
    client._get.return_value = success_response
    response = client.Utils.GetAvgs("ruk")
    client._get.assert_called_with("GetAvgs", params={"ruk": "ruk"})
    assert response == success_response


def test_get_avgs2(client):
    client._get.return_value = success_response
    response = client.Utils.GetAvgs2("ruk")
    client._get.assert_called_with("GetAvgs2", params={"ruk": "ruk"})
    assert response == success_response


def test_get_balance_stat(client):
    client._get.return_value = success_response
    response = client.Utils.GetBalancerStat(CURRENT_DATETIME, CURRENT_DATETIME, "ruk")
    client._get.assert_called_with(
        "GetBalancerStat",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_cloud_lets_usage(client):
    client._get.return_value = success_response
    response = client.Utils.GetCloudletsUsage("ruk")
    client._get.assert_called_with("GetCloudletsUsage", params={"ruk": "ruk"})
    assert response == success_response


def test_get_db_creation_stat(client):
    client._get.return_value = success_response
    response = client.Utils.GetDBCreationStat(CURRENT_DATETIME, CURRENT_DATETIME, "ruk")
    client._get.assert_called_with(
        "GetDBCreationStat",
        params={
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_errors(client):
    client._get.return_value = success_response
    response = client.Utils.GetErrors(
        CURRENT_DATETIME, CURRENT_DATETIME, 1, 1, 1, "ruk"
    )
    client._get.assert_called_with(
        "GerErrors",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "startrow": 1,
            "resultCount": 1,
            "filter": 1,
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_errors_by_date(client):
    client._get.return_value = success_response
    response = client.Utils.GetErrorsByDate(
        CURRENT_DATETIME, CURRENT_DATETIME, 1, 1, "ruk"
    )
    client._get.assert_called_with(
        "GetErrorsByDate",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "interval": 1,
            "filter": 1,
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_system_external_dns_records(client):
    client._get.return_value = success_response
    response = client.Utils.GetSystemExternalDNSRecords("ruk")
    client._get.assert_called_with("GetSystemExternalDNSRecords", params={"ruk": "ruk"})
    assert response == success_response


def test_get_zone(client):
    client._get.return_value = success_response
    response = client.Utils.GetZone("ruk")
    client._get.assert_called_with("GetZone", params={"ruk": "ruk"})
    assert response == success_response


def test_import_env(client):
    client._get.return_value = success_response
    response = client.Utils.ImportEnv("env1", "env_name", True, "ruk")
    client._get.assert_called_with(
        "ImportEnv",
        params={
            "envInfo": "env1",
            "envName": "env_name",
            "enableFirewall": True,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_inspect_envs(client):
    client._get.return_value = success_response
    response = client.Utils.InspectEnvs(True, "ruk")
    client._get.assert_called_with("InspectEnvs", params={"remove": True, "ruk": "ruk"})
    assert response == success_response


def test_manage_service(client):
    client._get.return_value = success_response
    response = client.Utils.ManageService(1, "command", "service 1", "ruk")
    client._get.assert_called_with(
        "ManageServices",
        params={
            "nodeid": 1,
            "command": "command",
            "servicename": "service 1",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_remove_system_external_dns_record(client):
    client._get.return_value = success_response
    response = client.Utils.RemoveSystemExternalDNSRecord(1, "ruk")
    client._get.assert_called_with(
        "RemoveSystemExternalDNSRecord",
        params={"id": 1, "ruk": "ruk"},
    )
    assert response == success_response


def test_update_env(client):
    client._get.return_value = success_response
    response = client.Utils.UpdateEnv("app 1", "ruk")
    client._get.assert_called_with(
        "UpdateEnv",
        params={"targetAppId": "app 1", "ruk": "ruk"},
    )
    assert response == success_response


def test_update_inv_in_thread(client):
    client._get.return_value = success_response
    response = client.Utils.UpdateEnvInThread("thread app 1", "ruk")
    client._get.assert_called_with(
        "UpdateEnvInThread",
        params={"targetAppId": "thread app 1", "ruk": "ruk"},
    )
    assert response == success_response


def test_update_nodes(client):
    client._get.return_value = success_response
    response = client.Utils.UpdateNodes("ruk")
    client._get.assert_called_with("UpdateNodes", params={"ruk": "ruk"})
    assert response == success_response
