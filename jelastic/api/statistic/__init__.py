from ..abstract import ClientAbstract

__all__ = ["Statistic"]


class Statistic(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.statistic
    Ref: https://docs.jelastic.com/api/private/#!/api/statistic
    """

    _endpoint1 = "statistic"

    @property
    def System(self) -> "_System":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.statistic.System
        Ref: https://docs.jelastic.com/api/private/#!/api/statistic.System
        """
        return _System(session=self._session, token=self._token, debug=self._debug)


class _System(Statistic):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/statistic.System
    """

    _endpoint2 = "system"

    def Event(
        self,
        topic: str,
        publish_local: list[bool] = None,
    ):
        return self._get(
            "Event",
            params={
                "topic": topic,
                "publishLocal": publish_local,
            },
        )

    def GetAPIDescriptions(
        self,
        is_public_only: list[bool] = None,
        is_token: list[bool] = None,
    ):
        return self._get(
            "GetAPIDescriptions",
            params={
                "isPublicOnly": is_public_only,
                "isToken": is_token,
            },
        )

    def GetCacheStatus(
        self,
    ):
        return self._get(
            "GetCacheStatus",
            params={},
        )

    def GetInstanceCacheStatus(
        self,
    ):
        return self._get(
            "GetInstanceCacheStatus",
            params={},
        )

    def GetVersion(
        self,
    ):
        return self._get(
            "GetVersion",
            params={},
        )

    def RefreshEmailTemplates(
        self,
    ):
        return self._get(
            "RefreshEmailTemplates",
            params={},
        )

    def RefreshUser(self, language: list[str] = None):
        return self._get(
            "RefreshUser",
            params={"language": language},
        )

    def ReloadConfiguration(
        self, reseller_id: list[int] = None, changed_place_holders: list[str] = None
    ):
        return self._get(
            "ReloadConfiguration",
            params={
                "resellerId": reseller_id,
                "changedPlaceholders": changed_place_holders,
            },
        )
