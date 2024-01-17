from . import *


def test_add_system_external_dns_records(client):
    client._get.return_value = success_response
    response = client.Utils.AddSystemExternalDNSRecord(
        "record1",
        "name1",
        1,
        "data type 1",
        True,
        True,
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
        },
    )
    assert response == success_response


def test_analize_env(client):
    client._get.return_value = success_response
    response = client.Utils.AnalizeEnv(
        "domain",
    )
    client._get.assert_called_with(
        "AnalizeEnv",
        params={
            "domain": "domain",
        },
    )
    assert response == success_response


def test_balance_resources(client):
    client._get.return_value = success_response
    response = client.Utils.BalanceResources(
        1,
    )
    client._get.assert_called_with("BalanceResources", params={"domain": 1})
    assert response == success_response


def test_clear_envs(client):
    client._get.return_value = success_response
    response = client.Utils.ClearEnvs()
    client._get.assert_called_with("ClearEnvs", params={})
    assert response == success_response


def test_delete_broken_envs(client):
    client._get.return_value = success_response
    response = client.Utils.DeleteBrokenEnvs("target_app_ids")
    client._get.assert_called_with(
        "DeleteBrokenEnvs", params={"targetAppIds": "target_app_ids"}
    )
    assert response == success_response


def test_edit_system_external_dns_record(client):
    client._get.return_value = success_response
    response = client.Utils.EditSystemExternalDNSRecord(
        1, "record", "name", 1, "datatype", True, True
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
        },
    )
    assert response == success_response


def test_export_env(client):
    client._get.return_value = success_response
    response = client.Utils.ExportEnv(
        "app id 1",
    )
    client._get.assert_called_with(
        "ExportEnv",
        params={
            "targetAppId": "app id 1",
        },
    )
    assert response == success_response


def test_utils_fix_ext_dns(client):
    client._get.return_value = success_response
    response = client.Utils.FixExtDns(1, "target_app_id")
    client._get.assert_called_with(
        "FixExtDns", params={"uid": 1, "targetAppId": "target_app_id"}
    )
    assert response == success_response


def test_fix_launching(client):
    client._get.return_value = success_response
    response = client.Utils.FixLaunching()
    client._get.assert_called_with("FixLaunching", params={})
    assert response == success_response


def test_generate_zone(client):
    client._get.return_value = success_response
    response = client.Utils.GenerateZone(
        True,
    )
    client._get.assert_called_with(
        "GenerateZone",
        params={
            "generateSlept": True,
        },
    )
    assert response == success_response


def test_get_avgs(client):
    client._get.return_value = success_response
    response = client.Utils.GetAvgs()
    client._get.assert_called_with("GetAvgs", params={})
    assert response == success_response


def test_get_avgs2(client):
    client._get.return_value = success_response
    response = client.Utils.GetAvgs2()
    client._get.assert_called_with("GetAvgs2", params={})
    assert response == success_response


def test_get_balance_stat(client):
    client._get.return_value = success_response
    response = client.Utils.GetBalancerStat(
        CURRENT_DATETIME,
        CURRENT_DATETIME,
    )
    client._get.assert_called_with(
        "GetBalancerStat",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_cloud_lets_usage(client):
    client._get.return_value = success_response
    response = client.Utils.GetCloudletsUsage()
    client._get.assert_called_with("GetCloudletsUsage", params={})
    assert response == success_response


def test_get_db_creation_stat(client):
    client._get.return_value = success_response
    response = client.Utils.GetDBCreationStat(CURRENT_DATETIME, CURRENT_DATETIME)
    client._get.assert_called_with(
        "GetDBCreationStat",
        params={"startTime": CURRENT_DATETIME, "endTime": CURRENT_DATETIME},
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_errors(client):
    client._get.return_value = success_response
    response = client.Utils.GetErrors(CURRENT_DATETIME, CURRENT_DATETIME, 1, 1, 1)
    client._get.assert_called_with(
        "GerErrors",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "startrow": 1,
            "resultCount": 1,
            "filter": 1,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_errors_by_date(client):
    client._get.return_value = success_response
    response = client.Utils.GetErrorsByDate(CURRENT_DATETIME, CURRENT_DATETIME, 1, 1)
    client._get.assert_called_with(
        "GetErrorsByDate",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "interval": 1,
            "filter": 1,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_system_external_dns_records(client):
    client._get.return_value = success_response
    response = client.Utils.GetSystemExternalDNSRecords()
    client._get.assert_called_with("GetSystemExternalDNSRecords", params={})
    assert response == success_response


def test_get_zone(client):
    client._get.return_value = success_response
    response = client.Utils.GetZone()
    client._get.assert_called_with("GetZone", params={})
    assert response == success_response


def test_import_env(client):
    client._get.return_value = success_response
    response = client.Utils.ImportEnv("env1", "env_name", True)
    client._get.assert_called_with(
        "ImportEnv",
        params={"envInfo": "env1", "envName": "env_name", "enableFirewall": True},
    )
    assert response == success_response


def test_inspect_envs(client):
    client._get.return_value = success_response
    response = client.Utils.InspectEnvs(True)
    client._get.assert_called_with("InspectEnvs", params={"remove": True})
    assert response == success_response


def test_manage_service(client):
    client._get.return_value = success_response
    response = client.Utils.ManageService(
        1,
        "command",
        "service 1",
    )
    client._get.assert_called_with(
        "ManageServices",
        params={
            "nodeid": 1,
            "command": "command",
            "servicename": "service 1",
        },
    )
    assert response == success_response


def test_remove_system_external_dns_record(client):
    client._get.return_value = success_response
    response = client.Utils.RemoveSystemExternalDNSRecord(1)
    client._get.assert_called_with(
        "RemoveSystemExternalDNSRecord",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_update_env(client):
    client._get.return_value = success_response
    response = client.Utils.UpdateEnv("app 1")
    client._get.assert_called_with(
        "UpdateEnv",
        params={
            "targetAppId": "app 1",
        },
    )
    assert response == success_response


def test_update_inv_in_thread(client):
    client._get.return_value = success_response
    response = client.Utils.UpdateEnvInThread(
        "thread app 1",
    )
    client._get.assert_called_with(
        "UpdateEnvInThread",
        params={
            "targetAppId": "thread app 1",
        },
    )
    assert response == success_response


def test_update_nodes(client):
    client._get.return_value = success_response
    response = client.Utils.UpdateNodes()
    client._get.assert_called_with("UpdateNodes", params={})
    assert response == success_response
