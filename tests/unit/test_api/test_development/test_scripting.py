from . import *


def test_build(client):
    client._get.return_value = success_response
    response = client.Scripting.Build("app_id", "script")
    client._get.assert_called_once_with(
        "Build",
        params={
            "appid": "app_id",
            "script": "script",
        },
    )
    assert response == success_response


def test_build_stubs(client):
    client._get.return_value = success_response
    response = client.Scripting.BuildStubs("app_id")
    client._get.assert_called_once_with(
        "BuildStubs",
        params={
            "appid": "app_id",
        },
    )
    assert response == success_response


def test_change_script(client):
    client._get.return_value = success_response
    response = client.Scripting.ChangeScript(
        "app_id",
        "name",
        "field",
        "value",
    )
    client._get.assert_called_once_with(
        "ChangeScript",
        params={
            "appid": "app_id",
            "name": "name",
            "field": "field",
            "value": "value",
        },
    )
    assert response == success_response


def test_create_script(client):
    client._get.return_value = success_response
    response = client.Scripting.CreateScript(
        "app_id",
        "name",
        "type",
        "code",
        "annotations",
    )
    client._get.assert_called_once_with(
        "CreateScript",
        params={
            "appid": "app_id",
            "name": "name",
            "type": "type",
            "code": "code",
            "annotations": "annotations",
        },
    )
    assert response == success_response


def test_delete_script(client):
    client._get.return_value = success_response
    response = client.Scripting.DeleteScript("app_id", "name")
    client._get.assert_called_once_with(
        "DeleteScript",
        params={
            "appid": "app_id",
            "name": "name",
        },
    )
    assert response == success_response


def test_eval(client):
    client._get.return_value = success_response
    response = client.Scripting.Eval(
        "app_id",
        "script",
        "code",
    )
    client._get.assert_called_once_with(
        "Eval",
        params={
            "appid": "app_id",
            "script": "script",
            "params": "code",
        },
    )
    assert response == success_response


def test_eval_code(client):
    client._get.return_value = success_response
    response = client.Scripting.EvalCode(
        "app_id", "code", "type", "annotations", "params"
    )
    client._get.assert_called_once_with(
        "EvalCode",
        params={
            "appid": "app_id",
            "code": "code",
            "type": "type",
            "annotations": "annotations",
            "params": "params",
        },
    )
    assert response == success_response


def test_export_scripts(client):
    client._get.return_value = success_response
    response = client.Scripting.ExportScripts("app_id", True)
    client._get.assert_called_once_with(
        "ExportScripts",
        params={
            "appid": "app_id",
            "overwrite": True,
        },
    )
    assert response == success_response


def test_get_engine_info(client):
    client._get.return_value = success_response
    response = client.Scripting.GetEngineInfo("app_id")
    client._get.assert_called_once_with(
        "GetEngineInfo",
        params={
            "appid": "app_id",
        },
    )
    assert response == success_response


def test_get_script(client):
    client._get.return_value = success_response
    response = client.Scripting.GetScript("app_id", "name")
    client._get.assert_called_once_with(
        "GetScript",
        params={
            "appid": "app_id",
            "name": "name",
        },
    )
    assert response == success_response


def test_get_scripts(client):
    client._get.return_value = success_response
    response = client.Scripting.GetScripts("app_id", "type", 1, 2)
    client._get.assert_called_once_with(
        "GetScripts",
        params={
            "appid": "app_id",
            "type": "type",
            "from": 1,
            "count": 2,
        },
    )
    assert response == success_response
