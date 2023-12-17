from unittest.mock import patch, Mock

import pytest

from jelastic.api.thirdparty import ThirdParty

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        thirdparty = ThirdParty(session=Mock(), token="token")
        thirdparty._get = mock_get
        yield thirdparty


def test_geoip(client):
    client._get.return_value = success_response
    response = client.GeoIp.GeoIp()
    client._get.assert_called_with("GeoIp")
    assert response == success_response
