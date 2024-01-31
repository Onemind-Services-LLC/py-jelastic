from . import *


def test_get_fraud_check_url(client):
    client._get.return_value = success_response
    response = client.Order.GetFraudCheckUrl("ruk")
    client._get.assert_called_with("GetFraudCheckUrl", params={"ruk": "ruk"})
    assert response == success_response


def test_get_history_url(client):
    client._get.return_value = success_response
    response = client.Order.GetHistoryUrl("ruk")
    client._get.assert_called_with("GetHistoryUrl", params={"ruk": "ruk"})
    assert response == success_response


def test_get_orders(client):
    client._get.return_value = success_response
    response = client.Order.GetOrders("status", "ruk")
    client._get.assert_called_with(
        "GetOrders",
        params={"status": "status", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_url_supplying_cookies_for_history_url(client):
    client._get.return_value = success_response
    response = client.Order.GetUrlSupplyingCookiesForHistoryUrl("ruk")
    client._get.assert_called_with(
        "GetUrlSupplyingCookiesForHistoryUrl", params={"ruk": "ruk"}
    )
    assert response == success_response


def test_order_event(client):
    client._get.return_value = success_response
    response = client.Order.OrderEvent("order_id", "event_type", "ruk")
    client._get.assert_called_with(
        "OrderEvent",
        params={"externOrderId": "order_id", "eventType": "event_type", "ruk": "ruk"},
    )
    assert response == success_response


def test_pay_service_plan(client):
    client._get.return_value = success_response
    response = client.Order.PayServicePlan(1, "payment_method", "ruk")
    client._get.assert_called_with(
        "PayServicePlan",
        params={"servicePlanId": 1, "payMethodId": "payment_method", "ruk": "ruk"},
    )
    assert response == success_response
