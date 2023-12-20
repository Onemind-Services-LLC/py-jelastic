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

    @property
    def Subscription(self) -> "_Subscription":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.Subscription

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.Subscription
        """
        return _Subscription(
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


class _Resource(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Resource
    """

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


class _Subscription(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Subscription
    """

    _endpoint2 = "subscription"

    def AddCategory(
        self,
        category: dict,
        reseller_id: list[int] = None,
    ):
        """
        :param category: JSON representation of an object (subscription Category) that should be created
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "AddCategory",
            params={
                "category": category,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def AddProduct(
        self,
        product: dict = None,
        reseller_id: list[int] = None,
    ):
        """
        :param category: JSON representation of an object (subscription Product) that should be created.
        :param product: unique identifier of the target reseller platform.
        """
        return self._get(
            "AddProduct",
            params={
                "product": product,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def AddServicePlan(
        self,
        service_plan: dict,
        reseller_id: list[int] = None,
        expand_fields: list[str] = None,
    ):
        """
        :param service_plan: JSON representation of an object (subscription Service Plan) that should be created.
        :param reseller_id: unique identifier of the target reseller platform.
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "AddServicePlan",
            params={
                "servicePlan": service_plan,
                "resellerId": reseller_id,
                "expandFields": expand_fields,
            },
            delimiter=",",
        )

    def AddSubscriptionItemResource(
        self,
        subscription_id: int,
        item_id: int,
        item_resource_id: int,
        resources: dict,
    ):
        """

        :param subscription_id: unique identifier of the target subscription.
        :param item_id: unique identifier of the target subscription item.
        :param item_resource_id: unique identifier of the target subscription item resource.
        :param resources: JSON representation of an object (subscription item resource) that should be created.
        """
        return self._get(
            "AddSubscriptionItemResource",
            params={
                "subscriptionId": subscription_id,
                "itemId": item_id,
                "itemResourceId": item_resource_id,
                "resources": resources,
            },
            delimiter=",",
        )

    def AdjustProduct(
        self,
        subscription_id: int,
        item_id: int,
        item_resource_id: int,
    ):
        """
        :param subscription_id: unique identifier of the target subscription.
        :param item_id: unique identifier of the target subscription item.
        :param item_resource_id: unique identifier of the target subscription item resource.
        """
        return self._get(
            "AdjustProduct",
            params={
                "subscriptionId": subscription_id,
                "itemId": item_id,
                "itemResourceId": item_resource_id,
            },
        )

    def DeleteCategory(
        self,
        id: int,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the target category.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "DeleteCategory",
            params={"id": id, "resellerId": reseller_id},
            delimiter=",",
        )

    def DeleteProduct(
        self,
        id: int,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the target product.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "DeleteProduct",
            params={"id": id, "resellerId": reseller_id},
            delimiter=",",
        )

    def DeleteServicePlan(
        self,
        id: int,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the target service plan.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "DeleteServicePlan",
            params={"id": id, "resellerId": reseller_id},
            delimiter=",",
        )

    def EditCategory(self, category: dict, reseller_id: list[int] = None):
        """
        :param category: JSON representation of an object (subscription Category) that should be created.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "EditCategory",
            params={
                "category": category,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def EditProduct(self, category: dict, reseller_id: list[int] = None):
        """
        :param category: JSON representation of an object (subscription Product) that should be created.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "EditProduct",
            params={
                "category": category,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def EditServicePlan(
        self,
        service_plan: dict,
        reseller_id: list[int] = None,
        expend_fields: list[str] = None,
    ):
        """
        :param service_plan: JSON representation of an object (subscription Service Plan) that should be created.
        :param reseller_id: unique identifier of the target reseller platform.
        :param expend_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "EditServicePlan",
            params={
                "servicePlan": service_plan,
                "resellerId": reseller_id,
                "expendFields": expend_fields,
            },
            delimiter=",",
        )

    def GetCategories(
        self,
        reseller_id: list[int] = None,
        expend_fields: list[str] = None,
    ):
        """
        :param reseller_id: unique identifier of the target reseller platform.
        :param expend_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "GetCategories",
            params={
                "resellerId": reseller_id,
                "expendFields": expend_fields,
            },
            delimiter=",",
        )

    def GetProducts(
        self,
        id: list[int] = None,
        status: list[str] = None,
        reseller_id: list[int] = None,
        subscription_status: list[str] = None,
        expend_fields: list[str] = None,
        start_row: list[int] = None,
        result_count: list[int] = None,
        order_field: list[str] = None,
        order_direction: list[str] = None,
    ):
        """
        :param id: unique identifier of the product (for filtering).
        :param status: a comma-separated list of the subscription Product statuses (ProductStatus) that should be returned.
        :param reseller_id: unique identifier of the target reseller platform.
        :param subscription_status: a comma-separated list of the subscription statuses (SubscriptionStatus) that should be returned.
        :param expend_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        :param start_row: returns information starting from the specified row in the response (starts with 0, by default).
        :param result_count: returns the specified number of rows from the response (0 – unlimited – by default).
        :param order_field: sorts results by the specified field
        :param order_direction: sorts results in the ascending (ASC) or descending (DESC) order
        """
        return self._get(
            "GetProduct",
            params={
                "id": id,
                "status": status,
                "resellerId": reseller_id,
                "subscriptionStatus": subscription_status,
                "expandFields": expend_fields,
                "startRow": start_row,
                "resultCount": result_count,
                "orderField": order_field,
                "orderDirection": order_direction,
            },
            delimiter=",",
        )

    def GetServicePlans(
        self,
        id: list[int] = None,
        has_products: list[bool] = None,
        subscription_status: list[str] = None,
        product_id: list[int] = None,
        expend_fields: list[str] = None,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the service plan (for filtering).
        :param has_products: a flag that indicates if returned Service Plans should have (true) or not (false) assigned products
        :param subscription_status: a comma-separated list of the subscription statuses (SubscriptionStatus) that should be returned.
        :param product_id: unique identifier of the subscription product (for filtering).
        :param expend_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "GetServicePlans",
            params={
                "id": id,
                "hasProducts": has_products,
                "subscriptionStatus": subscription_status,
                "productId": product_id,
                "expandFields": expend_fields,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def GetSubscriptions(
        self,
        id: list[int] = None,
        uid: list[int] = None,
        status: list[str] = None,
        reseller_id: list[int] = None,
        product_id: list[int] = None,
        service_plan_id: list[int] = None,
        expend_fields: list[str] = None,
        start_row: list[int] = None,
        result_count: list[int] = None,
        order_field: list[str] = None,
        order_direction: list[str] = None,
    ):
        """
        :param id: unique identifier of the subscription (for filtering).
        :param uid: unique identifier of the target user.
        :param status: a comma-separated list of the subscription statuses (SubscriptionStatus) that should be returned.
        :param reseller_id: unique identifier of the target reseller platform.
        :param product_id: unique identifier of the target product.
        :param service_plan_id: unique identifier of the target service plan.
        :param expend_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        :param start_row: returns information starting from the specified row in the response (starts with 0, by default).
        :param result_count: returns the specified number of rows from the response (0 – unlimited – by default).
        :param order_field: sorts results by the specified field
        :param order_direction: sorts results in the ascending (ASC) or descending (DESC) order
        """
        return self._get(
            "GetSubscriptions",
            params={
                "id": id,
                "uid": uid,
                "status": status,
                "resellerId": reseller_id,
                "productId": product_id,
                "servicePlanId": service_plan_id,
                "expandFields": expend_fields,
                "startRow": start_row,
                "resultCount": result_count,
                "orderField": order_field,
                "orderDirection": order_direction,
            },
            delimiter=",",
        )

    def SetCategoryPublished(
        self,
        id: int,
        published: bool,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the target category.
        :param published: publishes (true) or unpublishes (false) the subscription Category.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "SetCategoryPublished",
            params={
                "id": id,
                "published": published,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def SetProductStatus(
        self,
        id: int,
        status: str,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the target product.
        :param status: a new status (ProductStatus) that should be set for the subscription Product.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "SetProductStatus",
            params={
                "id": id,
                "status": status,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def SetServicePlanStatus(
        self,
        id: int,
        status: str,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the target service plan.
        :param status: a new status (ServicePlanStatus) that should be set for the subscription Service Plan.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "SetServicePlanStatus",
            params={
                "id": id,
                "status": status,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def TerminateSubscription(
        self,
        subscription_id: int,
        password: str,
    ):
        """
        :param subscription_id: unique identifier of the target subscription.
        :param password: current (admin) user's password to confirm subscription resources deletion.
        """
        return self._get(
            "TerminateSubscription",
            params={
                "subscriptionId": subscription_id,
                "password": password,
            },
        )
