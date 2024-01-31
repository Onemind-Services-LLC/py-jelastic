from . import *


def test_copy(client):
    client._get.return_value = success_response
    response = client.File.Copy("src", "dest","ruk",)
    client._get.assert_called_with(
        "Copy",
        params={"src": "src", "dest": "dest","ruk": "ruk",},
    )
    assert response == success_response


def test_create(client):
    client._get.return_value = success_response
    response = client.File.Create("path", True,"ruk",)
    client._get.assert_called_with("Create", params={"path": "path", "isdir": True,"ruk": "ruk",})
    assert response == success_response


def test_delete(client):
    client._get.return_value = success_response
    response = client.File.Delete("path", "ext","ruk",)
    client._get.assert_called_with(
        "Delete",
        params={"path": "path", "ext": "ext","ruk": "ruk",},
    )
    assert response == success_response


def test_get_list(client):
    client._get.return_value = success_response
    response = client.File.GetList("path", "ext","ruk",)
    client._get.assert_called_with(
        "GetList",
        params={"path": "path", "ext": "ext","ruk": "ruk",},
    )
    assert response == success_response


def test_read(client):
    client._get.return_value = success_response
    response = client.File.Read("path","ruk",)
    client._get.assert_called_with(
        "Read",
        params={
            "path": "path","ruk": "ruk",
        },
    )
    assert response == success_response


def test_rename(client):
    client._get.return_value = success_response
    response = client.File.Rename(
        "old_path",
        "new_path","ruk",
    )
    client._get.assert_called_with(
        "Rename",
        params={
            "oldPath": "old_path",
            "newPath": "new_path","ruk": "ruk",
        },
    )
    assert response == success_response


def test_upload(client):
    client._get.return_value = success_response
    response = client.File.Upload("source_path", "dest_path", True,"ruk",)
    client._get.assert_called_with(
        "Upload",
        params={
            "sourcePath": "source_path",
            "destPath": "dest_path",
            "overWrite": True,"ruk": "ruk",
        },
    )
    assert response == success_response


def test_write(client):
    client._get.return_value = success_response
    response = client.File.Write("path", "body", True,"ruk",)
    client._get.assert_called_with(
        "Write", params={"path": "path", "body": "body", "append": True,"ruk": "ruk",}
    )
    assert response == success_response
