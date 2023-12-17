from ..abstract import ClientAbstract

__all__ = ["S3"]


class S3(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.s3

    Ref: https://docs.jelastic.com/api/private/#!/api/s3
    """
    _endpoint1 = "s3"

    @property
    def Account(self) -> "_Account":
        """
        Service provides an interface for managing S3 stuff

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.s3.Account

        Ref: https://docs.jelastic.com/api/private/#!/api/s3.Account
        """
        return _Account(
            session=self._session,
            token=self._token,
            debug=self._debug
        )


class _Account(S3):
    """
    Service provides an interface for managing S3 stuff

    Ref: https://docs.jelastic.com/api/private/#!/api/s3.Account
    """
    _endpoint2 = "account"

    def Create(self, host_group: str, name: str, owner_uid: int = None):
        """
        Creates a new S3 account.

        :param host_group: unique name of the target host group.
        :param name: a name of the account to be created.
        :param owner_uid: unique identifier of the S3 account owner.
        """
        return self._get(
            "Create",
            params={
                "hostGroup": host_group,
                "name": name,
                "ownerUid": owner_uid
            }
        )

    def Delete(self, host_group: str, name: str, owner_uid: int = None):
        """
        Deletes an S3 account.

        :param host_group: unique name of the target host group.
        :param name: a name of the account to be deleted.
        :param owner_uid: unique identifier of the S3 account owner.
        """
        return self._get(
            "Delete",
            params={
                "hostGroup": host_group,
                "name": name,
                "ownerUid": owner_uid
            }
        )

    def GenerateKey(self, host_group: str, name: str, owner_uid: int = None):
        """
        Generates a new key for an S3 account.

        :param host_group: unique name of the target host group.
        :param name: a name of the account to be updated.
        :param owner_uid: unique identifier of the S3 account owner.
        """
        return self._get(
            "GenerateKey",
            params={
                "hostGroup": host_group,
                "name": name,
                "ownerUid": owner_uid
            }
        )

    def GetKeys(self, owner_uid: int = None):
        """
        Returns the list of accounts together with keys for each available S3 cluster.

        :param owner_uid: unique identifier of the S3 account owner.
        """
        return self._get(
            "GetKeys",
            params={
                "ownerUid": owner_uid
            }
        )

    def RegenerateKeys(self, host_group: str, acc_key: str, owner_uid: int = None):
        """
        Regenerates the target key pair by access key.

        :param host_group: unique name of the target host group.
        :param acc_key: access key that should be regenerated.
        :param owner_uid: unique identifier of the S3 account owner.
        """
        return self._get(
            "RegenerateKeys",
            params={
                "hostGroup": host_group,
                "accKey": acc_key,
                "ownerUid": owner_uid
            })

    def RevokeKey(self, host_group: str, acc_key: str, owner_uid: int = None):
        """
        Revokes the target key to the S3 account for the current user.

        :param host_group: unique name of the target host group.
        :param acc_key: access key that should be revoked.
        :param owner_uid: unique identifier of the S3 account owner.
        """
        return self._get(
            "RevokeKey",
            params={
                "hostGroup": host_group,
                "accKey": acc_key,
                "ownerUid": owner_uid
            }
        )
