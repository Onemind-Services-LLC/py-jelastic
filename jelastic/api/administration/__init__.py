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

    @property
    def Utils(self) -> "_Utils":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.Utils

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.Utils
        """
        return _Utils(
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


class _Utils(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Utils
    """

    def AddSystemExternalDNSRecord(
        self,
        record_data: str,
        name: str,
        ttl: int,
        record_data_type: str,
        ssl_enabled: list[bool] = None,
        enabled: list[bool] = None,
    ):
        """
        :param record_data: custom data for the DNS record.
        :param name: name for DNS records (must be the same as one of the existing record).
        :param ttl: TTL (time to live) value for the DNS record.
        :param record_data_type: type of the DNS record data (currently, only the ‘TXT’ value is supported).
        :param ssl_enabled: defines whether the SSL is enabled for the record (true, by default) or not (false).
        :param enabled: defines whether the record is enabled (true, by default) or not (false).
        """
        return self._get(
            "AddSystemExternalDNSRecord",
            params={
                "recordData": record_data,
                "name": name,
                "ttl": ttl,
                "recordDataType": record_data_type,
                "sslEnabled": ssl_enabled,
                "enabled": enabled,
            },
            delimiter=",",
        )

    def AnalizeEnv(
        self,
        domain: str,
    ):
        return self._get(
            "AnalizeEnv",
            params={
                "domain": domain,
            },
        )

    def BalanceResources(self, domain: int):
        return self._get("BalanceResources", params={"domain": domain})

    def ClearEnvs(self):
        return self._get("ClearEnvs", params={})

    def DeleteBrokenEnvs(
        self,
        target_app_ids: list[str] = None,
    ):
        return self._get(
            "DeleteBrokenEnvs",
            params={
                "targetAppIds": target_app_ids,
            },
            delimiter=",",
        )

    def EditSystemExternalDNSRecord(
        self,
        id: int,
        record_data: list[str] = None,
        name: list[str] = None,
        ttl: list[int] = None,
        record_data_type: list[str] = None,
        ssl_enabled: list[bool] = None,
        enabled: list[bool] = None,
    ):
        """
        :param id: unique identifier of the target custom external DNS record.
        :param record_data: new custom data for the DNS record.
        :param name: name for DNS records (must be the same as one of the existing record).
        :param ttl: TTL (time to live) value for the DNS record.
        :param record_data_type: type of the DNS record data (currently, only the ‘TXT’ value is supported).
        :param ssl_enabled: defines whether the SSL is enabled for the record (true, by default) or not (false).
        :param enabled: defines whether the record is enabled (true, by default) or not (false).
        """
        return self._get(
            "EditSystemExternalDNSRecord",
            params={
                "id": id,
                "recordData": record_data,
                "name": name,
                "ttl": ttl,
                "recordDataType": record_data_type,
                "sslEnabled": ssl_enabled,
                "enabled": enabled,
            },
            delimiter=",",
        )

    def ExportEnv(self, target_app_id: str):
        return self._get(
            "ExportEnv",
            params={
                "targetAppId": target_app_id,
            },
        )

    def FixExtDns(self, uid: list[int] = None, target_app_id: list[str] = None):
        return self._get(
            "FixExtDns",
            params={
                "uid": uid,
                "targetAppId": target_app_id,
            },
            delimiter=",",
        )

    def FixLaunching(self):
        return self._get("FixLaunching", params={})

    def GenerateZone(
        self,
        generate_slept: bool,
    ):
        return self._get(
            "GenerateZone",
            params={
                "generateSlept": generate_slept,
            },
        )

    def GetAvgs(self):
        return self._get("GetAvgs", params={})

    def GetAvgs2(self):
        return self._get("GetAvgs2", params={})

    def GetBalancerStat(
        self,
        start_time: str,
        end_time: str,
    ):
        return self._get(
            "GetBalancerStat",
            params={
                "starttime": start_time,
                "endtime": end_time,
            },
        )

    def GetCloudletsUsage(self):
        return self._get("GetCloudletsUsage", params={})

    def GetDBCreationStat(
        self,
        start_time: str,
        end_time: str,
    ):
        return self._get(
            "GetDBCreationStat",
            params={
                "startTime": start_time,
                "endTime": end_time,
            },
        )

    def GetErrors(
        self,
        start_time: str,
        end_time: str,
        start_row: int,
        result_count: int,
        filter: list[int] = None,
    ):
        return self._get(
            "GerErrors",
            params={
                "starttime": start_time,
                "endtime": end_time,
                "startrow": start_row,
                "resultCount": result_count,
                "filter": filter,
            },
            delimiter=",",
        )

    def GetErrorsByDate(
        self,
        start_time: str,
        end_time: str,
        interval: int,
        filter: list[int] = None,
    ):
        return self._get(
            "GetErrorsByDate",
            params={
                "starttime": start_time,
                "endtime": end_time,
                "interval": interval,
                "filter": filter,
            },
            delimiter=",",
        )

    def GetSystemExternalDNSRecords(self):
        return self._get("GetSystemExternalDNSRecords", params={})

    def GetZone(self):
        return self._get("GetZone", params={})

    def ImportEnv(
        self,
        env_info: str,
        env_name: list[str] = None,
        enable_firewall: list[bool] = None,
    ):
        return self._get(
            "ImportEnv",
            params={
                "envInfo": env_info,
                "envName": env_name,
                "enableFirewall": enable_firewall,
            },
            delimiter=",",
        )

    def InspectEnvs(
        self,
        remove: list[bool] = None,
    ):
        return self._get(
            "InspectEnvs",
            params={
                "remove": remove,
            },
            delimiter=",",
        )

    def ManageService(self, node_id: int, command: str, service_name: str):
        return self._get(
            "ManageServices",
            params={
                "nodeid": node_id,
                "command": command,
                "servicename": service_name,
            },
        )

    def RemoveSystemExternalDNSRecord(self, id: int):
        return self._get(
            "RemoveSystemExternalDNSRecord",
            params={
                "id": id,
            },
        )

    def UpdateEnv(self, target_app_id: str):
        return self._get(
            "UpdateEnv",
            params={
                "targetAppId": target_app_id,
            },
        )

    def UpdateEnvInThread(self, target_app_id: str):
        return self._get(
            "UpdateEnvInThread",
            params={
                "targetAppId": target_app_id,
            },
        )

    def UpdateNodes(self):
        return self._get("UpdateNodes", params={})
