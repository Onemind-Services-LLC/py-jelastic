from . import *


def test_build(client):
    client._get.return_value = success_response
    response = client.Scripting.Build(
        "script",
        "app_id",
    )
    client._get.assert_called_once_with(
        "Build",
        params={
            "script": "script",
            "appid": "app_id",
        },
    )
    assert response == success_response


def test_build_stubs(client):
    client._get.return_value = success_response
    response = client.Scripting.BuildStubs(
        "app_id",
    )
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
        "name",
        "field",
        "value",
        "app_id",
    )
    client._get.assert_called_once_with(
        "ChangeScript",
        params={
            "name": "name",
            "field": "field",
            "value": "value",
            "appid": "app_id",
        },
    )
    assert response == success_response


def test_create_script(client):
    client._get.return_value = success_response
    response = client.Scripting.CreateScript(
        "name",
        "type",
        "code",
        "annotations",
        "app_id",
    )
    client._get.assert_called_once_with(
        "CreateScript",
        params={
            "name": "name",
            "type": "type",
            "code": "code",
            "annotations": "annotations",
            "appid": "app_id",
        },
    )
    assert response == success_response


def test_delete_script(client):
    client._get.return_value = success_response
    response = client.Scripting.DeleteScript(
        "name",
        "app_id",
    )
    client._get.assert_called_once_with(
        "DeleteScript",
        params={
            "name": "name",
            "appid": "app_id",
        },
    )
    assert response == success_response


def test_eval(client):
    client._get.return_value = success_response
    response = client.Scripting.Eval(
        "script",
        "code",
        "app_id",
    )
    client._get.assert_called_once_with(
        "Eval",
        params={
            "script": "script",
            "params": "code",
            "appid": "app_id",
        },
    )
    assert response == success_response


def test_eval_code(client):
    client._get.return_value = success_response
    response = client.Scripting.EvalCode(
        "code",
        "type",
        "annotations",
        "params",
        "app_id",
    )
    client._get.assert_called_once_with(
        "EvalCode",
        params={
            "code": "code",
            "type": "type",
            "annotations": "annotations",
            "params": "params",
            "appid": "app_id",
        },
    )
    assert response == success_response


def test_export_scripts(client):
    client._get.return_value = success_response
    response = client.Scripting.ExportScripts(
        True,
        "app_id",
    )
    client._get.assert_called_once_with(
        "ExportScripts",
        params={
            "overwrite": True,
            "appid": "app_id",
        },
    )
    assert response == success_response


def test_get_engine_info(client):
    client._get.return_value = success_response
    response = client.Scripting.GetEngineInfo(
        "app_id",
    )
    client._get.assert_called_once_with(
        "GetEngineInfo",
        params={
            "appid": "app_id",
        },
    )
    assert response == success_response


def test_get_script(client):
    client._get.return_value = success_response
    response = client.Scripting.GetScript(
        "name",
        "app_id",
    )
    client._get.assert_called_once_with(
        "GetScript",
        params={
            "name": "name",
            "appid": "app_id",
        },
    )
    assert response == success_response


def test_get_scripts(client):
    client._get.return_value = success_response
    response = client.Scripting.GetScripts(
        "type",
        1,
        2,
        "app_id",
    )
    client._get.assert_called_once_with(
        "GetScripts",
        params={
            "type": "type",
            "from": 1,
            "count": 2,
            "appid": "app_id",
        },
    )
    assert response == success_response
