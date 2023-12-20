import pytest
from datetime import datetime
from unittest.mock import patch, Mock
from jelastic.api import Billing

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        billing = Billing(session=Mock(), token="token")
        billing._get = mock_get
        yield billing


def test_add_account(client):
    client._get.return_value = success_response
    response = client.Account.AddAccount(123)
    client._get.assert_called_with("AddAccount", params={"uid": 123})
    assert response == success_response


def test_change_email(client):
    client._get.return_value = success_response
    response = client.Account.ChangeEmail("dummy@example.com", "new@example.com")
    client._get.assert_called_with(
        "ChangeEmail", params={"email": "new@example.com", "login": "dummy@example.com"}
    )
    assert response == success_response


def test_change_group(client):
    client._get.return_value = success_response
    response = client.Account.ChangeGroup("group", ["123", "456"], True)
    client._get.assert_called_with(
        "ChangeGroup",
        params={
            "groupName": "group",
            "uids": ["123", "456"],
            "sendEmail": True,
            "template": None,
        },
    )
    assert response == success_response


def test_change_phone_number(client):
    client._get.return_value = success_response
    response = client.Account.ChangePhoneNumber("dummy@example.com", "12346789")
    client._get.assert_called_with(
        "ChangePhoneNumber",
        params={
            "login": "dummy@example.com",
            "number": "12346789",
        },
    )
    assert response == success_response


def test_charge_account_by_uid(client):
    client._get.return_value = success_response
    response = client.Account.ChargeAccountByUid(123, 20.10, "comment", "env")
    client._get.assert_called_with(
        "ChargeAccountByUid",
        params={
            "uid": 123,
            "amount": 20.10,
            "description": "comment",
            "envName": "env",
        },
    )
    assert response == success_response


def test_convert_to_commercial(client):
    client._get.return_value = success_response
    response = client.Account.ConvertToCommercial({"uid": 123})
    client._get.assert_called_with(
        "ConvertToCommercial",
        params={
            "customer": '{"uid": 123}',
        },
    )

    assert response == success_response


def test_convert_to_commercial_and_pay(client):
    client._get.return_value = success_response
    response = client.Account.ConvertToCommercialAndPay(
        {"uid": 123}, "stripe", 1, 2, 30, "period"
    )
    client._get.assert_called_with(
        "ConvertToCommercialAndPay",
        params={
            "customer": '{"uid": 123}',
            "payMethodType": "stripe",
            "servicePlanId": 1,
            "autoServicePlanId": 2,
            "autoRefillMainBalance": 30,
            "autoRefillPeriod": "period",
        },
    )


def test_convert_to_trial(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.ConvertToTrial(
        "template", ["123", "456"], now, now, 1, 10, 100.25
    )
    client._get.assert_called_with(
        "ConvertToTrial",
        params={
            "template": "template",
            "uids": ["123", "456"],
            "startTime": now,
            "endTime": now,
            "start": 1,
            "count": 10,
            "bonus": 100.25,
        },
    )

    assert response == success_response


def test_enable_user(client):
    client._get.return_value = success_response
    response = client.Account.EnableUser(123)
    client._get.assert_called_with("EnableUser", params={"uid": 123})
    assert response == success_response


def test_export_account_billing_history_by_period(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.ExportAccountBillingHistoryByPeriod(
        now, now, "period", 10, True, "app_id"
    )
    client._get.assert_called_with(
        "ExportAccountBillingHistoryByPeriod",
        params={
            "startTime": now,
            "endTime": now,
            "period": "period",
            "timeOffset": 10,
            "groupNodes": True,
            "targetAppid": "app_id",
        },
    )
    assert response == success_response


def test_export_env_billing_history_by_period(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.ExportEnvBillingHistoryByPeriod(now, now, 10, "DAY", True)
    client._get.assert_called_with(
        "ExportEnvBillingHistoryByPeriod",
        params={
            "startTime": now,
            "endTime": now,
            "period": "DAY",
            "timeOffset": 10,
            "groupNodes": True,
        },
    )
    assert response == success_response


def test_fund_account(client):
    client._get.return_value = success_response
    response = client.Account.FundAccount(123, 20.10, True, "comment")
    client._get.assert_called_with(
        "FundAccount",
        params={
            "uid": 123,
            "amount": 20.10,
            "isBonus": True,
            "note": "comment",
        },
    )
    assert response == success_response


def test_fund_and_activate_account(client):
    client._get.return_value = success_response
    response = client.Account.FundAndActivateAccount(123, 20.10, "comment")
    client._get.assert_called_with(
        "FundAndActivateAccount",
        params={
            "uid": 123,
            "amount": 20.10,
            "note": "comment",
        },
    )
    assert response == success_response


def test_get_account(client):
    client._get.return_value = success_response
    response = client.Account.GetAccount()
    client._get.assert_called_with(
        "GetAccount",
    )
    assert response == success_response


def test_get_account_billing_by_engine_type_and_period(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.GetAccountBillingByEngineTypeAndPeriod(
        now, now, "123", ["vz4", "vz7"], "DAY", 10
    )
    client._get.assert_called_with(
        "GetAccountBillingByEngineTypeAndPeriod",
        params={
            "ownerUid": "123",
            "engineTypes": ["vz4", "vz7"],
            "startTime": now.strftime("%Y-%m-%d %H:%M:%S"),
            "endTime": now.strftime("%Y-%m-%d %H:%M:%S"),
            "period": "DAY",
            "timeOffset": 10,
        },
    )
    assert response == success_response


def test_get_account_billing_history_by_period(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.GetAccountBillingHistoryByPeriod(
        now, now, "DAY", 10, True, "app_id"
    )
    client._get.assert_called_with(
        "GetAccountBillingHistoryByPeriod",
        params={
            "startTime": now.strftime("%Y-%m-%d %H:%M:%S"),
            "endTime": now.strftime("%Y-%m-%d %H:%M:%S"),
            "period": "DAY",
            "timeOffset": 10,
            "groupNodes": True,
            "targetAppid": "app_id",
        },
    )
    assert response == success_response


def test_get_accounts(client):
    client._get.return_value = success_response
    response = client.Account.GetAccounts(
        "100", "name", "asc", "email", "dummy@example.com", 1, 50
    )
    client._get.assert_called_with(
        "GetAccounts",
        params={
            "lebalance": "100",
            "orderField": "name",
            "orderDirection": "asc",
            "filterField": "email",
            "filterValue": "dummy@example.com",
            "startRow": 1,
            "resultCount": 50,
        },
    )
    assert response == success_response


def test_get_accounts_by_limits(client):
    client._get.return_value = success_response
    response = client.Account.GetAccountsByLimits(["123", "456"])
    client._get.assert_called_with(
        "GetAccountsByLimits",
        params={
            "uidslimits": ["123", "456"],
        },
        delimiter=";",
    )
    assert response == success_response


def test_get_accounts_by_personal_threshold(client):
    client._get.return_value = success_response
    response = client.Account.GetAccountsByPersonalThreshold()
    client._get.assert_called_with(
        "GetAccountsByPersonalThreshold",
    )
    assert response == success_response


def test_get_accounts_by_uids(client):
    client._get.return_value = success_response
    response = client.Account.GetAccountsByUids(["123", "456"], "100")
    client._get.assert_called_with(
        "GetAccountsByUids",
        params={
            "uids": ["123", "456"],
            "lebalance": "100",
        },
    )
    assert response == success_response


def test_get_accounts_for_deactivation(client):
    client._get.return_value = success_response
    response = client.Account.GetAccountsForDeactivation()
    client._get.assert_called_with(
        "GetAccountsForDeactivation",
    )
    assert response == success_response


def test_get_accounts_for_destroying(client):
    client._get.return_value = success_response
    response = client.Account.GetAccountsForDestroying()
    client._get.assert_called_with(
        "GetAccountsForDestroying",
    )
    assert response == success_response


def test_get_agg_cluster_billing_history(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.GetAggClusterBillingHistory(now, now, 10, ["CPU"], True)
    client._get.assert_called_with(
        "GetAggClusterBillingHistory",
        params={
            "startTime": now,
            "endTime": now,
            "interval": 10,
            "sumFields": ["CPU"],
            "isPaid": True,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_agg_extra_billing_history(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.GetAggExtraBillingHistory(
        now, now, 10, False, "vz4", ["name1", "name2"]
    )
    client._get.assert_called_with(
        "GetAggExtraBillingHistory",
        params={
            "startTime": now,
            "endTime": now,
            "interval": 10,
            "isPaid": False,
            "type": "vz4",
            "names": ["name1", "name2"],
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_billing_info(client):
    client._get.return_value = success_response
    response = client.Account.GetBillingInfo()
    client._get.assert_called_with(
        "GetBillingInfo",
    )
    assert response == success_response


def test_get_cluster_billing_history(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.GetClusterBillingHistory(now, now, 10)
    client._get.assert_called_with(
        "GetClusterBillingHistory",
        params={
            "startTime": now,
            "endTime": now,
            "interval": 10,
        },
    )
    assert response == success_response


def test_get_collaboration_quotas(client):
    client._get.return_value = success_response
    response = client.Account.GetCollaborationQuotas(
        123, quota_names=["quota1", "quota2"]
    )
    client._get.assert_called_with(
        "GetCollaborationQuotas",
        params={
            "collaborationId": 123,
            "ownerUid": None,
            "quotaNames": ["quota1", "quota2"],
        },
    )
    assert response == success_response

    with pytest.raises(ValueError):
        client.Account.GetCollaborationQuotas(quota_names=["quota1", "quota2"])

    with pytest.raises(ValueError):
        client.Account.GetCollaborationQuotas(
            123, owner_uid=123, quota_names=["quota1", "quota2"]
        )


def test_get_countries(client):
    client._get.return_value = success_response
    response = client.Account.GetCountries()
    client._get.assert_called_with(
        "GetCountries",
    )
    assert response == success_response


def test_get_country_states(client):
    client._get.return_value = success_response
    response = client.Account.GetCountryStates("IN")
    client._get.assert_called_with(
        "GetCountryStates",
        params={"ccode": "IN"},
    )
    assert response == success_response


def test_get_env_billing_history_by_period(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.GetEnvBillingHistoryByPeriod(now, now, "period", 10, True)
    client._get.assert_called_with(
        "GetEnvBillingHistoryByPeriod",
        params={
            "startTime": now,
            "endTime": now,
            "period": "period",
            "timeOffset": 10,
            "groupNodes": True,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_extended_account_billing_history_by_period(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.GetExtendedAccountBillingHistoryByPeriod(
        now, now, "app_id"
    )
    client._get.assert_called_with(
        "GetExtendedAccountBillingHistoryByPeriod",
        params={
            "starttime": now,
            "endtime": now,
            "targetAppid": "app_id",
        },
    )
    assert response == success_response


def test_get_extern_billing_system_session(client):
    client._get.return_value = success_response
    response = client.Account.GetExternBillingSystemSession()
    client._get.assert_called_with(
        "GetExternBillingSystemSession",
    )
    assert response == success_response


def test_get_external_billing_systems(client):
    client._get.return_value = success_response
    response = client.Account.GetExternBillingSystems()
    client._get.assert_called_with(
        "GetExternBillingSystems",
    )
    assert response == success_response


def test_get_external_user_by_id(client):
    client._get.return_value = success_response
    response = client.Account.GetExternalUserById("123")
    client._get.assert_called_with(
        "GetExternalUserById",
        params={"id": "123"},
    )
    assert response == success_response


def test_get_fund_account_history(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.GetFundAccountHistory(now, now, 123)
    client._get.assert_called_with(
        "GetFundAccountHistory",
        params={
            "startTime": now,
            "endTime": now,
            "uid": 123,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_quotas(client):
    client._get.return_value = success_response
    response = client.Account.GetQuotas(["quota1", "quota2"])
    client._get.assert_called_with(
        "GetQuotas",
        params={
            "quotasnames": ["quota1", "quota2"],
        },
    )
    assert response == success_response


def test_get_sum(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.GetSum(
        123,
        now,
        now,
    )
    client._get.assert_called_with(
        "GetSum",
        params={
            "uid": 123,
            "startTime": now,
            "endTime": now,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_sum_account_billing_history(client):
    now = datetime.now()
    client._get.return_value = success_response
    response = client.Account.GetSumAccountBillingHistory(
        123,
        now,
        now,
        10,
    )
    client._get.assert_called_with(
        "GetSumAccountBillingHistory",
        params={
            "uid": 123,
            "startTime": now,
            "endTime": now,
            "bonus": 10,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_suspended_accounts(client):
    client._get.return_value = success_response
    response = client.Account.GetSuspendedAccounts()
    client._get.assert_called_with(
        "GetSuspendedAccounts",
    )
    assert response == success_response


def test_remove_quota(client):
    client._get.return_value = success_response
    response = client.Account.RemoveQuota(123, "quota1")
    client._get.assert_called_with(
        "RemoveQuota",
        params={
            "uid": 123,
            "name": "quota1",
        },
    )
    assert response == success_response


def test_reset_test_accounts(client):
    client._get.return_value = success_response
    response = client.Account.ResetTestAccounts()
    client._get.assert_called_with(
        "ResetTestAccounts",
    )
    assert response == success_response


def test_set_account_status(client):
    client._get.return_value = success_response
    response = client.Account.SetAccountStatus(123, 1)
    client._get.assert_called_with(
        "SetAccountStatus",
        params={
            "uid": 123,
            "status": 1,
        },
    )
    assert response == success_response


def test_set_billing_info(client):
    client._get.return_value = success_response
    response = client.Account.SetBillingInfo({"uid": 123})
    client._get.assert_called_with(
        "SetBillingInfo",
        params={
            "customer": {"uid": 123},
        },
    )
    assert response == success_response


def test_set_fund_note(client):
    client._get.return_value = success_response
    response = client.Account.SetFundNote(123, "note")
    client._get.assert_called_with(
        "SetFundNote",
        params={
            "id": 123,
            "note": "note",
        },
    )
    assert response == success_response


def test_set_group(client):
    client._get.return_value = success_response
    response = client.Account.SetGroup(123, "group", True, True)
    client._get.assert_called_with(
        "SetGroup",
        params={
            "uid": 123,
            "groupName": "group",
            "resetBalance": True,
            "resetBonus": True,
        },
    )
    assert response == success_response


def test_set_quota(client):
    client._get.return_value = success_response
    response = client.Account.SetQuota(123, "quota1", "10", 1)
    client._get.assert_called_with(
        "SetQuota",
        params={"uid": 123, "name": "quota1", "value": "10", "referenceId": 1},
    )
    assert response == success_response


def test_set_user_note(client):
    client._get.return_value = success_response
    response = client.Account.SetUserNote(123, "note")
    client._get.assert_called_with(
        "SetUserNote",
        params={
            "uid": 123,
            "note": "note",
        },
    )
    assert response == success_response


def test_surcharge_accounts(client):
    now = datetime.now().date()
    client._get.return_value = success_response
    response = client.Account.SurchargeAccounts(now, now)
    client._get.assert_called_with(
        "SurchargeAccounts",
        params={
            "startDate": now.strftime("%Y-%m-%d"),
            "endDate": now.strftime("%Y-%m-%d"),
        },
    )
    assert response == success_response


def test_suspend_user(client):
    client._get.return_value = success_response
    response = client.Account.SuspendUser(123)
    client._get.assert_called_with(
        "SuspendUser",
        params={
            "uid": 123,
        },
    )
    assert response == success_response


def test_unfund_account(client):
    client._get.return_value = success_response
    response = client.Account.UnfundAccount(123, 20.10, True, "comment")
    client._get.assert_called_with(
        "UnfundAccount",
        params={
            "uid": 123,
            "amount": 20.10,
            "isBonus": True,
            "note": "comment",
        },
    )
    assert response == success_response


def test_withdraw_accounts(client):
    now = datetime.now().date()
    client._get.return_value = success_response
    response = client.Account.WithdrawAccounts(now, now)
    client._get.assert_called_with(
        "WithdrawAccounts",
        params={
            "startDate": now.strftime("%Y-%m-%d"),
            "endDate": now.strftime("%Y-%m-%d"),
        },
    )
    assert response == success_response


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
        ["name1", "name2", "name3"],
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
            "tariffGridNames": ["name1", "name2", "name3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_resource(client):
    client._get.return_value = success_response
    response = client.Pricing.AddResource("resource")
    client._get.assert_called_with("AddResource", params={"resource": "resource"})
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
        }
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
            }
        },
        delimiter=",",
    )
    assert response == success_response


def test_attach_tariff(client):
    client._get.return_value = success_response
    response = client.Pricing.AttachTariff("name", "app_id")
    client._get.assert_called_with(
        "AttachTariff", params={"uniqName": "name", "targetAppId": "app_id"}
    )
    assert response == success_response


def test_attach_tariff_grid(client):
    client._get.return_value = success_response
    response = client.Pricing.AttachTariffGrid("name", "id")
    client._get.assert_called_with(
        "AttachTariffGrid",
        params={
            "tariffGridName": "name",
            "id": "id",
        },
    )
    assert response == success_response


def test_check_host_groups_allowed(client):
    client._get.return_value = success_response
    response = client.Pricing.CheckHostGroupsAllowed(
        [1, 2, 3],
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_with(
        "CheckHostGroupsAllowed",
        params={
            "ownerUid": [1, 2, 3],
            "hardwareNodeGroups": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_pricing(client):
    client._get.return_value = success_response
    response = client.Pricing.DeletePricing("id")
    client._get.assert_called_with("DeletePricing", params={"id": "id"})
    assert response == success_response


def test_delete_tariff(client):
    client._get.return_value = success_response
    response = client.Pricing.DeleteTariff("id")
    client._get.assert_called_with("DeleteTariff", params={"id": "id"})
    assert response == success_response


def test_detach_tariff(client):
    client._get.return_value = success_response
    response = client.Pricing.DetachTariff("name", "app id 1")
    client._get.assert_called_with(
        "DetachTariff", params={"uniqName": "name", "targetAppId": "app id 1"}
    )
    assert response == success_response


def test_detach_tariff_grid(client):
    client._get.return_value = success_response
    response = client.Pricing.DetachTariffGrid("grid 1", "id")
    client._get.assert_called_with(
        "DetachTariffGrid", params={"tariffGridName": "grid 1", "id": "id"}
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
        }
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
            }
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_resource(client):
    client._get.return_value = success_response
    response = client.Pricing.EditResource("resource")
    client._get.assert_called_with("EditResource", params={"resource": "resource"})
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
        }
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
            }
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_currencies(client):
    client._get.return_value = success_response
    response = client.Pricing.GetCurrencies(["USD", "INR"])
    client._get.assert_called_with(
        "GetCurrencies",
        params={"currency": ["USD", "INR"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_platform_currency(client):
    client._get.return_value = success_response
    response = client.Pricing.GetPlatformCurrency([1, 2, 3])
    client._get.assert_called_with(
        "GetPlatformCurrency",
        params={"resellerId": [1, 2, 3]},
        delimiter=",",
    )
    assert response == success_response


def test_get_pricing(client):
    client._get.return_value = success_response
    response = client.Pricing.GetPricing([1, 2, 3])
    client._get.assert_called_with(
        "GetPricing",
        params={"ownerUid": [1, 2, 3]},
        delimiter=",",
    )
    assert response == success_response


def test_get_pricing_inner(client):
    client._get.return_value = success_response
    response = client.Pricing.GetPricingInner([1, 2, 3])
    client._get.assert_called_with(
        "GetPricingInner",
        params={"resellerId": [1, 2, 3]},
        delimiter=",",
    )
    assert response == success_response


def test_get_resources(client):
    client._get.return_value = success_response
    response = client.Pricing.GetResources(
        [1, 2, 3],
        ["name1", "name2", "name3"],
    )
    client._get.assert_called_with(
        "GetResources",
        params={"id": [1, 2, 3], "name": ["name1", "name2", "name3"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_tariffs_inner(client):
    client._get.return_value = success_response
    response = client.Pricing.GetTariffsInner(
        ["pid1", "pid2", "pid3", "pid4"],
        ["type1", "type2", "type3", "type4"],
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "GetTariffsInner",
        params={
            "priceId": ["pid1", "pid2", "pid3", "pid4"],
            "type": ["type1", "type2", "type3", "type4"],
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_unique_resource_name(client):
    client._get.return_value = success_response
    response = client.Pricing.GetUniqueResourceNames()
    client._get.assert_called_with("GetUniqueResourceNames", params={})
    assert response == success_response


def test_set_tariff(client):
    client._get.return_value = success_response
    response = client.Pricing.SetTariffs(
        "pid",
        "tariff_id",
        ["name1", "name2", "name3"],
    )
    client._get.assert_called_with(
        "SetTariffs",
        params={
            "pricingId": "pid",
            "tariffIds": "tariff_id",
            "tariffGridNames": ["name1", "name2", "name3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_validate_environment(client):
    client._get.return_value = success_response
    response = client.Pricing.ValidateEnvironment("node", [1, 2, 3])
    client._get.assert_called_with(
        "ValidateEnvironment",
        params={
            "hardwareNodeGroup": "node",
            "ownerUid": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_test_validate_node(client):
    client._get.return_value = success_response
    response = client.Pricing.ValidateNode(
        1,
        "node",
        "node type",
        10,
        20,
    )
    client._get.assert_called_with(
        "ValidateNode",
        params={
            "uid": 1,
            "hardwareNodeGroup": "node",
            "nodeType": "node type",
            "fixedCloudlets": 10,
            "flexibleCloudlets": 20,
        },
    )
    assert response == success_response


def test_validate_node_inner(client):
    client._get.return_value = success_response
    response = client.Pricing.ValidateNodeInner(
        1,
        "node",
        "node type",
        10,
        20,
    )
    client._get.assert_called_with(
        "ValidateNodeInner",
        params={
            "uid": 1,
            "hardwareNodeGroup": "node",
            "nodeType": "node type",
            "fixedCloudlets": 10,
            "flexibleCloudlets": 20,
        },
    )
    assert response == success_response


def test_add_reseller(client):
    client._get.return_value = success_response
    response = client.Reseller.AddReseller(
        "reseller",
        "platform",
        "regions",
        ["setting1", "setting2", "setting3"],
    )
    client._get.assert_called_with(
        "AddReseller",
        params={
            "reseller": "reseller",
            "platform": "platform",
            "regions": "regions",
            "settings": ["setting1", "setting2", "setting3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_reseller(client):
    client._get.return_value = success_response
    response = client.Reseller.EditReseller(
        "reseller",
        "platform",
        ["region1", "region2", "region3"],
    )
    client._get.assert_called_with(
        "EditReseller",
        params={
            "reseller": "reseller",
            "platform": "platform",
            "regions": ["region1", "region2", "region3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_all_resellers(client):
    client._get.return_value = success_response
    response = client.Reseller.GetAllResellers()
    client._get.assert_called_with("GetAllResellers", params={})
    assert response == success_response


def test_get_reseller_by_app_id(client):
    client._get.return_value = success_response
    response = client.Reseller.GetResellerByAppid("app id")
    client._get.assert_called_with(
        "GetResellerByAppid", params={"targetAppid": "app id"}
    )
    assert response == success_response


def test_get_reseller_by_id(client):
    client._get.return_value = success_response
    response = client.Reseller.GetResellerById(1)
    client._get.assert_called_with("GetResellerById", params={"id": 1})
    assert response == success_response


def test_get_reseller_by_owner_uid(client):
    client._get.return_value = success_response
    response = client.Reseller.GetResellerByOwnerUid(1)
    client._get.assert_called_with("GetResellerByOwnerUid", params={"uid": 1})
    assert response == success_response


def test_get_reseller_by_uid(client):
    client._get.return_value = success_response
    response = client.Reseller.GetResellerByUid(1)
    client._get.assert_called_with("GetResellerByUid", params={"uid": 1})
    assert response == success_response


def test_remove_reseller(client):
    client._get.return_value = success_response
    response = client.Reseller.RemoveReseller(1)
    client._get.assert_called_with("RemoveReseller", params={"id": 1})
    assert response == success_response


def test_remove_reseller_status(client):
    client._get.return_value = success_response
    response = client.Reseller.SetResellerStatus(1, "status")
    client._get.assert_called_with(
        "SetResellerStatus", params={"id": 1, "status": "status"}
    )
    assert response == success_response
