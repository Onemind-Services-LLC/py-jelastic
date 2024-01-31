from . import *


def test_add_auto_scaling_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.AddAutoScalingTrigger(
        "env_name",
        {"data1": "data1", "data2": "data2"},"ruk",
    )
    client._get.assert_called_with(
        "AddAutoScalingTrigger",
        params={
            "envName": "env_name",
            "data": {"data1": "data1", "data2": "data2"},"ruk": "ruk",
        },
    )
    assert response == success_response


def test_add_load_alert_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.AddLoadAlertTrigger(
        "env_name",
        {"data1": "data1", "data2": "data2"},"ruk",
    )
    client._get.assert_called_with(
        "AddLoadAlertTrigger",
        params={
            "envName": "env_name",
            "data": {"data1": "data1", "data2": "data2"},"ruk": "ruk",
        },
    )
    assert response == success_response


def test_add_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.AddTrigger(
        "env_name",
        {"data1": "data1", "data2": "data2"},"ruk",
    )
    client._get.assert_called_with(
        "AddTrigger",
        params={
            "envName": "env_name",
            "data": {"data1": "data1", "data2": "data2"},"ruk": "ruk",
        },
    )
    assert response == success_response


def test_auto_scaling_history(client):
    client._get.return_value = success_response
    response = client.Trigger.AutoScalingHistory(
        "env_name",
        1,
        1,
        1,
        ["action_types1", "action_types2"],
        CURRENT_DATETIME,
        CURRENT_DATETIME,
        "orderField",
        "orderDirection",
        "skipResults",
        "nodeGroup",
        ["resourceTypes1", "resourceTypes2"],
        1,"ruk",
    )
    client._get.assert_called_with(
        "AutoScalingHistory",
        params={
            "envName": "env_name",
            "startRow": 1,
            "resultCount": 1,
            "triggerId": 1,
            "actionTypes": ["action_types1", "action_types2"],
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
            "orderField": "orderField",
            "orderDirection": "orderDirection",
            "skipResults": "skipResults",
            "nodeGroup": "nodeGroup",
            "resourceTypes": ["resourceTypes1", "resourceTypes2"],
            "triggerLogId": 1,"ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_delete_auto_scaling_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.DeleteAutoScalingTrigger("env_name", 1,"ruk",)
    client._get.assert_called_with(
        "DeleteAutoScalingTrigger",
        params={"envName": "env_name", "id": 1,"ruk": "ruk",},
    )
    assert response == success_response


def test_delete_load_alert_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.DeleteLoadAlertTrigger("env_name", 1,"ruk",)
    client._get.assert_called_with(
        "DeleteLoadAlertTrigger",
        params={"envName": "env_name", "id": 1,"ruk": "ruk",},
    )
    assert response == success_response


def test_delete_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.DeleteTrigger("env_name", 1,"ruk",)
    client._get.assert_called_with(
        "DeleteTrigger",
        params={"envName": "env_name", "id": 1,"ruk": "ruk",},
    )
    assert response == success_response


def test_edit_auto_scaling_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.EditAutoScalingTrigger("env_name", 1, "data","ruk",)
    client._get.assert_called_with(
        "EditAutoScalingTrigger",
        params={"envName": "env_name", "id": 1, "data": "data","ruk": "ruk",},
    )
    assert response == success_response


def test_edit_load_alert_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.EditLoadAlertTrigger("env_name", 1, "data","ruk",)
    client._get.assert_called_with(
        "EditLoadAlertTrigger",
        params={"envName": "env_name", "id": 1, "data": "data","ruk": "ruk",},
    )
    assert response == success_response


def test_edit_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.EditTrigger("env_name", 1, "data","ruk",)
    client._get.assert_called_with(
        "EditTrigger",
        params={"envName": "env_name", "id": 1, "data": "data","ruk": "ruk",},
    )
    assert response == success_response


def test_get_auto_scaling_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.GetAutoScalingTriggers(
        "env_name", ["action_types1", "action_types2"],"ruk",
    )
    client._get.assert_called_with(
        "GetAutoScalingTriggers",
        params={
            "envName": "env_name",
            "actionTypes": ["action_types1", "action_types2"],"ruk": "ruk",
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_load_alert_trigger(client):
    client._get.return_value = success_response
    response = client.Trigger.GetAutoScalingTriggers(
        "env_name", ["action_types1", "action_types2"],"ruk",
    )
    client._get.assert_called_with(
        "GetAutoScalingTriggers",
        params={
            "envName": "env_name",
            "actionTypes": ["action_types1", "action_types2"],"ruk": "ruk",
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_trigger_logs(client):
    client._get.return_value = success_response
    response = client.Trigger.GetTriggerLogs(
        "env_name",
        1,
        1,
        1,
        ["action_types1", "action_types2"],
        CURRENT_DATETIME,
        CURRENT_DATETIME,
        "orderField",
        "orderDirection",
        "skipResults",
        "nodeGroup",
        ["resourceTypes1", "resourceTypes2"],
        1,"ruk",
    )
    client._get.assert_called_with(
        "GetTriggerLogs",
        params={
            "envName": "env_name",
            "startRow": 1,
            "resultCount": 1,
            "triggerId": 1,
            "actionTypes": ["action_types1", "action_types2"],
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
            "orderField": "orderField",
            "orderDirection": "orderDirection",
            "skipResults": "skipResults",
            "nodeGroup": "nodeGroup",
            "resourceTypes": ["resourceTypes1", "resourceTypes2"],
            "triggerLogId": 1,"ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_get_triggers(client):
    client._get.return_value = success_response
    response = client.Trigger.GetTriggers(
        "env_name", ["action_types1", "action_types2"],"ruk",
    )
    client._get.assert_called_with(
        "GetTriggers",
        params={
            "envName": "env_name",
            "actionTypes": ["action_types1", "action_types2"],"ruk": "ruk",
        },
        delimiter=",",
    )
    assert response == success_response


def test_load_alert_history(client):
    client._get.return_value = success_response
    response = client.Trigger.LoadAlertHistory(
        "env_name",
        1,
        1,
        1,
        ["action_types1", "action_types2"],
        CURRENT_DATETIME,
        CURRENT_DATETIME,
        "orderField",
        "orderDirection",
        "skipResults",
        "nodeGroup",
        ["resourceTypes1", "resourceTypes2"],
        1,"ruk",
    )
    client._get.assert_called_with(
        "LoadAlertHistory",
        params={
            "envName": "env_name",
            "startRow": 1,
            "resultCount": 1,
            "triggerId": 1,
            "actionTypes": ["action_types1", "action_types2"],
            "startTime": CURRENT_DATETIME,
            "endTime": CURRENT_DATETIME,
            "orderField": "orderField",
            "orderDirection": "orderDirection",
            "skipResults": "skipResults",
            "nodeGroup": "nodeGroup",
            "resourceTypes": ["resourceTypes1", "resourceTypes2"],
            "triggerLogId": 1,"ruk": "ruk",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_set_auto_scaling_trigger_enabled(client):
    client._get.return_value = success_response
    response = client.Trigger.SetAutoScalingTriggerEnabled("env_name", 1, True,"ruk",)
    client._get.assert_called_with(
        "SetAutoScalingTriggerEnabled",
        params={"envName": "env_name", "id": 1, "enabled": True,"ruk": "ruk",},
    )
    assert response == success_response


def test_set_load_alert_trigger_enabled(client):
    client._get.return_value = success_response
    response = client.Trigger.SetLoadAlertTriggerEnabled("env_name", 1, True,"ruk",)
    client._get.assert_called_with(
        "SetLoadAlertTriggerEnabled",
        params={"envName": "env_name", "id": 1, "enabled": True,"ruk": "ruk",},
    )
    assert response == success_response


def test_set_trigger_enabled(client):
    client._get.return_value = success_response
    response = client.Trigger.SetTriggerEnabled("env_name", 1, True,"ruk",)
    client._get.assert_called_with(
        "SetTriggerEnabled",
        params={"envName": "env_name", "id": 1, "enabled": True,"ruk": "ruk",},
    )
    assert response == success_response


def test_get_load_alert_triggers(client):
    client._get.return_value = success_response
    response = client.Trigger.GetLoadAlertTriggers(
        "env_name", ["action_types1", "action_types2"],"ruk",
    )
    client._get.assert_called_with(
        "GetLoadAlertTriggers",
        params={
            "envName": "env_name",
            "actionTypes": ["action_types1", "action_types2"],"ruk": "ruk",
        },
        delimiter=",",
    )
    assert response == success_response
