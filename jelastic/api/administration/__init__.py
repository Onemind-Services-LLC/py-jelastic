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
    def Config(self) -> "_Config":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.Config

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.Config
        """
        return _Config(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Analytics(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Config
    """

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


class _Config(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Config
    """

    _endpoint2 = "config"

    def ApplyConfig(
        self,
        type: str,
        password: str,
    ):
        return self._get(
            "ApplyConfig",
            params={
                "type": type,
                "password": password,
            },
        )

    def ApplyDefaults(
        self,
        edition: str,
    ):
        return self._get(
            "ApplyDefaults",
            params={
                "edition": edition,
            },
        )

    def ApplyResellerConfig(
        self,
        type: str,
        password: str,
        reseller_id: str,
    ):
        return self._get(
            "ApplyResellerConfig",
            params={
                "type": type,
                "password": password,
                "resellerId": reseller_id,
            },
        )

    def ChangeConfigKey(
        self,
        type: str,
        key: str,
        value: list[str] = None,
    ):
        return self._get(
            "ChangeConfigKey",
            params={
                "type": type,
                "key": key,
                "value": value,
            },
            delimiter=",",
        )

    def ChangePropertiesForReseller(
        self,
        reseller_id: str,
    ):
        return self._get(
            "ChangePropertiesForReseller",
            params={
                "resellerId": reseller_id,
            },
        )

    def CreatingConfigType(
        self,
        type: str,
        description: str,
    ):
        return self._get(
            "CreatingConfigType",
            params={
                "type": type,
                "description": description,
            },
        )

    def CreatingKeyConfig(
        self,
        type: str,
        key: str,
        value: str,
        default_value: str,
        expert: str,
        description: str,
        key_type: str,
    ):
        return self._get(
            "CreatingKeyConfig",
            params={
                "type": type,
                "key": key,
                "value": value,
                "default_value": default_value,
                "expert": expert,
                "description": description,
                "keyType": key_type,
            },
        )

    def FindConfigKey(
        self,
        value: str,
    ):
        return self._get(
            "FindConfigKey",
            params={
                "value": value,
            },
        )

    def GetAllConfigType(
        self,
        expert: str,
    ):
        return self._get(
            "GetAllConfigType",
            params={
                "expert": expert,
            },
        )

    def GetAllKeyConfigByType(
        self,
        type: str,
        expert: str,
    ):
        return self._get(
            "GetAllKeyConfigByType",
            params={
                "type": type,
                "expert": expert,
            },
        )

    def GetConfigKey(
        self,
        type: str,
        key: str,
    ):
        """
        :param type: configuration type
        :param key: configuration key name
        """
        return self._get(
            "GetConfigKey",
            params={
                "type": type,
                "key": key,
            },
        )

    def GetConfigKeyByResellerId(
        self,
        type: str,
        key: str,
        reseller_id: list[int] = None,
    ):
        """
        :param type: configuration type
        :param key: configuration key name
        :param reseller_id: unique identifier of the reseller (Optional)
        """
        return self._get(
            "GetConfigKeyByResellerId",
            params={
                "type": type,
                "key": key,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def GetConfigKeys(
        self,
        type: list[str] = None,
        key: list[str] = None,
    ):
        """
        :param type: a comma-separated list of the setting types (for filtering).
        :param key: a comma-separated list of the setting names (for filtering).
        """
        return self._get(
            "GetConfigKeys",
            params={
                "type": type,
                "key": key,
            },
            delimiter=",",
        )

    def RemoveConfigKey(
        self,
        type: str,
        key: str,
    ):
        return self._get(
            "RemoveConfigKey",
            params={
                "type": type,
                "key": key,
            },
        )

    def RemoveConfigType(
        self,
        type: str,
    ):
        return self._get(
            "RemoveConfigType",
            params={
                "type": type,
            },
        )

    def RemoveResellerProperties(
        self,
        reseller_id: int,
    ):
        return self._get(
            "RemoveResellerProperties",
            params={
                "resellerId": reseller_id,
            },
        )

    def RevertConfigKey(
        self,
        type: str,
        key: str,
    ):
        return self._get(
            "RevertConfigKey",
            params={
                "type": type,
                "key": key,
            },
        )

    def SetResellerConfigKey(
        self,
        type: str,
        key: str,
        value: str,
        reseller_id: int,
    ):
        return self._get(
            "SetResellerConfigKey",
            params={
                "type": type,
                "key": key,
                "value": value,
                "resellerId": reseller_id,
            },
        )
