from . import *


def test_get(client):
    client._get.return_value = success_response
    response = client.Engine.Get("docker", 77,"ruk",)
    client._get.assert_called_with(
        "Get", params={"engineType": "docker", "ownerUid": 77,"ruk": "ruk",}
    )
    assert response == success_response


def test_get_entry_point(client):
    client._get.return_value = success_response
    response = client.Engine.GetEntryPoint("COLUMBUS", 1,"ruk",)
    client._get.assert_called_with(
        "GetEntryPoint", params={"hostGroup": "COLUMBUS", "ownerUid": 1,"ruk": "ruk",}
    )
    assert response == success_response
