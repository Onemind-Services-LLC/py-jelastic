from . import *


def test_geoip(client):
    client._get.return_value = success_response
    response = client.GeoIp.GeoIp()
    client._get.assert_called_with("GeoIp")
    assert response == success_response
