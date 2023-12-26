import pytest
from unittest.mock import patch, Mock
from jelastic.api import Security

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        security = Security(session=Mock(), token="token")
        security._get = mock_get
        yield security


def test_add_policy(client):
    client._get.return_value = success_response
    response = client.AccessControl.AddPolicy(
        "role",
        "object",
        "rights",
    )
    client._get.assert_called_once_with(
        "AddPolicy", params={"role": "role", "object": "object", "rights": "rights"}
    )
    assert response == success_response


def test_apply_role(client):
    client._get.return_value = success_response
    response = client.AccessControl.ApplyRole("role", "subject")
    client._get.assert_called_once_with(
        "ApplyRole",
        params={
            "role": "role",
            "subject": "subject",
        },
    )
    assert response == success_response


def test_check_rights(client):
    client._get.return_value = success_response
    response = client.AccessControl.CheckRights(
        "subject",
        "object",
        "rights",
    )
    client._get.assert_called_once_with(
        "CheckRights",
        params={"subject": "subject", "object": "object", "rights": "rights"},
    )
    assert response == success_response


def test_create_role(client):
    client._get.return_value = success_response
    response = client.AccessControl.CreateRole("role")
    client._get.assert_called_once_with(
        "CreateRole",
        params={
            "role": "role",
        },
    )
    assert response == success_response


def test_delete_role(client):
    client._get.return_value = success_response
    response = client.AccessControl.DeleteRole("role")
    client._get.assert_called_once_with(
        "DeleteRole",
        params={
            "role": "role",
        },
    )
    assert response == success_response


def test_get_object_by_role(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetObjectsByRole("role")
    client._get.assert_called_once_with(
        "GetObjectsByRole",
        params={
            "role": "role",
        },
    )
    assert response == success_response


def test_get_policy(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetPolicy(
        "role",
        ["object1", "object2", "object3"],
    )
    client._get.assert_called_once_with(
        "GetPolicy",
        params={
            "role": "role",
            "object": ["object1", "object2", "object3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_rights(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetRights("subject", "object")
    client._get.assert_called_once_with(
        "GetRights",
        params={
            "subject": "subject",
            "object": "object",
        },
    )
    assert response == success_response


def test_get_rights_by_object(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetRightsByObject(
        "object",
    )
    client._get.assert_called_once_with(
        "GetRightsByObject",
        params={
            "object": "object",
        },
    )
    assert response == success_response


def test_get_rights_by_subject(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetRightsBySubject(
        "subject",
    )
    client._get.assert_called_once_with(
        "GetRightsBySubject",
        params={
            "subject": "subject",
        },
    )
    assert response == success_response


def test_get_roles(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetRoles()
    client._get.assert_called_once_with("GetRoles", params={})
    assert response == success_response


def test_get_roles_by_subject(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetRolesBySubject("subject")
    client._get.assert_called_once_with(
        "GetRolesBySubject",
        params={
            "subject": "subject",
        },
    )
    assert response == success_response


def test_get_roles_by_object(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetRolesByObject("object")
    client._get.assert_called_once_with(
        "GetRolesByObject",
        params={
            "object": "object",
        },
    )
    assert response == success_response


def test_get_subject_by_role(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetSubjectsByRole("role")
    client._get.assert_called_once_with(
        "GetSubjectsByRole",
        params={
            "role": "role",
        },
    )
    assert response == success_response


def test_remove_policy(client):
    client._get.return_value = success_response
    response = client.AccessControl.RemovePolicy("role", "object")
    client._get.assert_called_once_with(
        "RemovePolicy",
        params={
            "role": "role",
            "object": "object",
        },
    )
    assert response == success_response


def test_remove_rights(client):
    client._get.return_value = success_response
    response = client.AccessControl.RemoveRights("subject", "object")
    client._get.assert_called_once_with(
        "RemoveRights",
        params={
            "subject": "subject",
            "object": "object",
        },
    )
    assert response == success_response


def test_remove_rights_by_object(client):
    client._get.return_value = success_response
    response = client.AccessControl.RemoveRightsByObject("object")
    client._get.assert_called_once_with(
        "RemoveRightsByObject",
        params={
            "object": "object",
        },
    )
    assert response == success_response


def test_remove_rights_by_subject(client):
    client._get.return_value = success_response
    response = client.AccessControl.RemoveRightsBySubject("subject")
    client._get.assert_called_once_with(
        "RemoveRightsBySubject",
        params={
            "subject": "subject",
        },
    )
    assert response == success_response


def test_remove_role(client):
    client._get.return_value = success_response
    response = client.AccessControl.RemoveRole("role", "subject")
    client._get.assert_called_once_with(
        "RemoveRole",
        params={
            "role": "role",
            "subject": "subject",
        },
    )
    assert response == success_response


def test_set_rights(client):
    client._get.return_value = success_response
    response = client.AccessControl.SetRights("object", "subject", "rights")
    client._get.assert_called_once_with(
        "SetRights",
        params={
            "object": "object",
            "subject": "subject",
            "rights": "rights",
        },
    )
    assert response == success_response


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
