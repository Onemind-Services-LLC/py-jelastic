from datetime import datetime

from ..abstract import ClientAbstract

__all__ = ["Users"]


class Users(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users
    Ref: https://docs.jelastic.com/api/private/#!/api/users
    """

    _endpoint1 = "users"

    @property
    def Authentication(self) -> "_Authentication":
        """
        This service is responsible for the identification and authentication of registered users. It includes sign-in/out actions, session and tokens management, etc.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.users.Authentication
        Ref: https://docs.jelastic.com/api/private/#!/api/users.Authentication
        """
        return _Authentication(
            session=self._session, token=self._token, debug=self._debug
        )

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
    def Registration(self) -> "_Registration":
        """
        Registration of new users.
         >>> from jelastic import Jelastic
         >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
         >>> jelastic.users.Registration
         Ref: https://docs.jelastic.com/api/private/#!/api/users.Registration
        """
        return _Registration(
            session=self._session, token=self._token, debug=self._debug
        )

    @property
    def SSO(self) -> "_SSO":
        """
        SSO methods
         >>> from jelastic import Jelastic
         >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
         >>> jelastic.users.SSO
         Ref: https://docs.jelastic.com/api/private/#!/api/users.SSO
        """
        return _SSO(session=self._session, token=self._token, debug=self._debug)


class _Authentication(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.Authentication
     Ref: https://docs.jelastic.com/api/private/#!/api/users.Authentication
    """

    _endpoint2 = "authentication"

    def ChangeSession(
        self,
    ):
        return self._get(
            "ChangeSession",
            params={},
        )

    def CheckAuthKey(self, auth_key: str):
        return self._get(
            "CheckAuthKey",
            params={"authKey": auth_key},
        )

    def CheckPassword(self, password: str):
        return self._get(
            "CheckPassword",
            params={"password": password},
        )

    def CheckSign(
        self,
    ):
        return self._get(
            "CheckSign",
            params={},
        )

    def CheckUser(self, login: str):
        return self._get(
            "CheckUser",
            params={"login": login},
        )

    def ClearApiListData(
        self,
    ):
        return self._get(
            "ClearApiListData",
            params={},
        )

    def ClearApiListDataInner(
        self,
    ):
        return self._get(
            "ClearApiListDataInner",
            params={},
        )

    def CreateToken(
        self,
        description: str,
        password: list[str] = None,
        token_template: list[str] = None,
        api_list: list[str] = None,
        expires_at: list[datetime] = None,
    ):
        """
        param description: custom description for the created token.
        param password: password for authenticating the current user.
        param token_template: one of standard tokens configurations with the predefined permissions (Marketplace, Maven Plugin, IDE Plugins, Extended Access). You can get the full list with the "GetTokenTemplates" method. If not specified, a "Custom" token with manually provided "apiList" will be created.
        param api_list: a comma-separated list of API methods that are allowed by the token. You can get the full list with the "GetTokenApiList" method. For example: ["env.control.CreateEnvironment", "env.control.RedeployContainersByGroup", "env.file.AddMountPointByGroup"].
        param expires_at: expiration date (UTC) for the token. In the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        """
        return self._get(
            "CreateToken",
            params={
                "description": description,
                "password": password,
                "tokenTemplate": token_template,
                "apiList": api_list,
                "expiresAt": expires_at,
            },
            delimiter=",",
        )

    def CreateTokenInner(
        self,
        login: str,
        description: str,
        token_template: list[str] = None,
        api_list: list[str] = None,
        expires_at: list[datetime] = None,
        is_protected: list[bool] = None,
        skip_notification: list[bool] = None,
    ):
        return self._get(
            "CreateTokenInner",
            params={
                "login": login,
                "description": description,
                "tokenTemplate": token_template,
                "apiList": api_list,
                "expiresAt": expires_at,
                "isProtected": is_protected,
                "skipNotification": skip_notification,
            },
            delimiter=",",
        )

    def DeleteTokens(
        self,
        ids: str,
        password: list[str] = None,
    ):
        """
        param ids: a comma- or semicolon-separated list of target token IDs. For example: 1;4;6. Also, you can use * for selecting all your tokens.
        param password: password for authenticating the current user.
        """
        return self._get(
            "DeleteTokens",
            params={"ids": ids, "password": password},
            delimiter=",",
        )

    def EditToken(
        self,
        id: int,
        password: list[str] = None,
        description: list[str] = None,
        token_template: list[str] = None,
        api_list: list[str] = None,
        expires_at: list[datetime] = None,
    ):
        """
        param id: unique identifier of the target token.
        param description: custom description for the created token.
        param password: password for authenticating the current user.
        param token_template: one of standard tokens configurations with the predefined permissions (Marketplace, Maven Plugin, IDE Plugins, Extended Access). You can get the full list with the "GetTokenTemplates" method. If not specified, a "Custom" token with manually provided "apiList" will be created.
        param api_list: a comma-separated list of API methods that are allowed by the token. You can get the full list with the "GetTokenApiList" method. For example: ["env.control.CreateEnvironment", "env.control.RedeployContainersByGroup", "env.file.AddMountPointByGroup"].
        param expires_at: expiration date (UTC) for the token. In the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        """
        return self._get(
            "EditToken",
            params={
                "id": id,
                "password": password,
                "description": description,
                "tokenTemplate": token_template,
                "apiList": api_list,
                "expiresAt": expires_at,
            },
            delimiter=",",
        )

    def GetAuthKey(self, auth_key: str):
        return self._get(
            "GetAuthKey",
            params={"authKey": auth_key},
        )

    def GetDescriptionByToken(self, checksum: str):
        return self._get(
            "GetDescriptionByToken",
            params={"checksum": checksum},
        )

    def GetDeviceSignature(
        self,
    ):
        return self._get(
            "GetDeviceSignature",
            params={},
        )

    def GetPolicyMethods(
        self,
        unique_name: list[str] = None,
    ):
        return self._get(
            "GetPolicyMethods",
            params={"uniqueName": unique_name},
            delimiter=",",
        )

    def GetSessions(
        self,
    ):
        return self._get(
            "GetSessions",
            params={},
        )

    def GetSigninAttempts(self, search: list[str] = None):
        return self._get(
            "GetSigninAttempts",
            params={"search": search},
            delimiter=",",
        )

    def GetTokenApiList(
        self, show_private: list[str] = None, sort_param: list[str] = None
    ):
        """
        param show_private: showPrivate : "boolean" (optional)
        param sort_param: filter by method name.
        """
        return self._get(
            "GetTokenApiList",
            params={
                "showPrivate": show_private,
                "sortParam": sort_param,
            },
            delimiter=",",
        )

    def GetTokenTemplates(
        self,
    ):
        return self._get(
            "GetTokenTemplates",
            params={},
        )

    def GetTokens(self, ids: list[str] = None):
        """
        param ids: a comma- or semicolon-separated list of target token IDs. For example: 1;4;6. Also, you can use * for selecting all your tokens.
        """
        return self._get(
            "GetTokens",
            params={"ids": ids},
            delimiter=",",
        )

    def GetUidByToken(self, checksum: str):
        return self._get(
            "GetUidByToken",
            params={"checksum": checksum},
        )

    def RegenerateToken(
        self,
        ids: str,
        password: list[str] = None,
    ):
        """
        param ids: unique identifier of the target token.
        param password: password for authenticating the current user.
        """
        return self._get(
            "RegenerateToken",
            params={"ids": ids, "password": password},
            delimiter=",",
        )

    def ResetSigninAttempts(
        self,
        login: list[str] = None,
        ip_address: list[str] = None,
    ):
        return self._get(
            "ResetSigninAttempts",
            params={"login": login, "ipAddress": ip_address},
            delimiter=",",
        )

    def Signin(self, login: str, password: str):
        return self._get("Signin", params={"login": login, "password": password})

    def SigninByAuthKey(self, auth_key: str):
        return self._get(
            "SigninByAuthKey",
            params={"authKey": auth_key},
        )

    def SigninByToken(self, token: str, user_headers: str):
        return self._get(
            "SigninByToken",
            params={"token": token, "userHeaders": user_headers},
        )

    def Signout(
        self,
    ):
        return self._get(
            "Signout",
            params={},
        )

    def SignoutSessions(self, ids: str):
        """
        param ids: a comma- or semicolon-separated list of target token IDs. For example: 1;4;6. Also, you can use * for selecting all your tokens.
        """
        return self._get(
            "SignoutSessions",
            params={"ids": ids},
        )

    def ValidateCaptcha(self, code: str):
        return self._get(
            "ValidateCaptcha",
            params={"code": code},
        )

    def Verify2FACode(self, code: str):
        return self._get(
            "Verify2FACode",
            params={"code": code},
        )


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


class _SSO(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.SSO
     Ref: https://docs.jelastic.com/api/private/#!/api/users.SSO
    """

    _endpoint2 = "sso"

    def GetAuthEndpoint(self, redirect_uri: str):
        """
        param redirectUri: a link to display after the authentication.
        """
        return self._get(
            "GetAuthEndpoint",
            params={"redirectUri": redirect_uri},
        )

    def GetImpersonationData(self, uid: int):
        """
        param uid: application identifier of the platform.
        """
        return self._get(
            "GetImpersonationData",
            params={"uid": uid},
        )

    def GetSettings(self):
        return self._get(
            "GetSettings",
            params={},
        )

    def ResetPassword(self):
        return self._get(
            "ResetPassword",
            params={},
        )

    def SigninByCode(self, code: str, redirect_uri: str):
        """
        param code: a security code for SSO authentication.
        param redirectUri: a link to display after the authentication.
        """
        return self._get(
            "SigninByCode",
            params={"code": code, "redirectUri": redirect_uri},
        )

    def SigninByToken(self, token: str):
        """
        param token: an access token for SSO authentication.
        """
        return self._get(
            "SigninByToken",
            params={"token": token},
        )


class _Registration(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.Registration
     Ref: https://docs.jelastic.com/api/private/#!/api/users.Registration
    """

    _endpoint2 = "registration"

    def Activate(
        self,
        key: str,
        password: list[str] = None,
        skip_send_email: list[bool] = None,
        code: list[str] = None,
        reseller_id: list[int] = None,
    ):
        """
        param key: activation key received after registration. The activation key is sent to the email address provided during registration.
        param password: password for the new user.
        param skip_send_email: defines whether to send the activation email (false) or not (true).
        param code: custom code to be executed upon activation.
        param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "Activate",
            params={
                "key": key,
                "password": password,
                "skipSendEmail": skip_send_email,
                "code": code,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def CheckEmailExist(
        self,
        email: str,
    ):
        """
        param email: verifiable e-mail address
        """
        return self._get("CheckEmailExist", params={"email": email})

    def CheckEmailRegistration(
        self,
        email: str,
    ):
        """
        param email: verifiable e-mail address
        """
        return self._get("CheckEmailRegistration", params={"email": email})

    def CheckPassword(
        self,
        password: str,
    ):
        return self._get("CheckPassword", params={"password": password})

    def ClearSmsListData(
        self,
        email: str,
    ):
        """
        param email: email to generate confirmation key
        """
        return self._get("ClearSmsListData", params={"email": email})

    def CreateAccount(
        self,
        email: str,
        password: str,
        name: list[str] = None,
        check_email: list[bool] = None,
        welcome: list[str] = None,
        skip_send_email: list[bool] = None,
        reseller_id: list[int] = None,
    ):
        """
        param email: mailing address to which will be sent an activation key (as specified by user). The key activation is valid 24 hours after registration, if the key was not activated during this time, the user is automatically deleted, the key is not valid
        param password: password for the new user.
        param name: user name
        param check_email: verifying the existence of e-mail address (default is false)
        param welcome: optional. if invitation letter should be sent, url to redirect to after activation
        param skip_send_email: defines whether to send the activation email (false) or not (true).
        param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "CreateAccount",
            params={
                "email": email,
                "password": password,
                "name": name,
                "checkEmail": check_email,
                "welcome": welcome,
                "skipSendEmail": skip_send_email,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def CreateAuthKey(
        self,
        login: str,
        solution: str,
        auth_type: list[str] = None,
        expires_at: list[datetime] = None,
        type: list[str] = None,
    ):
        return self._get(
            "CreateAuthKey",
            params={
                "login": login,
                "solution": solution,
                "authType": auth_type,
                "expiresAt": expires_at,
                "type": type,
            },
            delimiter=",",
        )

    def CreateConfirmLinkUserKey(
        self,
        email: str,
        role: str,
        target_app_id: list[str] = None,
        application_right: list[str] = None,
    ):
        """
        param email: email to generate confirmation key
        param role: role that will be applied to a linked user after confirmation
        """
        return self._get(
            "CreateConfirmLinkUserKey",
            params={
                "email": email,
                "role": role,
                "targetAppid": target_app_id,
                "applicationRight": application_right,
            },
            delimiter=",",
        )

    def GeneratePassword(
        self,
        length: list[int] = None,
    ):
        """
        param length: define password length (default value is set by password policy: minLength, can not be less than minLength)
        """
        return self._get("GeneratePassword", params={"length": length})

    def GetSmsListData(
        self,
    ):
        return self._get("GetSmsListData", params={})

    def ResendInvitation(self, welcome: str):
        return self._get("ResendInvitation", params={"welcome": welcome})

    def SendSms(
        self,
        activation_key: str,
        email: str,
        phone: str,
        lang: list[str] = None,
    ):
        """
        param email: email to generate confirmation key
        param phone: phone number of user that receive message with verification code.
        param lang: localization language in standart ISO 639-1
        """
        return self._get(
            "SendSms",
            params={
                "activationKey ": activation_key,
                "email ": email,
                "phone ": phone,
                "lang ": lang,
            },
        )
