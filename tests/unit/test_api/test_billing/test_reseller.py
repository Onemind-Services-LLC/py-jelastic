from . import *


def test_add_reseller(client):
    client._get.return_value = success_response
    response = client.Reseller.AddReseller(
        "reseller", "platform", "regions", "settings", "ruk"
    )
    client._get.assert_called_with(
        "AddReseller",
        params={
            "reseller": "reseller",
            "platform": "platform",
            "regions": "regions",
            "settings": "settings",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_edit_reseller(client):
    client._get.return_value = success_response
    response = client.Reseller.EditReseller("reseller", "platform", "regions", "ruk")
    client._get.assert_called_with(
        "EditReseller",
        params={
            "reseller": "reseller",
            "platform": "platform",
            "regions": "regions",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_all_resellers(client):
    client._get.return_value = success_response
    response = client.Reseller.GetAllResellers("ruk")
    client._get.assert_called_with("GetAllResellers", params={"ruk": "ruk"})
    assert response == success_response


def test_get_reseller_by_app_id(client):
    client._get.return_value = success_response
    response = client.Reseller.GetResellerByAppid("app id", "ruk")
    client._get.assert_called_with(
        "GetResellerByAppid", params={"targetAppid": "app id", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_reseller_by_id(client):
    client._get.return_value = success_response
    response = client.Reseller.GetResellerById(1, "ruk")
    client._get.assert_called_with("GetResellerById", params={"id": 1, "ruk": "ruk"})
    assert response == success_response


def test_get_reseller_by_owner_uid(client):
    client._get.return_value = success_response
    response = client.Reseller.GetResellerByOwnerUid(1, "ruk")
    client._get.assert_called_with(
        "GetResellerByOwnerUid", params={"uid": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_get_reseller_by_uid(client):
    client._get.return_value = success_response
    response = client.Reseller.GetResellerByUid(1, "ruk")
    client._get.assert_called_with("GetResellerByUid", params={"uid": 1, "ruk": "ruk"})
    assert response == success_response


def test_remove_reseller(client):
    client._get.return_value = success_response
    response = client.Reseller.RemoveReseller(1, "ruk")
    client._get.assert_called_with("RemoveReseller", params={"id": 1, "ruk": "ruk"})
    assert response == success_response


def test_remove_reseller_status(client):
    client._get.return_value = success_response
    response = client.Reseller.SetResellerStatus(1, "status", "ruk")
    client._get.assert_called_with(
        "SetResellerStatus", params={"id": 1, "status": "status", "ruk": "ruk"}
    )
    assert response == success_response
