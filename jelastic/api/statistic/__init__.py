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
    def Utils(self) -> "_Utils":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.statistic.Utils
        Ref: https://docs.jelastic.com/api/private/#!/api/statistic.Utils
        """
        return _Utils(session=self._session, token=self._token, debug=self._debug)


class _Utils(Statistic):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/statistic.Utils
    """

    _endpoint2 = "utils"

    def GenerateStatistics(
        self,
        duration_hours: int,
        node_id: int,
        stat_json: str,
        checksum: str,
    ):
        return self._get(
            "GenerateStatistics",
            params={
                "durationHours": duration_hours,
                "nodeId": node_id,
                "statJSON": stat_json,
                "checksum": checksum,
            },
        )