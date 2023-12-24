from . import *


def test_add_reseller(client):
    client._get.return_value = success_response
    response = client.Reseller.AddReseller(
        "reseller",
        "platform",
        "regions",
        ["setting1", "setting2", "setting3"],
    )
    client._get.assert_called_with(
        "AddReseller",
        params={
            "reseller": "reseller",
            "platform": "platform",
            "regions": "regions",
            "settings": ["setting1", "setting2", "setting3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_reseller(client):
    client._get.return_value = success_response
    response = client.Reseller.EditReseller(
        "reseller",
        "platform",
        ["region1", "region2", "region3"],
    )
    client._get.assert_called_with(
        "EditReseller",
        params={
            "reseller": "reseller",
            "platform": "platform",
            "regions": ["region1", "region2", "region3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_all_resellers(client):
    client._get.return_value = success_response
    response = client.Reseller.GetAllResellers()
    client._get.assert_called_with("GetAllResellers", params={})
    assert response == success_response


def test_get_reseller_by_app_id(client):
    client._get.return_value = success_response
    response = client.Reseller.GetResellerByAppid("app id")
    client._get.assert_called_with(
        "GetResellerByAppid", params={"targetAppid": "app id"}
    )
    assert response == success_response


def test_get_reseller_by_id(client):
    client._get.return_value = success_response
    response = client.Reseller.GetResellerById(1)
    client._get.assert_called_with("GetResellerById", params={"id": 1})
    assert response == success_response


def test_get_reseller_by_owner_uid(client):
    client._get.return_value = success_response
    response = client.Reseller.GetResellerByOwnerUid(1)
    client._get.assert_called_with("GetResellerByOwnerUid", params={"uid": 1})
    assert response == success_response


def test_get_reseller_by_uid(client):
    client._get.return_value = success_response
    response = client.Reseller.GetResellerByUid(1)
    client._get.assert_called_with("GetResellerByUid", params={"uid": 1})
    assert response == success_response


def test_remove_reseller(client):
    client._get.return_value = success_response
    response = client.Reseller.RemoveReseller(1)
    client._get.assert_called_with("RemoveReseller", params={"id": 1})
    assert response == success_response


def test_remove_reseller_status(client):
    client._get.return_value = success_response
    response = client.Reseller.SetResellerStatus(1, "status")
    client._get.assert_called_with(
        "SetResellerStatus", params={"id": 1, "status": "status"}
    )
    assert response == success_response
