from . import *


def test_add_app(client):
    client._get.return_value = success_response
    response = client.Cluster.AddApp(
        "app id",
        "ruk",
    )
    client._get.assert_called_once_with(
        "AddApp",
        params={"targetAppId": "app id", "ruk": "ruk"},
    )
    assert response == success_response


def test_add_host_map_records(client):
    client._get.return_value = success_response
    response = client.Cluster.AddHostMapRecords(
        "host map",
        "ruk",
    )
    client._get.assert_called_once_with(
        "AddHostMapRecords",
        params={"hostMaps": "host map", "ruk": "ruk"},
    )
    assert response == success_response


def test_duplicate_host_map_records(client):
    client._get.return_value = success_response
    response = client.Cluster.DuplicateHostMapRecords(
        "from host",
        "to host",
        "ruk",
    )
    client._get.assert_called_once_with(
        "DuplicateHostMapRecords",
        params={"fromHost": "from host", "toHost": "to host", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_active_apps(client):
    client._get.return_value = success_response
    response = client.Cluster.GetActiveApps(
        "ruk",
    )
    client._get.assert_called_once_with("GetActiveApps", params={"ruk": "ruk"})
    assert response == success_response


def test_get__apps(client):
    client._get.return_value = success_response
    response = client.Cluster.GetApps(
        "path",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetApps", params={"path": "path", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_cup_usage(client):
    client._get.return_value = success_response
    response = client.Cluster.GetCpuUsage(
        "ruk",
    )
    client._get.assert_called_once_with("GetCpuUsage", params={"ruk": "ruk"})
    assert response == success_response


def test_get_disk_usage(client):
    client._get.return_value = success_response
    response = client.Cluster.GetDiskUsage(
        "ruk",
    )
    client._get.assert_called_once_with("GetDiskUsage", params={"ruk": "ruk"})
    assert response == success_response


def test_get_maintenance_mode(client):
    client._get.return_value = success_response
    response = client.Cluster.GetMaintenanceMode(
        "ruk",
    )
    client._get.assert_called_once_with("GetMaintenanceMode", params={"ruk": "ruk"})
    assert response == success_response


def test_get_nodes(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodes(
        "id",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetNodes", params={"targetAppId": "id", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_system_usage(client):
    client._get.return_value = success_response
    response = client.Cluster.GetSystemUsage(
        "ruk",
    )
    client._get.assert_called_once_with("GetSystemUsage", params={"ruk": "ruk"})
    assert response == success_response


def test_move_app(client):
    client._get.return_value = success_response
    response = client.Cluster.MoveApp(
        "app id",
        "ruk",
    )
    client._get.assert_called_once_with(
        "MoveApp",
        params={"targetAppId": "app id", "ruk": "ruk"},
    )
    assert response == success_response


def test_reload_app(client):
    client._get.return_value = success_response
    response = client.Cluster.ReloadApp(
        "app id",
        "ruk",
    )
    client._get.assert_called_once_with(
        "ReloadApp",
        params={"targetAppId": "app id", "ruk": "ruk"},
    )
    assert response == success_response


def test_remove_all_host_map_records(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveAllHostMapRecords(
        "host",
        "ruk",
    )
    client._get.assert_called_once_with(
        "RemoveAllHostMapRecords",
        params={"host": "host", "ruk": "ruk"},
    )
    assert response == success_response


def test_remove_app(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveApp(
        "app id",
        "ruk",
    )
    client._get.assert_called_once_with(
        "RemoveApp",
        params={"targetAppId": "app id", "ruk": "ruk"},
    )
    assert response == success_response


def test_remove_host_map_records(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveHostMapRecords(
        "host",
        "ruk",
    )
    client._get.assert_called_once_with(
        "RemoveHostMapRecords",
        params={"hostMaps": "host", "ruk": "ruk"},
    )
    assert response == success_response


def test_restart_node(client):
    client._get.return_value = success_response
    response = client.Cluster.RestartNode(
        "ruk",
    )
    client._get.assert_called_once_with("RestartNode", params={"ruk": "ruk"})
    assert response == success_response


def test_set_maintenance_mode(client):
    client._get.return_value = success_response
    response = client.Cluster.SetMaintenanceMode(
        True,
        "ruk",
    )
    client._get.assert_called_once_with(
        "SetMaintenanceMode",
        params={"enabled": True, "ruk": "ruk"},
    )
    assert response == success_response


def test_unload_app(client):
    client._get.return_value = success_response
    response = client.Cluster.UnloadApp(
        "app id",
        "ruk",
    )
    client._get.assert_called_once_with(
        "UnloadApp",
        params={"targetAppId": "app id", "ruk": "ruk"},
    )
    assert response == success_response


def test_update_application_host(client):
    client._get.return_value = success_response
    response = client.Cluster.UpdateApplicationHost(
        "from host",
        "to host",
        "ruk",
    )
    client._get.assert_called_once_with(
        "UpdateApplicationHost",
        params={"fromHost": "from host", "toHost": "to host", "ruk": "ruk"},
    )
    assert response == success_response


def test_update_system_app(client):
    client._get.return_value = success_response
    response = client.Cluster.UpdateSystemApps(
        "apps",
        "ruk",
    )
    client._get.assert_called_once_with(
        "UpdateSystemApps", params={"recompileAll": "apps", "ruk": "ruk"}
    )
    assert response == success_response
