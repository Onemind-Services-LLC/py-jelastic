from . import *


def test_cancel(client):
    client._get.return_value = success_response
    response = client.Subscription.Cancel(1, True, CURRENT_DATETIME.date(), "pf", "exp")
    client._get.assert_called_with(
        "Cancel",
        params={
            "id": 1,
            "immediately": True,
            "cancelDate": CURRENT_DATETIME.date(),
            "passphrase": "pf",
            "expandFields": "exp",
        },
        datetime_format="%Y-%m-%d",
    )
    assert response == success_response


def test_clone_product(client):
    client._get.return_value = success_response
    response = client.Subscription.CloneProduct(
        1,
        1,
        "env",
        1,
    )
    client._get.assert_called_with(
        "CloneProduct",
        params={
            "subscriptionId": 1,
            "itemResource": 1,
            "targetEnvName": "env",
            "itemId": 1,
        },
    )
    assert response == success_response


def test_discard_update_subscription(client):
    client._get.return_value = success_response
    response = client.Subscription.DiscardUpdateSubscription(1)
    client._get.assert_called_with(
        "DiscardUpdateSubscription", params={"subscriptionId": 1}
    )
    assert response == success_response


def test_get_categories(client):
    client._get.return_value = success_response
    response = client.Subscription.GetCategories("category")
    client._get.assert_called_with("GetCategories", params={"expandFields": "category"})
    assert response == success_response


def test_get_products(client):
    client._get.return_value = success_response
    response = client.Subscription.GetProducts(1, 1, "exp", 1, 1, "field", "dir")
    client._get.assert_called_with(
        "GetProducts",
        params={
            "id": 1,
            "categoryId": 1,
            "expandFields": "exp",
            "startRow": 1,
            "resultCount": 1,
            "orderField": "field",
            "orderDirection": "dir",
        },
    )
    assert response == success_response


def test_get_get_restricted_hard_node_groups(client):
    client._get.return_value = success_response
    response = client.Subscription.GetRestrictedHardNodeGroups(1)
    client._get.assert_called_with(
        "GetHardNodeGroups",
        params={
            "subscriptionItemId": 1,
        },
    )
    assert response == success_response


def test_get_service_plans(client):
    client._get.return_value = success_response
    response = client.Subscription.GetServicePlans(
        1,
        1,
        "exp",
    )
    client._get.assert_called_with(
        "GetServicePlans", params={"id": 1, "productId": 1, "expandFields": "exp"}
    )
    assert response == success_response


def test_get_subscriptions(client):
    client._get.return_value = success_response
    response = client.Subscription.GetSubscriptions(
        1, 1, ["status1", "status2", "status3"], "exp", 1, 1, "order", "direction"
    )
    client._get.assert_called_with(
        "GetSubscriptions",
        params={
            "id": 1,
            "productId": 1,
            "status": ["status1", "status2", "status3"],
            "expandFields": "exp",
            "startRow": 1,
            "resultCount": 1,
            "orderField": "order",
            "orderDirection": "direction",
        },
        delimiter=",",
    )
    assert response == success_response


def test_install_product(client):
    client._get.return_value = success_response
    response = client.Subscription.InstallProduct(
        1, 1, "settings", "env", "name", "group", "region", "lang"
    )
    client._get.assert_called_with(
        "InstallProduct",
        params={
            "subscriptionId": 1,
            "itemId": 1,
            "settings": "settings",
            "envName": "env",
            "displayName": "name",
            "envGroups": "group",
            "region": "region",
            "lang": "lang",
        },
    )
    assert response == success_response


def test_move_product(client):
    client._get.return_value = success_response
    response = client.Subscription.MoveProduct(
        1,
        1,
        1,
        1,
        "passphrase",
        1,
    )
    client._get.assert_called_with(
        "MoveProduct",
        params={
            "subscriptionId": 1,
            "itemResourceId": 1,
            "targetSubscriptionId": 1,
            "targetItemId": 1,
            "passphrase": "passphrase",
            "itemId": 1,
        },
    )
    assert response == success_response


def test_set_autopay(client):
    client._get.return_value = success_response
    response = client.Subscription.SetAutopay(1, True, "exp")
    client._get.assert_called_with(
        "SetAutopay", params={"id": 1, "enabled": True, "expandFields": "exp"}
    )
    assert response == success_response


def test_subscribe(client):
    client._get.return_value = success_response
    response = client.Subscription.Subscribe(
        1,
        "item",
        True,
        "exp",
    )
    client._get.assert_called_with(
        "Subscribe",
        params={
            "productId": 1,
            "items": "item",
            "chargeAutomatically": True,
            "expandFields": "exp",
        },
    )
    assert response == success_response


def test_undo_cancel(client):
    client._get.return_value = success_response
    response = client.Subscription.UndoCancel(1, "exp")
    client._get.assert_called_with(
        "UndoCancel",
        params={"id": 1, "expandFields": "exp"},
    )
    assert response == success_response


def test_uninstall_product(client):
    client._get.return_value = success_response
    response = client.Subscription.UninstallProduct(1, 1, 1, "passphrase")
    client._get.assert_called_with(
        "UninstallProduct",
        params={
            "subscriptionId": 1,
            "itemId": 1,
            "itemResourceId": 1,
            "passphrase": "passphrase",
        },
    )
    assert response == success_response


def test_upcoming_invoice(client):
    client._get.return_value = success_response
    response = client.Subscription.UpcomingInvoice(1, 1, 1)
    client._get.assert_called_with(
        "UpcomingInvoice",
        params={
            "subscriptionId": 1,
            "itemId": 1,
            "quantity": 1,
        },
    )
    assert response == success_response


def test_update_subscription(client):
    client._get.return_value = success_response
    response = client.Subscription.UpdateSubscription(1, 1, 1, "exp")
    client._get.assert_called_with(
        "UpdateSubscription",
        params={"subscriptionId": 1, "itemId": 1, "quantity": 1, "expandFields": "exp"},
    )
    assert response == success_response
