from . import *


def test_add_policy(client):
    client._get.return_value = success_response
    response = client.AccessControl.AddPolicy(
        "role",
        "object",
        "rights",
        "ruk",
    )
    client._get.assert_called_once_with(
        "AddPolicy",
        params={"role": "role", "object": "object", "rights": "rights", "ruk": "ruk"},
    )
    assert response == success_response


def test_apply_role(client):
    client._get.return_value = success_response
    response = client.AccessControl.ApplyRole(
        "role",
        "subject",
        "ruk",
    )
    client._get.assert_called_once_with(
        "ApplyRole",
        params={"role": "role", "subject": "subject", "ruk": "ruk"},
    )
    assert response == success_response


def test_check_rights(client):
    client._get.return_value = success_response
    response = client.AccessControl.CheckRights(
        "subject",
        "object",
        "rights",
        "ruk",
    )
    client._get.assert_called_once_with(
        "CheckRights",
        params={
            "subject": "subject",
            "object": "object",
            "rights": "rights",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_create_role(client):
    client._get.return_value = success_response
    response = client.AccessControl.CreateRole(
        "role",
        "ruk",
    )
    client._get.assert_called_once_with(
        "CreateRole",
        params={"role": "role", "ruk": "ruk"},
    )
    assert response == success_response


def test_delete_role(client):
    client._get.return_value = success_response
    response = client.AccessControl.DeleteRole("role", "ruk")
    client._get.assert_called_once_with(
        "DeleteRole",
        params={"role": "role", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_object_by_role(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetObjectsByRole(
        "role",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetObjectsByRole",
        params={"role": "role", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_policy(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetPolicy(
        "role",
        "object",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetPolicy", params={"role": "role", "object": "object", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_rights(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetRights(
        "subject",
        "object",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetRights",
        params={"subject": "subject", "object": "object", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_rights_by_object(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetRightsByObject(
        "object",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetRightsByObject",
        params={"object": "object", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_rights_by_subject(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetRightsBySubject(
        "subject",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetRightsBySubject",
        params={"subject": "subject", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_roles(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetRoles(
        "ruk",
    )
    client._get.assert_called_once_with("GetRoles", params={"ruk": "ruk"})
    assert response == success_response


def test_get_roles_by_subject(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetRolesBySubject(
        "subject",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetRolesBySubject",
        params={"subject": "subject", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_roles_by_object(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetRolesByObject(
        "object",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetRolesByObject",
        params={"object": "object", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_subject_by_role(client):
    client._get.return_value = success_response
    response = client.AccessControl.GetSubjectsByRole(
        "role",
        "ruk",
    )
    client._get.assert_called_once_with(
        "GetSubjectsByRole",
        params={"role": "role", "ruk": "ruk"},
    )
    assert response == success_response


def test_remove_policy(client):
    client._get.return_value = success_response
    response = client.AccessControl.RemovePolicy(
        "role",
        "object",
        "ruk",
    )
    client._get.assert_called_once_with(
        "RemovePolicy",
        params={"role": "role", "object": "object", "ruk": "ruk"},
    )
    assert response == success_response


def test_remove_rights(client):
    client._get.return_value = success_response
    response = client.AccessControl.RemoveRights(
        "subject",
        "object",
        "ruk",
    )
    client._get.assert_called_once_with(
        "RemoveRights",
        params={"subject": "subject", "object": "object", "ruk": "ruk"},
    )
    assert response == success_response


def test_remove_rights_by_object(client):
    client._get.return_value = success_response
    response = client.AccessControl.RemoveRightsByObject(
        "object",
        "ruk",
    )
    client._get.assert_called_once_with(
        "RemoveRightsByObject",
        params={"object": "object", "ruk": "ruk"},
    )
    assert response == success_response


def test_remove_rights_by_subject(client):
    client._get.return_value = success_response
    response = client.AccessControl.RemoveRightsBySubject(
        "subject",
        "ruk",
    )
    client._get.assert_called_once_with(
        "RemoveRightsBySubject",
        params={"subject": "subject", "ruk": "ruk"},
    )
    assert response == success_response


def test_remove_role(client):
    client._get.return_value = success_response
    response = client.AccessControl.RemoveRole(
        "role",
        "subject",
        "ruk",
    )
    client._get.assert_called_once_with(
        "RemoveRole",
        params={"role": "role", "subject": "subject", "ruk": "ruk"},
    )
    assert response == success_response


def test_set_rights(client):
    client._get.return_value = success_response
    response = client.AccessControl.SetRights(
        "object",
        "subject",
        "rights",
        "ruk",
    )
    client._get.assert_called_once_with(
        "SetRights",
        params={
            "object": "object",
            "subject": "subject",
            "rights": "rights",
            "ruk": "ruk",
        },
    )
    assert response == success_response
