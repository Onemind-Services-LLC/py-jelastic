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


def test_event(client):
    client._get.return_value = success_response
    response = client.Invoice.Event("id_1", "type_1")
    client._get.assert_called_with(
        "Event", params={"externId": "id_1", "eventType": "type_1"}
    )
    assert response == success_response


def test_get_external_invoices(client):
    client._get.return_value = success_response
    response = client.Invoice.GetExternalInvoices(
        [1, 2, 3, 4],
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "ExternalInvoices",
        params={
            "limit": [1, 2, 3, 4],
            "ownerUid": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_invoices(client):
    client._get.return_value = success_response
    response = client.Invoice.GetInvoices(
        [1, 2, 3],
        ["uname1", "uname2", "uname3"],
        ["type1", "type2", "type3"],
        ["status1", "status2", "status3"],
        [1, 2, 3],
        ["sub_status1", "sub_status2", "sub_status3"],
        ["field1", "field2", "field3"],
        ["direction1", "direction2", "direction3"],
        [1, 2, 3],
        [1, 2, 3],
        ["exp_fields1", "exp_fields2", "exp_fields3"],
    )
    client._get.assert_called_with(
        "GetInvoices",
        params={
            "id": [1, 2, 3],
            "uniqueName": ["uname1", "uname2", "uname3"],
            "type": ["type1", "type2", "type3"],
            "status": ["status1", "status2", "status3"],
            "subscriptionId": [1, 2, 3],
            "subscriptionStatus": ["sub_status1", "sub_status2", "sub_status3"],
            "orderFields": ["field1", "field2", "field3"],
            "orderDirection": ["direction1", "direction2", "direction3"],
            "startRow": [1, 2, 3],
            "resultCount": [1, 2, 3],
            "expandFields": ["exp_fields1", "exp_fields2", "exp_fields3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_make_invoice(client):
    client._get.return_value = success_response
    response = client.Invoice.MakeInvoice(
        "uid1",
        [True, False, True],
    )
    client._get.assert_called_with(
        "MakeInvoice",
        params={
            "uid": "uid1",
            "skipPay": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_mark_as_paid(client):
    client._get.return_value = success_response
    response = client.Invoice.MarkAsPaid(
        [1, 2, 3],
        ["envoice1", "envoice2", "envoice3"],
    )
    client._get.assert_called_with(
        "MarkAsPaid",
        params={
            "id": [1, 2, 3],
            "ebsInvoiceId": ["envoice1", "envoice2", "envoice3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_mark_as_void(client):
    client._get.return_value = success_response
    response = client.Invoice.MarkAsVoid(
        [1, 2, 3],
        ["envoice1", "envoice2", "envoice3"],
    )
    client._get.assert_called_with(
        "MarkAsVoid",
        params={
            "id": [1, 2, 3],
            "ebsInvoiceId": ["envoice1", "envoice2", "envoice3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_pay(client):
    client._get.return_value = success_response
    response = client.Invoice.Pay(
        1,
        ["pid1", "pid2", "pid3"],
        ["type1", "type2", "type3"],
    )
    client._get.assert_called_with(
        "Pay",
        params={
            "id": 1,
            "paymentMethodId": ["pid1", "pid2", "pid3"],
            "paymentMethodType": ["type1", "type2", "type3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_search_invoices(client):
    client._get.return_value = success_response
    response = client.Invoice.SearchInvoices(
        "search",
        ["field1", "field2", "field3"],
        [1, 2, 3],
    )
    client._get.assert_called_with(
        "SearchInvoices",
        params={
            "search": "search",
            "expandFields": ["field1", "field2", "field3"],
            "resellerId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.AddGroup(
        "type",
        "group name",
        ["description1", "description2", "description3"],
        ["source group 1", "source group 2", "source group 3"],
        ["domain 1", "domain 2", "domain 3"],
        ["conversion group 1", "conversion group 2", "conversion group 3"],
    )
    client._get.assert_called_with(
        "AddGroup",
        params={
            "type": "type",
            "name": "group name",
            "description": ["description1", "description2", "description3"],
            "sourceGroupName": ["source group 1", "source group 2", "source group 3"],
            "domain": ["domain 1", "domain 2", "domain 3"],
            "conversionGroup": [
                "conversion group 1",
                "conversion group 2",
                "conversion group 3",
            ],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_quota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.AddQuota(
        "name",
        ["description1", "description2", "description3"],
        ["rid 1", "rid 2", "rid 3"],
        [1, 2, 3],
        [True, False, True],
    )
    client._get.assert_called_with(
        "AddQuota",
        params={
            "name": "name",
            "description": ["description1", "description2", "description3"],
            "referenceId": ["rid 1", "rid 2", "rid 3"],
            "defaultValue": [1, 2, 3],
            "assignToGroup": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.DeleteGroup("name")
    client._get.assert_called_with("DeleteGroup", params={"name": "name"})
    assert response == success_response


def test_edit_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.EditGroup(
        "name",
        ["new name 1", "new name 2", "new name 3"],
        ["description1", "description2", "description3"],
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_with(
        "EditGroup",
        params={
            "name": "name",
            "newName": ["new name 1", "new name 2", "new name 3"],
            "description": ["description1", "description2", "description3"],
            "conversionGroup": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_quota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.EditQuota(
        "name",
        ["rid 1", "rid 2", "rid 3"],
        ["new rid 1", "new rid 2", "new rid 3"],
        ["description1", "description2", "description3"],
    )
    client._get.assert_called_with(
        "EditQuota",
        params={
            "name": "name",
            "referenceId": ["rid 1", "rid 2", "rid 3"],
            "newReferenceId": ["new rid 1", "new rid 2", "new rid 3"],
            "description": ["description1", "description2", "description3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_group_quotas(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetGroupQuotas(
        "name",
        ["quota 1", "quota 2", "quota 3"],
    )
    client._get.assert_called_with(
        "GetGroupQuotas",
        params={
            "name": "name",
            "quotasnames": ["quota 1", "quota 2", "quota 3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_groups(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetGroups()
    client._get.assert_called_with("GetGroups", params={})
    assert response == success_response


def test_pricing_models(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetPricingModels("name")
    client._get.assert_called_with("GetPricingModels", params={"groupName": "name"})
    assert response == success_response


def test_get_quotas_GroupQuota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetQuotas()
    client._get.assert_called_with("GetQuotas", params={})
    assert response == success_response


def test_is_domain_bound(client):
    client._get.return_value = success_response
    response = client.GroupQuota.IsDomainBound(
        ["checksum 1", "checksum 2", "checksum"],
    )
    client._get.assert_called_with(
        "IsDomainBound",
        params={"checksum": ["checksum 1", "checksum 2", "checksum"]},
        delimiter=",",
    )
    assert response == success_response


def test_remove_groupQuota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.RemoveGroupQuota(
        "group name",
        "quota name",
    )
    client._get.assert_called_with(
        "RemoveGroupQuota",
        params={
            "groupName": "group name",
            "quotaName": "quota name",
        },
    )
    assert response == success_response


def test_remove_quota_GroupQuota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.RemoveQuota(
        "name",
        [True, False, True],
        ["rid 1", "rid 2", "rid 3"],
    )
    client._get.assert_called_with(
        "RemoveQuota",
        params={
            "name": "name",
            "force": [True, False, True],
            "referenceId": ["rid 1", "rid 2", "rid 3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_collaboration_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetCollaborationGroup("name")
    client._get.assert_called_with("SetCollaborationGroup", params={"name": "name"})
    assert response == success_response


def test_set_default_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetDefaultGroup("name")
    client._get.assert_called_with("DefaultGroup", params={"name": "name"})
    assert response == success_response


def test_set_group_quota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetGroupQuota(
        "name",
        "quota name",
        1,
        ["rid 1", "rid 2", "rid 3"],
    )
    client._get.assert_called_with(
        "SetGroupQuota",
        params={
            "groupName": "name",
            "quotaName": "quota name",
            "value": 1,
            "referenceId": ["rid 1", "rid 2", "rid 3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_pricing_models(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetPricingModels("name", "data")
    client._get.assert_called_with(
        "SetPricingModel", params={"groupName": "name", "data": "data"}
    )
    assert response == success_response


def test_set_win_domain(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetWinDomain("name", 1)
    client._get.assert_called_with(
        "SetWinDomain", params={"groupName": "name", "winDomainId": 1}
    )
    assert response == success_response


def test_unassign_hd_node_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.UnassignHdNodeGroup("group", "checksum")
    client._get.assert_called_with(
        "UnassignHdNodeGroup",
        params={
            "hardwareNodeGroup": "group",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_get_invoice_url(client):
    client._get.return_value = success_response
    response = client.Integration.GetInvoiceUrl(1)
    client._get.assert_called_with("GetInvoiceUrl", params={"invoiceId": 1})
    assert response == success_response


def test_get_sso_url(client):
    client._get.return_value = success_response
    response = client.Integration.GetSSOUrl(
        ["path 1", "path 2"],
    )
    client._get.assert_called_with(
        "GetSSOUrl",
        params={
            "path": ["path 1", "path 2"],
        },
    )
    assert response == success_response


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
    response = client.PayMethod.RegisterPayMethodAndPay(
        "pay type",
        1,
        [1, 1, 0],
        [500, 500, 500],
        ["WEEK", "MONTH", "WEEK"],
    )
    client._get.assert_called_with(
        "RegisterPayMethodAndPay",
        params={
            "payMethodType": "pay type",
            "servicePlanId": 1,
            "autoServicePlanId": [1, 1, 0],
            "autoRefillMinBalance": [500, 500, 500],
            "autoRefillPeriod": ["WEEK", "MONTH", "WEEK"],
        },
        delimiter=",",
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
    response = client.PayMethod.SetupIntent(["type1", "type2", "type3"])
    client._get.assert_called_with(
        "SetupIntent",
        params={"paymentMethodType": ["type1", "type2", "type3"]},
        delimiter=",",
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


def test_create_level_auto_pay(client):
    client._get.return_value = success_response
    response = client.ServicePlan.CreateLevelAutoPay(
        1000,
        "2024-11-11",
        10,
        "online",
        5,
    )
    client._get.assert_called_with(
        "CreateLevelAutoPay",
        params={
            "minBalance": 1000,
            "expires": "2024-11-11",
            "servicePlanId": 10,
            "paymentMethodId": "online",
            "minPeriod": 5,
        },
    )
    assert response == success_response


def test_create_regular_auto_pay(client):
    client._get.return_value = success_response
    response = client.ServicePlan.CreateRegularAutoPay(
        "exp",
        "2024-11-11",
        "GMT+4",
        1,
        "online",
    )
    client._get.assert_called_with(
        "CreateRegularAutoPay",
        params={
            "cronExpression": "exp",
            "expires": "2024-11-11",
            "timeZone": "GMT+4",
            "servicePlanId": 1,
            "paymentMethodId": "online",
        },
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
    response = client.ServicePlan.GetServicePlanByType([1, 2, 3])
    client._get.assert_called_with(
        "GetServicePlanByType", params={"planType": [1, 2, 3]}
    )
    assert response == success_response


def test_payment_news_read(client):
    client._get.return_value = success_response
    response = client.ServicePlan.PaymentNewsRead(1)
    client._get.assert_called_with("PaymentNewsRead", params={"id": 1})
    assert response == success_response


def test_set_extern_plan_id(client):
    client._get.return_value = success_response
    response = client.ServicePlan.SetExternPlanId(1, 1)
    client._get.assert_called_with(
        "SetExternPlanId",
        params={
            "servicePlanId": 1,
            "externalPlanId": 1,
        },
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


def test_add_stats(client):
    client._get.return_value = success_response
    response = client.Order.AddStats(
        "resource",
        1,
        1,
        ["2022-11-11", "2022-11-22", "2022-11-21"],
        ["2022-11-22", "2022-11-12", "2022-11-13"],
        ["env1", "env2", "env3"],
        [1, 2, 3],
        ["note1", "note2", "note3"],
        ["value1", "value2", "value3"],
    )
    client._get.assert_called_with(
        "AddStats",
        params={
            "resourceName": "resource",
            "uid": 1,
            "value": 1,
            "startDate": ["2022-11-11", "2022-11-22", "2022-11-21"],
            "endDate": ["2022-11-22", "2022-11-12", "2022-11-13"],
            "envName": ["env1", "env2", "env3"],
            "nodeId": [1, 2, 3],
            "note": ["note1", "note2", "note3"],
            "valueGroup": ["value1", "value2", "value3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_env_resources(client):
    now = datetime.now().date()
    client._get.return_value = success_response
    response = client.Order.EnvResources(now, now)
    client._get.assert_called_with(
        "EnvResources",
        params={
            "startDate": now.strftime("%Y-%m-%d"),
            "endDate": now.strftime("%Y-%m-%d"),
        },
    )
    assert response == success_response


def test_envs_resources(client):
    now = datetime.now().date()
    client._get.return_value = success_response
    response = client.Order.EnvsResources(now, now, "tid_1", "checksum")
    client._get.assert_called_with(
        "EnvsResources",
        params={
            "startDate": now.strftime("%Y-%m-%d"),
            "endDate": now.strftime("%Y-%m-%d"),
            "targetAppId": "tid_1",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_envs_resources_by_account(client):
    now = datetime.now().date()
    client._get.return_value = success_response
    response = client.Order.EnvsResourcesByAccount(now, now, 1, "checksum")
    client._get.assert_called_with(
        "EnvsResourcesByAccount",
        params={
            "startDate": now.strftime("%Y-%m-%d"),
            "endDate": now.strftime("%Y-%m-%d"),
            "uid": 1,
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_get_options(client):
    client._get.return_value = success_response
    response = client.Order.GetOptions("env", "group")
    client._get.assert_called_with(
        "GetOptions",
        params={
            "targetEnvName": "env",
            "nodeGroup": "group",
        },
    )
    assert response == success_response


def test_set_options(client):
    client._get.return_value = success_response
    response = client.Order.SetOptions(
        "env",
        "group",
        "option",
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "SetOptions",
        params={
            "targetEnvName": "env",
            "nodeGroup": "group",
            "options": "option",
            "nodeId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_clean_check_request_cache(client):
    client._get.return_value = success_response
    response = client.System.CleanCheckRequestCache(
        [1, 2, 3],
        [True, False, True],
    )
    client._get.assert_called_with(
        "CleanCheckRequestCache",
        params={
            "uid": [1, 2, 3],
            "localOnly": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_event_Sys(client):
    client._get.return_value = success_response
    response = client.System.Event(
        "topic",
        "message",
        [True, False, True],
    )
    client._get.assert_called_with(
        "Event",
        params={
            "topic": "topic",
            "message": "message",
            "publishLocal": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_api_description(client):
    client._get.return_value = success_response
    response = client.System.GetAPIDescriptions(
        [True, False, True],
        [True, False, True],
    )
    client._get.assert_called_with(
        "GetAPIDescriptions",
        params={
            "isPublicOnly": [True, False, True],
            "isToken": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_auto_percent(client):
    client._get.return_value = success_response
    response = client.System.GetAutoPercent()
    client._get.assert_called_with("GetAutoPercent", params={})
    assert response == success_response


def test_get_cache_stats(client):
    client._get.return_value = success_response
    response = client.System.GetCacheStats()
    client._get.assert_called_with("GetCacheStats", params={})
    assert response == success_response


def test_get_cache_status(client):
    client._get.return_value = success_response
    response = client.System.GetCacheStatus()
    client._get.assert_called_with("GetCacheStatus", params={})
    assert response == success_response


def test_get_instance_cache_status(client):
    client._get.return_value = success_response
    response = client.System.GetInstanceCacheStatus()
    client._get.assert_called_with("GetInstanceCacheStatus", params={})
    assert response == success_response


def test_get_status(client):
    client._get.return_value = success_response
    response = client.System.GetStatus(1)
    client._get.assert_called_with("GetStatus", params={"checksum": 1})
    assert response == success_response


def test_get_version(client):
    client._get.return_value = success_response
    response = client.System.GetVersion()
    client._get.assert_called_with("GetVersion", params={})
    assert response == success_response


def test_refresh_email_templates(client):
    client._get.return_value = success_response
    response = client.System.RefreshEmailTemplates()
    client._get.assert_called_with("RefreshEmailTemplates", params={})
    assert response == success_response


def test_refresh_user(client):
    client._get.return_value = success_response
    response = client.System.RefreshUser(["lang1", "lang2"])
    client._get.assert_called_with(
        "RefreshUser",
        params={"language": ["lang1", "lang2"]},
        delimiter=",",
    )
    assert response == success_response


def test_reload_configuration(client):
    client._get.return_value = success_response
    response = client.System.ReloadConfiguration(
        [1, 2, 3, 4],
        ["place holder 1", "place holder 2", "place holder 3", "place holder 4"],
    )
    client._get.assert_called_with(
        "ReloadConfiguration",
        params={
            "resellerId": [1, 2, 3, 4],
            "changedPlaceholders": [
                "place holder 1",
                "place holder 2",
                "place holder 3",
                "place holder 4",
            ],
        },
        delimiter=",",
    )
    assert response == success_response


def test_send_email(client):
    client._get.return_value = success_response
    response = client.System.SendEmail(
        "template",
        ["test1@email.com", "test2@email.com", "test3@email.com"],
        ["language1", "language2", "language3"],
        [1, 2, 3],
    )
    client._get.assert_called_with(
        "SendEmail",
        params={
            "template": "template",
            "email": ["test1@email.com", "test2@email.com", "test3@email.com"],
            "language": ["language1", "language2", "language3"],
            "timeout": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_validate(client):
    client._get.return_value = success_response
    response = client.System.Validate()
    client._get.assert_called_with("Validate", params={})
    assert response == success_response


def test_validate_all(client):
    client._get.return_value = success_response
    response = client.System.ValidateAll()
    client._get.assert_called_with("ValidateAll", params={})
    assert response == success_response


def test_clear_billing_history(client):
    client._get.return_value = success_response
    response = client.Utils.ClearBillingHistory(
        "env",
        1,
        "2022-11-11",
        "2026-11-11",
        "checksum",
    )
    client._get.assert_called_with(
        "ClearBillingHistory",
        params={
            "envName": "env",
            "uid": 1,
            "startDate": "2022-11-11",
            "endDate": "2026-11-11",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_clear_month_traffic(client):
    client._get.return_value = success_response
    response = client.Utils.ClearMonthTraffic(
        1,
        "2022-11-11",
        "checksum",
    )
    client._get.assert_called_with(
        "ClearMonthTraffic",
        params={
            "uid": 1,
            "monthStart": "2022-11-11",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_get_uid_usage_by_period(client):
    client._get.return_value = success_response
    response = client.Utils.GetUidUsageByPeriod(
        1,
        "2022-11-11",
        "2026-11-11",
        "checksum",
    )
    client._get.assert_called_with(
        "GetUidUsageByPeriod",
        params={
            "uid": 1,
            "startDate": "2022-11-11",
            "endDate": "2026-11-11",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_set_account_date(client):
    client._get.return_value = success_response
    response = client.Utils.SetAccountDate(
        1,
        "type",
        "value",
        "checksum",
    )
    client._get.assert_called_with(
        "SetAccountDate",
        params={
            "uid": 1,
            "dateType": "type",
            "dateValue": "value",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_set_billing_history_date(client):
    client._get.return_value = success_response
    response = client.Utils.SetBillingHistoryDate(
        1,
        "env",
        "2022-11-11",
        "2026-11-11",
        "date type",
        "value",
        "checksum",
    )
    client._get.assert_called_with(
        "SetBillingHistoryDate",
        params={
            "uid": 1,
            "envName": "env",
            "startDateFrom": "2022-11-11",
            "startDateTo": "2026-11-11",
            "dateType": "date type",
            "dateValue": "value",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_set_month_traffic(client):
    client._get.return_value = success_response
    response = client.Utils.SetMonthTraffic(
        1,
        "2022-11-11",
        3,
        "checksum",
    )
    client._get.assert_called_with(
        "SetMonthTraffic",
        params={
            "uid": 1,
            "monthStart": "2022-11-11",
            "externalTraffic": 3,
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_set_signup_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetSignupGroup(
        "group",
    )
    client._get.assert_called_with(
        "SetSignupGroup",
        params={
            "name": "group",
        },
    )
    assert response == success_response
