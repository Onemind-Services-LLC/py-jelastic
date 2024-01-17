from . import *


def test_create_level_auto_pay(client):
    client._get.return_value = success_response
    response = client.ServicePlan.CreateLevelAutoPay(
        1000,
        CURRENT_DATETIME,
        10,
        "online",
        5,
    )
    client._get.assert_called_with(
        "CreateLevelAutoPay",
        params={
            "minBalance": 1000,
            "expires": CURRENT_DATETIME,
            "servicePlanId": 10,
            "paymentMethodId": "online",
            "minPeriod": 5,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_create_regular_auto_pay(client):
    client._get.return_value = success_response
    response = client.ServicePlan.CreateRegularAutoPay(
        "exp",
        CURRENT_DATETIME,
        "GMT+4",
        1,
        "online",
    )
    client._get.assert_called_with(
        "CreateRegularAutoPay",
        params={
            "cronExpression": "exp",
            "expires": CURRENT_DATETIME,
            "timeZone": "GMT+4",
            "servicePlanId": 1,
            "paymentMethodId": "online",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_create_service_plan(client):
    client._get.return_value = success_response
    response = client.ServicePlan.CreateServicePlan(
        "name",
        "description",
        "one-time",
        "ext1",
    )
    client._get.assert_called_with(
        "CreateServicePlan",
        params={
            "name": "name",
            "description": "description",
            "servicePlanType": "one-time",
            "externPlanId": "ext1",
        },
    )
    assert response == success_response


def test_delete_auto_pay(client):
    client._get.return_value = success_response
    response = client.ServicePlan.DeleteAutoPay(1)
    client._get.assert_called_with("DeleteAutoPay", params={"autoPayId": 1})
    assert response == success_response


def test_delete_service_plan(client):
    client._get.return_value = success_response
    response = client.ServicePlan.DeleteServicePlan(1)
    client._get.assert_called_with("DeleteServicePlan", params={"servicePlanId": 1})
    assert response == success_response


def test_enable_service_plan(client):
    client._get.return_value = success_response
    response = client.ServicePlan.EnableServicePlan(1, 1)
    client._get.assert_called_with(
        "EnableServicePlan", params={"servicePlanId": 1, "enabled": 1}
    )
    assert response == success_response


def test_extended_create_service_plan(client):
    client._get.return_value = success_response
    response = client.ServicePlan.ExtendedCreateServicePlan(
        "label",
        "ext1",
        "description",
        True,
        "type",
        True,
        "1000",
    )
    client._get.assert_called_with(
        "ExtendedCreateServicePlan",
        params={
            "label": "label",
            "externalPlanId": "ext1",
            "description": "description",
            "enabled": True,
            "type": "type",
            "byDefault": True,
            "price": "1000",
        },
    )
    assert response == success_response


def test_extended_get_service_plans(client):
    client._get.return_value = success_response
    response = client.ServicePlan.ExtendedGetServicePlans()
    client._get.assert_called_with("ExtendedGetServicePlans", params={})
    assert response == success_response


def test_extended_get_service_plan_update(client):
    client._get.return_value = success_response
    response = client.ServicePlan.ExtendedServicePlanUpdate(
        1,
        "label",
        "ext1",
        "description",
        True,
        "type",
        True,
        "1000",
    )
    client._get.assert_called_with(
        "ExtendedServicePlanUpdate",
        params={
            "id": 1,
            "label": "label",
            "externalPlanId": "ext1",
            "description": "description",
            "enabled": True,
            "type": "type",
            "byDefault": True,
            "price": "1000",
        },
    )
    assert response == success_response


def test_get_auto_pay_history(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetAutoPayHistory(1)
    client._get.assert_called_with("GetAutoPayHistory", params={"autoPayId": 1})
    assert response == success_response


def test_get_auto_pays(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetAutoPays()
    client._get.assert_called_with("GetAutoPays", params={})
    assert response == success_response


def test_get_bought_service_plans(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetBoughtServicePlans()
    client._get.assert_called_with("GetBoughtServicePlans", params={})
    assert response == success_response


def test_get_currency(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetCurrency()
    client._get.assert_called_with("GetCurrency", params={})
    assert response == success_response


def test_get_final_cost(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetFinalCost(1)
    client._get.assert_called_with("GetFinalCost", params={"servicePlanId": 1})
    assert response == success_response


def test_get_payment_method_list(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetPayMethodList()
    client._get.assert_called_with("GetPayMethodList", params={})
    assert response == success_response


def test_get_payment_news(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetPaymentNews()
    client._get.assert_called_with("GetPaymentNews", params={})
    assert response == success_response


def test_get_service_plan(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetServicePlan(1)
    client._get.assert_called_with("GetServicePlan", params={"servicePlanId": 1})
    assert response == success_response


def test_get_service_plan_by_type(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetServicePlanByType("planType")
    client._get.assert_called_with(
        "GetServicePlanByType", params={"planType": "planType"}
    )
    assert response == success_response


def test_payment_news_read(client):
    client._get.return_value = success_response
    response = client.ServicePlan.PaymentNewsRead("id")
    client._get.assert_called_with("PaymentNewsRead", params={"id": "id"})
    assert response == success_response


def test_set_extern_plan_id(client):
    client._get.return_value = success_response
    response = client.ServicePlan.SetExternPlanId(1, "externalPlanId")
    client._get.assert_called_with(
        "SetExternPlanId",
        params={"servicePlanId": 1, "externalPlanId": "externalPlanId"},
    )
    assert response == success_response


def test_update_service_plan(client):
    client._get.return_value = success_response
    response = client.ServicePlan.UpdateServicePlan(
        1,
        "name",
        "description",
        "ext1",
    )
    client._get.assert_called_with(
        "UpdateServicePlan",
        params={
            "servicePlanId": 1,
            "name": "name",
            "description": "description",
            "externServicePlanId": "ext1",
        },
    )
    assert response == success_response
