from datetime import date
from typing import Literal

from ..abstract import ClientAbstract

__all__ = ["Administration"]

MODE = Literal["STRONG", "MODERATE", "WEAK"]


class Administration(ClientAbstract):
    _endpoint1 = "administration"

    @property
    def Analytics(self) -> "_Analytics":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.Analytics

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.Analytics
        """
        return _Analytics(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Resource(self) -> "_Resource":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.Resource

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.Resource
        """
        return _Resource(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Analytics(Administration):
    _endpoint2 = "analytics"

    def GetNodesAffinitySuggestion(
        self,
        target_app_ids: list[str] = None,
        node_groups: list[str] = None,
        uids: list[int] = None,
        thread_count: int = None,
    ):
        """
        A list of environments with one node in every layer where distribution can be optimized

        :param target_app_ids: list of the exact environments that should be analyzed
        :param node_groups: list of the node group IDs that should be analyzed
        :param uids: list of the user IDs that should be analyzed
        :param thread_count: a number of threads for container distribution analysis
        """
        return self._get(
            "GetNodesAffinitySuggestion",
            params={
                "targetAppIds": target_app_ids,
                "nodeGroups": node_groups,
                "uids": uids,
                "threadCount": thread_count,
            },
            delimiter=",",
        )

    def GetNodesAntiAffinitySuggestion(
        self,
        target_app_ids: list[str] = None,
        mode: MODE = None,
        node_groups: list[str] = None,
        uids: list[int] = None,
        thread_count: int = None,
    ):
        """
        A list of environments with non-optimal container distribution with optimization suggestions

        :param target_app_ids: list of the exact environments that should be analyzed
        :param mode: a mode of the anti-affinity analysis
        :param node_groups: list of the node group IDs that should be analyzed
        :param uids: list of the user IDs that should be analyzed
        :param thread_count: a number of threads for container distribution analysis
        """
        return self._get(
            "GetNodesAntiAffinitySuggestion",
            params={
                "targetAppIds": target_app_ids,
                "mode": mode,
                "nodeGroups": node_groups,
                "uids": uids,
                "threadCount": thread_count,
            },
            delimiter=",",
        )


class _Resource(Administration):
    _endpoint2 = "resource"

    def AddStatistics(
        self,
        resource_name: str,
        uid: int,
        value: int,
        start_date: list[date] = None,
        end_date: list[date] = None,
        env_name: list[str] = None,
        node_id: list[int] = None,
        note: list[str] = None,
        value_group: list[str] = None,
    ):
        return self._get(
            "AddStatistics",
            params={
                "resourceName": resource_name,
                "uid": uid,
                "value": value,
                "startDate": start_date,
                "endDate": end_date,
                "envName": env_name,
                "nodeId": node_id,
                "note": note,
                "valueGroup": value_group,
            },
            delimiter=",",
        )
