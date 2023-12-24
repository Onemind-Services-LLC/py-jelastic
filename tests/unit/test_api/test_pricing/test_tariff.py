from . import *


def test_tariff_create_grid(client):
    client._get.return_value = success_response
    response = client.Tariff.CreateGrid({"name": "test"}, 1)
    client._get.assert_called_with(
        "CreateGrid", params={"tariffGrid": {"name": "test"}, "resellerId": 1}
    )
    assert response == success_response


def test_tariff_create_grid_item(client):
    client._get.return_value = success_response
    response = client.Tariff.CreateGridItem({"name": "test"}, 1)
    client._get.assert_called_with(
        "CreateGridItem", params={"gridItem": {"name": "test"}, "resellerId": 1}
    )
    assert response == success_response


def test_tariff_delete_grid(client):
    client._get.return_value = success_response
    response = client.Tariff.DeleteGrid("test", 1)
    client._get.assert_called_with(
        "DeleteGrid", params={"name": "test", "resellerId": 1}
    )
    assert response == success_response


def test_tariff_delete_grid_item(client):
    client._get.return_value = success_response
    response = client.Tariff.DeleteGridItem("test", 1)
    client._get.assert_called_with(
        "DeleteGridItem", params={"name": "test", "resellerId": 1}
    )
    assert response == success_response


def test_tariff_edit_grid(client):
    client._get.return_value = success_response
    response = client.Tariff.EditGrid({"name": "test"}, 1)
    client._get.assert_called_with(
        "EditGrid", params={"tariffGrid": {"name": "test"}, "resellerId": 1}
    )
    assert response == success_response


def test_tariff_edit_grid_item(client):
    client._get.return_value = success_response
    response = client.Tariff.EditGridItem({"name": "test"}, 1)
    client._get.assert_called_with(
        "EditGridItem", params={"gridItem": {"name": "test"}, "resellerId": 1}
    )
    assert response == success_response


def test_tariff_get_grid_items(client):
    client._get.return_value = success_response
    response = client.Tariff.GetGridItems("test", 1)
    client._get.assert_called_with(
        "GetGridItems", params={"name": "test", "resellerId": 1}
    )
    assert response == success_response


def test_tariff_get_grids(client):
    client._get.return_value = success_response
    response = client.Tariff.GetGrids(["test1", "test2"], 1)
    client._get.assert_called_with(
        "GetGrids", params={"names": ["test1", "test2"], "resellerId": 1}
    )
    assert response == success_response
