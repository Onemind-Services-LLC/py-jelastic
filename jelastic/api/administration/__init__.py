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
    def HostGroup(self) -> "_HostGroup":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.HostGroup

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.HostGroup
        """
        return _HostGroup(
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


class _HostGroup(Administration):
    _endpoint2 = "hostGroup"

    def Add(
        self,
        data: dict,
    ):
        """
        :param data: JSON representation of an object (host group) that should be created.
        """
        return self._get(
            "Add",
            params={
                "data": data,
            },
            delimiter=",",
        )

    def AddEndpoints(
        self,
        host_group: str,
        end_points: dict,
    ):
        """
        :param host_group: unique identifier of the target host group.
        :param end_points: JSON array of endpoint objects.
        """
        return self._get(
            "AddEndpoints",
            params={
                "hostGroup": host_group,
                "endpoints": end_points,
            },
            delimiter=",",
        )

    def Edit(
        self,
        data: dict,
    ):
        """
        :param data: JSON representation of an object (host group) that should be edited.
        """
        return self._get(
            "Edit",
            params={
                "data": data,
            },
            delimiter=",",
        )

    def EditEndpoints(
        self,
        host_group: str,
        end_points: dict,
    ):
        """
        :param end_points: JSON array of endpoint objects
        """
        return self._get(
            "EditEndpoints",
            params={
                "hostGroup": host_group,
                "endpoints": end_points,
            },
            delimiter=",",
        )

    def Get(
        self,
    ):
        return self._get("Get", params={})

    def GetEndpoints(
        self,
        host_group: str,
    ):
        """
        :param host_group: unique identifier of the target host group.
        """
        return self._get(
            "GetEndpoints",
            params={
                "hostGroup": host_group,
            },
        )

    def Remove(
        self,
        id: int,
    ):
        """
        :param id:unique identifier of the target host group.
        """
        return self._get(
            "Remove",
            params={
                "id": id,
            },
        )

    def RemoveEndpoints(
        self,
        id: int,
    ):
        """
        :param id:unique identifier of the target endpoint.
        """
        return self._get(
            "RemoveEndpoints",
            params={
                "id": id,
            },
        )

    def RenameRemoteUser(
        self,
        uid: int,
        email: str,
    ):
        """
        :param uid: unique identifier of the target user.
        :param email: new email address for the user.
        """
        return self._get(
            "RenameRemoteUser",
            params={"uid": uid, "email": email},
        )

    def TestEndpoints(
        self,
        end_points: dict,
    ):
        """
        :param end_points: JSON array with endpoints objects with ids.
        """
        return self._get(
            "TestEndpoints",
            params={
                "endPoints": end_points,
            },
            delimiter=",",
        )
