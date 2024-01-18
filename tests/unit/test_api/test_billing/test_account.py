import pytest
from . import *


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
    client._get.return_value = success_response
    response = client.Account.ConvertToTrial(
        "template", ["123", "456"], CURRENT_DATETIME, CURRENT_DATETIME, 1, 10, 100.25
    )
    client._get.assert_called_with(
        "ConvertToTrial",
        params={
            "template": "template",
            "uids": ["123", "456"],
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
            "start": 1,
            "count": 10,
            "bonus": 100.25,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )

    assert response == success_response


def test_enable_user(client):
    client._get.return_value = success_response
    response = client.Account.EnableUser(123)
    client._get.assert_called_with("EnableUser", params={"uid": 123})
    assert response == success_response


def test_export_account_billing_history_by_period(client):
    client._get.return_value = success_response
    response = client.Account.ExportAccountBillingHistoryByPeriod(
        CURRENT_DATETIME, CURRENT_DATETIME, "period", 10, True, "app_id"
    )
    client._get.assert_called_with(
        "ExportAccountBillingHistoryByPeriod",
        params={
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
            "period": "period",
            "timeOffset": 10,
            "groupNodes": True,
            "targetAppid": "app_id",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_export_env_billing_history_by_period(client):
    client._get.return_value = success_response
    response = client.Account.ExportEnvBillingHistoryByPeriod(
        CURRENT_DATETIME, CURRENT_DATETIME, 10, "DAY", True
    )
    client._get.assert_called_with(
        "ExportEnvBillingHistoryByPeriod",
        params={
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
            "period": "DAY",
            "timeOffset": 10,
            "groupNodes": True,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
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
    client._get.return_value = success_response
    response = client.Account.GetAccountBillingByEngineTypeAndPeriod(
        CURRENT_DATETIME, CURRENT_DATETIME, "123", ["vz4", "vz7"], "DAY", 10
    )
    client._get.assert_called_with(
        "GetAccountBillingByEngineTypeAndPeriod",
        params={
            "ownerUid": "123",
            "engineTypes": ["vz4", "vz7"],
            "startTime": CURRENT_DATETIME.strftime("%Y-%m-%d %H:%M:%S"),
            "endTime": CURRENT_DATETIME.strftime("%Y-%m-%d %H:%M:%S"),
            "period": "DAY",
            "timeOffset": 10,
        },
    )
    assert response == success_response


def test_get_account_billing_history_by_period(client):
    client._get.return_value = success_response
    response = client.Account.GetAccountBillingHistoryByPeriod(
        CURRENT_DATETIME, CURRENT_DATETIME, "DAY", 10, True, "app_id"
    )
    client._get.assert_called_with(
        "GetAccountBillingHistoryByPeriod",
        params={
            "startTime": CURRENT_DATETIME.strftime("%Y-%m-%d %H:%M:%S"),
            "endTime": CURRENT_DATETIME.strftime("%Y-%m-%d %H:%M:%S"),
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
    client._get.return_value = success_response
    response = client.Account.GetAggClusterBillingHistory(
        CURRENT_DATETIME, CURRENT_DATETIME, 10, ["CPU"], True
    )
    client._get.assert_called_with(
        "GetAggClusterBillingHistory",
        params={
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
            "interval": 10,
            "sumFields": ["CPU"],
            "isPaid": True,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_agg_extra_billing_history(client):
    client._get.return_value = success_response
    response = client.Account.GetAggExtraBillingHistory(
        CURRENT_DATETIME, CURRENT_DATETIME, 10, False, "vz4", ["name1", "name2"]
    )
    client._get.assert_called_with(
        "GetAggExtraBillingHistory",
        params={
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
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
    client._get.return_value = success_response
    response = client.Account.GetClusterBillingHistory(
        CURRENT_DATETIME, CURRENT_DATETIME, 10
    )
    client._get.assert_called_with(
        "GetClusterBillingHistory",
        params={
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
            "interval": 10,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
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
    client._get.return_value = success_response
    response = client.Account.GetEnvBillingHistoryByPeriod(
        CURRENT_DATETIME, CURRENT_DATETIME, "period", 10, True
    )
    client._get.assert_called_with(
        "GetEnvBillingHistoryByPeriod",
        params={
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
            "period": "period",
            "timeOffset": 10,
            "groupNodes": True,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_extended_account_billing_history_by_period(client):
    client._get.return_value = success_response
    response = client.Account.GetExtendedAccountBillingHistoryByPeriod(
        CURRENT_DATETIME, CURRENT_DATETIME, "app_id"
    )
    client._get.assert_called_with(
        "GetExtendedAccountBillingHistoryByPeriod",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "targetAppid": "app_id",
        },
        datetime_format="%Y-%m-%d",
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
    client._get.return_value = success_response
    response = client.Account.GetFundAccountHistory(
        CURRENT_DATETIME, CURRENT_DATETIME, 123
    )
    client._get.assert_called_with(
        "GetFundAccountHistory",
        params={
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
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
    client._get.return_value = success_response
    response = client.Account.GetSum(
        123,
        CURRENT_DATETIME,
        CURRENT_DATETIME,
    )
    client._get.assert_called_with(
        "GetSum",
        params={
            "uid": 123,
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_sum_account_billing_history(client):
    client._get.return_value = success_response
    response = client.Account.GetSumAccountBillingHistory(
        123,
        CURRENT_DATETIME,
        CURRENT_DATETIME,
        10,
    )
    client._get.assert_called_with(
        "GetSumAccountBillingHistory",
        params={
            "uid": 123,
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
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
    client._get.return_value = success_response
    response = client.Account.SurchargeAccounts(CURRENT_DATETIME, CURRENT_DATETIME)
    client._get.assert_called_with(
        "SurchargeAccounts",
        params={
            "startDate": CURRENT_DATETIME.strftime("%Y-%m-%d"),
            "endDate": CURRENT_DATETIME.strftime("%Y-%m-%d"),
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
    client._get.return_value = success_response
    response = client.Account.WithdrawAccounts(CURRENT_DATETIME, CURRENT_DATETIME)
    client._get.assert_called_with(
        "WithdrawAccounts",
        params={
            "startDate": CURRENT_DATETIME.strftime("%Y-%m-%d"),
            "endDate": CURRENT_DATETIME.strftime("%Y-%m-%d"),
        },
    )
    assert response == success_response
