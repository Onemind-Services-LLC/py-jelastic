import pytest
from datetime import datetime
from httpx import Response
from unittest.mock import Mock
from urllib.parse import urlencode
from jelastic.api.abstract import ClientAbstract
from jelastic.api.execptions import *


class ConcreteClient(ClientAbstract):
    _endpoint1 = "endpoint1"
    _endpoint2 = "endpoint2"
    _required_permission = "required_permission"


client_mock = Mock()


@pytest.fixture
def client():
    return ConcreteClient(session=client_mock, token="token", debug=True)


def test_init(client):
    assert client._session == client_mock
    assert client._token == "token"
    assert client._debug is True


def test_endpoint_construction(client):
    path = "path"
    endpoint = client._endpoint(path)
    assert endpoint == "endpoint1/endpoint2/rest/path?appid=cluster&session=token"


def test_serialize_params(client):
    params = {}
    serialized_params = client._serialize_params(params)
    assert serialized_params == "appid=cluster&session=token"

    now = datetime.now()
    params = {"start_datetime": now}
    serialized_params = client._serialize_params(params)
    assert (
        serialized_params
        == f'appid=cluster&session=token&{urlencode({"start_datetime": now.isoformat()})}'
    )

    params = {"list": ["l1", "l2"]}
    serialized_params = client._serialize_params(params, delimiter=",")
    assert serialized_params == "appid=cluster&list=l1%2Cl2&session=token"

    params = {"dict": {"key": "value"}}
    serialized_params = client._serialize_params(params)
    assert (
        serialized_params
        == "appid=cluster&dict=%7B%22key%22%3A+%22value%22%7D&session=token"
    )


def test_handle_response(client):
    response = {"result": 0}
    assert client._handle_response(response) == response

    response = {"result": 8202, "error": "Error"}
    with pytest.raises(JelasticPermissionError):
        client._handle_response(response)

    response = {"result": 2223, "error": "Error"}
    with pytest.raises(JelasticExternBillingRejected):
        client._handle_response(response)

    response = {"result": 2207, "error": "Error"}
    with pytest.raises(JelasticExternBillingError):
        client._handle_response(response)

    response = {"result": 5, "error": "Error"}
    with pytest.raises(JelasticResourceNotFound):
        client._handle_response(response)

    response = {"result": -1, "error": "Error"}
    with pytest.raises(JelasticApiError):
        client._handle_response(response)


def test_get(client):
    client._session.send = Mock(return_value=Response(200, json={"result": 0}))
    response = client._get("path")
    assert response == {"result": 0}

    client._session.send = Mock(
        return_value=Response(200, json={"result": 1, "error": "Error"})
    )
    with pytest.raises(JelasticApiError):
        client._get("path")

    client._debug = True
    client._log_debug = Mock()
    client._session.send = Mock(return_value=Response(200, json={"result": 0}))
    client._get("path")
    client._log_debug.assert_called()


def test_log_debug(capsys, client):
    client._log_debug("get", "path", params={"key": "value"})
    captured = capsys.readouterr()

    expected_prefix = "[Jelastic] [GET]"
    assert expected_prefix in captured.out
    assert "Path: endpoint1/endpoint2/rest/path?" in captured.out
    assert "key=value" in captured.out
    assert "session=test_token" not in captured.out
