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
    def Update(self) -> "_Update":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.Update

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.Update
        """
        return _Update(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Monitoring(self) -> "_Monitoring":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.Monitoring

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.Monitoring
        """
        return _Monitoring(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Template(self) -> "_Template":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.Template

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.Template
        """
        return _Template(
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


class _Update(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Update
    """

    _endpoint2 = "update"

    def FixExtDns(
        self,
        uid: list[int] = None,
        target_app_id: list[str] = None,
    ):
        return self._get(
            "FixExtDns",
            params={
                "uid": uid,
                "targetAppIds": target_app_id,
            },
            delimiter=",",
        )

    def RestoreEnv(
        self,
        env_name: list[str] = None,
        uid: list[int] = None,
        region: list[str] = None,
    ):
        return self._get(
            "RestoreEnv",
            params={
                "envName": env_name,
                "uid": uid,
                "region": region,
            },
            delimiter=",",
        )

    def SyncInfraEnv(
        self,
        domain: list[str] = None,
        registry: list[str] = None,
    ):
        return self._get(
            "SyncInfraEnv",
            params={
                "domain": domain,
                "registry": registry,
            },
            delimiter=",",
        )


class _Monitoring(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Monitoring
    """

    _endpoint2 = "monitoring"

    def GetDockerPullStatus(self):
        """
        Returns cached result of the "docker pull" operation (cache lifetime = 600s). Pulled image is selected randomly from the list of published DOCKERIZED templates. This method is used for monitoring.
        """
        return self._get("GetDockerPullStatus", params={})

    def GetHostFirewallStatus(self):
        return self._get("GetHostFirewallStatus", params={})


class _Template(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Template
    """

    _endpoint2 = "template"

    def SetDefaultRegistry(
        self,
        id: list[int] = None,
    ):
        """
        :param id: identifier of the registry.
        """
        return self._get(
            "SetDefaultRegistry",
            params={
                "id": id,
            },
            delimiter=",",
        )

    def SetDistribution(
        self,
        node_types: str,
        distribution: list[str] = None,
    ):
        """
        :param node_type: templates where distribution should be set.
        :param distribution: zone configuration JSON string, example: {"mode":"STRICT","zones":"windows"}.
        """
        return self._get(
            "SetDistribution",
            params={"nodeTypes": node_types, "distribution": distribution},
            delimiter=",",
        )


class _HostGroup(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.HostGroup
    """

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
