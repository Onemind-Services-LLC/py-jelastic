from . import *


def test_copy(client):
    client._get.return_value = success_response
    response = client.File.Copy("src", "dest")
    client._get.assert_called_with(
        "Copy",
        params={"src": "src", "dest": "dest"},
    )
    assert response == success_response


def test_create(client):
    client._get.return_value = success_response
    response = client.File.Create(
        "path",
        [True, False, True],
    )
    client._get.assert_called_with(
        "Create",
        params={
            "path": "path",
            "isdir": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete(client):
    client._get.return_value = success_response
    response = client.File.Delete("path", ["ext1", "ext2", "ext3"])
    client._get.assert_called_with(
        "Delete",
        params={"path": "path", "ext": ["ext1", "ext2", "ext3"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_list(client):
    client._get.return_value = success_response
    response = client.File.GetList(
        ["path1", "path2", "path3"], ["ext1", "ext2", "ext3"]
    )
    client._get.assert_called_with(
        "GetList",
        params={"path": ["path1", "path2", "path3"], "ext": ["ext1", "ext2", "ext3"]},
        delimiter=",",
    )
    assert response == success_response


def test_read(client):
    client._get.return_value = success_response
    response = client.File.Read("path")
    client._get.assert_called_with(
        "Read",
        params={
            "path": "path",
        },
    )
    assert response == success_response


def test_rename(client):
    client._get.return_value = success_response
    response = client.File.Rename(
        "old_path",
        "new_path",
    )
    client._get.assert_called_with(
        "Rename",
        params={
            "oldPath": "old_path",
            "newPath": "new_path",
        },
    )
    assert response == success_response


def test_upload(client):
    client._get.return_value = success_response
    response = client.File.Upload(
        "source_path",
        "dest_path",
        [True, False, True],
    )
    client._get.assert_called_with(
        "Upload",
        params={
            "sourcePath": "source_path",
            "destPath": "dest_path",
            "overWrite": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_write(client):
    client._get.return_value = success_response
    response = client.File.Write(
        "path",
        "body",
        [True, False, True],
    )
    client._get.assert_called_with(
        "Write",
        params={
            "path": "path",
            "body": "body",
            "append": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response
