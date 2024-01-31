from ..abstract import ClientAbstract

__all__ = ["Platform"]


class Platform(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.platform
    """

    _endpoint1 = "platform"

    @property
    def Engine(self) -> "_Engine":
        """
        Service provides an interface for managing host group engines.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.platform.Engine

        Ref: https://docs.jelastic.com/api/private/#!/api/platform.Engine
        """
        return _Engine(session=self._session, token=self._token, debug=self._debug)


class _Engine(Platform):
    """
    Service provides an interface for managing host group engines.

    Ref: https://docs.jelastic.com/api/private/#!/api/platform.Engine
    """

    _endpoint2 = "engine"

    def Get(self, engine_type: str = None, owner_uid: int = None, ruk: str = None,):
        """
        Returns a list of available engines for the user.

        :param engine_type: specific engine, support for which should be checked by the method.
        :param owner_uid: unique identifier of the platform owner.
        """
        return self._get(
            "Get", params={"engineType": engine_type, "ownerUid": owner_uid, "ruk": ruk,}
        )

    def GetEntryPoint(self, host_group: str, owner_uid: int = None, ruk: str = None,):
        """
        Connects a user to the host group.

        :param host_group: unique identifier of the target host group.
        :param owner_uid: unique identifier of the platform owner.
        """
        return self._get(
            "GetEntryPoint", params={"hostGroup": host_group, "ownerUid": owner_uid, "ruk": ruk,}
        )
