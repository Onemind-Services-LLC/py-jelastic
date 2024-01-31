from . import *


def test_get_action(client):
    client._get.return_value = success_response
    response = client.Tracking.GetAction(1, "ruk", )
    client._get.assert_called_with("GetAction", params={"id": 1, "ruk": "ruk", })
    assert response == success_response


def test_get_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.GetActions(CURRENT_DATETIME, CURRENT_DATETIME, "ruk", )
    client._get.assert_called_with(
        "GetActions",
        params={"starttime": CURRENT_DATETIME, "endtime": CURRENT_DATETIME, "ruk": "ruk", },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_all_service_name(client):
    client._get.return_value = success_response
    response = client.Tracking.GetAllServiceName(True, "type", "ruk", )
    client._get.assert_called_with(
        "GetAllServiceName", params={"addServicesWildcard": True, "type": "type", "ruk": "ruk", }
    )
    assert response == success_response


def test_get_current_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.GetCurrentActions("ruk", )
    client._get.assert_called_with(
        "GetCurrentActions",
        params={"ruk": "ruk", },
    )
    assert response == success_response


def test_get_env_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.GetEnvActions(
        CURRENT_DATETIME, [CURRENT_DATETIME, CURRENT_DATETIME], 1, 1, "ruk",
    )
    client._get.assert_called_with(
        "GetEnvActions",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": [CURRENT_DATETIME, CURRENT_DATETIME],
            "offset": 1,
            "count": 1, "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_server_utc_time(client):
    client._get.return_value = success_response
    response = client.Tracking.GetServerUTCTime("ruk", )
    client._get.assert_called_with(
        "GetServerUTCTime",
        params={"ruk": "ruk", },
    )
    assert response == success_response


def test_get_uid_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.GetUidActions(
        [1, 1], CURRENT_DATETIME, CURRENT_DATETIME, "actionTypes", "ruk",
    )
    client._get.assert_called_with(
        "GetUidActions",
        params={
            "count": [1, 1],
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "actionTypes": "actionTypes", "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_uid_actions_admin(client):
    client._get.return_value = success_response
    response = client.Tracking.GetUidActionsAdmin(
        1,
        1,
        CURRENT_DATETIME,
        CURRENT_DATETIME,
        1,
        "servicename",
        "orderField",
        "orderDirection",
        "searchText", "ruk",
    )
    client._get.assert_called_with(
        "GetUidActionsAdmin",
        params={
            "uid": 1,
            "startRow": 1,
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "resultCount": 1,
            "servicename": "servicename",
            "orderField": "orderField",
            "orderDirection": "orderDirection",
            "searchText": "searchText", "ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_search_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.SearchActions(
        "session", {"search1": "search1", "search2": "search2"}, "ruk",
    )
    client._get.assert_called_with(
        "SearchActions",
        params={
            "session": "session",
            "search": {"search1": "search1", "search2": "search2"}, "ruk": "ruk",
        },
    )
    assert response == success_response


def test_store_audit_admin_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.StoreAuditAdminActions(
        "session", {"trackedevent1": "trackedevent1", "trackedevent2": "trackedevent2"}, "ruk",
    )
    client._get.assert_called_with(
        "StoreAuditAdminActions",
        params={
            "session": "session",
            "trackedevent": {
                "trackedevent1": "trackedevent1",
                "trackedevent2": "trackedevent2",
            }, "ruk": "ruk",
        },
    )
    assert response == success_response


def test_store_user_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.StoreUserActions(
        "session",
        {
            "tracked_action_event1": "tracked_action_event2",
            "tracked_action_event2": "tracked_action_event2",
        }, "ruk",
    )
    client._get.assert_called_with(
        "StoreUserActions",
        params={
            "session": "session",
            "trackedActionEvent": {
                "tracked_action_event1": "tracked_action_event2",
                "tracked_action_event2": "tracked_action_event2",
            }, "ruk": "ruk",
        },
    )
    assert response == success_response
