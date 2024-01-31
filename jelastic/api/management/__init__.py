from ..abstract import ClientAbstract

__all__ = ["Management"]


class Management(ClientAbstract):
    _endpoint1 = "management"

    @property
    def Account(self) -> "_Account":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.management.Account

        Ref: https://docs.jelastic.com/api/private/#!/api/management.Account
        """
        return _Account(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Account(Management):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/management.Account
    """

    _endpoint2 = "account"

    def AddPrivateSSHKey(self, title: str, ssh_key: str, ruk: str = None,):
        """
        :param title: title of the ssh key.
        :param sshKey: value of the ssh key.
        """
        return self._get(
            "AddPrivateSSHKey",
            params={"title": title, "sshKey": ssh_key, "ruk": ruk,},
        )

    def AddPublicSSHKey(self, title: str, ssh_key: str, ruk: str = None,):
        """
        :param title: title of the ssh key.
        :param sshKey: value of the ssh key.
        """
        return self._get(
            "AddPublicSSHKey",
            params={"title": title, "sshKey": ssh_key, "ruk": ruk,},
        )

    def AddSSHKey(self, title: str, ssh_key: str, is_private: bool, ruk: str = None,):
        """
        :param title: title of the ssh key.
        :param sshKey: value of the ssh key.
        """
        return self._get(
            "AddSSHKey",
            params={"title": title, "sshKey": ssh_key, "isPrivate": is_private, "ruk": ruk,},
        )

    def AdjustContainersLimitsForAllUsers(
        self, ruk: str = None,
    ):
        return self._get(
            "AdjustContainersLimitsForAllUsers",
            params={"ruk": ruk,},
        )

    def CleanQuotasCache(
        self,
        uid: int,
        ruk: str = None,
    ):
        return self._get(
            "CleanQuotasCache",
            params={
                "uid": uid,
                "ruk": ruk,
            },
        )

    def DeleteSSHKey(self, id: int, ruk: str = None,):
        """
        :param id: unique identifier of the ssh key.
        """
        return self._get(
            "DeleteSSHKey",
            params={
                "id": id,
                "ruk": ruk,
            },
        )

    def GetQuotasByIpAddress(
        self,
        ip_address: str,
        quotasnames: str,
        ruk: str = None,
    ):
        return self._get(
            "GetQuotasByIpAddress",
            params={
                "ipAddress": ip_address,
                "quotasnames": quotasnames,
                "ruk": ruk,
            },
        )

    def GetSSHKeys(self, is_private: bool, ruk: str = None,):
        """
        :param isPrivate: defines whether to return the account's private (true) or public (false) SSH keys.
        """
        return self._get(
            "GetSSHKeys",
            params={"isPrivate": is_private, "ruk": ruk,},
        )

    def GetSSHKeysInner(
        self,
        uid: int,
        ruk: str = None,
    ):
        """
        :param uid: unique identifier of the user (key owner).
        """
        return self._get(
            "GetSSHKeysInner",
            params={
                "uid": uid,
                "ruk": ruk,
            },
        )
