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
    def NodePool(self) -> "_NodePool":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
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
            type:list[str]=None,

    ):
        """
        param checksum: authorization checksum = md5(appid + private key)
        """
        return self._get(
            "ClearOsPool",
            params={
                "checksum": checksum,
                "type": type
            }, delimiter=",",
        )
    def ClearPool(
            self,
            hn_id: int,
            type:list[str]=None,

    ):
        """
        param hnid: hardnode id (primary key) where OsNode to be allocated
        param checksum: authorization checksum = md5(appid + private key)
        """
        return self._get(
            "ClearPool",
            params={
                "hnid": hn_id,
                "type": type
            }, delimiter=",",
        )
    def GeneratePool(
            self,
            checksum: int,
            type:list[str]=None,
            hn_id: list[int]=None,

    ):
        return self._get(
            "GeneratePool",
            params={
                "checksum": checksum,
                "type": type,
                "hnid": hn_id,
            }, delimiter=",",
        )

    def Get(
            self,
            type:str,
            hn_id:str,
            checksum: str,
            os_template:list[str]=None,
            ct_id:list[str]=None

    ):
        """
        info about allocated new OsNode

        param type: OsNode type like "mysql5", "tomcat6", "jetty6" etc.
        param hn_id: hardnode id (primary key) where OsNode to be allocated
        param checksum: authorization checksum = md5(appid + private key)
        """
        return self._get(
            "Get",
            params={
                "type": type,
                "hnid": hn_id,
                "checksum": checksum,
                "osTemplate": os_template,
                "ctid": ct_id
            }, delimiter=",",
        )
    def GetStatus(
            self,
            checksum: str,
    ):
        """
        param checksum: authorization checksum = md5(appid + private key)
        """
        return self._get(
            "GetStatus",
            params={
                "checksum": checksum,
            }
        )

    def RegeneratePool(
            self,
            type: str,
            checksum: str,

    ):
        """
        param checksum: authorization checksum = md5(appid + private key)
        """
        return self._get(
            "RegeneratePool",
            params={
                "type": type,
                "checksum": checksum,

            }, delimiter=",",
        )






