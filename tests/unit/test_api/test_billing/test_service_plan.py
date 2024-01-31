from . import *


def test_create_level_auto_pay(client):
    client._get.return_value = success_response
    response = client.ServicePlan.CreateLevelAutoPay(
        1000, CURRENT_DATETIME, 10, "online", 5, "ruk"
    )
    client._get.assert_called_with(
        "CreateLevelAutoPay",
        params={
            "minBalance": 1000,
            "expires": CURRENT_DATETIME,
            "servicePlanId": 10,
            "paymentMethodId": "online",
            "minPeriod": 5,
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_create_regular_auto_pay(client):
    client._get.return_value = success_response
    response = client.ServicePlan.CreateRegularAutoPay(
        "exp", CURRENT_DATETIME, "GMT+4", 1, "online", "ruk"
    )
    client._get.assert_called_with(
        "CreateRegularAutoPay",
        params={
            "cronExpression": "exp",
            "expires": CURRENT_DATETIME,
            "timeZone": "GMT+4",
            "servicePlanId": 1,
            "paymentMethodId": "online",
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_create_service_plan(client):
    client._get.return_value = success_response
    response = client.ServicePlan.CreateServicePlan(
        "name", "description", "one-time", "ext1", "ruk"
    )
    client._get.assert_called_with(
        "CreateServicePlan",
        params={
            "name": "name",
            "description": "description",
            "servicePlanType": "one-time",
            "externPlanId": "ext1",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_delete_auto_pay(client):
    client._get.return_value = success_response
    response = client.ServicePlan.DeleteAutoPay(1, "ruk")
    client._get.assert_called_with(
        "DeleteAutoPay", params={"autoPayId": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_delete_service_plan(client):
    client._get.return_value = success_response
    response = client.ServicePlan.DeleteServicePlan(1, "ruk")
    client._get.assert_called_with(
        "DeleteServicePlan", params={"servicePlanId": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_enable_service_plan(client):
    client._get.return_value = success_response
    response = client.ServicePlan.EnableServicePlan(1, 1, "ruk")
    client._get.assert_called_with(
        "EnableServicePlan", params={"servicePlanId": 1, "enabled": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_extended_create_service_plan(client):
    client._get.return_value = success_response
    response = client.ServicePlan.ExtendedCreateServicePlan(
        "label", "ext1", "description", True, "type", True, "1000", "ruk"
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
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_extended_get_service_plans(client):
    client._get.return_value = success_response
    response = client.ServicePlan.ExtendedGetServicePlans("ruk")
    client._get.assert_called_with("ExtendedGetServicePlans", params={"ruk": "ruk"})
    assert response == success_response


def test_extended_get_service_plan_update(client):
    client._get.return_value = success_response
    response = client.ServicePlan.ExtendedServicePlanUpdate(
        1, "label", "ext1", "description", True, "type", True, "1000", "ruk"
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
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_auto_pay_history(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetAutoPayHistory(1, "ruk")
    client._get.assert_called_with(
        "GetAutoPayHistory", params={"autoPayId": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_get_auto_pays(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetAutoPays("ruk")
    client._get.assert_called_with("GetAutoPays", params={"ruk": "ruk"})
    assert response == success_response


def test_get_bought_service_plans(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetBoughtServicePlans("ruk")
    client._get.assert_called_with("GetBoughtServicePlans", params={"ruk": "ruk"})
    assert response == success_response


def test_get_currency(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetCurrency("ruk")
    client._get.assert_called_with("GetCurrency", params={"ruk": "ruk"})
    assert response == success_response


def test_get_final_cost(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetFinalCost(1, "ruk")
    client._get.assert_called_with(
        "GetFinalCost", params={"servicePlanId": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_get_payment_method_list(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetPayMethodList("ruk")
    client._get.assert_called_with("GetPayMethodList", params={"ruk": "ruk"})
    assert response == success_response


def test_get_payment_news(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetPaymentNews("ruk")
    client._get.assert_called_with("GetPaymentNews", params={"ruk": "ruk"})
    assert response == success_response


def test_get_service_plan(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetServicePlan(1, "ruk")
    client._get.assert_called_with(
        "GetServicePlan", params={"servicePlanId": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_get_service_plan_by_type(client):
    client._get.return_value = success_response
    response = client.ServicePlan.GetServicePlanByType("planType", "ruk")
    client._get.assert_called_with(
        "GetServicePlanByType", params={"planType": "planType", "ruk": "ruk"}
    )
    assert response == success_response


def test_payment_news_read(client):
    client._get.return_value = success_response
    response = client.ServicePlan.PaymentNewsRead("id", "ruk")
    client._get.assert_called_with("PaymentNewsRead", params={"id": "id", "ruk": "ruk"})
    assert response == success_response


def test_set_extern_plan_id(client):
    client._get.return_value = success_response
    response = client.ServicePlan.SetExternPlanId(1, "externalPlanId", "ruk")
    client._get.assert_called_with(
        "SetExternPlanId",
        params={"servicePlanId": 1, "externalPlanId": "externalPlanId", "ruk": "ruk"},
    )
    assert response == success_response


def test_update_service_plan(client):
    client._get.return_value = success_response
    response = client.ServicePlan.UpdateServicePlan(
        1, "name", "description", "ext1", "ruk"
    )
    client._get.assert_called_with(
        "UpdateServicePlan",
        params={
            "servicePlanId": 1,
            "name": "name",
            "description": "description",
            "externServicePlanId": "ext1",
            "ruk": "ruk",
        },
    )
    assert response == success_response
