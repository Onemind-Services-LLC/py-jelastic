import json
import requests
from abc import ABC
from datetime import date, datetime
from typing import Any, Literal, Optional
from urllib.parse import urlencode

from .exceptions import *

RequestData = dict[Any, Any]
VALID_METHODS = Literal["get", "post"]

__all__ = ["ClientAbstract"]


class ClientAbstract(ABC):
    """
    Abstract class representing a Jelastic API client.

    :param session: HTTPX session
    :param token: Jelastic API token
    :param debug: enable debug mode

    :cvar _endpoint1: first part of the endpoint
    :cvar _endpoint2: second part of the endpoint
    :cvar _required_permission: required permission for the endpoint

    :return: Jelastic API client
    """

    _endpoint1: str
    _endpoint2: str
    _required_permission: str

    def __init__(
        self,
        session: requests.Session,
        token: str,
        debug: bool = False,
        ruk: str = None,
    ) -> None:
        """
        Initialize the client with the given session and token.

        :param session: HTTPX session
        :param token: Jelastic API token
        :param debug: enable debug mode
        :param ruk: Jelastic RUK (random unique key)
        """
        self._session = session
        self._token = token
        self._debug = debug
        self._ruk = ruk

    def _log_debug(
        self, method: VALID_METHODS, path: str, params: Optional[dict[str, Any]] = None
    ) -> None:
        """
        Prints `debug` information about the request.

        :param method: HTTP method
        :param path: endpoint path
        :param params: endpoint params
        """
        endpoint = self._endpoint(path=path, params=params)
        prefix = f"[Jelastic] [{method.upper()}] [{self._ruk}]"
        message = f"{prefix}, Path: {endpoint}, Params: {params}"
        print(message)

    def _serialize_params(
        self, params: dict[str, Any], delimiter: str = None, datetime_format: str = None
    ) -> str:
        """
        Serialize params for endpoint URL

        :param params: endpoint params

        :return: serialized params for endpoint URL (e.g. `appid=cluster&session=token`)
        """
        if params is None:
            params = {}

        params.setdefault("appid", "cluster")
        params.setdefault("session", self._token)
        params.setdefault("ruk", self._ruk)

        # Remove None values and serialize params
        serialized_params = {}
        for key, value in params.items():
            if value is None:
                continue  # pragma: no cover

            if isinstance(value, (date, datetime)):
                if datetime_format:
                    serialized_params[key] = value.strftime(datetime_format)
                else:
                    serialized_params[key] = value.isoformat()
            elif (
                isinstance(value, list)
                and all(isinstance(item, str) for item in value)
                and delimiter
            ):
                serialized_params[key] = f"{delimiter}".join(value)
            elif isinstance(value, dict):
                serialized_params[key] = json.dumps(value)
            else:
                serialized_params[key] = value

        # Sort params and return serialized params
        serialized_params = dict(
            sorted(serialized_params.items(), key=lambda item: item[0])
        )
        return urlencode(serialized_params)

    def _endpoint(
        self,
        path: str,
        params: Optional[dict[str, Any]] = None,
        delimiter: str = None,
        datetime_format: str = None,
    ) -> str:
        """
        Returns the endpoint for the request.

        :param path: endpoint path
        :param params: endpoint params

        :return: endpoint for the request (e.g. `/endpoint1/endpoint2/rest/path?appid=cluster&session=token`)
        """
        # Build the required permissions
        self._required_permission = f"{self._endpoint1}.{self._endpoint2}.{path}"

        serialized_params = self._serialize_params(
            params, delimiter=delimiter, datetime_format=datetime_format
        )
        return f"{self._endpoint1}/{self._endpoint2}/rest/{path.lower()}?{serialized_params}"

    def _handle_response(self, response: dict[str, Any]) -> dict[str, Any]:
        """
        Handle the response from the API.

        :param response: response from the API
        """
        result_code = response.get("result", 0)
        error = response.get("error", "Unknown API error")

        if result_code == 8202:
            raise JelasticPermissionError(
                f"Permission denied, required permissions: {self._required_permission}"
            )

        if result_code == 2223:
            raise JelasticExternBillingRejected(error)

        if result_code == 2207:
            raise JelasticExternBillingError(error)

        if result_code == 5:
            raise JelasticResourceNotFound(error)

        if result_code != 0:
            raise JelasticApiError(error)

        return response

    def _get(
        self,
        *args: str,
        params: dict[str, Any] = None,
        delimiter: str = None,
        datetime_format: str = None,
    ) -> dict[str, Any]:
        if self._debug:
            self._log_debug("get", *args, params=params)

        url = self._endpoint(
            *args, params=params, delimiter=delimiter, datetime_format=datetime_format
        )

        # Get the X-Base-Url header and remove it from the session
        base_url = self._session.headers.get("X-Base-Url", None)
        assert base_url is not None
        url = f"{base_url}{url}"

        response = self._session.get(url)
        if not response.ok:
            if response.status_code == 404:
                raise JelasticResourceNotFound(f"API endpoint not found: {url}")

            raise JelasticApiError(response.text)

        return self._handle_response(response.json())
