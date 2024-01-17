from . import *


def test_enable_pay_method(client):
    client._get.return_value = success_response
    response = client.PayMethod.EnablePayMethod("pid1", 1)
    client._get.assert_called_with(
        "EnablePayMethod", params={"payMethodId": "pid1", "enable": 1}
    )
    assert response == success_response


def test_get_default_pay_method(client):
    client._get.return_value = success_response
    response = client.PayMethod.GetDefaultPayMethod()
    client._get.assert_called_with("GetDefaultPayMethod", params={})
    assert response == success_response


def test_get_public_token(client):
    client._get.return_value = success_response
    response = client.PayMethod.GetPublicToken()
    client._get.assert_called_with("GetPublicToken", params={})
    assert response == success_response


def test_get_valid_pay_types(client):
    client._get.return_value = success_response
    response = client.PayMethod.GetValidPayTypes()
    client._get.assert_called_with("GetValidPayTypes", params={})
    assert response == success_response


def test_register_bank_card(client):
    client._get.return_value = success_response
    response = client.PayMethod.RegisterBankCard(
        "f_name",
        "l_name",
        "1111-1111-1111-1111",
        "123",
        8,
        24,
        1,
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
        },
    )
    assert response == success_response


def test_register_pay_method_and_pay(client):
    client._get.return_value = success_response
    response = client.PayMethod.RegisterPayMethodAndPay("pay type", 1, 1, 500, "WEEK")
    client._get.assert_called_with(
        "RegisterPayMethodAndPay",
        params={
            "payMethodType": "pay type",
            "servicePlanId": 1,
            "autoServicePlanId": 1,
            "autoRefillMinBalance": 500,
            "autoRefillPeriod": "WEEK",
        },
    )
    assert response == success_response


def test_set_default_pay_method(client):
    client._get.return_value = success_response
    response = client.PayMethod.SetDefaultPayMethod("pay method")
    client._get.assert_called_with(
        "SetDefaultPayMethod", params={"payMethodId": "pay method"}
    )
    assert response == success_response


def test_setup_intent(client):
    client._get.return_value = success_response
    response = client.PayMethod.SetupIntent("type")
    client._get.assert_called_with("SetupIntent", params={"paymentMethodType": "type"})
    assert response == success_response
