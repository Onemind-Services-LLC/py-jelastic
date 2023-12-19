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
    def Host(self) -> "_Host":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.Host

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.Host
        """
        return _Host(
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


class _Host(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Host
    """

    _endpoint2 = "host"

    def AddLabels(
        self,
        ids: str,
        labels: str,
    ):
        return self._get(
            "AddLabels",
            params={
                "ids": ids,
                "labels": labels,
            },
        )

    def CheckHostConnection(
        self,
        host_id: str,
        port: list[int] = None,
        check_external_ip: list[bool] = None,
    ):
        """
        :param host_id: unique identifier of the target host.
        :param port: checks the connection through the custom port (host's SSH port from the settings if not specified).
        """
        return self._get(
            "CheckHostConnection",
            params={
                "hostId": host_id,
                "port": port,
                "checkExternalIp": check_external_ip,
            },
            delimiter=",",
        )

    def GetHostFirewallSets(self):
        return self._get("GetHostFirewallSets", params={})

    def RemoveLabels(self, ids: str, labels: str):
        return self._get("RemoveLabels", params={"ids": ids, "labels": labels})

    def SetLabels(self, ids: str, labels: str):
        return self._get("SetLabels", params={"ids": ids, "labels": labels})

    def UpdateHostFirewall(
        self,
        host_id: list[int] = None,
        force: list[bool] = None,
        check_external_ip: list[bool] = None,
    ):
        """
        :param host_id: unique identifier of the target host (all hosts if not defined).
        :param force: proceeds (true) or interrupts (false) the operation in case of errors.
        """
        return self._get(
            "UpdateHostFirewall",
            params={
                "hostId": host_id,
                "force": force,
                "checkExternalIp": check_external_ip,
            },
            delimiter=",",
        )
