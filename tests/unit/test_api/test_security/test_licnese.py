from . import *


def test_activate(client):
    client._get.return_value = success_response
    response = client.License.Activate(
        "serial",
        True,
        "ruk",
    )
    client._get.assert_called_once_with(
        "Activate", params={"serial": "serial", "generateSMTPCreds": True, "ruk": "ruk"}
    )
    assert response == success_response


def test_generate_smtp_settings(client):
    client._get.return_value = success_response
    response = client.License.GenerateSMTPSettings(
        "ruk",
    )
    client._get.assert_called_once_with(
        "GenerateSMTPSettings",
        params={"ruk": "ruk"},
    )
    assert response == success_response


def test_get_vz_license(client):
    client._get.return_value = success_response
    response = client.License.GetVZLicense(
        "vzType",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetVZLicense",
        params={"vzType": "vzType", "ruk": "ruk"},
    )
    assert response == success_response


def test_validate(client):
    client._get.return_value = success_response
    response = client.License.Validate(
        "ruk",
    )
    client._get.assert_called_once_with(
        "Validate",
        params={"ruk": "ruk"},
    )
    assert response == success_response


def test_validate_services(client):
    client._get.return_value = success_response
    response = client.License.ValidateServices(
        "ruk",
    )
    client._get.assert_called_once_with(
        "ValidateServices",
        params={"ruk": "ruk"},
    )
    assert response == success_response


def test_welcome(client):
    client._get.return_value = success_response
    response = client.License.Welcome(
        True,
        "ruk",
    )
    client._get.assert_called_once_with(
        "ValidateServices", params={"allowInfoSharing": True, "ruk": "ruk"}
    )
    assert response == success_response
