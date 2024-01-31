from ..abstract import ClientAbstract

__all__ = ["System"]


class System(ClientAbstract):
    _endpoint1 = "system"

    @property
    def Admin(self) -> "_Admin":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.system.Admin

        Ref: https://docs.jelastic.com/api/private/#!/api/system.Admin
        """
        return _Admin(session=self._session, token=self._token, debug=self._debug)

    @property
    def Cluster(self) -> "_Cluster":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.system.Cluster

        Ref: https://docs.jelastic.com/api/private/#!/api/system.Cluster
        """
        return _Cluster(session=self._session, token=self._token, debug=self._debug)

    @property
    def Groups(self) -> "_Groups":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.system.Groups

        Ref: https://docs.jelastic.com/api/private/#!/api/system.Groups
        """
        return _Groups(session=self._session, token=self._token, debug=self._debug)

    @property
    def IdentityProvider(self) -> "_IdentityProvider":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.system.IdentityProvider

        Ref: https://docs.jelastic.com/api/private/#!/api/system.IdentityProvider
        """
        return _IdentityProvider(
            session=self._session, token=self._token, debug=self._debug
        )

    @property
    def Service(self) -> "_Service":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.system.Service

        Ref: https://docs.jelastic.com/api/private/#!/api/system.Service
        """
        return _Service(session=self._session, token=self._token, debug=self._debug)

    @property
    def Usage(self) -> "_Usage":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.system.Usage

        Ref: https://docs.jelastic.com/api/private/#!/api/system.Usage
        """
        return _Usage(session=self._session, token=self._token, debug=self._debug)


class _Admin(System):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/system.Admin
    """

    _endpoint2 = "admin"

    def AddTrustedUser(
        self,
        login: str,
        ruk: str = None,
    ):
        return self._get(
            "AddTrustedUser",
            params={"login": login, "ruk": ruk},
        )

    def ChangeEmail(
        self,
        login: str,
        email: str,
        ruk: str = None,
    ):
        """
        :param login: email or unique identifier of the user
        :param email: new email address
        """
        return self._get(
            "ChangeEmail", params={"login": login, "email": email, "ruk": ruk}
        )

    def ChangePhoneNumber(
        self,
        login: str,
        number: str = None,
        ruk: str = None,
    ):
        return self._get(
            "ChangePhoneNumber",
            params={"login": login, "number": number, "ruk": ruk},
        )

    def CheckActivationKey(
        self,
        key: str,
        ruk: str = None,
    ):
        return self._get("CheckActivationKey", params={"key": key, "ruk": ruk})

    def CreateAccount(
        self,
        email: str,
        password: str,
        name: str = None,
        check_email: bool = None,
        welcome: str = None,
        skip_send_email: bool = None,
        auto_active: bool = None,
        send_credentials: bool = None,
        reseller_id: int = None,
        ruk: str = None,
    ):
        """
        :param email: unique email address of the new account. An activation key is sent to this user, it remains valid for 24 hours after registration. If the key was not activated during this period, it is invalidated and the user is automatically deleted.
        :param password: password for the new account.
        :param name: an account's name.
        :param check_email: defines whether to verify the existence of the email address (true) or not (false, by default).
        :param welcome: URL to redirect to after the account activation.
        :param skip_send_email: defines whether to send an invitation email (false) or not (true).
        :param auto_active: defines whether to immediately activate the account after creation (true) or not (false).
        :param send_credentials: defines whether to send account access credentials via email (true) or not (false).
        :param reseller_id: unique identifier of the target reseller platform.
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
                "autoActive": auto_active,
                "sendCredentials": send_credentials,
                "resellerId": reseller_id,
                "ruk": ruk,
            },
        )

    def DeleteApp(
        self,
        target_app_id: str,
        ruk: str = None,
    ):
        """
        :param target_app_id: target app
        """
        return self._get("DeleteApp", params={"targetAppid": target_app_id, "ruk": ruk})

    def Disable2FA(
        self,
        login: str,
        password: str = None,
        ruk: str = None,
    ):
        """
        :param login: user's email
        """
        return self._get(
            "Disable2FA",
            params={"login": login, "password": password, "ruk": ruk},
        )

    def DisableMandatory2FA(
        self,
        ruk: str = None,
    ):
        return self._get("DisableMandatory2FA", params={"ruk": ruk})

    def EnableMandatory2FA(
        self,
        period: int = None,
        notify: bool = None,
        trusted_users: str = None,
        ruk: str = None,
    ):
        return self._get(
            "EnableMandatory2FA",
            params={
                "period": period,
                "notify": notify,
                "trustedUsers": trusted_users,
                "ruk": ruk,
            },
        )

    def GetActivationKey(
        self,
        email: str,
        ruk: str = None,
    ):
        return self._get("GetActivationKey", params={"email": email, "ruk": ruk})

    def GetAdminUsersInfo(
        self,
        ruk: str = None,
    ):
        return self._get("GetAdminUsersInfo", params={"ruk": ruk})

    def GetApp(
        self,
        target_app_id: str,
        ruk: str = None,
    ):
        """
        :param target_app_id: target app
        """
        return self._get(
            "GetApp",
            params={"targetAppid": target_app_id, "ruk": ruk},
        )

    def GetAppPermission(
        self,
        target_app_id: str,
        ruk: str = None,
    ):
        """
        :param target_app_id: the application identifier for which information is requested
        """
        return self._get(
            "GetAppPermission",
            params={"targetAppid": target_app_id, "ruk": ruk},
        )

    def GetUserIDs(
        self,
        email: str,
        ruk: str = None,
    ):
        return self._get(
            "GetUserIDs",
            params={"email": email, "ruk": ruk},
        )

    def GetUserInfo(
        self,
        login: str,
        ruk: str = None,
    ):
        return self._get(
            "GetUserInfo",
            params={"login": login, "ruk": ruk},
        )

    def GetUserSSHKeys(
        self,
        login: str,
        is_private: bool = None,
        ruk: str = None,
    ):
        """
        :param login: email or unique identifier of the user (key owner).
        """
        return self._get(
            "GetUserSSHKeys",
            params={"login": login, "isPrivate": is_private, "ruk": ruk},
        )

    def GetUsersByStatus(
        self,
        status: str,
        ruk: str = None,
    ):
        return self._get(
            "GetUsersByStatus",
            params={"status": status, "ruk": ruk},
        )

    def GetUsersByUIDs(
        self,
        uid: str,
        ruk: str = None,
    ):
        return self._get(
            "GetUsersByUIDs",
            params={"uid": uid, "ruk": ruk},
        )

    def InvalidateAuthKey(
        self,
        reference_id: str = None,
        reference_type: str = None,
        auth_key: str = None,
        ruk: str = None,
    ):
        return self._get(
            "InvalidateAuthKey",
            params={
                "referenceId": reference_id,
                "referenceType": reference_type,
                "authKey": auth_key,
                "ruk": ruk,
            },
        )

    def RecoverPassword(
        self,
        email: str,
        password: str = None,
        skip_send_email: bool = None,
        lang: str = None,
        ruk: str = None,
    ):
        return self._get(
            "RecoverPassword",
            params={
                "email": email,
                "password": password,
                "skipSendEmail": skip_send_email,
                "lang": lang,
                "ruk": ruk,
            },
        )

    def RemovePersonalData(
        self,
        login: str,
        is_anonymize: bool = None,
        ruk: str = None,
    ):
        """
        :param login: email or unique identifier of the user
        """
        return self._get(
            "RemovePersonalData",
            params={"login": login, "isAnonymize": is_anonymize, "ruk": ruk},
        )

    def RemoveTrustedUser(
        self,
        login: str,
        ruk: str = None,
    ):
        return self._get("RemoveTrustedUser", params={"login": login, "ruk": ruk})

    def ResetPersistencePasswords(
        self,
        ruk: str = None,
    ):
        return self._get("ResetPersistencePasswords", params={"ruk": ruk})

    def SetPassword(
        self,
        login: str,
        password: str,
        invalidate_sessions: bool = None,
        ruk: str = None,
    ):
        """
        :param login: target user email address.
        :param password: user's new password.
        :param invalidate_sessions: defines whether to invalidate all active user sessions except the current one (true) or not (false, by default).
        """
        return self._get(
            "SetPassword",
            params={
                "login": login,
                "password": password,
                "invalidateSessions": invalidate_sessions,
                "ruk": ruk,
            },
        )

    def SetTrustedUsers(
        self,
        login: str,
        ruk: str = None,
    ):
        return self._get(
            "SetTrustedUsers",
            params={"login": login, "ruk": ruk},
        )

    def SetUserStatus(
        self,
        login: str,
        status: str,
        ruk: str = None,
    ):
        """
        :param login: user login
        """
        return self._get(
            "SetUserStatus",
            params={"login": login, "status": status, "ruk": ruk},
        )

    def SigninAsClient(
        self,
        login: str,
        ruk: str = None,
    ):
        return self._get(
            "SigninAsClient",
            params={"login": login, "ruk": ruk},
        )


class _Cluster(System):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/system.Cluster
    """

    _endpoint2 = "cluster"

    def AddApp(
        self,
        target_app_id: str,
        ruk: str = None,
    ):
        return self._get(
            "AddApp",
            params={"targetAppId": target_app_id, "ruk": ruk},
        )

    def AddHostMapRecords(
        self,
        host_maps: str,
        ruk: str = None,
    ):
        return self._get(
            "AddHostMapRecords",
            params={"hostMaps": host_maps, "ruk": ruk},
        )

    def DuplicateHostMapRecords(
        self,
        from_host: str,
        to_host: str,
        ruk: str = None,
    ):
        """
        :param from_host: source host's name.
        :param to_host: target host's name.
        """
        return self._get(
            "DuplicateHostMapRecords",
            params={"fromHost": from_host, "toHost": to_host, "ruk": ruk},
        )

    def GetActiveApps(
        self,
        ruk: str = None,
    ):
        return self._get("GetActiveApps", params={"ruk": ruk})

    def GetApps(
        self,
        path: str = None,
        ruk: str = None,
    ):
        return self._get("GetApps", params={"path": path, "ruk": ruk})

    def GetCpuUsage(
        self,
        ruk: str = None,
    ):
        return self._get("GetCpuUsage", params={"ruk": ruk})

    def GetDiskUsage(
        self,
        ruk: str = None,
    ):
        return self._get("GetDiskUsage", params={"ruk": ruk})

    def GetMaintenanceMode(
        self,
        ruk: str = None,
    ):
        return self._get("GetMaintenanceMode", params={"ruk": ruk})

    def GetNodes(
        self,
        target_app_id: str = None,
        ruk: str = None,
    ):
        return self._get(
            "GetNodes",
            params={"targetAppId": target_app_id, "ruk": ruk},
        )

    def GetSystemUsage(
        self,
        ruk: str = None,
    ):
        return self._get("GetSystemUsage", params={"ruk": ruk})

    def MoveApp(
        self,
        target_app_id: str,
        ruk: str = None,
    ):
        return self._get(
            "MoveApp",
            params={"targetAppId": target_app_id, "ruk": ruk},
        )

    def ReloadApp(
        self,
        target_app_id: str,
        ruk: str = None,
    ):
        return self._get(
            "ReloadApp",
            params={"targetAppId": target_app_id, "ruk": ruk},
        )

    def RemoveAllHostMapRecords(
        self,
        host: str,
        ruk: str = None,
    ):
        """
        :param host: target host's name.
        """
        return self._get(
            "RemoveAllHostMapRecords",
            params={"host": host, "ruk": ruk},
        )

    def RemoveApp(
        self,
        target_app_id: str,
        ruk: str = None,
    ):
        return self._get(
            "RemoveApp",
            params={"targetAppId": target_app_id, "ruk": ruk},
        )

    def RemoveHostMapRecords(
        self,
        host_maps: str,
        ruk: str = None,
    ):
        return self._get(
            "RemoveHostMapRecords",
            params={"hostMaps": host_maps, "ruk": ruk},
        )

    def RestartNode(
        self,
        ruk: str = None,
    ):
        return self._get("RestartNode", params={"ruk": ruk})

    def SetMaintenanceMode(
        self,
        enabled: bool,
        ruk: str = None,
    ):
        return self._get(
            "SetMaintenanceMode",
            params={"enabled": enabled, "ruk": ruk},
        )

    def UnloadApp(
        self,
        target_app_id: str,
        ruk: str = None,
    ):
        return self._get(
            "UnloadApp",
            params={"targetAppId": target_app_id, "ruk": ruk},
        )

    def UpdateApplicationHost(
        self,
        from_host: str,
        to_host: str,
        ruk: str = None,
    ):
        """
        :param from_host: source host's name.
        :param to_host: target host's name.
        """
        return self._get(
            "UpdateApplicationHost",
            params={"fromHost": from_host, "toHost": to_host, "ruk": ruk},
        )

    def UpdateSystemApps(
        self,
        recompile_all: str,
        ruk: str = None,
    ):
        return self._get(
            "UpdateSystemApps", params={"recompileAll": recompile_all, "ruk": ruk}
        )


class _Groups(System):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/system.Groups
    """

    _endpoint2 = "groups"

    def AddGroup(
        self,
        login: str,
        group: str,
        ruk: str = None,
    ):
        return self._get(
            "AddGroup",
            params={"login": login, "group": group, "ruk": ruk},
        )

    def GetGroups(
        self,
        login: str,
        ruk: str = None,
    ):
        return self._get(
            "GetGroups",
            params={"login": login, "ruk": ruk},
        )

    def RemoveGroup(
        self,
        login: str,
        group: str,
        ruk: str = None,
    ):
        return self._get(
            "RemoveGroup",
            params={"login": login, "group": group, "ruk": ruk},
        )


class _IdentityProvider(System):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/system.IdentityProvider
    """

    _endpoint2 = "identityprovider"

    def CreateUser(
        self,
        realm: str,
        user_json: str,
        ruk: str = None,
    ):
        """
        :param realm: a Keycloak realm to create a user at.
        :param user_json: JSON object with new user's parameters.
        """
        return self._get(
            "CreateUser",
            params={"realm": realm, "userJson": user_json, "ruk": ruk},
        )


class _Service(System):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/system.Service
    """

    _endpoint2 = "service"

    def CheckAppid(
        self,
        referer: str,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "CheckAppid",
            params={"referer": referer, "checksum": checksum, "ruk": ruk},
        )

    def CheckRequest(
        self,
        params: str,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "CheckRequest",
            params={"params": params, "checksum": checksum, "ruk": ruk},
        )

    def Event(
        self,
        topic: str,
        message: str,
        publishLocal: bool = None,
        ruk: str = None,
    ):
        return self._get(
            "Event",
            params={
                "topic": topic,
                "message": message,
                "publishLocal": publishLocal,
                "ruk": ruk,
            },
        )

    def GetAPIDescriptions(
        self,
        is_public_only: bool = None,
        is_token: bool = None,
        ruk: str = None,
    ):
        return self._get(
            "GetAPIDescriptions",
            params={"isPublicOnly": is_public_only, "isToken": is_token, "ruk": ruk},
        )

    def GetApps(
        self,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "GetApps",
            params={"checksum": checksum, "ruk": ruk},
        )

    def GetCacheStatus(
        self,
        ruk: str = None,
    ):
        return self._get("GetCacheStatus", params={"ruk": ruk})

    def GetInstanceCacheStatus(
        self,
        ruk: str = None,
    ):
        return self._get("GetInstanceCacheStatus", params={"ruk": ruk})

    def GetProperty(
        self,
        name: str,
        ruk: str = None,
    ):
        """
        :param name: name of the property
        """
        return self._get(
            "GetProperty",
            params={"name": name, "ruk": ruk},
        )

    def GetStatus(
        self,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "GetStatus",
            params={"checksum": checksum, "ruk": ruk},
        )

    def GetVersion(
        self,
        ruk: str = None,
    ):
        return self._get("GetVersion", params={"ruk": ruk})

    def NotifyEvent(
        self,
        checksum: str,
        params: str = None,
        ruk: str = None,
    ):
        return self._get(
            "NotifyEvent",
            params={"checksum": checksum, "params": params, "ruk": ruk},
        )

    def RefreshEmailTemplates(
        self,
        ruk: str = None,
    ):
        return self._get("RefreshEmailTemplates", params={"ruk": ruk})

    def RefreshUser(
        self,
        language: str = None,
        ruk: str = None,
    ):
        return self._get(
            "RefreshUser",
            params={"language": language, "ruk": ruk},
        )

    def ReloadConfiguration(
        self,
        reseller_id: str = None,
        changed_placeholders: str = None,
        ruk: str = None,
    ):
        return self._get(
            "ReloadConfiguration",
            params={
                "resellerId": reseller_id,
                "changedPlaceholders": changed_placeholders,
                "ruk": ruk,
            },
        )

    def SetStandbyMode(
        self,
        enabled: bool,
        ruk: str = None,
    ):
        return self._get(
            "SetStandbyMode",
            params={"enabled": enabled, "ruk": ruk},
        )


class _Usage(System):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/system.Usage
    """

    _endpoint2 = "usage"

    def GetCPUHours(
        self,
        start: str = None,
        period: str = None,
        series: bool = None,
        ruk: str = None,
    ):
        return self._get(
            "GetCPUHours",
            params={"start": start, "period": period, "series": series, "ruk": ruk},
        )

    def GetPlatformStats(
        self,
        ruk: str = None,
    ):
        return self._get(
            "GetPlatformStats",
            params={"ruk": ruk},
        )
