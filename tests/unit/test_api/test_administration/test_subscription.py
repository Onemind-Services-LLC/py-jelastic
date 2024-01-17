from . import *


def test_add_category(client):
    client._get.return_value = success_response
    response = client.Subscription.AddCategory(
        {
            "category1": "val1",
            "category2": "val2",
            "category3": "val3",
            "category4": "val4",
            "category5": "val5",
        },
        1,
    )
    client._get.assert_called_with(
        "AddCategory",
        params={
            "category": {
                "category1": "val1",
                "category2": "val2",
                "category3": "val3",
                "category4": "val4",
                "category5": "val5",
            },
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_add_product(client):
    client._get.return_value = success_response
    response = client.Subscription.AddProduct(
        {
            "product1": "val1",
            "product2": "val2",
            "product3": "val3",
            "product4": "val4",
            "product5": "val5",
        },
        1,
    )
    client._get.assert_called_with(
        "AddProduct",
        params={
            "product": {
                "product1": "val1",
                "product2": "val2",
                "product3": "val3",
                "product4": "val4",
                "product5": "val5",
            },
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_add_service_plan(client):
    client._get.return_value = success_response
    response = client.Subscription.AddServicePlan(
        {
            "servicePlan1": "val1",
            "servicePlan2": "val2",
            "servicePlan3": "val3",
            "servicePlan4": "val4",
        },
        1,
        "exp",
    )
    client._get.assert_called_with(
        "AddServicePlan",
        params={
            "servicePlan": {
                "servicePlan1": "val1",
                "servicePlan2": "val2",
                "servicePlan3": "val3",
                "servicePlan4": "val4",
            },
            "resellerId": 1,
            "expandFields": "exp",
        },
    )
    assert response == success_response


def test_add_subscription_item_resource(client):
    client._get.return_value = success_response
    response = client.Subscription.AddSubscriptionItemResource(
        1,
        1,
        1,
        {
            "resource1": "val1",
            "resource2": "val2",
            "resource3": "val3",
            "resource4": "val4",
            "resource5": "val5",
        },
    )
    client._get.assert_called_with(
        "AddSubscriptionItemResource",
        params={
            "subscriptionId": 1,
            "itemId": 1,
            "itemResourceId": 1,
            "resources": {
                "resource1": "val1",
                "resource2": "val2",
                "resource3": "val3",
                "resource4": "val4",
                "resource5": "val5",
            },
        },
    )
    assert response == success_response


def test_adjust_product(client):
    client._get.return_value = success_response
    response = client.Subscription.AdjustProduct(1, 1, 1)
    client._get.assert_called_with(
        "AdjustProduct",
        params={
            "subscriptionId": 1,
            "itemId": 1,
            "itemResourceId": 1,
        },
    )
    assert response == success_response


def test_delete_category(client):
    client._get.return_value = success_response
    response = client.Subscription.DeleteCategory(1, 1)
    client._get.assert_called_with("DeleteCategory", params={"id": 1, "resellerId": 1})
    assert response == success_response


def test_delete_product(client):
    client._get.return_value = success_response
    response = client.Subscription.DeleteProduct(1, 1)
    client._get.assert_called_with("DeleteProduct", params={"id": 1, "resellerId": 1})
    assert response == success_response


def test_delete_service_plan(client):
    client._get.return_value = success_response
    response = client.Subscription.DeleteServicePlan(1, 1)
    client._get.assert_called_with(
        "DeleteServicePlan",
        params={
            "id": 1,
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_edit_category(client):
    client._get.return_value = success_response
    response = client.Subscription.EditCategory(1, 1)
    client._get.assert_called_with(
        "EditCategory",
        params={
            "category": 1,
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_edit_product(client):
    client._get.return_value = success_response
    response = client.Subscription.EditProduct(
        {
            "category1": "val1",
            "category2": "val2",
            "category3": "val3",
            "category4": "val4",
            "category5": "val5",
        },
        1,
    )
    client._get.assert_called_with(
        "EditProduct",
        params={
            "category": {
                "category1": "val1",
                "category2": "val2",
                "category3": "val3",
                "category4": "val4",
                "category5": "val5",
            },
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_edit_service_plan(client):
    client._get.return_value = success_response
    response = client.Subscription.EditServicePlan(
        {
            "service_plan1": "val1",
            "service_plan2": "val2",
            "service_plan3": "val3",
            "service_plan4": "val4",
            "service_plan5": "val5",
        },
        1,
        "exp",
    )
    client._get.assert_called_with(
        "EditServicePlan",
        params={
            "servicePlan": {
                "service_plan1": "val1",
                "service_plan2": "val2",
                "service_plan3": "val3",
                "service_plan4": "val4",
                "service_plan5": "val5",
            },
            "resellerId": 1,
            "expendFields": "exp",
        },
    )
    assert response == success_response


def test_get_categories(client):
    client._get.return_value = success_response
    response = client.Subscription.GetCategories(1, "exp")
    client._get.assert_called_with(
        "GetCategories", params={"resellerId": 1, "expendFields": "exp"}
    )
    assert response == success_response


def test_get_products(client):
    client._get.return_value = success_response
    response = client.Subscription.GetProducts(
        1,
        ["status1", "status2", "status3", "status4", "status5"],
        1,
        ["sub1", "sub2", "sub3", "sub4", "sub5"],
        "exp",
        1,
        1,
        "order",
        "direction",
    )
    client._get.assert_called_with(
        "GetProduct",
        params={
            "id": 1,
            "status": ["status1", "status2", "status3", "status4", "status5"],
            "resellerId": 1,
            "subscriptionStatus": ["sub1", "sub2", "sub3", "sub4", "sub5"],
            "expandFields": "exp",
            "startRow": 1,
            "resultCount": 1,
            "orderField": "order",
            "orderDirection": "direction",
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_service_plan(client):
    client._get.return_value = success_response
    response = client.Subscription.GetServicePlans(
        1,
        True,
        ["sub1", "sub2", "sub3", "sub4"],
        1,
        "exp",
        1,
    )
    client._get.assert_called_with(
        "GetServicePlans",
        params={
            "id": 1,
            "hasProducts": True,
            "subscriptionStatus": ["sub1", "sub2", "sub3", "sub4"],
            "productId": 1,
            "expandFields": "exp",
            "resellerId": 1,
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_subscriptions(client):
    client._get.return_value = success_response
    response = client.Subscription.GetSubscriptions(
        1,
        1,
        ["status1", "status2", "status3"],
        1,
        1,
        1,
        "exp",
        1,
        1,
        "field",
        "direction",
    )
    client._get.assert_called_with(
        "GetSubscriptions",
        params={
            "id": 1,
            "uid": 1,
            "status": ["status1", "status2", "status3"],
            "resellerId": 1,
            "productId": 1,
            "servicePlanId": 1,
            "expandFields": "exp",
            "startRow": 1,
            "resultCount": 1,
            "orderField": "field",
            "orderDirection": "direction",
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_category_published(client):
    client._get.return_value = success_response
    response = client.Subscription.SetCategoryPublished(1, True, 1)
    client._get.assert_called_with(
        "SetCategoryPublished",
        params={
            "id": 1,
            "published": True,
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_set_product_status(client):
    client._get.return_value = success_response
    response = client.Subscription.SetProductStatus(1, "status", 1)
    client._get.assert_called_with(
        "SetProductStatus", params={"id": 1, "status": "status", "resellerId": 1}
    )
    assert response == success_response


def test_set_service_plan_status(client):
    client._get.return_value = success_response
    response = client.Subscription.SetServicePlanStatus(1, "status", 1)
    client._get.assert_called_with(
        "SetServicePlanStatus", params={"id": 1, "status": "status", "resellerId": 1}
    )
    assert response == success_response


def test_terminate_subscription(client):
    client._get.return_value = success_response
    response = client.Subscription.TerminateSubscription(
        1,
        "password",
    )
    client._get.assert_called_with(
        "TerminateSubscription",
        params={
            "subscriptionId": 1,
            "password": "password",
        },
    )
    assert response == success_response
