from . import *


def test_get_action(client):
    client._get.return_value = success_response
    response = client.Tracking.GetAction(1)
    client._get.assert_called_with("GetAction", params={"id": 1})
    assert response == success_response


def test_get_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.GetActions(CURRENT_DATETIME, CURRENT_DATETIME)
    client._get.assert_called_with(
        "GetActions",
        params={"starttime": CURRENT_DATETIME, "endtime": CURRENT_DATETIME},
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_all_service_name(client):
    client._get.return_value = success_response
    response = client.Tracking.GetAllServiceName(True, "type")
    client._get.assert_called_with(
        "GetAllServiceName", params={"addServicesWildcard": True, "type": "type"}
    )
    assert response == success_response


def test_get_current_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.GetCurrentActions()
    client._get.assert_called_with(
        "GetCurrentActions",
        params={},
    )
    assert response == success_response


def test_get_env_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.GetEnvActions(
        CURRENT_DATETIME, [CURRENT_DATETIME, CURRENT_DATETIME], 1, 1
    )
    client._get.assert_called_with(
        "GetEnvActions",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": [CURRENT_DATETIME, CURRENT_DATETIME],
            "offset": 1,
            "count": 1,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_server_utc_time(client):
    client._get.return_value = success_response
    response = client.Tracking.GetServerUTCTime()
    client._get.assert_called_with(
        "GetServerUTCTime",
        params={},
    )
    assert response == success_response


def test_get_uid_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.GetUidActions(
        [1, 1], CURRENT_DATETIME, CURRENT_DATETIME, "actionTypes"
    )
    client._get.assert_called_with(
        "GetUidActions",
        params={
            "count": [1, 1],
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "actionTypes": "actionTypes",
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
        "searchText",
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
            "searchText": "searchText",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_search_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.SearchActions(
        "session", {"search1": "search1", "search2": "search2"}
    )
    client._get.assert_called_with(
        "SearchActions",
        params={
            "session": "session",
            "search": {"search1": "search1", "search2": "search2"},
        },
    )
    assert response == success_response


def test_store_audit_admin_actions(client):
    client._get.return_value = success_response
    response = client.Tracking.StoreAuditAdminActions(
        "session", {"trackedevent1": "trackedevent1", "trackedevent2": "trackedevent2"}
    )
    client._get.assert_called_with(
        "StoreAuditAdminActions",
        params={
            "session": "session",
            "trackedevent": {
                "trackedevent1": "trackedevent1",
                "trackedevent2": "trackedevent2",
            },
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
        },
    )
    client._get.assert_called_with(
        "StoreUserActions",
        params={
            "session": "session",
            "trackedActionEvent": {
                "tracked_action_event1": "tracked_action_event2",
                "tracked_action_event2": "tracked_action_event2",
            },
        },
    )
    assert response == success_response
