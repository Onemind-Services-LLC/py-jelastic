from datetime import datetime
from unittest.mock import Mock, MagicMock
from urllib.parse import urlencode

import pytest
import requests

from jelastic.api.abstract import ClientAbstract
from jelastic.api.exceptions import *


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

    params = {"start_datetime": now}
    serialized_params = client._serialize_params(params, datetime_format="%Y-%m-%d")
    assert (
        serialized_params
        == f'appid=cluster&session=token&{urlencode({"start_datetime": now.strftime("%Y-%m-%d")})}'
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
    # Create a mock response object
    response = MagicMock(spec=requests.Response)
    response.status_code = 200
    response.json.return_value = {"result": 0}
    client._session.get = Mock(return_value=response)
    result = client._get("path")
    assert result == {"result": 0}

    response = MagicMock(spec=requests.Response)
    response.status_code = 200
    response.json.return_value = {"result": 1, "error": "Error"}
    client._session.get = Mock(return_value=response)
    with pytest.raises(JelasticApiError):
        client._get("path")

    response = MagicMock(spec=requests.Response)
    response.status_code = 200
    response.json.return_value = {"result": 0}
    client._debug = True
    client._log_debug = Mock()
    client._session.get = Mock(return_value=response)
    client._get("path")
    client._log_debug.assert_called()

    # Test for 404 error
    response = MagicMock(spec=requests.Response)
    response.status_code = 404
    response.ok = False
    response.text = "Not Found"
    client._session.get = Mock(return_value=response)
    with pytest.raises(JelasticResourceNotFound):
        client._get("path")

    # Test for 500 error
    response = MagicMock(spec=requests.Response)
    response.status_code = 500
    response.ok = False
    response.text = "Internal Server Error"
    client._session.get = Mock(return_value=response)
    with pytest.raises(JelasticApiError):
        client._get("path")


def test_log_debug(capsys, client):
    client._log_debug("get", "path", params={"key": "value"})
    captured = capsys.readouterr()

    expected_prefix = "[Jelastic] [GET]"
    assert expected_prefix in captured.out
    assert "Path: endpoint1/endpoint2/rest/path?" in captured.out
    assert "key=value" in captured.out
    assert "session=test_token" not in captured.out
