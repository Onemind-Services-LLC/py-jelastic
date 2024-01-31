from . import *


def test_export_create(client):
    client._get.return_value = success_response
    response = client.Export.Create({"key": "value"},"ruk",)
    client._get.assert_called_with(
        "Create",
        params={
            "settings": '{"key": "value"}',"ruk": "ruk",
        },
    )
    assert response == success_response


def test_export_delete(client):
    client._get.return_value = success_response
    response = client.Export.Delete("test","ruk",)
    client._get.assert_called_with("Delete", params={"id": "test","ruk": "ruk",})
    assert response == success_response


def test_export_delete_exported_data(client):
    client._get.return_value = success_response
    response = client.Export.DeleteExportedData("env", "file","ruk",)
    client._get.assert_called_with(
        "DeleteExportedData", params={"envName": "env", "fileName": "file","ruk": "ruk",}
    )
    assert response == success_response


def test_export_get_list(client):
    client._get.return_value = success_response
    response = client.Export.GetList("env","ruk",)
    client._get.assert_called_with("GetList", params={"envName": "env","ruk": "ruk",})
    assert response == success_response


def test_export_get_manifest(client):
    client._get.return_value = success_response
    response = client.Export.GetManifest("env", "manifest-id","ruk",)
    client._get.assert_called_with(
        "GetManifest", params={"envName": "env", "id": "manifest-id","ruk": "ruk",}
    )
    assert response == success_response
