from . import *


def test_add_domains(client):
    client._get.return_value = success_response
    response = client.Binder.AddDomains(
        "env_name",
        ["domains1", "domains2"],
        "node_group",
        1,
        "subdomain",
        "ruk",
    )
    client._get.assert_called_with(
        "AddDomains",
        params={
            "envName": "env_name",
            "domains": ["domains1", "domains2"],
            "nodeGroup": "node_group",
            "nodeId": 1,
            "subdomain": "subdomain",
            "ruk": "ruk",
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_ssl_cert(client):
    client._get.return_value = success_response
    response = client.Binder.AddSSLCert(
        "env_name",
        "key",
        "cert",
        "interm",
        "ruk",
    )
    client._get.assert_called_with(
        "AddSSLCert",
        params={
            "envName": "env_name",
            "key": "key",
            "cert": "cert",
            "interm": "interm",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_attach_ext_ip(client):
    client._get.return_value = success_response
    response = client.Binder.AttachExtIp(
        "env_name",
        "nodeid",
        "type",
        "ruk",
    )
    client._get.assert_called_with(
        "AttachExtIp",
        params={
            "envName": "env_name",
            "nodeid": "nodeid",
            "type": "type",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_bind_ext_domain(client):
    client._get.return_value = success_response
    response = client.Binder.BindExtDomain(
        "env_name",
        "extdomain",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "BindExtDomain",
        params={
            "envName": "env_name",
            "extdomain": "extdomain",
            "certId": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_bind_ext_domains(client):
    client._get.return_value = success_response
    response = client.Binder.BindExtDomains(
        "env_name",
        ["extdomains1", "extdomains2"],
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "BindExtDomains",
        params={
            "envName": "env_name",
            "extdomains": ["extdomains1", "extdomains2"],
            "certId": 1,
            "ruk": "ruk",
        },
        delimiter=",",
    )
    assert response == success_response


def test_bind_ssl(client):
    client._get.return_value = success_response
    response = client.Binder.BindSSL(
        "env_name",
        "cert_key",
        "cert",
        "intermediate",
        "ruk",
    )
    client._get.assert_called_with(
        "BindSSL",
        params={
            "envName": "env_name",
            "cert_key": "cert_key",
            "cert": "cert",
            "intermediate": "intermediate",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_bind_ssl_cert(client):
    client._get.return_value = success_response
    response = client.Binder.BindSSLCert(
        "env_name",
        1,
        "entry_point",
        ["ext_domains1", "ext_domains2"],
        "ruk",
    )
    client._get.assert_called_with(
        "BindSSLCert",
        params={
            "envName": "env_name",
            "certId": 1,
            "entryPoint": "entry_point",
            "extDomains": ["ext_domains1", "ext_domains2"],
            "ruk": "ruk",
        },
        delimiter=",",
    )
    assert response == success_response


def test_check_domain(client):
    client._get.return_value = success_response
    response = client.Binder.CheckDomain(
        "env_name",
        "domain",
        "region",
        "ruk",
    )
    client._get.assert_called_with(
        "CheckDomain",
        params={
            "envName": "env_name",
            "domain": "domain",
            "region": "region",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_check_ext_domain(client):
    client._get.return_value = success_response
    response = client.Binder.CheckExtDomain(
        "env_name",
        "extdomains",
        "ruk",
    )
    client._get.assert_called_with(
        "CheckExtDomain",
        params={
            "envName": "env_name",
            "extdomains": "extdomains",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_delete_ssl(client):
    client._get.return_value = success_response
    response = client.Binder.DeleteSSL(
        "env_name",
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteSSL",
        params={
            "envName": "env_name",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_detach_ext_ip(client):
    client._get.return_value = success_response
    response = client.Binder.DetachExtIp(
        "env_name",
        1,
        "ip",
        "ruk",
    )
    client._get.assert_called_with(
        "DetachExtIp",
        params={
            "envName": "env_name",
            "nodeid": 1,
            "ip": "ip",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_disable_ssl(client):
    client._get.return_value = success_response
    response = client.Binder.DisableSSL(
        "env_name",
        "ruk",
    )
    client._get.assert_called_with(
        "DisableSSL",
        params={
            "envName": "env_name",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_edit_ssl_cert(client):
    client._get.return_value = success_response
    response = client.Binder.EditSSLCert(
        "env_name",
        1,
        "key",
        "cert",
        "interm",
        "ruk",
    )
    client._get.assert_called_with(
        "EditSSLCert",
        params={
            "envName": "env_name",
            "id": 1,
            "key": "key",
            "cert": "cert",
            "interm": "interm",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_domain_info(client):
    client._get.return_value = success_response
    response = client.Binder.GetDomainInfo(
        "env_name",
        "domain",
        "ruk",
    )
    client._get.assert_called_with(
        "GetDomainInfo",
        params={
            "envName": "env_name",
            "domain": "domain",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_domains(client):
    client._get.return_value = success_response
    response = client.Binder.GetDomains(
        "env_name",
        "node_group",
        1,
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "GetDomains",
        params={
            "envName": "env_name",
            "nodeGroup": "node_group",
            "nodeId": 1,
            "inShort": True,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_ext_domains(client):
    client._get.return_value = success_response
    response = client.Binder.GetExtDomains(
        "env_name",
        "ruk",
    )
    client._get.assert_called_with(
        "GetExtDomains",
        params={
            "envName": "env_name",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_ssl(client):
    client._get.return_value = success_response
    response = client.Binder.GetSSL(
        "env_name",
        "ruk",
    )
    client._get.assert_called_with(
        "GetSSL",
        params={
            "envName": "env_name",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_ssl_certs(client):
    client._get.return_value = success_response
    response = client.Binder.GetSSLCerts(
        "env_name",
        ["id1", "id2"],
        "ruk",
    )
    client._get.assert_called_with(
        "GetSSLCerts",
        params={
            "envName": "env_name",
            "ids": ["id1", "id2"],
            "ruk": "ruk",
        },
        delimiter=",",
    )
    assert response == success_response


def test_manage_node_dns_state(client):
    client._get.return_value = success_response
    response = client.Binder.ManageNodeDnsState(
        "env_name",
        1,
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "ManageNodeDnsState",
        params={
            "envName": "env_name",
            "nodeId": 1,
            "enabled": True,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_move_ext_ips(client):
    client._get.return_value = success_response
    response = client.Binder.MoveExtIps(
        "env_name",
        1,
        2,
        ["ips1", "ips2"],
        "ruk",
    )
    client._get.assert_called_with(
        "MoveExtIps",
        params={
            "envName": "env_name",
            "sourceNodeId": 1,
            "targetNodeId": 2,
            "ips": ["ips1", "ips2"],
            "ruk": "ruk",
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_domains(client):
    client._get.return_value = success_response
    response = client.Binder.RemoveDomains(
        "env_name",
        ["domains1", "domains2"],
        "node_group",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "RemoveDomains",
        params={
            "envName": "env_name",
            "domains": ["domains1", "domains2"],
            "nodeGroup": "node_group",
            "node_id": 1,
            "ruk": "ruk",
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_ext_domains(client):
    client._get.return_value = success_response
    response = client.Binder.RemoveExtDomains(
        "env_name",
        "extdomains",
        "ruk",
    )
    client._get.assert_called_with(
        "RemoveExtDomains",
        params={
            "envName": "env_name",
            "extdomain": "extdomains",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_remove_ssl(client):
    client._get.return_value = success_response
    response = client.Binder.RemoveSSL(
        "env_name",
        "ruk",
    )
    client._get.assert_called_with(
        "RemoveSSL",
        params={
            "envName": "env_name",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_remove_ssl_certs(client):
    client._get.return_value = success_response
    response = client.Binder.RemoveSSLCerts(
        "env_name",
        ["ids1", "ids2"],
        "ruk",
    )
    client._get.assert_called_with(
        "RemoveSSLCerts",
        params={
            "envName": "env_name",
            "ids": ["ids1", "ids2"],
            "ruk": "ruk",
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_ext_ip_count(client):
    client._get.return_value = success_response
    response = client.Binder.SetExtIpCount(
        "env_name",
        "type",
        1,
        "node_group",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "SetExtIpCount",
        params={
            "envName": "env_name",
            "type": "type",
            "count": 1,
            "nodeGroup": "node_group",
            "node_id": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_swap_ext_domains(client):
    client._get.return_value = success_response
    response = client.Binder.SwapExtDomains(
        "env_name",
        "targetappid",
        "ruk",
    )
    client._get.assert_called_with(
        "SwapExtDomains",
        params={
            "envName": "env_name",
            "targetappid": "targetappid",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_swap_ext_ips(client):
    client._get.return_value = success_response
    response = client.Binder.SwapExtIps(
        "env_name",
        1,
        2,
        "source_ip",
        "target_ip",
        "ruk",
    )
    client._get.assert_called_with(
        "SwapExtIps",
        params={
            "envName": "env_name",
            "sourceNodeId": 1,
            "targetNodeId": 2,
            "sourceIp": "source_ip",
            "targetIp": "target_ip",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_unbind_ssl_cert(client):
    client._get.return_value = success_response
    response = client.Binder.UnbindSSLCert(
        "env_name",
        ["extdomains1", "extdomains2"],
        "ruk",
    )
    client._get.assert_called_with(
        "UnbindSSLCert",
        params={
            "envName": "env_name",
            "extDomains": ["extdomains1", "extdomains2"],
            "ruk": "ruk",
        },
        delimiter=",",
    )
    assert response == success_response
