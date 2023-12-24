from . import *


def test_option_create(client):
    client._get.return_value = success_response
    response = client.Option.Create({"name": "test"}, 1)
    client._get.assert_called_with(
        "Create", params={"tariffOption": {"name": "test"}, "resellerId": 1}
    )
    assert response == success_response


def test_option_delete(client):
    client._get.return_value = success_response
    response = client.Option.Delete("test", 1)
    client._get.assert_called_with("Delete", params={"name": "test", "resellerId": 1})
    assert response == success_response


def test_option_edit(client):
    client._get.return_value = success_response
    response = client.Option.Edit({"name": "test"}, 1)
    client._get.assert_called_with(
        "Edit", params={"tariffOption": {"name": "test"}, "resellerId": 1}
    )
    assert response == success_response


def test_option_get(client):
    client._get.return_value = success_response
    response = client.Option.Get(1)
    client._get.assert_called_with("Get", params={"resellerId": 1})
    assert response == success_response
