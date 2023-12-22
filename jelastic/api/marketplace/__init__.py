from ..abstract import ClientAbstract

__all__ = ["Marketplace"]


class Marketplace(ClientAbstract):
    _endpoint1 = "marketplace"

    @property
    def Favorite(self) -> "_Favorite":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.marketplace.Favorite
        Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Favorite
        """
        return _Favorite(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Favorite(Marketplace):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Favorite
    """

    _endpoint2 = "favorite"

    def Add(
        self,
        id: str,
    ):
        """
        param id: unique identifier of the target application.
        """
        return self._get(
            "Add",
            params={
                "id": id,
            },
        )

    def AddManifest(
        self,
        manifest: str,
    ):
        """
        param manifest: custom JPS (manifest body or link).
        """
        return self._get(
            "AddManifest",
            params={
                "manifest": manifest,
            },
        )

    def Delete(
        self,
        id: str,
    ):
        """
        param id: unique identifier of the target application.
        """
        return self._get(
            "Delete",
            params={
                "id": id,
            },
        )

    def GetList(
        self,
        search: list[str] = None,
        lang: list[str] = None,
        checksum: list[str] = None,
    ):
        """
        param search: JSON object with the search parameters
        param lang: target localization language.
        param checksum: hecksum of the Marketplace applications (to verify that you possess the most recent checksum and applications copy). If you send the same 'checksum' parameter as received in the previous response and if this 'checksum' hasn't changed on the server side, then the server assumes you have the latest local copy of applications on the client side. In this case, it will return an empty applications list, speeding up the response time.
        """
        return self._get(
            "Delete",
            params={
                "search": search,
                "lang": lang,
                "checksum": checksum,
            },
        )
