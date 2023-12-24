import datetime
from unittest.mock import patch, Mock

import pytest

from jelastic.api import Administration

CURRENT_DATETIME = datetime.datetime.now()
success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        jc = Administration(session=Mock(), token="token")
        jc._get = mock_get
        yield jc


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
        [1, 2, 3, 4],
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
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
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
        [1, 2, 3, 4],
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
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
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
        [1, 2, 3, 4],
        ["exp1", "exp2", "exp3", "exp4"],
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
            "resellerId": [1, 2, 3, 4],
            "expandFields": ["exp1", "exp2", "exp3", "exp4"],
        },
        delimiter=",",
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
        delimiter=",",
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
    response = client.Subscription.DeleteCategory(1, [1, 2, 3, 4])
    client._get.assert_called_with(
        "DeleteCategory",
        params={
            "id": 1,
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_product(client):
    client._get.return_value = success_response
    response = client.Subscription.DeleteProduct(1, [1, 2, 3, 4])
    client._get.assert_called_with(
        "DeleteProduct",
        params={
            "id": 1,
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_service_plan(client):
    client._get.return_value = success_response
    response = client.Subscription.DeleteServicePlan(1, [1, 2, 3, 4])
    client._get.assert_called_with(
        "DeleteServicePlan",
        params={
            "id": 1,
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_category(client):
    client._get.return_value = success_response
    response = client.Subscription.EditCategory(1, [1, 2, 3, 4])
    client._get.assert_called_with(
        "EditCategory",
        params={
            "category": 1,
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
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
        [1, 2, 3, 4],
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
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
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
        [1, 2, 3, 4, 5],
        ["exp1", "exp2", "exp3", "exp4", "exp5"],
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
            "resellerId": [1, 2, 3, 4, 5],
            "expendFields": ["exp1", "exp2", "exp3", "exp4", "exp5"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_categories(client):
    client._get.return_value = success_response
    response = client.Subscription.GetCategories(
        [1, 2, 3, 4], ["exp1", "exp2", "exp3", "exp4"]
    )
    client._get.assert_called_with(
        "GetCategories",
        params={
            "resellerId": [1, 2, 3, 4],
            "expendFields": ["exp1", "exp2", "exp3", "exp4"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_products(client):
    client._get.return_value = success_response
    response = client.Subscription.GetProducts(
        [1, 2, 3, 4, 5],
        ["status1", "status2", "status3", "status4", "status5"],
        [1, 2, 3, 4, 5],
        ["sub1", "sub2", "sub3", "sub4", "sub5"],
        ["exp1", "exp2", "exp3", "exp4"],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ["order1", "order2", "order3", "order4", "order5"],
        ["direction1", "direction2", "direction3", "direction4", "direction5"],
    )
    client._get.assert_called_with(
        "GetProduct",
        params={
            "id": [1, 2, 3, 4, 5],
            "status": ["status1", "status2", "status3", "status4", "status5"],
            "resellerId": [1, 2, 3, 4, 5],
            "subscriptionStatus": ["sub1", "sub2", "sub3", "sub4", "sub5"],
            "expandFields": ["exp1", "exp2", "exp3", "exp4"],
            "startRow": [1, 2, 3, 4, 5],
            "resultCount": [1, 2, 3, 4, 5],
            "orderField": ["order1", "order2", "order3", "order4", "order5"],
            "orderDirection": [
                "direction1",
                "direction2",
                "direction3",
                "direction4",
                "direction5",
            ],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_service_plan(client):
    client._get.return_value = success_response
    response = client.Subscription.GetServicePlans(
        [1, 2, 3, 4],
        [True, False, True, False],
        ["sub1", "sub2", "sub3", "sub4"],
        [1, 2, 3, 4],
        ["exp1", "exp2", "exp3", "exp4"],
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "GetServicePlans",
        params={
            "id": [1, 2, 3, 4],
            "hasProducts": [True, False, True, False],
            "subscriptionStatus": ["sub1", "sub2", "sub3", "sub4"],
            "productId": [1, 2, 3, 4],
            "expandFields": ["exp1", "exp2", "exp3", "exp4"],
            "resellerId": [1, 2, 3, 4],
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
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        ["exp1", "exp2", "exp3"],
        [1, 2, 3],
        [1, 2, 3],
        ["field1", "field2", "field3"],
        ["direction1", "direction2", "direction3"],
    )
    client._get.assert_called_with(
        "GetSubscriptions",
        params={
            "id": [1, 2, 3],
            "uid": [1, 2, 3],
            "status": ["status1", "status2", "status3"],
            "resellerId": [1, 2, 3],
            "productId": [1, 2, 3],
            "servicePlanId": [1, 2, 3],
            "expandFields": ["exp1", "exp2", "exp3"],
            "startRow": [1, 2, 3],
            "resultCount": [1, 2, 3],
            "orderField": ["field1", "field2", "field3"],
            "orderDirection": ["direction1", "direction2", "direction3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_category_published(client):
    client._get.return_value = success_response
    response = client.Subscription.SetCategoryPublished(1, True, [1, 2, 3])
    client._get.assert_called_with(
        "SetCategoryPublished",
        params={
            "id": 1,
            "published": True,
            "resellerId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_product_status(client):
    client._get.return_value = success_response
    response = client.Subscription.SetProductStatus(1, "status", [1, 2, 3])
    client._get.assert_called_with(
        "SetProductStatus",
        params={
            "id": 1,
            "status": "status",
            "resellerId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_service_plan_status(client):
    client._get.return_value = success_response
    response = client.Subscription.SetServicePlanStatus(1, "status", [1, 2, 3])
    client._get.assert_called_with(
        "SetServicePlanStatus",
        params={
            "id": 1,
            "status": "status",
            "resellerId": [1, 2, 3],
        },
        delimiter=",",
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
