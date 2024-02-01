from datetime import datetime

from ..abstract import ClientAbstract

__all__ = ["Users"]


class Users(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users
    Ref: https://docs.jelastic.com/api/private/#!/api/users
    """

    _endpoint1 = "users"

    @property
    def Account(self) -> "_Account":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.users.Account

        Ref: https://docs.jelastic.com/api/private/#!/api/users.Account
        """
        return _Account(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def Authentication(self) -> "_Authentication":
        """
        This service is responsible for the identification and authentication of registered users. It includes sign-in/out actions, session and tokens management, etc.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.users.Authentication
        Ref: https://docs.jelastic.com/api/private/#!/api/users.Authentication
        """
        return _Authentication(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def Collaboration(self) -> "_Collaboration":
        """
        This service is responsible for managing the accounts collaboration feature on the platform. The core idea is
        that users can share the necessary environments and access to some account features with other platform
        customers. Complete control over the shared management permissions makes the feature suitable for most
        possible use cases.

        Collaboration owner - a primary account where shared environments are hosted. All charges for the shared
        environments (including actions performed by collaborators) are applied to this account.
        Collaboration member - user account with partial access to the collaboration owner account. Shared
        functionality is defined by the collaboration owner.
        Collaboration (shared) resources - instances (environments, groups) shared in the collaboration.
        Collaboration policies - small API sets that allow specific operations.
        Collaboration roles - a combination of policies that create the required range of actions to share with members.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.users.Collaboration

        Ref: https://docs.jelastic.com/api/private/#!/api/users.Collaboration
        """
        return _Collaboration(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def Team(self) -> "_Team":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.users.Team

        Ref: https://docs.jelastic.com/api/private/#!/api/users.Team
        """
        return _Team(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def Registration(self) -> "_Registration":
        """
        Registration of new users.
         >>> from jelastic import Jelastic
         >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
         >>> jelastic.users.Registration
         Ref: https://docs.jelastic.com/api/private/#!/api/users.Registration
        """
        return _Registration(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def SSO(self) -> "_SSO":
        """
        SSO methods
         >>> from jelastic import Jelastic
         >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
         >>> jelastic.users.SSO
         Ref: https://docs.jelastic.com/api/private/#!/api/users.SSO
        """
        return _SSO(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )


class _Account(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.Account

     Ref: https://docs.jelastic.com/api/private/#!/api/users.Account
    """

    _endpoint2 = "account"

    def AddAccount(
        self,
        email: str,
        password: str,
        name: str = None,
        notify: bool = None,
        reseller_id: int = None,
        ruk: str = None,
    ):
        """
        :param email: unique email address of the new account.
        :param password: password for the new account.
        :param name: an account's name.
        :param notify: defines whether to send a confirmation letter to the new user email upon success (true) or not (false).
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "AddAccount",
            params={
                "email": email,
                "password": password,
                "name": name,
                "notify": notify,
                "resellerId": reseller_id,
                "ruk": ruk,
            },
        )

    def AddSSHKey(
        self,
        title: str,
        ssh_key: str,
        is_private: bool,
        ruk: str = None,
    ):
        """
        Response which contains new key data and operation result.

        param title: title of the ssh key.
        param ssh_key: value of the ssh key.
        """
        return self._get(
            "AddSSHKey",
            params={
                "title": title,
                "sshKey": ssh_key,
                "isPrivate": is_private,
                "ruk": ruk,
            },
        )

    def ChangeEmail(
        self,
        email: str,
        redirect_url: str = None,
        ruk: str = None,
    ):
        """
        param email: new account email address (provided by the user).
        param redirect_url: a link to display in user email message.
        """
        return self._get(
            "ChangeEmail",
            params={"email": email, "redirectUrl": redirect_url, "ruk": ruk},
        )

    def ChangeName(
        self,
        name: str,
        ruk: str = None,
    ):
        """
        param name: new account name (provided by the user).
        """
        return self._get(
            "ChangeName",
            params={"name": name, "ruk": ruk},
        )

    def ChangePassword(
        self,
        old_password: str,
        new_password: str,
        invalidate_sessions: bool = None,
        ruk: str = None,
    ):
        """
        param old_password: user's current password (as specified by the user).
        param new_password: user's new password (as specified by the user).
        param invalidate_sessions: defines whether to invalidate all active user sessions except the current one (true) or not (false, by default).
        """
        return self._get(
            "ChangePassword",
            params={
                "oldPassword": old_password,
                "newPassword": new_password,
                "invalidateSessions": invalidate_sessions,
                "ruk": ruk,
            },
        )

    def CheckUser(
        self,
        login: str,
        ruk: str = None,
    ):
        return self._get(
            "CheckUser",
            params={"login": login, "ruk": ruk},
        )

    def DeleteSSHKey(
        self,
        id: int,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the ssh key.
        """
        return self._get(
            "DeleteSSHKey",
            params={"id": id, "ruk": ruk},
        )

    def Disable2FA(
        self,
        password: str = None,
        ruk: str = None,
    ):
        return self._get(
            "Disable2FA",
            params={"password": password, "ruk": ruk},
        )

    def Enable2FA(
        self,
        code: str,
        password: str = None,
        ruk: str = None,
    ):
        return self._get(
            "Enable2FA",
            params={"code": code, "password": password, "ruk": ruk},
        )

    def Get2FABackupCodes(
        self,
        password: str = None,
        ruk: str = None,
    ):
        return self._get(
            "Get2FABackupCodes",
            params={"password": password, "ruk": ruk},
        )

    def Get2FAConfig(
        self,
        password: str = None,
        ruk: str = None,
    ):
        return self._get(
            "Get2FAConfig",
            params={"password": password, "ruk": ruk},
        )

    def GetSSHKeys(
        self,
        is_private: bool = None,
        ruk: str = None,
    ):
        return self._get(
            "GetSSHKeys",
            params={"isPrivate": is_private, "ruk": ruk},
        )

    def GetUserInfo(
        self,
        ruk: str = None,
    ):
        return self._get("GetUserInfo", params={"ruk": ruk})

    def GetUserInfoInner(
        self,
        login: str,
        ruk: str = None,
    ):
        return self._get(
            "GetUserInfoInner",
            params={"login": login, "ruk": ruk},
        )

    def RecoverPassword(
        self,
        email: str,
        lang: str = None,
        ruk: str = None,
    ):
        return self._get(
            "RecoverPassword",
            params={"email": email, "lang": lang, "ruk": ruk},
        )

    def Regenerate2FABackupCodes(
        self,
        password: str = None,
        ruk: str = None,
    ):
        return self._get(
            "Regenerate2FABackupCodes",
            params={"password": password, "ruk": ruk},
        )

    def SetAsTenantHost(
        self,
        uid: int,
        force_change: bool,
        ruk: str = None,
    ):
        """
        param uid: unique identifier of the target user.
        param force_change: defines whether to change tenant host if one already exists (true) or not (false).
        """
        return self._get(
            "SetAsTenantHost",
            params={"uid": uid, "forceChange": force_change, "ruk": ruk},
        )

    def SetPassword(
        self,
        auth_key: str,
        invalidate_sessions: bool = None,
        ruk: str = None,
    ):
        """
        param auth_key: authentication key to confirm the operation.
        param invalidate_sessions: defines whether to invalidate all active user sessions except the current one (true) or not (false, by default).
        """
        return self._get(
            "SetPassword",
            params={
                "authKey": auth_key,
                "invalidateSessions": invalidate_sessions,
                "ruk": ruk,
            },
        )

    def SetUserData(
        self,
        data: str,
        ruk: str = None,
    ):
        return self._get(
            "SetUserData",
            params={"data": data, "ruk": ruk},
        )


class _Authentication(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.Authentication
     Ref: https://docs.jelastic.com/api/private/#!/api/users.Authentication
    """

    _endpoint2 = "authentication"

    def ChangeSession(
        self,
        ruk: str = None,
    ):
        return self._get(
            "ChangeSession",
            params={"ruk": ruk},
        )

    def CheckAuthKey(
        self,
        auth_key: str,
        ruk: str = None,
    ):
        return self._get(
            "CheckAuthKey",
            params={"authKey": auth_key, "ruk": ruk},
        )

    def CheckPassword(
        self,
        password: str,
        ruk: str = None,
    ):
        return self._get(
            "CheckPassword",
            params={"password": password, "ruk": ruk},
        )

    def CheckSign(
        self,
        ruk: str = None,
    ):
        return self._get(
            "CheckSign",
            params={"ruk": ruk},
        )

    def CheckUser(
        self,
        login: str,
        ruk: str = None,
    ):
        return self._get(
            "CheckUser",
            params={"login": login, "ruk": ruk},
        )

    def ClearApiListData(
        self,
        ruk: str = None,
    ):
        return self._get(
            "ClearApiListData",
            params={"ruk": ruk},
        )

    def ClearApiListDataInner(
        self,
        ruk: str = None,
    ):
        return self._get(
            "ClearApiListDataInner",
            params={"ruk": ruk},
        )

    def CreateToken(
        self,
        description: str,
        password: str = None,
        token_template: str = None,
        api_list: list[str] = None,
        expires_at: datetime = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def CreateTokenInner(
        self,
        login: str,
        description: str,
        token_template: str = None,
        api_list: list[str] = None,
        expires_at: datetime = None,
        is_protected: bool = None,
        skip_notification: bool = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def DeleteTokens(
        self,
        ids: str,
        password: str = None,
        ruk: str = None,
    ):
        """
        param ids: a comma- or semicolon-separated list of target token IDs. For example: 1;4;6. Also, you can use * for selecting all your tokens.
        param password: password for authenticating the current user.
        """
        return self._get(
            "DeleteTokens", params={"ids": ids, "password": password, "ruk": ruk}
        )

    def EditToken(
        self,
        id: int,
        password: str = None,
        description: str = None,
        token_template: str = None,
        api_list: list[str] = None,
        expires_at: datetime = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetAuthKey(
        self,
        auth_key: str,
        ruk: str = None,
    ):
        return self._get(
            "GetAuthKey",
            params={"authKey": auth_key, "ruk": ruk},
        )

    def GetDescriptionByToken(
        self,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "GetDescriptionByToken",
            params={"checksum": checksum, "ruk": ruk},
        )

    def GetDeviceSignature(
        self,
        ruk: str = None,
    ):
        return self._get(
            "GetDeviceSignature",
            params={"ruk": ruk},
        )

    def GetPolicyMethods(
        self,
        unique_name: str = None,
        ruk: str = None,
    ):
        return self._get(
            "GetPolicyMethods", params={"uniqueName": unique_name, "ruk": ruk}
        )

    def GetSessions(
        self,
        ruk: str = None,
    ):
        return self._get(
            "GetSessions",
            params={"ruk": ruk},
        )

    def GetSigninAttempts(
        self,
        search: str = None,
        ruk: str = None,
    ):
        return self._get("GetSigninAttempts", params={"search": search, "ruk": ruk})

    def GetTokenApiList(
        self,
        show_private: str = None,
        sort_param: str = None,
        ruk: str = None,
    ):
        """
        param show_private: showPrivate : "boolean" (optional)
        param sort_param: filter by method name.
        """
        return self._get(
            "GetTokenApiList",
            params={"showPrivate": show_private, "sortParam": sort_param, "ruk": ruk},
        )

    def GetTokenTemplates(
        self,
        ruk: str = None,
    ):
        return self._get(
            "GetTokenTemplates",
            params={"ruk": ruk},
        )

    def GetTokens(
        self,
        ids: list[str] = None,
        ruk: str = None,
    ):
        """
        param ids: a comma- or semicolon-separated list of target token IDs. For example: 1;4;6. Also, you can use * for selecting all your tokens.
        """
        return self._get(
            "GetTokens",
            params={"ids": ids, "ruk": ruk},
            delimiter=",",
        )

    def GetUidByToken(
        self,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "GetUidByToken",
            params={"checksum": checksum, "ruk": ruk},
        )

    def RegenerateToken(
        self,
        ids: str,
        password: str = None,
        ruk: str = None,
    ):
        """
        param ids: unique identifier of the target token.
        param password: password for authenticating the current user.
        """
        return self._get(
            "RegenerateToken", params={"ids": ids, "password": password, "ruk": ruk}
        )

    def ResetSigninAttempts(
        self,
        login: str = None,
        ip_address: str = None,
        ruk: str = None,
    ):
        return self._get(
            "ResetSigninAttempts",
            params={"login": login, "ipAddress": ip_address, "ruk": ruk},
        )

    def Signin(
        self,
        login: str,
        password: str,
        ruk: str = None,
    ):
        return self._get(
            "Signin", params={"login": login, "password": password, "ruk": ruk}
        )

    def SigninByAuthKey(
        self,
        auth_key: str,
        ruk: str = None,
    ):
        return self._get(
            "SigninByAuthKey",
            params={"authKey": auth_key, "ruk": ruk},
        )

    def SigninByToken(
        self,
        token: str,
        user_headers: str,
        ruk: str = None,
    ):
        return self._get(
            "SigninByToken",
            params={"token": token, "userHeaders": user_headers, "ruk": ruk},
        )

    def Signout(
        self,
        ruk: str = None,
    ):
        return self._get(
            "Signout",
            params={"ruk": ruk},
        )

    def SignoutSessions(
        self,
        ids: str,
        ruk: str = None,
    ):
        """
        param ids: a comma- or semicolon-separated list of target token IDs. For example: 1;4;6. Also, you can use * for selecting all your tokens.
        """
        return self._get(
            "SignoutSessions",
            params={"ids": ids, "ruk": ruk},
        )

    def ValidateCaptcha(
        self,
        code: str,
        ruk: str = None,
    ):
        return self._get(
            "ValidateCaptcha",
            params={"code": code, "ruk": ruk},
        )

    def Verify2FACode(
        self,
        code: str,
        ruk: str = None,
    ):
        return self._get(
            "Verify2FACode",
            params={"code": code, "ruk": ruk},
        )


class _Collaboration(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.Collaboration
     Ref: https://docs.jelastic.com/api/private/#!/api/users.Collaboration
    """

    _endpoint2 = "collaboration"

    def AcceptCollaboration(
        self,
        id: int,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        """
        return self._get(
            "AcceptCollaboration",
            params={"id": id, "ruk": ruk},
        )

    def ActivateMember(
        self,
        id: int,
        owner_uid: int = None,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "ActivateMember",
            params={"id": id, "ownerUid": owner_uid, "ruk": ruk},
        )

    def AddPolicy(
        self,
        name: str,
        methods: list[str],
        description: str = None,
        ruk: str = None,
    ):
        """
        param name: custom name for the target policy.
        param methods: a comma-separated list of API methods allowed by this new policy.
        param description: custom description for the target new policy.
        """
        return self._get(
            "AddPolicy",
            params={
                "name": name,
                "methods": methods,
                "description": description,
                "ruk": ruk,
            },
            delimiter=",",
        )

    def AddResources(
        self,
        collaboration_id: int,
        resources: str,
        create_role_if_needed: bool = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def AddRole(
        self,
        name: str,
        policies: list[str],
        receive_notification: bool,
        description: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
            delimiter=",",
        )

    def CheckEnvironmentRights(
        self,
        service_method: list[str],
        is_any: bool = None,
        ruk: str = None,
    ):
        """
        param service_method: a semicolon-separated list of API methods.
        param is_any: defines whether all the listed methods should be allowed (false) or at least one (true).
        """
        return self._get(
            "CheckEnvironmentRights",
            params={"serviceMethod": service_method, "isAny": is_any, "ruk": ruk},
            delimiter=",",
        )

    def DeleteMember(
        self,
        id: int,
        owner_uid: int = None,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "DeleteMember", params={"id": id, "ownerUid": owner_uid, "ruk": ruk}
        )

    def DeletePolicy(
        self,
        id: int,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        """
        return self._get(
            "DeletePolicy",
            params={"id": id, "ruk": ruk},
        )

    def DeleteProjectFromResources(
        self,
        project_id: str,
        ruk: str = None,
    ):
        """
        param project_id: unique identifier of the target project.
        """
        return self._get(
            "DeleteProjectFromResources",
            params={"projectId": project_id, "ruk": ruk},
        )

    def DeleteResources(
        self,
        collaboration_id: str,
        ids: list[str] = None,
        ruk: str = None,
    ):
        """
        param collaboration_id: unique identifier of the target collaboration.
        param ids: a comma-separated list of shared resources identifiers.
        """
        return self._get(
            "DeleteResources",
            params={"collaborationId": collaboration_id, "ids": ids, "ruk": ruk},
            delimiter=",",
        )

    def DeleteResourcesInner(
        self,
        resource_type: str,
        resource_id: str,
        ruk: str = None,
    ):
        return self._get(
            "DeleteResourcesInner",
            params={
                "resourceType": resource_type,
                "resourceId": resource_id,
                "ruk": ruk,
            },
        )

    def DeleteRole(
        self,
        id: int,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the target collaboration role to delete.
        """
        return self._get(
            "DeleteRole",
            params={"id": id, "ruk": ruk},
        )

    def EditCollaboration(
        self,
        id: int,
        display_name: str = None,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the target collaboration to edit.
        param display_name: name of the collaboration displayed in the dashboard.
        """
        return self._get(
            "EditCollaboration",
            params={"id": id, "displayName": display_name, "ruk": ruk},
        )

    def EditMember(
        self,
        id: int,
        display_name: str = None,
        owner_uid: int = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def EditPolicy(
        self,
        id: int,
        methods: str,
        name: str = None,
        description: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def EditRole(
        self,
        id: int,
        policies: list[str],
        name: str = None,
        description: str = None,
        receive_notification: bool = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
            delimiter=",",
        )

    def GetCollaborationResourceMethods(
        self,
        resource_type: str,
        resource_id: str,
        ruk: str = None,
    ):
        """
        param resource_type: unique identifier of the target collaboration resource
        param resource_id: type (ENV, ENV_GROUP, ACCOUNT, VHI_REGION, S3_REGION) of the target collaboration resource.
        """
        return self._get(
            "GetCollaborationResourceMethods",
            params={
                "resourceType": resource_type,
                "resourceId": resource_id,
                "ruk": ruk,
            },
        )

    def GetCollaborationResources(
        self,
        collaboration_id: int = None,
        type: str = None,
        resource_group: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetCollaborationResourcesInner(
        self,
        uid: int = None,
        collaboration_id: int = None,
        type: str = None,
        resource_group: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetCollaborationRoleMethods(
        self,
        collaboration_id: int = None,
        role_id: int = None,
        ruk: str = None,
    ):
        """
        param collaboration_id: unique identifier of the target collaboration.
        param role_id: unique identifier of the target role.
        """
        return self._get(
            "GetCollaborationRoleMethods",
            params={"collaborationId": collaboration_id, "roleId": role_id, "ruk": ruk},
        )

    def GetCollaborations(
        self,
        id: int = None,
        owner_uid: int = None,
        collaboration_type: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetCollaborationsInner(
        self,
        login: str,
        ruk: str = None,
    ):
        return self._get(
            "GetCollaborationsInner",
            params={"login": login, "ruk": ruk},
        )

    def GetMemberResources(
        self,
        member_id: int = None,
        resource_group: str = None,
        ruk: str = None,
    ):
        """
        param member_id: unique identifier of the target collaboration member.
        param resource_group: filters results by the provided resource group (ALL, VAP, CMP).
        """
        return self._get(
            "GetMemberResources",
            params={"memberId": member_id, "resourceGroup": resource_group, "ruk": ruk},
        )

    def GetMembers(
        self,
        id: int,
        owner_uid: int = None,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "GetMembers", params={"id": id, "ownerUid": owner_uid, "ruk": ruk}
        )

    def GetMembersInner(
        self,
        login: str,
        ruk: str = None,
    ):
        return self._get(
            "GetMembersInner",
            params={"login": login, "ruk": ruk},
        )

    def GetPolicies(
        self,
        id: int = None,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the target policy.
        """
        return self._get(
            "GetPolicies",
            params={"id": id, "ruk": ruk},
        )

    def GetPolicyMethods(
        self,
        policy_id: int = None,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the target policy.
        """
        return self._get(
            "GetPolicyMethods",
            params={"policyId": policy_id, "ruk": ruk},
        )

    def GetResourceRoles(
        self,
        owner_uid: int,
        resource_id: str,
        resource_type: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetResourceRolesInner(
        self,
        target_app_id: str,
        ruk: str = None,
    ):
        return self._get(
            "GetResourceRolesInner",
            params={"targetAppid": target_app_id, "ruk": ruk},
        )

    def GetRoles(
        self,
        id: int,
        owner_uid: int = None,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "GetRoles", params={"id": id, "ownerUid": owner_uid, "ruk": ruk}
        )

    def InviteMember(
        self,
        email: str,
        display_name: str = None,
        owner_uid: int = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def LeaveCollaboration(
        self,
        id: int,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        """
        return self._get(
            "LeaveCollaboration",
            params={"id": id, "ruk": ruk},
        )

    def RejectCollaboration(
        self,
        id: int,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        """
        return self._get(
            "RejectCollaboration",
            params={"id": id, "ruk": ruk},
        )

    def ResendMemberInvitation(
        self,
        id: int,
        owner_uid: int = None,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "ResendMemberInvitation",
            params={"id": id, "ownerUid": owner_uid, "ruk": ruk},
        )

    def SetResource(
        self,
        collaboration_id: int,
        resource_id: str,
        role_id: list[str],
        resource_type: str = None,
        owner_uid: int = None,
        create_role_if_needed: bool = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
            delimiter=",",
        )

    def SetResources(
        self,
        collaboration_id: int,
        resource: str,
        create_role_if_needed: bool = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def SuspendMember(
        self,
        id: int,
        owner_uid: int = None,
        ruk: str = None,
    ):
        """
        param id: unique identifier of the collaboration invite.
        param owner_uid: unique identifier of the collaboration owner.
        """
        return self._get(
            "SuspendMember", params={"id": id, "ownerUid": owner_uid, "ruk": ruk}
        )


class _SSO(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.SSO
     Ref: https://docs.jelastic.com/api/private/#!/api/users.SSO
    """

    _endpoint2 = "sso"

    def GetAuthEndpoint(
        self,
        redirect_uri: str,
        ruk: str = None,
    ):
        """
        param redirectUri: a link to display after the authentication.
        """
        return self._get(
            "GetAuthEndpoint",
            params={"redirectUri": redirect_uri, "ruk": ruk},
        )

    def GetImpersonationData(
        self,
        uid: int,
        ruk: str = None,
    ):
        """
        param uid: application identifier of the platform.
        """
        return self._get(
            "GetImpersonationData",
            params={"uid": uid, "ruk": ruk},
        )

    def GetSettings(
        self,
        ruk: str = None,
    ):
        return self._get(
            "GetSettings",
            params={"ruk": ruk},
        )

    def ResetPassword(
        self,
        ruk: str = None,
    ):
        return self._get(
            "ResetPassword",
            params={"ruk": ruk},
        )

    def SigninByCode(
        self,
        code: str,
        redirect_uri: str,
        ruk: str = None,
    ):
        """
        param code: a security code for SSO authentication.
        param redirectUri: a link to display after the authentication.
        """
        return self._get(
            "SigninByCode",
            params={"code": code, "redirectUri": redirect_uri, "ruk": ruk},
        )

    def SigninByToken(
        self,
        token: str,
        ruk: str = None,
    ):
        """
        param token: an access token for SSO authentication.
        """
        return self._get(
            "SigninByToken",
            params={"token": token, "ruk": ruk},
        )


class _Registration(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.Registration
     Ref: https://docs.jelastic.com/api/private/#!/api/users.Registration
    """

    _endpoint2 = "registration"

    def Activate(
        self,
        key: str,
        password: str = None,
        skip_send_email: bool = None,
        code: str = None,
        reseller_id: int = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def CheckEmailExist(
        self,
        email: str,
        ruk: str = None,
    ):
        """
        param email: verifiable e-mail address
        """
        return self._get("CheckEmailExist", params={"email": email, "ruk": ruk})

    def CheckEmailRegistration(
        self,
        email: str,
        ruk: str = None,
    ):
        """
        param email: verifiable e-mail address
        """
        return self._get("CheckEmailRegistration", params={"email": email, "ruk": ruk})

    def CheckPassword(
        self,
        password: str,
        ruk: str = None,
    ):
        return self._get("CheckPassword", params={"password": password, "ruk": ruk})

    def ClearSmsListData(
        self,
        email: str,
        ruk: str = None,
    ):
        """
        param email: email to generate confirmation key
        """
        return self._get("ClearSmsListData", params={"email": email, "ruk": ruk})

    def CreateAccount(
        self,
        email: str,
        password: str,
        name: str = None,
        check_email: bool = None,
        welcome: str = None,
        skip_send_email: bool = None,
        reseller_id: int = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def CreateAuthKey(
        self,
        login: str,
        solution: str,
        auth_type: str = None,
        expires_at: datetime = None,
        type: str = None,
        ruk: str = None,
    ):
        return self._get(
            "CreateAuthKey",
            params={
                "login": login,
                "solution": solution,
                "authType": auth_type,
                "expiresAt": expires_at,
                "type": type,
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def CreateConfirmLinkUserKey(
        self,
        email: str,
        role: str,
        target_app_id: str = None,
        application_right: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GeneratePassword(
        self,
        length: int = None,
        ruk: str = None,
    ):
        """
        param length: define password length (default value is set by password policy: minLength, can not be less than minLength)
        """
        return self._get("GeneratePassword", params={"length": length, "ruk": ruk})

    def GetSmsListData(
        self,
        ruk: str = None,
    ):
        return self._get("GetSmsListData", params={"ruk": ruk})

    def ResendInvitation(
        self,
        welcome: str,
        ruk: str = None,
    ):
        return self._get("ResendInvitation", params={"welcome": welcome, "ruk": ruk})

    def SendSms(
        self,
        activation_key: str,
        email: str,
        phone: str,
        lang: str = None,
        ruk: str = None,
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
                "email": email,
                "phone": phone,
                "lang": lang,
                "ruk": ruk,
            },
        )


class _Team(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.Team
     Ref: https://docs.jelastic.com/api/private/#!/api/users.Team
    """

    _endpoint2 = "team"

    def Create(
        self,
        display_name: str,
        owner_uid: int = None,
        ruk: str = None,
    ):
        """
        param owner_uid: unique identifier of the collaboration Team owner.
        """
        return self._get(
            "Create",
            params={"displayName": display_name, "ownerUid": owner_uid, "ruk": ruk},
        )

    def Delete(
        self,
        team_id: int,
        owner_uid: int = None,
        ruk: str = None,
    ):
        """
        param team_id: unique identifier of the target collaboration Team.
        param owner_uid: unique identifier of the collaboration Team owner.
        """
        return self._get(
            "Delete",
            params={"teamId": team_id, "ownerUid": owner_uid, "ruk": ruk},
        )

    def DeleteMember(
        self,
        member_id: int,
        owner_uid: int = None,
        ruk: str = None,
    ):
        """
        param member_id: unique identifier of the collaboration Team member.
        param owner_uid: unique identifier of the collaboration Team owner.
        """
        return self._get(
            "DeleteMember",
            params={"memberId": member_id, "ownerUid": owner_uid, "ruk": ruk},
        )

    def Edit(
        self,
        team_id: int,
        display_name: str = None,
        external_id: str = None,
        owner_uid: int = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def Get(
        self,
        owner_uid: int = None,
        ruk: str = None,
    ):
        """
        param owner_uid: unique identifier of the collaboration Team owner.
        """
        return self._get(
            "Get",
            params={"ownerUid": owner_uid, "ruk": ruk},
        )

    def Invite(
        self,
        email: str,
        team_id: int,
        display_name: str = None,
        owner_uid: int = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def ResendInvite(
        self,
        member_id: int,
        owner_uid: int = None,
        ruk: str = None,
    ):
        """
        param member_id: unique identifier of the collaboration Team member.
        param owner_uid: unique identifier of the collaboration Team owner.
        """
        return self._get(
            "ResendInvite",
            params={"memberId": member_id, "ownerUid": owner_uid, "ruk": ruk},
        )
