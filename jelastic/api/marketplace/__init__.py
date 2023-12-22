from ..abstract import ClientAbstract

__all__ = ["Marketplace"]


class Marketplace(ClientAbstract):
    _endpoint1 = "marketplace"

    @property
    def Console(self) -> "_Console":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.marketplace.Console

        Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Console
        """
        return _Console(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Console(Marketplace):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Console
    """

    _endpoint2 = "console"

    def ClearLog(
        self,
    ):
        return self._get("ClearLog", params={})

    def ReadLog(
        self,
    ):
        return self._get("ReadLog", params={})

    def WriteLog(self, message: str):
        """
        param message: a custom message to be added to the console log.
        """
        return self._get("WriteLog", params={"message": message})
