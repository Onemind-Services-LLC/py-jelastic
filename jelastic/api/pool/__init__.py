from ..abstract import ClientAbstract

__all__ = ["Pool"]


class Pool(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.pool

    Ref: https://docs.jelastic.com/api/#!/pool
    """

    _endpoint1 = "pool"

    @property
    def IpPool(self) -> "_IpPool":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.pool.IpPool

        Ref: https://docs.jelastic.com/api/private/#!/api/pool.IpPool
        """
        return _IpPool(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def NodePool(self) -> "_NodePool":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.pool.NodePool

        Ref: https://docs.jelastic.com/api/private/#!/api/pool.NodePool
        """
        return _NodePool(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _NodePool(Pool):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/pool.NodePool
    """

    _endpoint2 = "nodepool"

    def ClearOsPool(
        self,
        checksum: str,
        type: str = None,
        ruk: str = None,
    ):
        """
        :param checksum: authorization checksum = md5(appid + private key)
        """
        return self._get(
            "ClearOsPool",
            params={
                "checksum": checksum,
                "type": type,
                "ruk": ruk,
            },
        )

    def ClearPool(
        self,
        hn_id: int,
        type: str = None,
        ruk: str = None,
    ):
        """
        :param hnid: hardnode id (primary key) where OsNode to be allocated
        :param checksum: authorization checksum = md5(appid + private key)
        """
        return self._get(
            "ClearPool",
            params={
                "hnid": hn_id,
                "type": type,
                "ruk": ruk,
            },
        )

    def GeneratePool(
        self,
        checksum: int,
        type: str = None,
        hn_id: int = None,
        ruk: str = None,
    ):
        return self._get(
            "GeneratePool",
            params={
                "checksum": checksum,
                "type": type,
                "hnid": hn_id,
                "ruk": ruk,
            },
        )

    def Get(
        self,
        type: str,
        hn_id: int,
        checksum: str,
        os_template: str = None,
        ct_id: int = None,
        ruk: str = None,
    ):
        """
        info about allocated new OsNode

        :param type: OsNode type like "mysql5", "tomcat6", "jetty6" etc.
        :param hn_id: hardnode id (primary key) where OsNode to be allocated
        :param checksum: authorization checksum = md5(appid + private key)
        """
        return self._get(
            "Get",
            params={
                "type": type,
                "hnid": hn_id,
                "checksum": checksum,
                "osTemplate": os_template,
                "ctid": ct_id,
                "ruk": ruk,
            },
        )

    def GetStatus(
        self,
        checksum: str,
        ruk: str = None,
    ):
        """
        :param checksum: authorization checksum = md5(appid + private key)
        """
        return self._get(
            "GetStatus",
            params={
                "checksum": checksum,
                "ruk": ruk,
            },
        )

    def RegeneratePool(
        self,
        type: str,
        checksum: str,
        ruk: str = None,
    ):
        """
        :param checksum: authorization checksum = md5(appid + private key)
        """
        return self._get(
            "RegeneratePool",
            params={
                "type": type,
                "checksum": checksum,
                "ruk": ruk,
            },
        )


class _IpPool(Pool):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/pool.IpPool
    """

    _endpoint2 = "ippool"

    def Add(
        self,
        ip_from: str,
        ip_to: str,
        region: str,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "Add",
            params={
                "ipfrom": ip_from,
                "ipto": ip_to,
                "region": region,
                "checksum": checksum,
                "ruk": ruk,
            },
        )

    def AddExt(
        self,
        ip_from: str,
        ip_to: str,
        regions: str,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "AddExt",
            params={
                "ipfrom": ip_from,
                "ipto": ip_to,
                "regions": regions,
                "checksum": checksum,
                "ruk": ruk,
            },
        )

    def AddIpv6Network(
        self,
        network: str,
        regions: str,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "AddIpv6Network",
            params={
                "network": network,
                "regions": regions,
                "checksum": checksum,
                "ruk": ruk,
            },
        )

    def Get(
        self,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "Get",
            params={
                "checksum": checksum,
                "ruk": ruk,
            },
        )

    def GetExt(
        self,
        regions: str,
        checksum: str,
        type: str = None,
        node_id: int = None,
        target_app_id: str = None,
        ruk: str = None,
    ):
        return self._get(
            "GetExt",
            params={
                "regions": regions,
                "checksum": checksum,
                "type": type,
                "nodeId": node_id,
                "targetAppid": target_app_id,
                "ruk": ruk,
            },
        )

    def GetFreePublicPort(
        self,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "GetFreePublicPort",
            params={
                "checksum": checksum,
                "ruk": ruk,
            },
        )

    def Release(
        self,
        id: int,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "Release",
            params={
                "id": id,
                "checksum": checksum,
                "ruk": ruk,
            },
        )

    def ReleaseExt(
        self,
        id: int,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "ReleaseExt",
            params={
                "id": id,
                "checksum": checksum,
                "ruk": ruk,
            },
        )

    def ReleaseSubnet(
        self,
        id: int,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "ReleaseSubnet",
            params={
                "id": id,
                "checksum": checksum,
                "ruk": ruk,
            },
        )

    def RemoveExt(
        self,
        ips: str,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "RemoveExt",
            params={
                "ips": ips,
                "checksum": checksum,
                "ruk": ruk,
            },
        )

    def RemoveFromReserve(
        self,
        checksum: str,
        target_app_id: str,
        ruk: str = None,
    ):
        return self._get(
            "RemoveFromReserve",
            params={
                "checksum": checksum,
                "targetAppid": target_app_id,
                "ruk": ruk,
            },
        )

    def ReserveExtIPv6(
        self,
        checksum: str,
        target_app_id: str,
        ruk: str = None,
    ):
        return self._get(
            "ReserveExtIPv6",
            params={
                "checksum": checksum,
                "targetAppid": target_app_id,
                "ruk": ruk,
            },
        )

    def UnreserveExtIPv6(
        self,
        id: int,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "UnreserveExtIPv6",
            params={
                "id": id,
                "checksum": checksum,
                "ruk": ruk,
            },
        )
