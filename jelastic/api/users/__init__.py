from ..abstract import ClientAbstract

__all__ = ["Users"]


class Users(ClientAbstract):
    """
    The methods of this service provide user account information (such as SSH keys, quotas, etc.) and manage account-related settings.


    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users

    Ref: https://docs.jelastic.com/api/private/#!/api/users
    """

    _endpoint1 = "users"

    @property
    def Account(self) -> "_Account":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.users.Account

        Ref: https://docs.jelastic.com/api/private/#!/api/users.Account
        """
        return _Account(session=self._session, token=self._token, debug=self._debug)


class _Account(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.Account

     Ref: https://docs.jelastic.com/api/private/#!/api/users.Account
    """

    _endpoint2 = "account"

    def AddAccount(
        self,
        email: str,
        password: str,
        name: list[str] = None,
        notify: list[bool] = None,
        reseller_id: list[int] = None,
    ):
        """
        param email: unique email address of the new account.
        param password: password for the new account.
        param name: an account's name.
        param notify: defines whether to send a confirmation letter to the new user email upon success (true) or not (false).
        param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "AddAccount",
            params={
                "email": email,
                "password": password,
                "name": name,
                "notify": notify,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def AddSSHKey(
        self,
        title: str,
        ssh_key: str,
        is_private: bool,
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
            },
        )

    def ChangeEmail(
        self,
        email: str,
        redirect_url: list[str] = None,
    ):
        """
        param email: new account email address (provided by the user).
        param redirect_url: a link to display in user email message.
        """
        return self._get(
            "ChangeEmail",
            params={
                "email": email,
                "redirectUrl": redirect_url,
            },
            delimiter=",",
        )

    def ChangeName(
        self,
        name: str,
    ):
        """
        param name: new account name (provided by the user).
        """
        return self._get(
            "ChangeName",
            params={
                "name": name,
            },
        )

    def ChangePassword(
        self,
        old_password: str,
        new_password: str,
        invalidate_sessions: list[str] = None,
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
            },
            delimiter=",",
        )

    def CheckUser(
        self,
        login: str,
    ):
        return self._get(
            "CheckUser",
            params={
                "login": login,
            },
        )

    def DeleteSSHKey(
        self,
        id: int,
    ):
        """
        param id: unique identifier of the ssh key.
        """
        return self._get(
            "DeleteSSHKey",
            params={
                "id": id,
            },
        )

    def Disable2FA(
        self,
        password: list[str] = None,
    ):
        return self._get(
            "Disable2FA",
            params={
                "password": password,
            },
            delimiter=",",
        )

    def Enable2FA(
        self,
        code: str,
        password: list[str] = None,
    ):
        return self._get(
            "Enable2FA",
            params={
                "code": code,
                "password": password,
            },
            delimiter=",",
        )

    def Get2FABackupCodes(
        self,
        password: list[str] = None,
    ):
        return self._get(
            "Get2FABackupCodes",
            params={
                "password": password,
            },
            delimiter=",",
        )

    def Get2FAConfig(
        self,
        password: list[str] = None,
    ):
        return self._get(
            "Get2FAConfig",
            params={
                "password": password,
            },
            delimiter=",",
        )

    def GetSSHKeys(
        self,
        is_private: list[str] = None,
    ):
        return self._get(
            "GetSSHKeys",
            params={
                "isPrivate": is_private,
            },
            delimiter=",",
        )

    def GetUserInfo(
        self,
    ):
        return self._get("GetUserInfo", params={})

    def GetUserInfoInner(
        self,
        login: str,
    ):
        return self._get(
            "GetUserInfoInner",
            params={
                "login": login,
            },
        )

    def RecoverPassword(self, email: str, lang: list[str] = None):
        return self._get(
            "RecoverPassword",
            params={
                "email": email,
                "lang": lang,
            },
            delimiter=",",
        )

    def Regenerate2FABackupCodes(
        self,
        password: list[str] = None,
    ):
        return self._get(
            "Regenerate2FABackupCodes",
            params={
                "password": password,
            },
            delimiter=",",
        )

    def SetAsTenantHost(
        self,
        uid: int,
        force_change: bool,
    ):
        """
        param uid: unique identifier of the target user.
        param force_change: defines whether to change tenant host if one already exists (true) or not (false).
        """
        return self._get(
            "SetAsTenantHost",
            params={
                "uid": uid,
                "forceChange": force_change,
            },
        )

    def SetPassword(
        self,
        auth_key: str,
        invalidate_sessions: list[bool] = None,
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
            },
            delimiter=",",
        )

    def SetUserData(
        self,
        data: str,
    ):
        return self._get(
            "SetUserData",
            params={
                "data": data,
            },
        )
