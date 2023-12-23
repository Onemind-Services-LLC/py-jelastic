from ..abstract import ClientAbstract

__all__ = ["Pool"]


class Pool(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.pool

    Ref: https://docs.jelastic.com/api/#!/pool
    """
    _endpoint1 = "pool"

    @property
    def IpPool(self) -> "_IpPool":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.pool.IpPool

        Ref: https://docs.jelastic.com/api/private/#!/api/pool.IpPool
        """
        return _IpPool(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _IpPool(Pool):
    """
     Ref: https://docs.jelastic.com/api/private/#!/api/pool.IpPool
    """

    _endpoint2 = "ippool"

    def Add(self,
            ip_from: str,
            ip_to: str,
            region: str,
            checksum: str,
            ):
        return self._get(
            "Add",
            params={
                "ipfrom": ip_from,
                "ipto": ip_to,
                "region": region,
                "checksum": checksum,
            },
        )

    def AddExt(self,
               ip_from: str,
               ip_to: str,
               regions: str,
               checksum: str,
               ):
        return self._get(
            "AddExt",
            params={
                "ipfrom": ip_from,
                "ipto": ip_to,
                "regions": regions,
                "checksum": checksum,
            },
        )

    def AddIpv6Network(self,
                       network: str,
                       regions: str,
                       checksum: str,
                       ):
        return self._get(
            "AddIpv6Network",
            params={
                "network": network,
                "regions": regions,
                "checksum": checksum,
            },
        )

    def Get(self,
            checksum: str
            ):
        return self._get(
            "Get",
            params={
                "checksum": checksum,
            },
        )

    def GetExt(self,
               regions: str,
               checksum: str,
               type: list[str] = None,
               node_id: list[str] = None,
               target_app_id: list[str] = None
               ):
        return self._get(
            "GetExt",
            params={
                "regions": regions,
                "checksum": checksum,
                "type": type,
                "nodeId": node_id,
                "targetAppid": target_app_id,
            }, delimiter=",",
        )

    def GetFreePublicPort(self,
                          checksum: str
                          ):
        return self._get(
            "GetFreePublicPort",
            params={
                "checksum": checksum,
            },
        )

    def Release(self,
                id: int,
                checksum: str
                ):
        return self._get(
            "Release",
            params={
                "id": id,
                "checksum": checksum,
            },
        )

    def ReleaseExt(self,
                   id: int,
                   checksum: str
                   ):
        return self._get(
            "ReleaseExt",
            params={
                "id": id,
                "checksum": checksum,
            },
        )

    def ReleaseSubnet(self,
                      id: int,
                      checksum: str
                      ):
        return self._get(
            "ReleaseSubnet",
            params={
                "id": id,
                "checksum": checksum,
            },
        )

    def RemoveExt(self,
                  ips: str,
                  checksum: str
                  ):
        return self._get(
            "RemoveExt",
            params={
                "ips": ips,
                "checksum": checksum,
            },
        )

    def RemoveFromReserve(self,
                          checksum: str,
                          target_app_id: str
                          ):
        return self._get(
            "RemoveFromReserve",
            params={
                "checksum": checksum,
                "targetAppid": target_app_id,
            }
        )

    def ReserveExtIPv6(self,
                       checksum: str,
                       target_app_id: str
                       ):
        return self._get(
            "ReserveExtIPv6",
            params={
                "checksum": checksum,
                "targetAppid": target_app_id,
            }
        )

    def UnreserveExtIPv6(self,
                         id: int,
                         checksum: str
                         ):
        return self._get(
            "UnreserveExtIPv6",
            params={
                "id": id,
                "checksum": checksum,
            },
        )
