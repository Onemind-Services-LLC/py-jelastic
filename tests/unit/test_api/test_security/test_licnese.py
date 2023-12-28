from . import *


def test_activate(client):
    client._get.return_value = success_response
    response = client.License.Activate(
        ["serial1", "serial2", "serial3"],
        [True, False, True],
    )
    client._get.assert_called_once_with(
        "Activate",
        params={
            "serial": ["serial1", "serial2", "serial3"],
            "generateSMTPCreds": [True, False, True],
        },
        delimiter=",",
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
    response = client.License.GetVZLicense(["type1", "type2", "type3"])
    client._get.assert_called_once_with(
        "GetVZLicense",
        params={
            "vzType": ["type1", "type2", "type3"],
        },
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
