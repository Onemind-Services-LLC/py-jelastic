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
