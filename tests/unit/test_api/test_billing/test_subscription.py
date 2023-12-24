from . import *


def test_cancel(client):
    client._get.return_value = success_response
    response = client.Subscription.Cancel(
        1,
        [True, False, True],
        ["2022-11-11", "2022-11-11", "2022-11-11"],
        ["pf1", "pf2", "pf3"],
        ["exp1", "exp2", "exp3"],
    )
    client._get.assert_called_with(
        "Cancel",
        params={
            "id": 1,
            "immediately": [True, False, True],
            "cancelDate": ["2022-11-11", "2022-11-11", "2022-11-11"],
            "passphrase": ["pf1", "pf2", "pf3"],
            "expandFields": ["exp1", "exp2", "exp3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_clone_product(client):
    client._get.return_value = success_response
    response = client.Subscription.CloneProduct(
        1,
        1,
        "env",
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "CloneProduct",
        params={
            "subscriptionId": 1,
            "itemResource": 1,
            "targetEnvName": "env",
            "itemId": [1, 2, 3, 4],
        },
        delimiter=",",
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
    response = client.Subscription.GetCategories(
        ["category1", "category2", "category3"]
    )
    client._get.assert_called_with(
        "GetCategories",
        params={"expandFields": ["category1", "category2", "category3"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_products(client):
    client._get.return_value = success_response
    response = client.Subscription.GetProducts(
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        ["exp1", "exp2", "exp3", "exp4"],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        ["field1", "field2", "field3", "field4"],
        ["dir1", "dir2", "dir3", "dir4"],
    )
    client._get.assert_called_with(
        "GetProducts",
        params={
            "id": [1, 2, 3, 4],
            "categoryId": [1, 2, 3, 4],
            "expandFields": ["exp1", "exp2", "exp3", "exp4"],
            "startRow": [1, 2, 3, 4],
            "resultCount": [1, 2, 3, 4],
            "orderField": ["field1", "field2", "field3", "field4"],
            "orderDirection": ["dir1", "dir2", "dir3", "dir4"],
        },
        delimiter=",",
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
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        ["exp1", "exp2", "exp3", "exp4"],
    )
    client._get.assert_called_with(
        "GetServicePlans",
        params={
            "id": [1, 2, 3, 4],
            "productId": [1, 2, 3, 4],
            "expandFields": ["exp1", "exp2", "exp3", "exp4"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_subscriptions(client):
    client._get.return_value = success_response
    response = client.Subscription.GetSubscriptions(
        [1, 2, 3],
        [1, 2, 3],
        ["status1", "status2", "status3"],
        ["exp1", "exp2", "exp3"],
        [1, 2, 3],
        [1, 2, 3],
        ["order1", "order2", "order3"],
        ["direction1", "direction2", "direction3"],
    )
    client._get.assert_called_with(
        "GetSubscriptions",
        params={
            "id": [1, 2, 3],
            "productId": [1, 2, 3],
            "status": ["status1", "status2", "status3"],
            "expandFields": ["exp1", "exp2", "exp3"],
            "startRow": [1, 2, 3],
            "resultCount": [1, 2, 3],
            "orderField": ["order1", "order2", "order3"],
            "orderDirection": ["direction1", "direction2", "direction3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_install_product(client):
    client._get.return_value = success_response
    response = client.Subscription.InstallProduct(
        1,
        [1, 2, 3],
        ["setting1", "setting2", "setting3"],
        ["env1", "env2", "env3"],
        ["name1", "name2", "name3"],
        ["group1", "group2", "group3"],
        ["region1", "region2", "region3"],
        ["lang1", "lang2", "lang3"],
    )
    client._get.assert_called_with(
        "InstallProduct",
        params={
            "subscriptionId": 1,
            "itemId": [1, 2, 3],
            "settings": ["setting1", "setting2", "setting3"],
            "envName": ["env1", "env2", "env3"],
            "displayName": ["name1", "name2", "name3"],
            "envGroups": ["group1", "group2", "group3"],
            "region": ["region1", "region2", "region3"],
            "lang": ["lang1", "lang2", "lang3"],
        },
        delimiter=",",
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
        [1, 2, 3],
    )
    client._get.assert_called_with(
        "MoveProduct",
        params={
            "subscriptionId": 1,
            "itemResourceId": 1,
            "targetSubscriptionId": 1,
            "targetItemId": 1,
            "passphrase": "passphrase",
            "itemId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_autopay(client):
    client._get.return_value = success_response
    response = client.Subscription.SetAutopay(
        1,
        True,
        ["exp1", "exp2", "exp3"],
    )
    client._get.assert_called_with(
        "SetAutopay",
        params={
            "id": 1,
            "enabled": True,
            "expandFields": ["exp1", "exp2", "exp3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_subscribe(client):
    client._get.return_value = success_response
    response = client.Subscription.Subscribe(
        1,
        "item",
        [True, False, True],
        ["exp1", "exp2", "exp3"],
    )
    client._get.assert_called_with(
        "Subscribe",
        params={
            "productId": 1,
            "items": "item",
            "chargeAutomatically": [True, False, True],
            "expandFields": ["exp1", "exp2", "exp3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_undo_cancel(client):
    client._get.return_value = success_response
    response = client.Subscription.UndoCancel(
        1,
        ["exp1", "exp2", "exp3"],
    )
    client._get.assert_called_with(
        "UndoCancel",
        params={
            "id": 1,
            "expandFields": ["exp1", "exp2", "exp3"],
        },
        delimiter=",",
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
    response = client.Subscription.UpdateSubscription(
        1,
        1,
        1,
        ["exp1", "exp2", "exp3"],
    )
    client._get.assert_called_with(
        "UpdateSubscription",
        params={
            "subscriptionId": 1,
            "itemId": 1,
            "quantity": 1,
            "expandFields": ["exp1", "exp2", "exp3"],
        },
        delimiter=",",
    )
    assert response == success_response
