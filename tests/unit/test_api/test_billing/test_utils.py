from . import *


def test_clear_billing_history(client):
    client._get.return_value = success_response
    response = client.Utils.ClearBillingHistory(
        "env",
        1,
        CURRENT_DATETIME.date(),
        CURRENT_DATETIME.date(),
        "checksum",
        "ruk",
    )
    client._get.assert_called_with(
        "ClearBillingHistory",
        params={
            "envName": "env",
            "uid": 1,
            "startDate": CURRENT_DATETIME.date(),
            "endDate": CURRENT_DATETIME.date(),
            "checksum": "checksum",
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_clear_month_traffic(client):
    client._get.return_value = success_response
    response = client.Utils.ClearMonthTraffic(
        1,
        "2022-11-11",
        "checksum",
        "ruk",
    )
    client._get.assert_called_with(
        "ClearMonthTraffic",
        params={
            "uid": 1,
            "monthStart": "2022-11-11",
            "checksum": "checksum",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_uid_usage_by_period(client):
    client._get.return_value = success_response
    response = client.Utils.GetUidUsageByPeriod(
        1,
        CURRENT_DATETIME.date(),
        CURRENT_DATETIME.date(),
        "checksum",
        "ruk",
    )
    client._get.assert_called_with(
        "GetUidUsageByPeriod",
        params={
            "uid": 1,
            "startDate": CURRENT_DATETIME.date(),
            "endDate": CURRENT_DATETIME.date(),
            "checksum": "checksum",
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_set_account_date(client):
    client._get.return_value = success_response
    response = client.Utils.SetAccountDate(
        1,
        "type",
        "value",
        "checksum",
        "ruk",
    )
    client._get.assert_called_with(
        "SetAccountDate",
        params={
            "uid": 1,
            "dateType": "type",
            "dateValue": "value",
            "checksum": "checksum",
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
        "date type",
        "value",
        "checksum",
        "ruk",
    )
    client._get.assert_called_with(
        "SetBillingHistoryDate",
        params={
            "uid": 1,
            "envName": "env",
            "startDateFrom": CURRENT_DATETIME.date(),
            "startDateTo": CURRENT_DATETIME.date(),
            "dateType": "date type",
            "dateValue": "value",
            "checksum": "checksum",
            "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d",
    )
    assert response == success_response


def test_set_month_traffic(client):
    client._get.return_value = success_response
    response = client.Utils.SetMonthTraffic(
        1,
        "2022-11-11",
        3,
        "checksum",
        "ruk",
    )
    client._get.assert_called_with(
        "SetMonthTraffic",
        params={
            "uid": 1,
            "monthStart": "2022-11-11",
            "externalTraffic": 3,
            "checksum": "checksum",
            "ruk": "ruk",
        },
    )
    assert response == success_response
