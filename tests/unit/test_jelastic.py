import pytest
from unittest.mock import patch
from jelastic import Jelastic, ClientState


@pytest.fixture
def client():
    with patch("jelastic.jelastic.Jelastic"):
        return Jelastic(
            base_url="https://api.jelastic.com",
            token="token",
        )


def test_init(client):
    assert client._session.base_url == "https://api.jelastic.com/1.0/"
    assert client._token == "token"
    assert client._debug is False
    assert client._state == ClientState.UNOPENED


def test_init_without_http_prefix(client):
    client = Jelastic(
        base_url="api.jelastic.com",
        token="token",
    )
    assert client._session.base_url == "https://api.jelastic.com/1.0/"


def test_init_with_trailing_slash(client):
    client = Jelastic(
        base_url="https://api.jelastic.com/",
        token="token",
    )
    assert client._session.base_url == "https://api.jelastic.com/1.0/"


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
