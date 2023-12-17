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
        return _Account(session=self._session, token=self._token, debug=self._debug)

    @property
    def Bucket(self) -> "_Bucket":
        """
        Service provides an interface for managing S3 stuff

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.s3.Bucket

        Ref: https://docs.jelastic.com/api/private/#!/api/s3.Bucket
        """
        return _Bucket(session=self._session, token=self._token, debug=self._debug)


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
            params={"hostGroup": host_group, "name": name, "ownerUid": owner_uid},
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
            params={"hostGroup": host_group, "name": name, "ownerUid": owner_uid},
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
            params={"hostGroup": host_group, "name": name, "ownerUid": owner_uid},
        )

    def GetKeys(self, owner_uid: int = None):
        """
        Returns the list of accounts together with keys for each available S3 cluster.

        :param owner_uid: unique identifier of the S3 account owner.
        """
        return self._get("GetKeys", params={"ownerUid": owner_uid})

    def RegenerateKeys(self, host_group: str, acc_key: str, owner_uid: int = None):
        """
        Regenerates the target key pair by access key.

        :param host_group: unique name of the target host group.
        :param acc_key: access key that should be regenerated.
        :param owner_uid: unique identifier of the S3 account owner.
        """
        return self._get(
            "RegenerateKeys",
            params={"hostGroup": host_group, "accKey": acc_key, "ownerUid": owner_uid},
        )

    def RevokeKey(self, host_group: str, acc_key: str, owner_uid: int = None):
        """
        Revokes the target key to the S3 account for the current user.

        :param host_group: unique name of the target host group.
        :param acc_key: access key that should be revoked.
        :param owner_uid: unique identifier of the S3 account owner.
        """
        return self._get(
            "RevokeKey",
            params={"hostGroup": host_group, "accKey": acc_key, "ownerUid": owner_uid},
        )


class _Bucket(S3):
    """
    Service provides an interface for managing S3 stuff

    Ref: https://docs.jelastic.com/api/private/#!/api/s3.Bucket
    """

    _endpoint2 = "bucket"

    def CopyObject(
        self,
        src_bucket_name: str,
        src_key: str,
        dest_bucket_name: str,
        dest_key: str,
        host_group: str,
        owner_uid: int = None,
    ):
        """
        Copies an object from one bucket to another.

        :param src_bucket_name: name of the source bucket.
        :param src_key: unique identifier of the source object key.
        :param dest_bucket_name: name of the target bucket.
        :param dest_key: unique identifier of the target object key.
        :param host_group: unique identifier of the target host group.
        :param owner_uid: unique identifier of the bucket owner.
        """
        return self._get(
            "CopyObject",
            params={
                "srcBucketName": src_bucket_name,
                "srcKey": src_key,
                "dstBucketName": dest_bucket_name,
                "dstKey": dest_key,
                "hostGroup": host_group,
                "ownerUid": owner_uid,
            },
        )

    def Create(self, bucket_name: str, host_group: str, owner_uid: int = None):
        """
        Creates a new bucket in the storage.

        :param bucket_name: name of the bucket to be created.
        :param host_group: unique identifier of the target host group.
        :param owner_uid: unique identifier of the bucket owner.
        """
        return self._get(
            "Create",
            params={
                "bucketName": bucket_name,
                "hostGroup": host_group,
                "ownerUid": owner_uid,
            },
        )

    def Delete(self, bucket_name: str, host_group: str, owner_uid: int = None):
        """
        Deletes a bucket from the storage.

        :param bucket_name: name of the bucket to be deleted.
        :param host_group: unique identifier of the target host group.
        :param owner_uid: unique identifier of the bucket owner.
        """
        return self._get(
            "Delete",
            params={
                "bucketName": bucket_name,
                "hostGroup": host_group,
                "ownerUid": owner_uid,
            },
        )

    def DeleteObject(
        self, bucket_name: str, key: str, host_group: str, owner_uid: int = None
    ):
        """
        Removes an object from the bucket.

        :param bucket_name: name of the bucket.
        :param key: unique identifier of the object key.
        :param host_group: unique identifier of the target host group.
        :param owner_uid: unique identifier of the bucket owner.
        """
        return self._get(
            "DeleteObject",
            params={
                "bucketName": bucket_name,
                "key": key,
                "hostGroup": host_group,
                "ownerUid": owner_uid,
            },
        )

    def DeletePolicy(self, bucket_name: str, host_group: str, owner_uid: int = None):
        """
        Removes bucket policy.

        :param bucket_name: name of the bucket.
        :param host_group: unique identifier of the target host group.
        :param owner_uid: unique identifier of the bucket owner.
        """
        return self._get(
            "DeletePolicy",
            params={
                "bucketName": bucket_name,
                "hostGroup": host_group,
                "ownerUid": owner_uid,
            },
        )

    def GetPolicy(self, bucket_name: str, host_group: str, owner_uid: int = None):
        """
        Returns a list of bucket policies.

        :param bucket_name: name of the bucket.
        :param host_group: unique identifier of the target host group.
        :param owner_uid: unique identifier of the bucket owner.
        """
        return self._get(
            "GetPolicy",
            params={
                "bucketName": bucket_name,
                "hostGroup": host_group,
                "ownerUid": owner_uid,
            },
        )

    def GetPresignedURL(
        self, bucket_name: str, key: str, host_group: str, owner_uid: int = None
    ):
        """
        Returns a link to the bucket.

        :param bucket_name: name of the bucket.
        :param key: unique identifier of the object key.
        :param host_group: unique identifier of the target host group.
        :param owner_uid: unique identifier of the bucket owner.
        """
        return self._get(
            "GetPresignedURL",
            params={
                "bucketName": bucket_name,
                "key": key,
                "hostGroup": host_group,
                "ownerUid": owner_uid,
            },
        )

    def List(self, owner_uid: int = None):
        """
        Returns a list of buckets in the storage.

        :param owner_uid: unique identifier of the bucket owner.
        """
        return self._get("List", params={"ownerUid": owner_uid})

    def ListObjects(
        self,
        bucket_name: str,
        host_group: str,
        prefix: str = None,
        continuation_token: str = None,
        delimiter: str = ",",
        max_keys: int = 100,
        owner_uid: int = None,
    ):
        """
        Returns a list of objects in a bucket.

        :param bucket_name: name of the bucket.
        :param host_group: unique identifier of the target host group.
        :param prefix: filters response to objects that start with the provided string.
        :param continuation_token: custom token to indicate that the list continues on the same bucket.
        :param delimiter: custom string to divide separate object records.
        :param max_keys: the maximum number of objects returned in the response.
        :param owner_uid: unique identifier of the bucket owner.
        """
        return self._get(
            "ListObjects",
            params={
                "bucketName": bucket_name,
                "hostGroup": host_group,
                "prefix": prefix,
                "continuationToken": continuation_token,
                "delimiter": delimiter,
                "maxKeys": max_keys,
                "ownerUid": owner_uid,
            },
        )

    def SetPolicy(
        self, bucket_name: str, host_group: str, policy: str, owner_uid: int = None
    ):
        """
        Replaces existing bucket policies with the provided value.

        :param bucket_name: name of the bucket.
        :param host_group: unique identifier of the target host group.
        :param policy: S3 policies to specify permissions for each resource to allow or deny actions requested by user or role.
        :param owner_uid: unique identifier of the bucket owner.
        """
        return self._get(
            "SetPolicy",
            params={
                "bucketName": bucket_name,
                "hostGroup": host_group,
                "policy": policy,
                "ownerUid": owner_uid,
            },
        )
