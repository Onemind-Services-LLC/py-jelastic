from . import *


def test_enable_pay_method(client):
    client._get.return_value = success_response
    response = client.PayMethod.EnablePayMethod("pid1", 1, "ruk")
    client._get.assert_called_with(
        "EnablePayMethod", params={"payMethodId": "pid1", "enable": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_get_default_pay_method(client):
    client._get.return_value = success_response
    response = client.PayMethod.GetDefaultPayMethod("ruk")
    client._get.assert_called_with("GetDefaultPayMethod", params={"ruk": "ruk"})
    assert response == success_response


def test_get_public_token(client):
    client._get.return_value = success_response
    response = client.PayMethod.GetPublicToken("ruk")
    client._get.assert_called_with("GetPublicToken", params={"ruk": "ruk"})
    assert response == success_response


def test_get_valid_pay_types(client):
    client._get.return_value = success_response
    response = client.PayMethod.GetValidPayTypes("ruk")
    client._get.assert_called_with("GetValidPayTypes", params={"ruk": "ruk"})
    assert response == success_response


def test_register_bank_card(client):
    client._get.return_value = success_response
    response = client.PayMethod.RegisterBankCard(
        "f_name", "l_name", "1111-1111-1111-1111", "123", 8, 24, 1, "ruk"
    )
    client._get.assert_called_with(
        "RegisterBankCard",
        params={
            "firstName": "f_name",
            "lastName": "l_name",
            "cardNumber": "1111-1111-1111-1111",
            "cardCode": "123",
            "expireMonth": 8,
            "expireYear": 24,
            "servicePlanId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_register_pay_method_and_pay(client):
    client._get.return_value = success_response
    response = client.PayMethod.RegisterPayMethodAndPay(
        "pay type", 1, 1, 500, "WEEK", "ruk"
    )
    client._get.assert_called_with(
        "RegisterPayMethodAndPay",
        params={
            "payMethodType": "pay type",
            "servicePlanId": 1,
            "autoServicePlanId": 1,
            "autoRefillMinBalance": 500,
            "autoRefillPeriod": "WEEK",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_set_default_pay_method(client):
    client._get.return_value = success_response
    response = client.PayMethod.SetDefaultPayMethod("pay method", "ruk")
    client._get.assert_called_with(
        "SetDefaultPayMethod", params={"payMethodId": "pay method", "ruk": "ruk"}
    )
    assert response == success_response


def test_setup_intent(client):
    client._get.return_value = success_response
    response = client.PayMethod.SetupIntent("type", "ruk")
    client._get.assert_called_with(
        "SetupIntent", params={"paymentMethodType": "type", "ruk": "ruk"}
    )
    assert response == success_response
