from . import *


def test_add_pricing(client):
    client._get.return_value = success_response
    response = client.Pricing.AddPricing(
        {
            "amount1": 20.10,
            "amount2": 20.10,
            "amount3": 20.10,
            "amount4": 20.10,
            "amount5": 20.10,
            "amount6": 20.10,
        },
        "tariff_id_1",
        "name",
        "ruk",
    )
    client._get.assert_called_with(
        "AddPricing",
        params={
            "pricing": {
                "amount1": 20.10,
                "amount2": 20.10,
                "amount3": 20.10,
                "amount4": 20.10,
                "amount5": 20.10,
                "amount6": 20.10,
            },
            "tariffIds": "tariff_id_1",
            "tariffGridNames": "name",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_add_resource(client):
    client._get.return_value = success_response
    response = client.Pricing.AddResource("resource", "ruk")
    client._get.assert_called_with(
        "AddResource", params={"resource": "resource", "ruk": "ruk"}
    )
    assert response == success_response


def test_add_tariff(client):
    client._get.return_value = success_response
    response = client.Pricing.AddTariff(
        {
            "tariff1": "val1",
            "tariff2": "val2",
            "tariff3": "val3",
            "tariff4": "val4",
            "tariff5": "val5",
        },
        "ruk",
    )
    client._get.assert_called_with(
        "AddTariff",
        params={
            "tariff": {
                "tariff1": "val1",
                "tariff2": "val2",
                "tariff3": "val3",
                "tariff4": "val4",
                "tariff5": "val5",
            },
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_attach_tariff(client):
    client._get.return_value = success_response
    response = client.Pricing.AttachTariff("name", "app_id", "ruk")
    client._get.assert_called_with(
        "AttachTariff",
        params={"uniqName": "name", "targetAppId": "app_id", "ruk": "ruk"},
    )
    assert response == success_response


def test_attach_tariff_grid(client):
    client._get.return_value = success_response
    response = client.Pricing.AttachTariffGrid("name", "id", "ruk")
    client._get.assert_called_with(
        "AttachTariffGrid",
        params={"tariffGridName": "name", "id": "id", "ruk": "ruk"},
    )
    assert response == success_response


def test_check_host_groups_allowed(client):
    client._get.return_value = success_response
    response = client.Pricing.CheckHostGroupsAllowed(1, "group", "ruk")
    client._get.assert_called_with(
        "CheckHostGroupsAllowed",
        params={"ownerUid": 1, "hardwareNodeGroups": "group", "ruk": "ruk"},
    )
    assert response == success_response


def test_delete_pricing(client):
    client._get.return_value = success_response
    response = client.Pricing.DeletePricing("id", "ruk")
    client._get.assert_called_with("DeletePricing", params={"id": "id", "ruk": "ruk"})
    assert response == success_response


def test_delete_tariff(client):
    client._get.return_value = success_response
    response = client.Pricing.DeleteTariff("id", "ruk")
    client._get.assert_called_with("DeleteTariff", params={"id": "id", "ruk": "ruk"})
    assert response == success_response


def test_detach_tariff(client):
    client._get.return_value = success_response
    response = client.Pricing.DetachTariff("name", "app id 1", "ruk")
    client._get.assert_called_with(
        "DetachTariff",
        params={"uniqName": "name", "targetAppId": "app id 1", "ruk": "ruk"},
    )
    assert response == success_response


def test_detach_tariff_grid(client):
    client._get.return_value = success_response
    response = client.Pricing.DetachTariffGrid("grid 1", "id", "ruk")
    client._get.assert_called_with(
        "DetachTariffGrid",
        params={"tariffGridName": "grid 1", "id": "id", "ruk": "ruk"},
    )
    assert response == success_response


def test_edit_pricing(client):
    client._get.return_value = success_response
    response = client.Pricing.EditPricing(
        {
            "price1": 10.1,
            "price2": 10.1,
            "price3": 10.1,
            "price4": 10.1,
            "price5": 10.1,
        },
        "ruk",
    )
    client._get.assert_called_with(
        "EditPricing",
        params={
            "pricing": {
                "price1": 10.1,
                "price2": 10.1,
                "price3": 10.1,
                "price4": 10.1,
                "price5": 10.1,
            },
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_edit_resource(client):
    client._get.return_value = success_response
    response = client.Pricing.EditResource("resource", "ruk")
    client._get.assert_called_with(
        "EditResource", params={"resource": "resource", "ruk": "ruk"}
    )
    assert response == success_response


def test_edit_tariff(client):
    client._get.return_value = success_response
    response = client.Pricing.EditTariff(
        {
            "tariff1": "val1",
            "tariff2": "val2",
            "tariff3": "val3",
            "tariff4": "val4",
            "tariff5": "val5",
        },
        "ruk",
    )
    client._get.assert_called_with(
        "EditTariff",
        params={
            "tariff": {
                "tariff1": "val1",
                "tariff2": "val2",
                "tariff3": "val3",
                "tariff4": "val4",
                "tariff5": "val5",
            },
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_currencies(client):
    client._get.return_value = success_response
    response = client.Pricing.GetCurrencies("USD", "ruk")
    client._get.assert_called_with(
        "GetCurrencies", params={"currency": "USD", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_platform_currency(client):
    client._get.return_value = success_response
    response = client.Pricing.GetPlatformCurrency(1, "ruk")
    client._get.assert_called_with(
        "GetPlatformCurrency", params={"resellerId": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_get_pricing(client):
    client._get.return_value = success_response
    response = client.Pricing.GetPricing(1, "ruk")
    client._get.assert_called_with("GetPricing", params={"ownerUid": 1, "ruk": "ruk"})
    assert response == success_response


def test_get_pricing_inner(client):
    client._get.return_value = success_response
    response = client.Pricing.GetPricingInner(1, "ruk")
    client._get.assert_called_with(
        "GetPricingInner", params={"resellerId": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_get_resources(client):
    client._get.return_value = success_response
    response = client.Pricing.GetResources(1, "name", "ruk")
    client._get.assert_called_with(
        "GetResources", params={"id": 1, "name": "name", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_tariffs_inner(client):
    client._get.return_value = success_response
    response = client.Pricing.GetTariffsInner("pid", "type", 1, "ruk")
    client._get.assert_called_with(
        "GetTariffsInner",
        params={"priceId": "pid", "type": "type", "resellerId": 1, "ruk": "ruk"},
    )
    assert response == success_response


def test_get_unique_resource_name(client):
    client._get.return_value = success_response
    response = client.Pricing.GetUniqueResourceNames("ruk")
    client._get.assert_called_with("GetUniqueResourceNames", params={"ruk": "ruk"})
    assert response == success_response


def test_set_tariff(client):
    client._get.return_value = success_response
    response = client.Pricing.SetTariffs("pid", "tariff_id", "name", "ruk")
    client._get.assert_called_with(
        "SetTariffs",
        params={
            "pricingId": "pid",
            "tariffIds": "tariff_id",
            "tariffGridNames": "name",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_validate_environment(client):
    client._get.return_value = success_response
    response = client.Pricing.ValidateEnvironment("node", 1, "ruk")
    client._get.assert_called_with(
        "ValidateEnvironment",
        params={"hardwareNodeGroup": "node", "ownerUid": 1, "ruk": "ruk"},
    )
    assert response == success_response


def test_test_validate_node(client):
    client._get.return_value = success_response
    response = client.Pricing.ValidateNode(1, "node", "node type", 10, 20, "ruk")
    client._get.assert_called_with(
        "ValidateNode",
        params={
            "uid": 1,
            "hardwareNodeGroup": "node",
            "nodeType": "node type",
            "fixedCloudlets": 10,
            "flexibleCloudlets": 20,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_validate_node_inner(client):
    client._get.return_value = success_response
    response = client.Pricing.ValidateNodeInner(1, "node", "node type", 10, 20, "ruk")
    client._get.assert_called_with(
        "ValidateNodeInner",
        params={
            "uid": 1,
            "hardwareNodeGroup": "node",
            "nodeType": "node type",
            "fixedCloudlets": 10,
            "flexibleCloudlets": 20,
            "ruk": "ruk",
        },
    )
    assert response == success_response
