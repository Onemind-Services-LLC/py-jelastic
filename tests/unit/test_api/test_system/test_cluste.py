from . import *


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        system = System(session=Mock(), token="token")
        system._get = mock_get
        yield system


def test_add_app(client):
    client._get.return_value = success_response
    response = client.Cluster.AddApp("app id")
    client._get.assert_called_once_with(
        "AddApp",
        params={
            "targetAppId": "app id",
        },
    )
    assert response == success_response


def test_add_host_map_records(client):
    client._get.return_value = success_response
    response = client.Cluster.AddHostMapRecords("host map")
    client._get.assert_called_once_with(
        "AddHostMapRecords",
        params={
            "hostMaps": "host map",
        },
    )
    assert response == success_response


def test_duplicate_host_map_records(client):
    client._get.return_value = success_response
    response = client.Cluster.DuplicateHostMapRecords("from host", "to host")
    client._get.assert_called_once_with(
        "DuplicateHostMapRecords",
        params={
            "fromHost": "from host",
            "toHost": "to host",
        },
    )
    assert response == success_response


def test_get_active_apps(client):
    client._get.return_value = success_response
    response = client.Cluster.GetActiveApps()
    client._get.assert_called_once_with("GetActiveApps", params={})
    assert response == success_response


def test_get__apps(client):
    client._get.return_value = success_response
    response = client.Cluster.GetApps(["path1", "path2", "path3"])
    client._get.assert_called_once_with(
        "GetApps",
        params={"path": ["path1", "path2", "path3"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_cup_usage(client):
    client._get.return_value = success_response
    response = client.Cluster.GetCpuUsage()
    client._get.assert_called_once_with("GetCpuUsage", params={})
    assert response == success_response


def test_get_disk_usage(client):
    client._get.return_value = success_response
    response = client.Cluster.GetDiskUsage()
    client._get.assert_called_once_with("GetDiskUsage", params={})
    assert response == success_response


def test_get_maintenance_mode(client):
    client._get.return_value = success_response
    response = client.Cluster.GetMaintenanceMode()
    client._get.assert_called_once_with("GetMaintenanceMode", params={})
    assert response == success_response


def test_get_nodes(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodes(["id 1", "id 2", "id 3"])
    client._get.assert_called_once_with(
        "GetNodes",
        params={
            "targetAppId": ["id 1", "id 2", "id 3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_system_usage(client):
    client._get.return_value = success_response
    response = client.Cluster.GetSystemUsage()
    client._get.assert_called_once_with("GetSystemUsage", params={})
    assert response == success_response


def test_move_app(client):
    client._get.return_value = success_response
    response = client.Cluster.MoveApp("app id")
    client._get.assert_called_once_with(
        "MoveApp",
        params={
            "targetAppId": "app id",
        },
    )
    assert response == success_response


def test_reload_app(client):
    client._get.return_value = success_response
    response = client.Cluster.ReloadApp("app id")
    client._get.assert_called_once_with(
        "ReloadApp",
        params={
            "targetAppId": "app id",
        },
    )
    assert response == success_response


def test_remove_all_host_map_records(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveAllHostMapRecords("host")
    client._get.assert_called_once_with(
        "RemoveAllHostMapRecords",
        params={
            "host": "host",
        },
    )
    assert response == success_response


def test_remove_app(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveApp("app id")
    client._get.assert_called_once_with(
        "RemoveApp",
        params={
            "targetAppId": "app id",
        },
    )
    assert response == success_response


def test_remove_host_map_records(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveHostMapRecords("host")
    client._get.assert_called_once_with(
        "RemoveHostMapRecords",
        params={
            "hostMaps": "host",
        },
    )
    assert response == success_response


def test_restart_node(client):
    client._get.return_value = success_response
    response = client.Cluster.RestartNode()
    client._get.assert_called_once_with("RestartNode", params={})
    assert response == success_response


def test_set_maintenance_mode(client):
    client._get.return_value = success_response
    response = client.Cluster.SetMaintenanceMode(True)
    client._get.assert_called_once_with(
        "SetMaintenanceMode",
        params={
            "enabled": True,
        },
    )
    assert response == success_response


def test_unload_app(client):
    client._get.return_value = success_response
    response = client.Cluster.UnloadApp("app id")
    client._get.assert_called_once_with(
        "UnloadApp",
        params={
            "targetAppId": "app id",
        },
    )
    assert response == success_response


def test_update_application_host(client):
    client._get.return_value = success_response
    response = client.Cluster.UpdateApplicationHost("from host", "to host")
    client._get.assert_called_once_with(
        "UpdateApplicationHost",
        params={
            "fromHost": "from host",
            "toHost": "to host",
        },
    )
    assert response == success_response


def test_update_system_app(client):
    client._get.return_value = success_response
    response = client.Cluster.UpdateSystemApps("apps")
    client._get.assert_called_once_with(
        "UpdateSystemApps", params={"recompileAll": "apps"}
    )
    assert response == success_response
