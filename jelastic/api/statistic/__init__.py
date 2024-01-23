from datetime import datetime

from ..abstract import ClientAbstract

__all__ = ["Statistic"]


class Statistic(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.statistic
    Ref: https://docs.jelastic.com/api/private/#!/api/statistic
    """

    _endpoint1 = "statistic"

    @property
    def Statistic(self) -> "_Statistic":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.statistic.Statistic

        Ref: https://docs.jelastic.com/api/private/#!/api/statistic.Statistic
        """
        return _Statistic(session=self._session, token=self._token, debug=self._debug)

    @property
    def Utils(self) -> "_Utils":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.statistic.Utils
        Ref: https://docs.jelastic.com/api/private/#!/api/statistic.Utils
        """
        return _Utils(session=self._session, token=self._token, debug=self._debug)

    @property
    def System(self) -> "_System":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.statistic.System
        Ref: https://docs.jelastic.com/api/private/#!/api/statistic.System
        """
        return _System(session=self._session, token=self._token, debug=self._debug)


class _Statistic(Statistic):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/statistic.Statistic
    """

    _endpoint2 = "statistic"

    def CreateStatTable(
        self,
        env_id: str,
        checksum: str,
    ):
        return self._get(
            "CreateStatTable",
            params={
                "envid": env_id,
                "checksum": checksum,
            },
        )

    def GetActiveCloudlets(
        self,
        checksum: str,
    ):
        return self._get(
            "GetActiveCloudlets",
            params={
                "checksum": checksum,
            },
        )

    def GetAggStats(
        self,
        start_time: datetime,
        env_id: str,
        checksum: str,
        end_time: datetime = None,
    ):
        """
        param start_time: start period inclusive date and time in format yyyy-MM-dd HH:mm:ss
        param env_id: unique identifier of the platform OS node (assigned by VZ)
        param checksum: calculated as MD5(os node is + private api key)
        param end_time: end period inclusive date and time in format yyyy-MM-dd HH:mm:ss

        """
        return self._get(
            "GetAggStats",
            params={
                "starttime": start_time,
                "envid": env_id,
                "checksum": checksum,
                "endtime": end_time,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetAllAggSumStatByUid(
        self, start_time: datetime, env_id: str, checksum: str, end_time: datetime
    ):
        return self._get(
            "GetAllAggSumStatByUid",
            params={
                "startTime": start_time,
                "envid": env_id,
                "checksum": checksum,
                "endTime": end_time,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetAllSumStatByUid(
        self,
        uid: int,
        duration: int,
        checksum: str,
        end_time: datetime = None,
    ):
        return self._get(
            "GetAllSumStatByUid",
            params={
                "uid": uid,
                "duration": duration,
                "checksum": checksum,
                "endtime": end_time,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetCurrentStatisticsForAllContainers(
        self,
        checksum: str,
    ):
        return self._get(
            "GetCurrentStatisticsForAllContainers",
            params={
                "checksum": checksum,
            },
        )

    def GetLastStats(self, node_group: str = None, node_id: int = None):
        return self._get(
            "GetLastStats",
            params={
                "nodeGroup": node_group,
                "nodeId": node_id,
            },
        )

    def GetStats(
        self,
        duration: int,
        interval: int,
        checksum: str,
        end_time: datetime = None,
        node_id: int = None,
        node_type: str = None,
        node_group: str = None,
    ):
        return self._get(
            "GetStats",
            params={
                "duration": duration,
                "interval": interval,
                "checksum": checksum,
                "end_time": end_time,
                "nodeid": node_id,
                "nodetype": node_type,
                "nodeGroup": node_group,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetStatus(
        self,
        checksum: str,
    ):
        return self._get(
            "GetStatus",
            params={
                "checksum": checksum,
            },
        )

    def GetSumStat(
        self,
        duration: int,
        checksum: str,
        end_time: datetime = None,
    ):
        return self._get(
            "GetSumStat",
            params={
                "duration": duration,
                "checksum": checksum,
                "endtime": end_time,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetSumStatsByPeriod(
        self,
        start_time: datetime,
        env_id: str,
        checksum: str,
        end_time: datetime = None,
    ):
        """
        param start_time: start period inclusive date and time in format yyyy-MM-dd HH:mm:ss
        param env_id: unique identifier of the platform OS node (assigned by VZ)
        param checksum: calculated as MD5(os node is + private api key)
        param end_time: end period inclusive date and time in format yyyy-MM-dd HH:mm:ss

        """
        return self._get(
            "GetSumStatsByPeriod",
            params={
                "starttime": start_time,
                "envid": env_id,
                "checksum": checksum,
                "endtime": end_time,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def SearchNodes(self, checksum: str, search: str = None):
        return self._get(
            "SearchNodes",
            params={"checksum": checksum, "search": search},
        )


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


class _System(Statistic):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/statistic.System
    """

    _endpoint2 = "system"

    def Event(
        self,
        topic: str,
        publish_local: bool = None,
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
        is_public_only: bool = None,
        is_token: bool = None,
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

    def RefreshUser(self, language: str = None):
        return self._get(
            "RefreshUser",
            params={"language": language},
        )

    def ReloadConfiguration(
        self, reseller_id: int = None, changed_place_holders: str = None
    ):
        return self._get(
            "ReloadConfiguration",
            params={
                "resellerId": reseller_id,
                "changedPlaceholders": changed_place_holders,
            },
        )
