from ..abstract import ClientAbstract

__all__ = ["Management"]


class Management(ClientAbstract):
    _endpoint1 = "management"
    @property
    def Account(self) -> "_Account":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
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

    def AddPrivateSSHKey(
        self,
        title: str,
        ssh_key: str
    ):
        """
        :param title: title of the ssh key.
        :param sshKey: value of the ssh key.
        """
        return self._get(
            "AddPrivateSSHKey",
            params={
                "title": title,
                "sshKey": ssh_key
            },
        )
    def AddPublicSSHKey(
        self,
        title: str,
        ssh_key: str
    ):
        """
        :param title: title of the ssh key.
        :param sshKey: value of the ssh key.
        """
        return self._get(
            "AddPublicSSHKey",
            params={
                "title": title,
                "sshKey": ssh_key
            },
        )
    def AddSSHKey(
        self,
        title: str,
        ssh_key: str,
        is_private: bool
    ):
        """
        :param title: title of the ssh key.
        :param sshKey: value of the ssh key.
        """
        return self._get(
            "AddSSHKey",
            params={
                "title": title,
                "sshKey": ssh_key,
                "isPrivate": is_private
            },
        )

    def AdjustContainersLimitsForAllUsers(
        self,
    ):
        return self._get(
            "AdjustContainersLimitsForAllUsers",
            params={},
        )

    def CleanQuotasCache(
        self,
        uid: int,
    ):
        return self._get(
            "CleanQuotasCache",
            params={
                "uid": uid,
            },
        )

    def DeleteSSHKey(
        self,
        id: int
    ):
        """
        :param id: unique identifier of the ssh key.
        """
        return self._get(
            "DeleteSSHKey",
            params={
                "id": id,
            },
        )

    def GetQuotasByIpAddress(
        self,
        ip_address: str,
        quotasnames: str,
    ):
        return self._get(
            "GetQuotasByIpAddress",
            params={
                "ipAddress": ip_address,
                "quotasnames": quotasnames,
            },
        )

    def GetSSHKeys(
        self,
        is_private: bool
    ):
        """
        :param isPrivate: defines whether to return the account's private (true) or public (false) SSH keys.
        """
        return self._get(
            "GetSSHKeys",
            params={
                "isPrivate": is_private
            },
        )

    def GetSSHKeysInner(
        self,
        uid: int,
    ):
        """
        :param uid: unique identifier of the user (key owner).
        """
        return self._get(
            "GetSSHKeysInner",
            params={
                "uid": uid,
            },
        )