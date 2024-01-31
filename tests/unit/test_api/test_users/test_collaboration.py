from . import *


def test_accept_collaboration(client):
    client._get.return_value = success_response
    response = client.Collaboration.AcceptCollaboration(
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "AcceptCollaboration", params={"id": 1, "ruk": "ruk"}
    )

    assert response == success_response


def test_activate_member(client):
    client._get.return_value = success_response
    response = client.Collaboration.ActivateMember(
        1,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "ActivateMember", params={"id": 1, "ownerUid": 1, "ruk": "ruk"}
    )

    assert response == success_response


def test_add_policy(client):
    client._get.return_value = success_response
    response = client.Collaboration.AddPolicy(
        "name",
        ["methods1", "methods2"],
        "description",
        "ruk",
    )
    client._get.assert_called_with(
        "AddPolicy",
        params={
            "name": "name",
            "methods": ["methods1", "methods2"],
            "description": "description",
            "ruk": "ruk",
        },
        delimiter=",",
    )

    assert response == success_response


def test_add_resources(client):
    client._get.return_value = success_response
    response = client.Collaboration.AddResources(
        1,
        "resources",
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "AddResources",
        params={
            "collaborationId": 1,
            "resources": "resources",
            "createRoleIfNeeded": True,
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_add_role(client):
    client._get.return_value = success_response
    response = client.Collaboration.AddRole(
        "name",
        ["policies1", "policies2"],
        True,
        "description",
        "ruk",
    )
    client._get.assert_called_with(
        "AddRole",
        params={
            "name": "name",
            "policies": ["policies1", "policies2"],
            "receiveNotification": True,
            "description": "description",
            "ruk": "ruk",
        },
        delimiter=",",
    )

    assert response == success_response


def test_check_environment_rights(client):
    client._get.return_value = success_response
    response = client.Collaboration.CheckEnvironmentRights(
        ["service_method1", "service_method2"],
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "CheckEnvironmentRights",
        params={
            "serviceMethod": ["service_method1", "service_method2"],
            "isAny": True,
            "ruk": "ruk",
        },
        delimiter=",",
    )

    assert response == success_response


def test_delete_member(client):
    client._get.return_value = success_response
    response = client.Collaboration.DeleteMember(
        1,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteMember", params={"id": 1, "ownerUid": 1, "ruk": "ruk"}
    )

    assert response == success_response


def test_delete_policy(client):
    client._get.return_value = success_response
    response = client.Collaboration.DeletePolicy(
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "DeletePolicy",
        params={"id": 1, "ruk": "ruk"},
    )

    assert response == success_response


def test_delete_project_from_resources(client):
    client._get.return_value = success_response
    response = client.Collaboration.DeleteProjectFromResources(
        "project_id",
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteProjectFromResources", params={"projectId": "project_id", "ruk": "ruk"}
    )

    assert response == success_response


def test_delete_resources(client):
    client._get.return_value = success_response
    response = client.Collaboration.DeleteResources(
        "collaboration_id",
        ["ids1", "ids2"],
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteResources",
        params={
            "collaborationId": "collaboration_id",
            "ids": ["ids1", "ids2"],
            "ruk": "ruk",
        },
        delimiter=",",
    )

    assert response == success_response


def test_delete_resources_inner(client):
    client._get.return_value = success_response
    response = client.Collaboration.DeleteResourcesInner(
        "resource_type",
        "resource_id",
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteResourcesInner",
        params={
            "resourceType": "resource_type",
            "resourceId": "resource_id",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_delete_role(client):
    client._get.return_value = success_response
    response = client.Collaboration.DeleteRole(
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteRole",
        params={"id": 1, "ruk": "ruk"},
    )

    assert response == success_response


def test_edit_collaboration(client):
    client._get.return_value = success_response
    response = client.Collaboration.EditCollaboration(
        1,
        "displayName",
        "ruk",
    )
    client._get.assert_called_with(
        "EditCollaboration",
        params={"id": 1, "displayName": "displayName", "ruk": "ruk"},
    )

    assert response == success_response


def test_edit_member(client):
    client._get.return_value = success_response
    response = client.Collaboration.EditMember(
        1,
        "displayName",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "EditMember",
        params={"id": 1, "displayName": "displayName", "ownerUid": 1, "ruk": "ruk"},
    )

    assert response == success_response


def test_edit_policy(client):
    client._get.return_value = success_response
    response = client.Collaboration.EditPolicy(
        1,
        "methods",
        "name",
        "description",
        "ruk",
    )
    client._get.assert_called_with(
        "EditPolicy",
        params={
            "id": 1,
            "methods": "methods",
            "name": "name",
            "description": "description",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_edit_role(client):
    client._get.return_value = success_response
    response = client.Collaboration.EditRole(
        1,
        ["policies1", "policies2", "policies3"],
        "name",
        "description",
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "EditRole",
        params={
            "id": 1,
            "policies": ["policies1", "policies2", "policies3"],
            "name": "name",
            "description": "description",
            "receiveNotification": True,
            "ruk": "ruk",
        },
        delimiter=",",
    )

    assert response == success_response


def test_get_collaboration_resource_methods(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetCollaborationResourceMethods(
        "resource_type",
        "resource_id",
        "ruk",
    )
    client._get.assert_called_with(
        "GetCollaborationResourceMethods",
        params={
            "resourceType": "resource_type",
            "resourceId": "resource_id",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_get_collaboration_resource(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetCollaborationResources(
        1,
        "type",
        "resourceGroup",
        "ruk",
    )
    client._get.assert_called_with(
        "GetCollaborationResources",
        params={
            "collaborationId": 1,
            "type": "type",
            "resourceGroup": "resourceGroup",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_get_collaboration_resource_inner(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetCollaborationResourcesInner(
        1,
        1,
        "type",
        "resourceGroup",
        "ruk",
    )
    client._get.assert_called_with(
        "GetCollaborationResourcesInner",
        params={
            "uid": 1,
            "collaborationId": 1,
            "type": "type",
            "resourceGroup": "resourceGroup",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_get_collaboration_role_methods(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetCollaborationRoleMethods(
        1,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "GetCollaborationRoleMethods",
        params={"collaborationId": 1, "roleId": 1, "ruk": "ruk"},
    )

    assert response == success_response


def test_get_collaboration(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetCollaborations(
        1,
        1,
        "collaborationType",
        "ruk",
    )
    client._get.assert_called_with(
        "GetCollaborations",
        params={
            "id": 1,
            "ownerUid": 1,
            "collaborationType": "collaborationType",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_get_collaborations_inner(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetCollaborationsInner(
        "login",
        "ruk",
    )
    client._get.assert_called_with(
        "GetCollaborationsInner",
        params={"login": "login", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_member_resources(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetMemberResources(
        1,
        "resourceGroup",
        "ruk",
    )
    client._get.assert_called_with(
        "GetMemberResources",
        params={"memberId": 1, "resourceGroup": "resourceGroup", "ruk": "ruk"},
    )

    assert response == success_response


def test_get_member(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetMembers(
        1,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "GetMembers", params={"id": 1, "ownerUid": 1, "ruk": "ruk"}
    )

    assert response == success_response


def test_get_members_inner(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetMembersInner(
        "login",
        "ruk",
    )
    client._get.assert_called_with(
        "GetMembersInner",
        params={"login": "login", "ruk": "ruk"},
    )
    assert response == success_response


def test_get_policies(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetPolicies(
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "GetPolicies",
        params={"id": 1, "ruk": "ruk"},
    )
    assert response == success_response


def test_get_policy_methods(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetPolicyMethods(
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "GetPolicyMethods", params={"policyId": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_get_resource_roles(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetResourceRoles(
        1,
        "resource_id",
        "resourceType",
        "ruk",
    )
    client._get.assert_called_with(
        "GetResourceRoles",
        params={
            "ownerUid": 1,
            "resourceId": "resource_id",
            "resourceType": "resourceType",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_resource_roles_inner(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetResourceRolesInner(
        "target_app_id",
        "ruk",
    )
    client._get.assert_called_with(
        "GetResourceRolesInner", params={"targetAppid": "target_app_id", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_roles(client):
    client._get.return_value = success_response
    response = client.Collaboration.GetRoles(
        1,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "GetRoles", params={"id": 1, "ownerUid": 1, "ruk": "ruk"}
    )

    assert response == success_response


def test_invite_member(client):
    client._get.return_value = success_response
    response = client.Collaboration.InviteMember(
        "email",
        "displayName",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "InviteMember",
        params={
            "email": "email",
            "displayName": "displayName",
            "ownerUid": 1,
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_leave_collaboration(client):
    client._get.return_value = success_response
    response = client.Collaboration.LeaveCollaboration(
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "LeaveCollaboration",
        params={"id": 1, "ruk": "ruk"},
    )

    assert response == success_response


def test_reject_collaboration(client):
    client._get.return_value = success_response
    response = client.Collaboration.RejectCollaboration(
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "RejectCollaboration",
        params={"id": 1, "ruk": "ruk"},
    )

    assert response == success_response


def test_resend_member_invitation(client):
    client._get.return_value = success_response
    response = client.Collaboration.ResendMemberInvitation(
        1,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "ResendMemberInvitation", params={"id": 1, "ownerUid": 1, "ruk": "ruk"}
    )

    assert response == success_response


def test_set_resource(client):
    client._get.return_value = success_response
    response = client.Collaboration.SetResource(
        1,
        "resource_id",
        ["role_id1", "role_id2"],
        "resourceType",
        1,
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "SetResource",
        params={
            "collaborationId": 1,
            "resourceId": "resource_id",
            "roleIds": ["role_id1", "role_id2"],
            "resourceType": "resourceType",
            "ownerUid": 1,
            "createRoleIfNeeded": True,
            "ruk": "ruk",
        },
        delimiter=",",
    )

    assert response == success_response


def test_set_resources(client):
    client._get.return_value = success_response
    response = client.Collaboration.SetResources(
        1,
        "resource",
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "SetResources",
        params={
            "collaborationId": 1,
            "resource": "resource",
            "createRoleIfNeeded": True,
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_suspend_member(client):
    client._get.return_value = success_response
    response = client.Collaboration.SuspendMember(
        1,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "SuspendMember", params={"id": 1, "ownerUid": 1, "ruk": "ruk"}
    )

    assert response == success_response
