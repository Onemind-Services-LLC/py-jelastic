from . import *


def test_add_favorite(client):
    client._get.return_value = success_response
    response = client.File.AddFavorite(
        "env_name",
        "path",
        "nodeGroup",
        1,
        "keyword",
        "filter",
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "AddFavorite",
        params={
            "envName": "env_name",
            "path": "path",
            "nodeGroup": "nodeGroup",
            "nodeId": 1,
            "keyword": "keyword",
            "filter": "filter",
            "isDir": True,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_add_mount_point_by_group(client):
    client._get.return_value = success_response
    response = client.File.AddMountPointByGroup(
        "env_name",
        "node_group",
        "path",
        "source_path",
        "protocol",
        "sourceHost",
        1,
        "name",
        True,
        "sourceAddressType",
        "ruk",
    )
    client._get.assert_called_with(
        "AddMountPointByGroup",
        params={
            "envName": "env_name",
            "nodeGroup": "node_group",
            "path": "path",
            "sourcePath": "source_path",
            "protocol": "protocol",
            "sourceHost": "sourceHost",
            "sourceNodeId": 1,
            "name": "name",
            "readOnly": True,
            "sourceAddressType": "sourceAddressType",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_add_mount_point_by_id(client):
    client._get.return_value = success_response
    response = client.File.AddMountPointById(
        "env_name",
        1,
        "path",
        "source_path",
        "protocol",
        "sourceHost",
        1,
        "name",
        True,
        "sourceAddressType",
        "ruk",
    )
    client._get.assert_called_with(
        "AddMountPointById",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "path": "path",
            "sourcePath": "source_path",
            "protocol": "protocol",
            "sourceHost": "sourceHost",
            "sourceNodeId": 1,
            "name": "name",
            "readOnly": True,
            "sourceAddressType": "sourceAddressType",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_append(client):
    client._get.return_value = success_response
    response = client.File.Append(
        "env_name",
        "path",
        "body",
        "nodeType",
        "nodeGroup",
        True,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "Append",
        params={
            "envName": "env_name",
            "path": "path",
            "body": "body",
            "nodeType": "nodeType",
            "nodeGroup": "nodeGroup",
            "masterOnly": True,
            "nodeId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_check_cross_mount(client):
    client._get.return_value = success_response
    response = client.File.CheckCrossMount(
        "env_name",
        1,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "CheckCrossMount",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "sourceNodeId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_clone_cross_mount_points(client):
    client._get.return_value = success_response
    response = client.File.CloneMountPoints(
        "env_name",
        1,
        1,
        "mountPoints",
        "ruk",
    )
    client._get.assert_called_with(
        "CloneMountPoints",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "sourceNodeId": 1,
            "mountPoints": "mountPoints",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_copy(client):
    client._get.return_value = success_response
    response = client.File.Copy(
        "env_name",
        "src",
        "dest",
        "nodeType",
        "nodeGroup",
        True,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "Copy",
        params={
            "envName": "env_name",
            "src": "src",
            "dest": "dest",
            "nodeType": "nodeType",
            "nodeGroup": "nodeGroup",
            "masterOnly": True,
            "nodeId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_create(client):
    client._get.return_value = success_response
    response = client.File.Create(
        "env_name",
        "path",
        "nodeType",
        "nodeGroup",
        True,
        True,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "Create",
        params={
            "envName": "env_name",
            "path": "path",
            "nodeType": "nodeType",
            "nodeGroup": "nodeGroup",
            "masterOnly": True,
            "isdir": True,
            "nodeId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_delete(client):
    client._get.return_value = success_response
    response = client.File.Delete(
        "env_name",
        "path",
        "nodeType",
        "nodeGroup",
        True,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "Delete",
        params={
            "envName": "env_name",
            "path": "path",
            "nodeType": "nodeType",
            "nodeGroup": "nodeGroup",
            "masterOnly": True,
            "nodeId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_exported_list(client):
    client._get.return_value = success_response
    response = client.File.GetExportedList(
        "env_name",
        1,
        "path",
        "ruk",
    )
    client._get.assert_called_with(
        "GetExportedList",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "path": "path",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_favorites(client):
    client._get.return_value = success_response
    response = client.File.GetFavorites(
        "env_name",
        "nodeGroup",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "GetFavorites",
        params={
            "envName": "env_name",
            "nodeGroup": "nodeGroup",
            "nodeId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_add_list(client):
    client._get.return_value = success_response
    response = client.File.GetList(
        "env_name",
        "path",
        "nodeType",
        "nodeGroup",
        1,
        "filter",
        "ruk",
    )
    client._get.assert_called_with(
        "GetList",
        params={
            "envName": "env_name",
            "path": "path",
            "nodeType": "nodeType",
            "nodeGroup": "nodeGroup",
            "nodeId": 1,
            "filter": "filter",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_mount_points(client):
    client._get.return_value = success_response
    response = client.File.GetMountPoints(
        "env_name",
        "nodeGroup",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "GetMountPoints",
        params={
            "envName": "env_name",
            "nodeGroup": "nodeGroup",
            "nodeId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_prepare_mount_points(client):
    client._get.return_value = success_response
    response = client.File.PrepareMountPoints(
        "env_name",
        "data",
        "ruk",
    )
    client._get.assert_called_with(
        "PrepareMountPoints",
        params={
            "envName": "env_name",
            "data": "data",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_read(client):
    client._get.return_value = success_response
    response = client.File.Read(
        "env_name",
        "path",
        "nodeType",
        "nodeGroup",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "Read",
        params={
            "envName": "env_name",
            "path": "path",
            "nodeType": "nodeType",
            "nodeGroup": "nodeGroup",
            "nodeId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_remove_export(client):
    client._get.return_value = success_response
    response = client.File.RemoveExport(
        "env_name",
        1,
        "path",
        1,
        "client_path",
        "ruk",
    )
    client._get.assert_called_with(
        "RemoveExport",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "path": "path",
            "clientNodeId": 1,
            "clientPath": "client_path",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_remove_favorite(client):
    client._get.return_value = success_response
    response = client.File.RemoveFavorite(
        "env_name",
        "path",
        "nodeType",
        "nodeGroup",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "RemoveFavorite",
        params={
            "envName": "env_name",
            "path": "path",
            "nodeType": "nodeType",
            "nodeGroup": "nodeGroup",
            "nodeId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_remove_mount_point_by_group(client):
    client._get.return_value = success_response
    response = client.File.RemoveMountPointByGroup(
        "env_name",
        "path",
        "node_group",
        "ruk",
    )
    client._get.assert_called_with(
        "RemoveMountPointByGroup",
        params={
            "envName": "env_name",
            "path": "path",
            "nodeGroup": "node_group",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_remove_mount_point_by_id(client):
    client._get.return_value = success_response
    response = client.File.RemoveMountPointById(
        "env_name",
        "path",
        "node_id",
        "ruk",
    )
    client._get.assert_called_with(
        "RemoveMountPointById",
        params={
            "envName": "env_name",
            "path": "path",
            "nodeId": "node_id",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_rename(client):
    client._get.return_value = success_response
    response = client.File.Rename(
        "env_name",
        "old_path",
        "new_path",
        "nodeType",
        "nodeGroup",
        True,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "Rename",
        params={
            "envName": "env_name",
            "oldPath": "old_path",
            "newPath": "new_path",
            "nodeType": "nodeType",
            "nodeGroup": "nodeGroup",
            "masterOnly": True,
            "nodeId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_replace_in_body(client):
    client._get.return_value = success_response
    response = client.File.ReplaceInBody(
        "env_name",
        "path",
        "pattern",
        "replacement",
        1,
        "nodeType",
        "nodeGroup",
        True,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "ReplaceInBody",
        params={
            "envName": "env_name",
            "path": "path",
            "pattern": "pattern",
            "replacement": "replacement",
            "nth": 1,
            "nodeType": "nodeType",
            "nodeGroup": "nodeGroup",
            "masterOnly": True,
            "nodeId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_unpack_by_id(client):
    client._get.return_value = success_response
    response = client.File.UnpackById(
        "env_name",
        "path",
        "node_id",
        "source_path",
        "dest_path",
        "ruk",
    )
    client._get.assert_called_with(
        "UnpackById",
        params={
            "envName": "env_name",
            "path": "path",
            "nodeId": "node_id",
            "sourcePath": "source_path",
            "destPath": "dest_path",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_unpack_by_type(client):
    client._get.return_value = success_response
    response = client.File.UnpackByType(
        "env_name",
        "path",
        "node_type",
        "source_path",
        "dest_path",
        "ruk",
    )
    client._get.assert_called_with(
        "UnpackByType",
        params={
            "envName": "env_name",
            "path": "path",
            "nodeType": "node_type",
            "sourcePath": "source_path",
            "destPath": "dest_path",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_upload(client):
    client._get.return_value = success_response
    response = client.File.Upload(
        "env_name",
        "source_path",
        "dest_path",
        "nodeType",
        "nodeGroup",
        True,
        1,
        "overwrite",
        "ruk",
    )
    client._get.assert_called_with(
        "Upload",
        params={
            "envName": "env_name",
            "sourcePath": "source_path",
            "destPath": "dest_path",
            "nodeType": "nodeType",
            "nodeGroup": "nodeGroup",
            "masterOnly": True,
            "nodeId": 1,
            "overwrite": "overwrite",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_write(client):
    client._get.return_value = success_response
    response = client.File.Write(
        "env_name",
        "path",
        "body",
        "node_type",
        "nodeGroup",
        True,
        1,
        False,
        "ruk",
    )
    client._get.assert_called_with(
        "Write",
        params={
            "envName": "env_name",
            "path": "path",
            "body": "body",
            "nodeType": "node_type",
            "nodeGroup": "nodeGroup",
            "masterOnly": True,
            "nodeId": 1,
            "isAppendMode": False,
            "ruk": "ruk",
        },
    )
    assert response == success_response
