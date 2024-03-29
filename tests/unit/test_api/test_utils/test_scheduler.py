from . import *


def test_create_account_task(client):
    client._get.return_value = success_response
    response = client.Scheduler.CreateAccountTask(
        "script1",
        {"cron": "* * * * *"},
        "Trigger script on before install",
        {"key": "value"},
        "ruk",
    )
    client._get.assert_called_with(
        "CreateAccountTask",
        params={
            "script": "script1",
            "trigger": "cron:* * * * *",
            "description": "Trigger script on before install",
            "params": '{"key": "value"}',
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_create_env_task(client):
    client._get.return_value = success_response
    response = client.Scheduler.CreateEnvTask(
        "script1",
        {"cron": "* * * * *"},
        "env name",
        "Trigger script on before install",
        {"key": "value"},
        "ruk",
    )
    client._get.assert_called_with(
        "CreateEnvTask",
        params={
            "script": "script1",
            "trigger": "cron:* * * * *",
            "envName": "env name",
            "description": "Trigger script on before install",
            "params": '{"key": "value"}',
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_delete_tasks(client):
    client._get.return_value = success_response
    response = client.Scheduler.DeleteTasks(
        ["1", "2"],
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteTasks", params={"ids": ["1", "2"], "ruk": "ruk"}, delimiter=","
    )
    assert response == success_response


def test_edit_task(client):
    client._get.return_value = success_response
    response = client.Scheduler.EditTask(
        "script1",
        {"cron": "* * * * *"},
        1,
        "Trigger script on before install",
        {"key": "value"},
        "ruk",
    )
    client._get.assert_called_with(
        "EditTask",
        params={
            "script": "script1",
            "trigger": "cron:* * * * *",
            "id": 1,
            "description": "Trigger script on before install",
            "params": '{"key": "value"}',
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_task(client):
    client._get.return_value = success_response
    response = client.Scheduler.GetTasks(
        ["1", "2"],
        "ruk",
    )
    client._get.assert_called_with(
        "GetTasks", params={"ids": ["1", "2"], "ruk": "ruk"}, delimiter=","
    )
    assert response == success_response


def test_reschedule_task(client):
    client._get.return_value = success_response
    response = client.Scheduler.RescheduleTasks(
        "ruk",
    )
    client._get.assert_called_with("RescheduleTasks", params={"ruk": "ruk"})
    assert response == success_response


def test_unschedule_tasks(client):
    client._get.return_value = success_response
    response = client.Scheduler.UnscheduleTasks("ruk")
    client._get.assert_called_with("UnscheduleTasks", params={"ruk": "ruk"})
    assert response == success_response
