from . import *


def test_activate(client):
    client._get.return_value = success_response
    response = client.License.Activate("serial", True)
    client._get.assert_called_once_with(
        "Activate", params={"serial": "serial", "generateSMTPCreds": True}
    )
    assert response == success_response


def test_generate_smtp_settings(client):
    client._get.return_value = success_response
    response = client.License.GenerateSMTPSettings()
    client._get.assert_called_once_with(
        "GenerateSMTPSettings",
        params={},
    )
    assert response == success_response


def test_get_vz_license(client):
    client._get.return_value = success_response
    response = client.License.GetVZLicense("vzType")
    client._get.assert_called_once_with(
        "GetVZLicense",
        params={"vzType": "vzType"},
    )
    assert response == success_response


def test_validate(client):
    client._get.return_value = success_response
    response = client.License.Validate()
    client._get.assert_called_once_with(
        "Validate",
        params={},
    )
    assert response == success_response


def test_validate_services(client):
    client._get.return_value = success_response
    response = client.License.ValidateServices()
    client._get.assert_called_once_with(
        "ValidateServices",
        params={},
    )
    assert response == success_response


def test_welcome(client):
    client._get.return_value = success_response
    response = client.License.Welcome(True)
    client._get.assert_called_once_with(
        "ValidateServices", params={"allowInfoSharing": True}
    )
    assert response == success_response
