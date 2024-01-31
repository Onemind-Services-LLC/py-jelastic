from . import *


def test_clear_billing_history(client):
    client._get.return_value = success_response
    response = client.Utils.ClearBillingHistory(
        1, CURRENT_DATETIME.date(), CURRENT_DATETIME.date(), "env", "ruk"
    )
    client._get.assert_called_with(
        "ClearBillingHistory",
        params={
            "uid": 1,
            "startDate": CURRENT_DATETIME.date(),
            "endDate": CURRENT_DATETIME.date(),
            "envName": "env",
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d",
    )

    assert response == success_response


def test_clear_monthly_traffic(client):
    client._get.return_value = success_response
    response = client.Utils.ClearMonthTraffic(1, "1", "ruk")
    client._get.assert_called_with(
        "ClearMonthTraffic", params={"uid": 1, "monthStart": "1", "ruk": "ruk"}
    )

    assert response == success_response


def test_clear_resource_statistics(client):
    client._get.return_value = success_response
    response = client.Utils.ClearResourceStatistics(
        1, CURRENT_DATETIME.date(), CURRENT_DATETIME.date(), "ruk"
    )
    client._get.assert_called_with(
        "ClearResourceStatistics",
        params={
            "uid": 1,
            "startDateFrom": CURRENT_DATETIME.date(),
            "startDateTo": CURRENT_DATETIME.date(),
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d",
    )

    assert response == success_response


def test_generate_billable_item_statistics(client):
    client._get.return_value = success_response
    response = client.Utils.GenerateBillableItemStatistics(
        CURRENT_DATETIME.date(), 1, 1, 1, "env", "ruk"
    )
    client._get.assert_called_with(
        "GenerateBillableItemStatistics",
        params={
            "startDate": CURRENT_DATETIME.date(),
            "durationHour": 1,
            "nodeId": 1,
            "itemId": 1,
            "envName": "env",
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d",
    )
    assert response == success_response


def test_generate_statistics(client):
    client._get.return_value = success_response
    response = client.Utils.GenerateStatistics(
        CURRENT_DATETIME.date(), 1, 1, {"cpu": "1"}, "ruk"
    )
    client._get.assert_called_with(
        "GenerateStatistics",
        params={
            "startDate": CURRENT_DATETIME.date(),
            "durationHour": 1,
            "nodeId": 1,
            "statJson": '{"cpu": "1"}',
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d",
    )
    assert response == success_response


def test_get_uid_usage_by_period(client):
    client._get.return_value = success_response
    response = client.Utils.GetUidUsageByPeriod(
        1, CURRENT_DATETIME.date(), CURRENT_DATETIME.date(), "ruk"
    )
    client._get.assert_called_with(
        "GetUidUsageByPeriod",
        params={
            "uid": 1,
            "startDate": CURRENT_DATETIME.date(),
            "endDate": CURRENT_DATETIME.date(),
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d",
    )
    assert response == success_response


def test_set_account_date(client):
    client._get.return_value = success_response
    response = client.Utils.SetAccountDate(1, "type", "value", "ruk")
    client._get.assert_called_with(
        "SetAccountDate",
        params={"uid": 1, "dateType": "type", "dateValue": "value", "ruk": "ruk"},
    )
    assert response == success_response


def test_set_app_node_date(client):
    client._get.return_value = success_response
    response = client.Utils.SetAppNodeDate("env", "type", "value", "ruk")
    client._get.assert_called_with(
        "SetAppNodeDate",
        params={
            "envName": "env",
            "dateType": "type",
            "dateValue": "value",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_set_billing_history_date(client):
    client._get.return_value = success_response
    response = client.Utils.SetBillingHistoryDate(
        1,
        "env",
        CURRENT_DATETIME.date(),
        CURRENT_DATETIME.date(),
        "type",
        "value",
        "ruk",
    )
    client._get.assert_called_with(
        "SetBillingHistoryDate",
        params={
            "uid": 1,
            "envName": "env",
            "startDateFrom": CURRENT_DATETIME.date(),
            "startDateTo": CURRENT_DATETIME.date(),
            "dateType": "type",
            "dateValue": "value",
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d",
    )
    assert response == success_response


def test_set_month_traffic(client):
    client._get.return_value = success_response
    response = client.Utils.SetMonthTraffic(1, "1", 1.0, "ruk")
    client._get.assert_called_with(
        "SetMonthTraffic",
        params={"uid": 1, "monthStart": "1", "externalTraffic": 1.0, "ruk": "ruk"},
    )
    assert response == success_response


def test_shift_resource_created_on_date_to_start_date(client):
    client._get.return_value = success_response
    response = client.Utils.ShiftResourceCreatedOnDateToStartDate(
        1, "env", CURRENT_DATETIME.date(), CURRENT_DATETIME.date(), "ruk"
    )
    client._get.assert_called_with(
        "ShiftResourceCreatedOnDateToStartDate",
        params={
            "uid": 1,
            "envName": "env",
            "startDateFrom": CURRENT_DATETIME.date(),
            "startDateTo": CURRENT_DATETIME.date(),
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d",
    )
    assert response == success_response
