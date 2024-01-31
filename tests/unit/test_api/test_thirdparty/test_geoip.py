from . import *


def test_geoip(client):
    client._get.return_value = success_response
    response = client.GeoIp.GeoIp("ruk")
    client._get.assert_called_with("GeoIp", params={"ruk": "ruk"})
    assert response == success_response
