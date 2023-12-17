from datetime import datetime
from unittest.mock import patch, Mock

import pytest

from jelastic.api import Environment

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}
CURRENT_DATETIME = datetime.now()


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        env = Environment(session=Mock(), token="token")
        env._get = mock_get
        yield env


def test_billing_add_stats(client):
    client._get.return_value = success_response
    response = client.Billing.AddStats(
        "resource_name",
        1,
        CURRENT_DATETIME.date(),
        CURRENT_DATETIME.date(),
        "env_name",
        1,
        1.0,
        "note",
        "value_group",
    )
    client._get.assert_called_with(
        "AddStats",
        params={
            "resourceName": "resource_name",
            "uid": 1,
            "startDate": CURRENT_DATETIME.date(),
            "endDate": CURRENT_DATETIME.date(),
            "envName": "env_name",
            "nodeId": 1,
            "value": 1.0,
            "note": "note",
            "valueGroup": "value_group",
        },
        datetime_format="%Y-%m-%d",
    )

    assert response == success_response


def test_billing_env_resources(client):
    client._get.return_value = success_response
    response = client.Billing.EnvResources(CURRENT_DATETIME, CURRENT_DATETIME)
    client._get.assert_called_with(
        "EnvResources",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_billing_envs_resources(client):
    client._get.return_value = success_response
    response = client.Billing.EnvsResources(
        CURRENT_DATETIME, CURRENT_DATETIME, "app_id", "checksum"
    )
    client._get.assert_called_with(
        "EnvsResources",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "targetAppid": "app_id",
            "checksum": "checksum",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_billing_envs_resources_by_account(client):
    client._get.return_value = success_response
    response = client.Billing.EnvsResourcesByAccount(
        CURRENT_DATETIME, CURRENT_DATETIME, 1, "checksum"
    )
    client._get.assert_called_with(
        "EnvsResourcesByAccount",
        params={
            "starttime": CURRENT_DATETIME,
            "endtime": CURRENT_DATETIME,
            "uid": 1,
            "checksum": "checksum",
        },
        datetime_format="%Y-%m-%d %H:%M:%S",
    )
    assert response == success_response


def test_billing_get_options(client):
    client._get.return_value = success_response
    response = client.Billing.GetOptions("env_name", "node_group")
    client._get.assert_called_with(
        "GetOptions",
        params={
            "targetEnvName": "env_name",
            "nodeGroup": "node_group",
        },
    )
    assert response == success_response


def test_billing_set_options(client):
    client._get.return_value = success_response
    response = client.Billing.SetOptions("env_name", "node_group", {"key": "value"}, 1)
    client._get.assert_called_with(
        "SetOptions",
        params={
            "targetEnvName": "env_name",
            "nodeGroup": "node_group",
            "options": '{"key": "value"}',
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_export_create(client):
    client._get.return_value = success_response
    response = client.Export.Create({"key": "value"})
    client._get.assert_called_with(
        "Create",
        params={
            "settings": '{"key": "value"}',
        },
    )
    assert response == success_response


def test_export_delete(client):
    client._get.return_value = success_response
    response = client.Export.Delete("test")
    client._get.assert_called_with("Delete", params={"id": "test"})
    assert response == success_response


def test_export_delete_exported_data(client):
    client._get.return_value = success_response
    response = client.Export.DeleteExportedData("env", "file")
    client._get.assert_called_with(
        "DeleteExportedData", params={"envName": "env", "fileName": "file"}
    )
    assert response == success_response


def test_export_get_list(client):
    client._get.return_value = success_response
    response = client.Export.GetList("env")
    client._get.assert_called_with("GetList", params={"envName": "env"})
    assert response == success_response


def test_export_get_manifest(client):
    client._get.return_value = success_response
    response = client.Export.GetManifest("env", "manifest-id")
    client._get.assert_called_with(
        "GetManifest", params={"envName": "env", "id": "manifest-id"}
    )
    assert response == success_response


def test_jerror_error(client):
    client._get.return_value = success_response
    response = client.JError.Error(
        "name", "param", 82, 1, "dummy@example.com", "not found"
    )
    client._get.assert_called_with(
        "Error",
        params={
            "actionName": "name",
            "callParameters": "param",
            "errorCode": 82,
            "priority": 1,
            "email": "dummy@example.com",
            "errorMessage": "not found",
        },
    )
    assert response == success_response


def test_node_send_event(client):
    client._get.return_value = success_response
    response = client.Node.SendEvent({"key": "value"}, "OOM_KILLER")
    client._get.assert_called_with(
        "SendEvent", params={"params": '{"key": "value"}', "eventName": "OOM_KILLER"}
    )
    assert response == success_response


def test_node_send_notification(client):
    client._get.return_value = success_response
    response = client.Node.SendNotification("message", "title")
    client._get.assert_called_with(
        "SendNotification", params={"message": "message", "name": "title"}
    )
    assert response == success_response
