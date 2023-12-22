from datetime import datetime
from unittest.mock import patch, Mock

import pytest

from jelastic.api import Marketplace

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}
CURRENT_DATETIME = datetime.now()


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        marketplace = Marketplace(session=Mock(), token="token")
        marketplace._get = mock_get
        yield marketplace


def test_add(client):
    client._get.return_value = success_response
    response = client.Favorite.Add(
        "id"
    )
    client._get.assert_called_with(
        "Add",
        params={
            "id":"id"
        },
    )
    assert response == success_response


def test_add_manifest(client):
    client._get.return_value = success_response
    response = client.Favorite.AddManifest(
        "manifest"
    )
    client._get.assert_called_with(
        "AddManifest",
        params={
            "manifest":"manifest"
        },
    )
    assert response == success_response
def test_delete(client):
    client._get.return_value = success_response
    response = client.Favorite.Delete(
        "id"
    )
    client._get.assert_called_with(
        "Delete",
        params={
            "id":"id"
        },
    )
    assert response == success_response
def test_get_list(client):
    client._get.return_value = success_response
    response = client.Favorite.GetList(
        "search","lang","checksum",
    )
    client._get.assert_called_with(
        "Delete",
        params={
            "search": "search",
            "lang": "lang",
            "checksum": "checksum",
        },
    )
    assert response == success_response
