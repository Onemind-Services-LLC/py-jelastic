from . import *


def test_add(client):
    client._get.return_value = success_response
    response = client.IpPool.Add("ip_from", "ip_to", "region", "checksum")
    client._get.assert_called_with(
        "Add",
        params={
            "ipfrom": "ip_from",
            "ipto": "ip_to",
            "region": "region",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_add_ext(client):
    client._get.return_value = success_response
    response = client.IpPool.AddExt("ip_from", "ip_to", "regions", "checksum")
    client._get.assert_called_with(
        "AddExt",
        params={
            "ipfrom": "ip_from",
            "ipto": "ip_to",
            "regions": "regions",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_add_ipv6_network(client):
    client._get.return_value = success_response
    response = client.IpPool.AddIpv6Network("network", "regions", "checksum")
    client._get.assert_called_with(
        "AddIpv6Network",
        params={"network": "network", "regions": "regions", "checksum": "checksum"},
    )
    assert response == success_response


def test_get(client):
    client._get.return_value = success_response
    response = client.IpPool.Get("checksum")
    client._get.assert_called_with("Get", params={"checksum": "checksum"})
    assert response == success_response


def test_get_ext(client):
    client._get.return_value = success_response
    response = client.IpPool.GetExt(
        "regions",
        "checksum",
        "type",
        11,
        "targetAppid",
    )
    client._get.assert_called_with(
        "GetExt",
        params={
            "regions": "regions",
            "checksum": "checksum",
            "type": "type",
            "nodeId": 11,
            "targetAppid": "targetAppid",
        },
    )
    assert response == success_response


def test_get_free_public_port(client):
    client._get.return_value = success_response
    response = client.IpPool.GetFreePublicPort("checksum")
    client._get.assert_called_with("GetFreePublicPort", params={"checksum": "checksum"})
    assert response == success_response


def test_release(client):
    client._get.return_value = success_response
    response = client.IpPool.Release(1, "checksum")
    client._get.assert_called_with("Release", params={"id": 1, "checksum": "checksum"})
    assert response == success_response


def test_release_ext(client):
    client._get.return_value = success_response
    response = client.IpPool.ReleaseExt(1, "checksum")
    client._get.assert_called_with(
        "ReleaseExt", params={"id": 1, "checksum": "checksum"}
    )
    assert response == success_response


def test_release_subnet(client):
    client._get.return_value = success_response
    response = client.IpPool.ReleaseSubnet(1, "checksum")
    client._get.assert_called_with(
        "ReleaseSubnet", params={"id": 1, "checksum": "checksum"}
    )
    assert response == success_response


def test_remove_ext(client):
    client._get.return_value = success_response
    response = client.IpPool.RemoveExt("ips", "checksum")
    client._get.assert_called_with(
        "RemoveExt", params={"ips": "ips", "checksum": "checksum"}
    )
    assert response == success_response


def test_remove_from_reserve(client):
    client._get.return_value = success_response
    response = client.IpPool.RemoveFromReserve(
        "checksum",
        "target_app_id",
    )
    client._get.assert_called_with(
        "RemoveFromReserve",
        params={
            "checksum": "checksum",
            "targetAppid": "target_app_id",
        },
    )
    assert response == success_response


def test_reserve_ext_ipv6(client):
    client._get.return_value = success_response
    response = client.IpPool.ReserveExtIPv6(
        "checksum",
        "target_app_id",
    )
    client._get.assert_called_with(
        "ReserveExtIPv6",
        params={
            "checksum": "checksum",
            "targetAppid": "target_app_id",
        },
    )
    assert response == success_response


def test_unreserve_ext_ipv6(client):
    client._get.return_value = success_response
    response = client.IpPool.UnreserveExtIPv6(1, "checksum")
    client._get.assert_called_with(
        "UnreserveExtIPv6", params={"id": 1, "checksum": "checksum"}
    )
    assert response == success_response
