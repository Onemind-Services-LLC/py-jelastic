from . import *


def test_accept_collaboration(client):
    client._get.return_value = success_response
    response = client.Collaboration.AcceptCollaboration(1)
    client._get.assert_called_with("AcceptCollaboration", params={"id": 1})

    assert response == success_response


def test_activate_member(client):
    client._get.return_value = success_response
    response = client.Collaboration.ActivateMember(1, [1, 1])
    client._get.assert_called_with(
        "ActivateMember", params={"id": 1, "ownerUid": [1, 1]}
    )

    assert response == success_response


def test_add_policy(client):
    client._get.return_value = success_response
    response = client.Collaboration.AddPolicy(
        "name", "methods", ["description1", "description2"]
    )
    client._get.assert_called_with(
        "AddPolicy",
        params={
            "name": "name",
            "methods": "methods",
            "description": ["description1", "description2"],
        },
    )

    assert response == success_response


def test_add_resources(client):
    client._get.return_value = success_response
    response = client.Collaboration.AddResources(1, "resources", [True, True])
    client._get.assert_called_with(
        "AddResources",
        params={
            "collaborationId": 1,
            "resources": "resources",
            "createRoleIfNeeded": [True, True],
        },
        delimeter=",",
    )

    assert response == success_response


def test_add_role(client):
    client._get.return_value = success_response
    response = client.Collaboration.AddRole(
        "name", "policies", True, ["description1", "description2"]
    )
    client._get.assert_called_with(
        "AddRole",
        params={
            "name": "name",
            "policies": "policies",
            "receiveNotification": True,
            "description": ["description1", "description2"],
        },
        delimeter=",",
    )

    assert response == success_response


def test_check_environment_rights(client):
    client._get.return_value = success_response
    response = client.Collaboration.CheckEnvironmentRights(
        "service_method", [True, True]
    )
    client._get.assert_called_with(
        "CheckEnvironmentRights",
        params={"serviceMethod": "service_method", "isAny": [True, True]},
        delimeter=",",
    )

    assert response == success_response


def test_delete_member(client):
    client._get.return_value = success_response
    response = client.Collaboration.DeleteMember(1, [1, 1])
    client._get.assert_called_with(
        "DeleteMember",
        params={"id": 1, "ownerUid": [1, 1]},
        delimeter=",",
    )

    assert response == success_response


def test_delete_policy(client):
    client._get.return_value = success_response
    response = client.Collaboration.DeletePolicy(1)
    client._get.assert_called_with(
        "DeletePolicy",
        params={
            "id": 1,
        },
    )

    assert response == success_response


def test_delete_project_from_resources(client):
    client._get.return_value = success_response
    response = client.Collaboration.DeleteProjectFromResources("project_id")
    client._get.assert_called_with(
        "DeleteProjectFromResources", params={"projectId": "project_id"}
    )

    assert response == success_response


def test_delete_resources(client):
    client._get.return_value = success_response
    response = client.Collaboration.DeleteResources(
        "collaboration_id",
        ["ids1", "ids2"],
    )
    client._get.assert_called_with(
        "DeleteResources",
        params={
            "collaborationId": "collaboration_id",
            "ids": ["ids1", "ids2"],
        },
        delimeter=",",
    )

    assert response == success_response


def test_delete_resources_inner(client):
    client._get.return_value = success_response
    response = client.Collaboration.DeleteResourcesInner("resource_type", "resource_id")
    client._get.assert_called_with(
        "DeleteResourcesInner",
        params={
            "resourceType": "resource_type",
            "resourceId": "resource_id",
        },
        delimeter=",",
    )

    assert response == success_response


def test_delete_role(client):
    client._get.return_value = success_response
    response = client.Collaboration.DeleteRole(1)
    client._get.assert_called_with(
        "DeleteRole",
        params={
            "id": 1,
        },
    )

    assert response == success_response


def test_edit_collaboration(client):
    client._get.return_value = success_response
    response = client.Collaboration.EditCollaboration(
        1,
        ["display_name1", "display_name2"],
    )
    client._get.assert_called_with(
        "EditCollaboration",
        params={
            "id": 1,
            "displayName": ["display_name1", "display_name2"],
        },
        delimeter=",",
    )

    assert response == success_response


def test_edit_member(client):
    client._get.return_value = success_response
    response = client.Collaboration.EditMember(
        1, ["display_name1", "display_name2"], [1, 2]
    )
    client._get.assert_called_with(
        "EditMember",
        params={
            "id": 1,
            "displayName": ["display_name1", "display_name2"],
            "ownerUid": [1, 2],
        },
        delimeter=",",
    )

    assert response == success_response


def test_edit_policy(client):
    client._get.return_value = success_response
    response = client.Collaboration.EditPolicy(
        1, "methods", ["name1", "name2"], ["description1", "description2"]
    )
    client._get.assert_called_with(
        "EditPolicy",
        params={
            "id": 1,
            "methods": "methods",
            "name": ["name1", "name2"],
            "description": ["description1", "description2"],
        },
        delimeter=",",
    )

    assert response == success_response


def test_edit_role(client):
    client._get.return_value = success_response
    response = client.Collaboration.EditRole(
        1,
        "policies",
        ["name1", "name2"],
        ["description1", "description2"],
        [True, True],
    )
    client._get.assert_called_with(
        "EditRole",
        params={
            "id": 1,
            "policies": "policies",
            "name": ["name1", "name2"],
            "description": ["description1", "description2"],
            "receiveNotification": [True, True],
        },
        delimeter=",",
    )

    assert response == success_response


def test_get_collaboration_resource_methods(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetCollaborationResourceMethods(
        "resource_type", "resource_id"
    )
    client._get.assert_called_with(
        "GetCollaborationResourceMethods",
        params={
            "resourceType": "resource_type",
            "resourceId": "resource_id",
        },
        delimeter=",",
    )

    assert response == success_response


def test_get_collaboration_resource(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetCollaborationResources(
        [1, 1], ["type1", "type2"], ["resource_group1", "resource_group2"]
    )
    client._get.assert_called_with(
        "GetCollaborationResources",
        params={
            "collaborationId": [1, 1],
            "type": ["type1", "type2"],
            "resourceGroup": ["resource_group1", "resource_group2"],
        },
        delimeter=",",
    )

    assert response == success_response


def test_get_collaboration_resource_inner(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetCollaborationResourcesInner(
        [1, 1], [1, 1], ["type1", "type2"], ["resource_group1", "resource_group2"]
    )
    client._get.assert_called_with(
        "GetCollaborationResourcesInner",
        params={
            "uid": [1, 1],
            "collaborationId": [1, 1],
            "type": ["type1", "type2"],
            "resourceGroup": ["resource_group1", "resource_group2"],
        },
        delimeter=",",
    )

    assert response == success_response


def test_get_collaboration_role_methods(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetCollaborationRoleMethods([1, 1], [1, 1])
    client._get.assert_called_with(
        "GetCollaborationRoleMethods",
        params={
            "collaborationId": [1, 1],
            "roleId": [1, 1],
        },
        delimeter=",",
    )

    assert response == success_response


def test_get_collaboration(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetCollaborations(
        [1, 1], [1, 1], ["collaboration_type1", "collaboration_type2"]
    )
    client._get.assert_called_with(
        "GetCollaborations",
        params={
            "id": [1, 1],
            "ownerUid": [1, 1],
            "collaborationType": ["collaboration_type1", "collaboration_type2"],
        },
        delimeter=",",
    )

    assert response == success_response


def test_get_collaborations_inner(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetCollaborationsInner("login")
    client._get.assert_called_with(
        "GetCollaborationsInner",
        params={
            "login": "login",
        },
    )
    assert response == success_response


def test_get_member_resources(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetMemberResources(
        [1, 1], ["resource_group1", "resource_group2"]
    )
    client._get.assert_called_with(
        "GetMemberResources",
        params={
            "memberId": [1, 1],
            "resourceGroup": ["resource_group1", "resource_group2"],
        },
        delimeter=",",
    )

    assert response == success_response


def test_get_member(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetMembers(1, [1, 1])
    client._get.assert_called_with(
        "GetMembers",
        params={"id": 1, "ownerUid": [1, 1]},
        delimeter=",",
    )

    assert response == success_response


def test_get_members_inner(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetMembersInner("login")
    client._get.assert_called_with(
        "GetMembersInner",
        params={
            "login": "login",
        },
    )
    assert response == success_response


def test_get_polcies(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetPolicies([1, 1])
    client._get.assert_called_with(
        "GetPolicies",
        params={
            "id": [1, 1],
        },
    )
    assert response == success_response


def test_get_policy_methods(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetPolicyMethods([1, 1])
    client._get.assert_called_with("GetPolicyMethods", params={"policyId": [1, 1]})
    assert response == success_response


def test_get_resource_roles(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetResourceRoles(
        1,
        "resource_id",
        ["resource_type1", "resource_type2"],
    )
    client._get.assert_called_with(
        "GetResourceRoles",
        params={
            "ownerUid": 1,
            "resourceId": "resource_id",
            "resourceType": ["resource_type1", "resource_type2"],
        },
        delimeter=",",
    )
    assert response == success_response


def test_get_resource_roles_inner(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetResourceRolesInner("target_app_id")
    client._get.assert_called_with(
        "GetResourceRolesInner", params={"targetAppid": "target_app_id"}
    )
    assert response == success_response


def test_get_roles(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetRoles(1, [1, 1])
    client._get.assert_called_with(
        "GetRoles",
        params={"id": 1, "ownerUid": [1, 1]},
        delimeter=",",
    )

    assert response == success_response


def test_invite_member(client):
    client._get.return_value = success_response
    response = client.Collaboration.InviteMember(
        "email", ["display_name1", "display_name2"], [1, 1]
    )
    client._get.assert_called_with(
        "InviteMember",
        params={
            "email": "email",
            "displayName": ["display_name1", "display_name2"],
            "ownerUid": [1, 1],
        },
        delimeter=",",
    )

    assert response == success_response


def test_leave_collaboration(client):
    client._get.return_value = success_response
    response = client.Collaboration.LeaveCollaboration(1)
    client._get.assert_called_with(
        "LeaveCollaboration",
        params={
            "id": 1,
        },
    )

    assert response == success_response


def test_reject_collaboration(client):
    client._get.return_value = success_response
    response = client.Collaboration.RejectCollaboration(1)
    client._get.assert_called_with(
        "RejectCollaboration",
        params={
            "id": 1,
        },
    )

    assert response == success_response


def test_resend_member_invitation(client):
    client._get.return_value = success_response
    response = client.Collaboration.ResendMemberInvitation(1, [1, 1])
    client._get.assert_called_with(
        "ResendMemberInvitation",
        params={"id": 1, "ownerUid": [1, 1]},
        delimeter=",",
    )

    assert response == success_response


def test_set_resource(client):
    client._get.return_value = success_response
    response = client.Collaboration.SetResource(
        1,
        "resource_id",
        "role_id",
        ["resource_type1", "resource_type2"],
        [1, 1],
        [True, True],
    )
    client._get.assert_called_with(
        "SetResource",
        params={
            "collaborationId": 1,
            "resourceId": "resource_id",
            "roleIds": "role_id",
            "resourceType": ["resource_type1", "resource_type2"],
            "ownerUid": [1, 1],
            "createRoleIfNeeded": [True, True],
        },
        delimeter=",",
    )

    assert response == success_response


def test_set_resources(client):
    client._get.return_value = success_response
    response = client.Collaboration.SetResources(1, "resource", [True, True])
    client._get.assert_called_with(
        "SetResources",
        params={
            "collaborationId": 1,
            "resource": "resource",
            "createRoleIfNeeded": [True, True],
        },
        delimeter=",",
    )

    assert response == success_response


def test_suspend_member(client):
    client._get.return_value = success_response
    response = client.Collaboration.SuspendMember(1, [1, 1])
    client._get.assert_called_with(
        "SuspendMember",
        params={"id": 1, "ownerUid": [1, 1]},
        delimeter=",",
    )

    assert response == success_response


def test_get_auth_endpoint(client):
    client._get.return_value = success_response
    response = client.SSO.GetAuthEndpoint("redirect_uri")
    client._get.assert_called_with(
        "GetAuthEndpoint",
        params={
            "redirectUri": "redirect_uri",
        },
    )

    assert response == success_response


def test_get_impersonation_data(client):
    client._get.return_value = success_response
    response = client.SSO.GetImpersonationData(1)
    client._get.assert_called_with(
        "GetImpersonationData",
        params={
            "uid": 1,
        },
    )

    assert response == success_response


def test_get_settings(client):
    client._get.return_value = success_response
    response = client.SSO.GetSettings()
    client._get.assert_called_with(
        "GetSettings",
        params={},
    )

    assert response == success_response


def test_reset_password(client):
    client._get.return_value = success_response
    response = client.SSO.ResetPassword()
    client._get.assert_called_with(
        "ResetPassword",
        params={},
    )

    assert response == success_response


def test_sign_in_by_code(client):
    client._get.return_value = success_response
    response = client.SSO.SigninByCode("code", "redirect_uri")
    client._get.assert_called_with(
        "SigninByCode",
        params={
            "code": "code",
            "redirectUri": "redirect_uri",
        },
    )

    assert response == success_response


def test_sign_in_by_token(client):
    client._get.return_value = success_response
    response = client.SSO.SigninByToken("token")
    client._get.assert_called_with(
        "SigninByToken",
        params={
            "token": "token",
        },
    )

    assert response == success_response
