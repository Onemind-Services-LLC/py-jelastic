from ..abstract import ClientAbstract

__all__ = ["Users"]

from datetime import datetime


class Users(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users
    Ref: https://docs.jelastic.com/api/private/#!/api/users
    """

    _endpoint1 = "users"

    @property
    def Collaboration(self) -> "_Collaboration":
        """
               This service is responsible for managing the accounts collaboration feature on the platform. The core idea is that users can share the necessary environments and access to some account features with other platform customers. Complete control over the shared management permissions makes the feature suitable for most possible use cases.

        Collaboration owner - a primary account where shared environments are hosted. All charges for the shared environments (including actions performed by collaborators) are applied to this account.
        Collaboration member - user account with partial access to the collaboration owner account. Shared functionality is defined by the collaboration owner.
        Collaboration (shared) resources - instances (environments, groups) shared in the collaboration.
        Collaboration policies - small API sets that allow specific operations.
        Collaboration roles - a combination of policies that create the required range of actions to share with members.
                >>> from jelastic import Jelastic
                >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
                >>> jelastic.users.Collaboration
                Ref: https://docs.jelastic.com/api/private/#!/api/users.Collaboration
        """
        return _Collaboration(
            session=self._session, token=self._token, debug=self._debug
        )

    @property
    def Team(self) -> "_Team":
        """
            >>> from jelastic import Jelastic
            >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
            >>> jelastic.users.Team
        Ref: https://docs.jelastic.com/api/private/#!/api/users.Team
        """
        return _Team(session=self._session, token=self._token, debug=self._debug)


class _Collaboration(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.Collaboration
     Ref: https://docs.jelastic.com/api/private/#!/api/users.Collaboration
    """

    _endpoint2 = "collaboration"

    def AcceptCollaboration(self, id: int):
        """
        param id: unique identifier of the collaboration invite.
        """
        return self._get(
            "AcceptCollaboration",
            params={"id": id},
        )

    def ActivateMember(
        self,
        id: int,
        owner_uid: list[int] = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "ActivateMember",
            params={"id": id, "ownerUid": owner_uid},
        )

    def AddPolicy(self, name: str, methods: str, description: list[str] = None):
        """
        param name: custom name for the target policy.
        param methods: a comma-separated list of API methods allowed by this new policy.
        param description: custom description for the target new policy.
        """
        return self._get(
            "AddPolicy",
            params={"name": name, "methods": methods, "description": description},
        )

    def AddResources(
        self,
        collaboration_id: int,
        resources: str,
        create_role_if_needed: list[bool] = None,
    ):
        """
        param collaboration_id: create_role_if_needed
        param resources: JSON object with shared resources (environments and groups) to be added to the collaboration.
        param create_role_if_needed: defines whether to create a new role for the added shared resources (true) or not (false).
        """
        return self._get(
            "AddResources",
            params={
                "collaborationId": collaboration_id,
                "resources": resources,
                "createRoleIfNeeded": create_role_if_needed,
            },
            delimeter=",",
        )

    def AddRole(
        self,
        name: str,
        policies: str,
        receive_notification: bool,
        description: list[str] = None,
    ):
        """
        param name: custom name for the target new role.
        param policies: a comma-separated list of policies for the target new role.
        param receive_notification: a comma-separated list of policies for the target new role.
        param description:  custom description for the target new role.
        """
        return self._get(
            "AddRole",
            params={
                "name": name,
                "policies": policies,
                "receiveNotification": receive_notification,
                "description": description,
            },
            delimeter=",",
        )

    def CheckEnvironmentRights(
        self,
        service_method: str,
        is_any: list[bool] = None,
    ):
        """
        param service_method: a semicolon-separated list of API methods.
        param is_any: defines whether all the listed methods should be allowed (false) or at least one (true).
        """
        return self._get(
            "CheckEnvironmentRights",
            params={"serviceMethod": service_method, "isAny": is_any},
            delimeter=",",
        )

    def DeleteMember(
        self,
        id: int,
        owner_uid: list[int] = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "DeleteMember",
            params={"id": id, "ownerUid": owner_uid},
            delimeter=",",
        )

    def DeletePolicy(
        self,
        id: int,
    ):
        """
        param id: unique identifier of the collaboration invite.
        """
        return self._get(
            "DeletePolicy",
            params={
                "id": id,
            },
        )

    def DeleteProjectFromResources(
        self,
        project_id: str,
    ):
        """
        param project_id: unique identifier of the target project.
        """
        return self._get(
            "DeleteProjectFromResources",
            params={
                "projectId": project_id,
            },
        )

    def DeleteResources(
        self,
        collaboration_id: str,
        ids: list[str] = None,
    ):
        """
        param collaboration_id: unique identifier of the target collaboration.
        param ids: a comma-separated list of shared resources identifiers.
        """
        return self._get(
            "DeleteResources",
            params={
                "collaborationId": collaboration_id,
                "ids": ids,
            },
            delimeter=",",
        )

    def DeleteResourcesInner(self, resource_type: str, resource_id: str):
        return self._get(
            "DeleteResourcesInner",
            params={
                "resourceType": resource_type,
                "resourceId": resource_id,
            },
            delimeter=",",
        )

    def DeleteRole(
        self,
        id: int,
    ):
        """
        param id: unique identifier of the target collaboration role to delete.
        """
        return self._get(
            "DeleteRole",
            params={
                "id": id,
            },
        )

    def EditCollaboration(self, id: int, display_name: list[str] = None):
        """
        param id: unique identifier of the target collaboration to edit.
        param display_name: name of the collaboration displayed in the dashboard.
        """
        return self._get(
            "EditCollaboration",
            params={
                "id": id,
                "displayName": display_name,
            },
            delimeter=",",
        )

    def EditMember(
        self, id: int, display_name: list[str] = None, owner_uid: list[int] = None
    ):
        """
        param id: unique identifier of the target collaboration to edit.
        param display_name: name of the collaboration displayed in the dashboard.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "EditMember",
            params={
                "id": id,
                "displayName": display_name,
                "ownerUid": owner_uid,
            },
            delimeter=",",
        )

    def EditPolicy(
        self,
        id: int,
        methods: str,
        name: list[str] = None,
        description: list[str] = None,
    ):
        """
        param id: unique identifier of the target collaboration to edit.
        param methods: custom name for the target policy.
        param name: custom name for the target policy.
        param description: custom description for the target policy.
        """
        return self._get(
            "EditPolicy",
            params={
                "id": id,
                "methods": methods,
                "name": name,
                "description": description,
            },
            delimeter=",",
        )

    def EditRole(
        self,
        id: int,
        policies: str,
        name: list[str] = None,
        description: list[str] = None,
        receive_notification: list[bool] = None,
    ):
        """
        param id: unique identifier of the target collaboration to edit.
        param policies: a comma-separated list of policies for the target role.
        param name: custom name for the target policy.
        param description: custom description for the target policy.
        param receive_notification: defines whether to allow (true) collaboration members with this role to receive load alert notifications about shared environments or not (false).
        """
        return self._get(
            "EditRole",
            params={
                "id": id,
                "policies": policies,
                "name": name,
                "description": description,
                "receiveNotification": receive_notification,
            },
            delimeter=",",
        )

    def GetCollaborationResourceMethods(self, resource_type: str, resource_id: str):
        """
        param resource_type: unique identifier of the target collaboration resource
        param resource_id: type (ENV, ENV_GROUP, ACCOUNT, VHI_REGION, S3_REGION) of the target collaboration resource.
        """
        return self._get(
            "GetCollaborationResourceMethods",
            params={
                "resourceType": resource_type,
                "resourceId": resource_id,
            },
            delimeter=",",
        )

    def GetCollaborationResources(
        self,
        collaboration_id: list[int] = None,
        type: list[str] = None,
        resource_group: list[str] = None,
    ):
        """
        param collaboration_id: unique identifier of the target collaboration.
        param type: filters results by the provided resource type (ENV, ENV_GROUP, ACCOUNT, VHI_REGION, S3_REGION).
        param resource_group: filters results by the provided resource group (ALL, VAP, CMP).
        """
        return self._get(
            "GetCollaborationResources",
            params={
                "collaborationId": collaboration_id,
                "type": type,
                "resourceGroup": resource_group,
            },
            delimeter=",",
        )

    def GetCollaborationResourcesInner(
        self,
        uid: list[int] = None,
        collaboration_id: list[int] = None,
        type: list[str] = None,
        resource_group: list[str] = None,
    ):
        """
        param uid: unique identifier of the target user.
        param collaboration_id: unique identifier of the target collaboration.
        param type: filters results by the provided resource type (ENV, ENV_GROUP, ACCOUNT, VHI_REGION, S3_REGION).
        param resource_group: filters results by the provided resource group (ALL, VAP, CMP).
        """
        return self._get(
            "GetCollaborationResourcesInner",
            params={
                "uid": uid,
                "collaborationId": collaboration_id,
                "type": type,
                "resourceGroup": resource_group,
            },
            delimeter=",",
        )

    def GetCollaborationRoleMethods(
        self,
        collaboration_id: list[int] = None,
        role_id: list[int] = None,
    ):
        """
        param collaboration_id: unique identifier of the target collaboration.
        param role_id: unique identifier of the target role.
        """
        return self._get(
            "GetCollaborationRoleMethods",
            params={
                "collaborationId": collaboration_id,
                "roleId": role_id,
            },
            delimeter=",",
        )

    def GetCollaborations(
        self,
        id: list[int] = None,
        owner_uid: list[int] = None,
        collaboration_type: list[str] = None,
    ):
        """
        param id: unique identifier of the target collaboration
        param owner_uid: unique identifier of the collaboration owner.
        param collaboration_type: collaboration type (ACCOUNT or GROUP)
        """
        return self._get(
            "GetCollaborations",
            params={
                "id": id,
                "ownerUid": owner_uid,
                "collaborationType": collaboration_type,
            },
            delimeter=",",
        )

    def GetCollaborationsInner(
        self,
        login: str,
    ):
        return self._get(
            "GetCollaborationsInner",
            params={
                "login": login,
            },
        )

    def GetMemberResources(
        self,
        member_id: list[int] = None,
        resource_group: list[str] = None,
    ):
        """
        param member_id: unique identifier of the target collaboration member.
        param resource_group: filters results by the provided resource group (ALL, VAP, CMP).
        """
        return self._get(
            "GetMemberResources",
            params={
                "memberId": member_id,
                "resourceGroup": resource_group,
            },
            delimeter=",",
        )

    def GetMembers(
        self,
        id: int,
        owner_uid: list[int] = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "GetMembers",
            params={"id": id, "ownerUid": owner_uid},
            delimeter=",",
        )

    def GetMembersInner(
        self,
        login: str,
    ):
        return self._get(
            "GetMembersInner",
            params={
                "login": login,
            },
        )

    def GetPolicies(
        self,
        id: list[int] = None,
    ):
        """
        param id: unique identifier of the target policy.
        """
        return self._get(
            "GetPolicies",
            params={
                "id": id,
            },
        )

    def GetPolicyMethods(
        self,
        policy_id: list[int] = None,
    ):
        """
        param id: unique identifier of the target policy.
        """
        return self._get(
            "GetPolicyMethods",
            params={
                "policyId": policy_id,
            },
        )

    def GetResourceRoles(
        self,
        owner_uid: int,
        resource_id: str,
        resource_type: list[str] = None,
    ):
        """
        param owner_uid: unique identifier of the target collaboration resource.
         param resource_id: type (ENV, ENV_GROUP, ACCOUNT, VHI_REGION, S3_REGION) of the target collaboration resource.
        param resource_type: unique identifier of the target collaboration resource
        """
        return self._get(
            "GetResourceRoles",
            params={
                "ownerUid": owner_uid,
                "resourceId": resource_id,
                "resourceType": resource_type,
            },
            delimeter=",",
        )

    def GetResourceRolesInner(
        self,
        target_app_id: str,
    ):
        return self._get(
            "GetResourceRolesInner",
            params={
                "targetAppid": target_app_id,
            },
        )

    def GetRoles(
        self,
        id: int,
        owner_uid: list[int] = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "GetRoles",
            params={"id": id, "ownerUid": owner_uid},
            delimeter=",",
        )

    def InviteMember(
        self, email: str, display_name: list[str] = None, owner_uid: list[int] = None
    ):
        """
        param email: email address of the user to invite to the collaboration.
        param display_name: name of the collaboration displayed in the dashboard.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "InviteMember",
            params={
                "email": email,
                "displayName": display_name,
                "ownerUid": owner_uid,
            },
            delimeter=",",
        )

    def LeaveCollaboration(
        self,
        id: int,
    ):
        """
        param id: unique identifier of the collaboration invite.
        """
        return self._get(
            "LeaveCollaboration",
            params={
                "id": id,
            },
        )

    def RejectCollaboration(
        self,
        id: int,
    ):
        """
        param id: unique identifier of the collaboration invite.
        """
        return self._get(
            "RejectCollaboration",
            params={
                "id": id,
            },
        )

    def ResendMemberInvitation(
        self,
        id: int,
        owner_uid: list[int] = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "ResendMemberInvitation",
            params={"id": id, "ownerUid": owner_uid},
            delimeter=",",
        )

    def SetResource(
        self,
        collaboration_id: int,
        resource_id: str,
        role_id: str,
        resource_type: list[str] = None,
        owner_uid: list[int] = None,
        create_role_if_needed: list[bool] = None,
    ):
        """
        param collaboration_id:unique identifier of the target collaboration
        param resource_id: unique identifier of the target collaboration resource.
        param role_id: a comma-separated list of the role IDs for the provided resource.
        param resource_type: type (ENV, ENV_GROUP, ACCOUNT, VHI_REGION, S3_REGION) of the provided resource.
        param owner_uid: unique identifier of the collaboration owner.
        param create_role_if_needed: defines whether to create a new role for the added shared resources (true) or not (false).
        """
        return self._get(
            "SetResource",
            params={
                "collaborationId": collaboration_id,
                "resourceId": resource_id,
                "roleIds": role_id,
                "resourceType": resource_type,
                "ownerUid": owner_uid,
                "createRoleIfNeeded": create_role_if_needed,
            },
            delimeter=",",
        )

    def SetResources(
        self,
        collaboration_id: int,
        resource: str,
        create_role_if_needed: list[bool] = None,
    ):
        """
        param collaboration_id:unique identifier of the target collaboration
        param resource: unique identifier of the target collaboration resource.
        param create_role_if_needed: defines whether to create a new role for the added shared resources (true) or not (false).
        """
        return self._get(
            "SetResources",
            params={
                "collaborationId": collaboration_id,
                "resource": resource,
                "createRoleIfNeeded": create_role_if_needed,
            },
            delimeter=",",
        )

    def SuspendMember(
        self,
        id: int,
        owner_uid: list[int] = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "SuspendMember",
            params={"id": id, "ownerUid": owner_uid},
            delimeter=",",
        )


class _Team(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.Team
     Ref: https://docs.jelastic.com/api/private/#!/api/users.Team
    """

    _endpoint2 = "team"

    def Create(self, display_name: str, owner_uid: list[int] = None):
        """
        param owner_uid: unique identifier of the collaboration Team owner.
        """
        return self._get(
            "Create",
            params={
                "displayName": display_name,
                "ownerUid": owner_uid,
            },
            delimeter=",",
        )

    def Delete(self, team_id: int, owner_uid: list[int] = None):
        """
        param team_id: unique identifier of the target collaboration Team.
        param owner_uid: unique identifier of the collaboration Team owner.
        """
        return self._get(
            "Delete",
            params={
                "teamId": team_id,
                "ownerUid": owner_uid,
            },
            delimeter=",",
        )

    def DeleteMember(self, member_id: int, owner_uid: list[int] = None):
        """
        param member_id: unique identifier of the collaboration Team member.
        param owner_uid: unique identifier of the collaboration Team owner.
        """
        return self._get(
            "DeleteMember",
            params={
                "memberId": member_id,
                "ownerUid": owner_uid,
            },
            delimeter=",",
        )

    def Edit(
        self,
        team_id: int,
        display_name: list[str] = None,
        external_id: list[str] = None,
        owner_uid: list[int] = None,
    ):
        """
        param team_id:  unique identifier of the collaboration Team
        param external_id: unique identifier of the collaboration Team that links it with external resources.
        param owner_uid: unique identifier of the collaboration Team owner.
        """
        return self._get(
            "Edit",
            params={
                "teamId": team_id,
                "displayName": display_name,
                "externalId": external_id,
                "ownerUid": owner_uid,
            },
            delimeter=",",
        )

    def Get(self, owner_uid: list[int] = None):
        """
        param owner_uid: unique identifier of the collaboration Team owner.
        """
        return self._get(
            "Get",
            params={
                "ownerUid": owner_uid,
            },
            delimeter=",",
        )

    def Invite(
        self,
        email: str,
        team_id: int,
        display_name: list[str] = None,
        owner_uid: list[int] = None,
    ):
        """
        param email: email address to send an invitation to.
        param team_id:  unique identifier of the collaboration Team
        param display_name: invited user's display name (in the collaboration Team owner dashboard).
        param owner_uid: unique identifier of the collaboration Team owner.
        """
        return self._get(
            "Invite",
            params={
                "email": email,
                "teamId": team_id,
                "displayName": display_name,
                "ownerUid": owner_uid,
            },
            delimeter=",",
        )

    def ResendInvite(self, member_id: int, owner_uid: list[int] = None):
        """
        param member_id: unique identifier of the collaboration Team member.
        param owner_uid: unique identifier of the collaboration Team owner.
        """
        return self._get(
            "ResendInvite",
            params={
                "memberId": member_id,
                "ownerUid": owner_uid,
            },
            delimeter=",",
        )
