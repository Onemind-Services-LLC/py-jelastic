import pytest
from unittest.mock import patch
from jelastic import Jelastic, ClientState


@pytest.fixture
def client():
    with patch("jelastic.Jelastic"):
        return Jelastic(
            base_url="https://api.jelastic.com",
            token="token",
        )


def test_init(client):
    assert client._session.headers.get('X-Base-Url') == "https://api.jelastic.com/1.0/"
    assert client._token == "token"
    assert client._debug is False
    assert client._state == ClientState.UNOPENED


def test_init_without_http_prefix(client):
    client = Jelastic(
        base_url="api.jelastic.com",
        token="token",
    )
    assert client._session.headers.get('X-Base-Url') == "https://api.jelastic.com/1.0/"


def test_init_with_trailing_slash(client):
    client = Jelastic(
        base_url="https://api.jelastic.com/",
        token="token",
    )
    assert client._session.headers.get('X-Base-Url') == "https://api.jelastic.com/1.0/"


def test_enter(client):
    with client as c:
        assert c._state == ClientState.OPENED


def test_exit(client):
    with client as c:
        pass
    assert c._state == ClientState.CLOSED


def test_reenter_closed_client(client):
    with client:
        pass
    with pytest.raises(RuntimeError) as exc_info:
        with client:
            pass

    assert "Cannot reopen a client instance" in str(exc_info.value)


def test_properties(client):
    assert client.administration._session == client._session
    assert client.administration._token == client._token
    assert client.administration._debug == client._debug

    assert client.automation._session == client._session
    assert client.automation._token == client._token
    assert client.automation._debug == client._debug

    assert client.billing._session == client._session
    assert client.billing._token == client._token
    assert client.billing._debug == client._debug

    assert client.data._session == client._session
    assert client.data._token == client._token
    assert client.data._debug == client._debug

    assert client.development._session == client._session
    assert client.development._token == client._token
    assert client.development._debug == client._debug

    assert client.environment._session == client._session
    assert client.environment._token == client._token
    assert client.environment._debug == client._debug

    assert client.iaas._session == client._session
    assert client.iaas._token == client._token
    assert client.iaas._debug == client._debug

    assert client.io._session == client._session
    assert client.io._token == client._token
    assert client.io._debug == client._debug

    assert client.management._session == client._session
    assert client.management._token == client._token
    assert client.management._debug == client._debug

    assert client.marketplace._session == client._session
    assert client.marketplace._token == client._token
    assert client.marketplace._debug == client._debug

    assert client.message._session == client._session
    assert client.message._token == client._token
    assert client.message._debug == client._debug

    assert client.migration._session == client._session
    assert client.migration._token == client._token
    assert client.migration._debug == client._debug

    assert client.platform._session == client._session
    assert client.platform._token == client._token
    assert client.platform._debug == client._debug

    assert client.pool._session == client._session
    assert client.pool._token == client._token
    assert client.pool._debug == client._debug

    assert client.pricing._session == client._session
    assert client.pricing._token == client._token
    assert client.pricing._debug == client._debug

    assert client.s3._session == client._session
    assert client.s3._token == client._token
    assert client.s3._debug == client._debug

    assert client.security._session == client._session
    assert client.security._token == client._token
    assert client.security._debug == client._debug

    assert client.statistic._session == client._session
    assert client.statistic._token == client._token
    assert client.statistic._debug == client._debug

    assert client.system._session == client._session
    assert client.system._token == client._token
    assert client.system._debug == client._debug

    assert client.thirdparty._session == client._session
    assert client.thirdparty._token == client._token
    assert client.thirdparty._debug == client._debug

    assert client.users._session == client._session
    assert client.users._token == client._token
    assert client.users._debug == client._debug

    assert client.utils._session == client._session
    assert client.utils._token == client._token
    assert client.utils._debug == client._debug
