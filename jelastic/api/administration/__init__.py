from datetime import date
from typing import Literal
from datetime import date, datetime
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
    def Cluster(self) -> "_Cluster":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.Cluster

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.Cluster
        """
        return _Cluster(
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

    @property
    def VirtualNetwork(self) -> "_VirtualNetwork":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.VirtualNetwork

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.VirtualNetwork
        """
        return _VirtualNetwork(
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


class _Cluster(Administration):
    _endpoint2 = "cluster"

    def AddActionToIsolationQueue(self, count: int = None, delay: int = None):
        return self._get(
            "AddActionToIsolationQueue",
            params={
                "count": count,
                "delay": delay,
            },
        )

    def AddCartridge(
        self,
        manifest_url: str,
    ):
        return self._get(
            "AddCartridge",
            params={"manifestUrl": manifest_url},
        )

    def AddCertifiedTemplates(self, repositories: str, publish: bool = None):
        return self._get(
            "AddCertifiedTemplates",
            params={"repositories": repositories, "publish": publish},
        )

    def AddExtIps(
        self,
        ipfrom: str,
        ipto: str,
        regions: str,
    ):
        return self._get(
            "AddExtIps",
            params={"ipfrom": ipfrom, "ipto": ipto, "regions": regions},
        )

    def AddHardWareNodeMessage(
        self,
        hn_id: int,
        message_type: str,
        process_response_code: int,
        percentage: int,
        message: str,
        custom_data: str,
    ):
        return self._get(
            "AddHardWareNodeMessage",
            params={
                "hnId": hn_id,
                "messageType": message_type,
                "processResponseCode": process_response_code,
                "percentage": percentage,
                "message": message,
                "customData": custom_data,
            },
        )

    def AddHdNode(
        self,
        hdnode: dict,
        set_as_docker_host: bool = None,
        skip_configuration: bool = None,
    ):
        return self._get(
            "AddHdNode",
            params={
                "hdnode": hdnode,
                "setAsDockerHost": set_as_docker_host,
                "skipConfiguration": skip_configuration,
            },
        )

    def AddHdNodeGroup(
        self,
        data: dict,
    ):
        return self._get(
            "AddHdNodeGroup",
            params={
                "data": data,
            },
        )

    def AddIps(
        self,
        ipfrom: str,
        ipto: str,
        region: str,
    ):
        return self._get(
            "AddIps",
            params={"ipfrom": ipfrom, "ipto": ipto, "region": region},
        )

    def AddIpv6Network(
        self,
        region: str,
        network: str = None,
    ):
        return self._get(
            "AddIpv6Network",
            params={"network": network, "region": region},
        )

    def AddNameserver(
        self,
        node_id: int,
        nameserver: str,
    ):
        return self._get(
            "AddNameserver",
            params={
                "nodeId": node_id,
                "nameserver": nameserver,
            },
        )

    def AddRegion(
        self,
        data: dict,
        test_authentication: bool = None,
    ):
        """
        :param data: JSON object with the new hardware region data.
        :param test_authentication: defines whether to check (true) or not (false) authentication on the region's Docker host.
        """
        return self._get(
            "AddRegion",
            params={
                "data": data,
                "testAuthentication": test_authentication,
            },
        )

    def AddRegionDomain(
        self,
        region_id: int,
        domain: str,
        primary: bool = None,
    ):
        """
        :param region_id: unique identifier of the target region.
        :param domain: new domain name to be added for the region.
        :param primary: defines whether to set the domain name as the region’s primary (true) or not (false).
        """
        return self._get(
            "AddRegionDomain",
            params={
                "regionId": region_id,
                "domain": domain,
                "primary": primary,
            },
        )

    def AddRegionReseller(
        self,
        reseller_id: int,
        domain: str,
        type: str,
        generate_dns: bool,
        ssl_type: str = None,
        region_id: int = None,
        key: str = None,
        intermediate: str = None,
        cert: str = None,
        source502: str = None,
    ):
        """
        :param reseller_id: unique identifier of the target reseller platform.
        :param domain: reseller platform domain name.
        :param type: region type (PLATFORM or REGION).
        :param generate_dns: defines whether to generate new DNS records (true) or just update existing SSL settings (false).
        :param ssl_type: SSL certificate type (CUSTOM or LETSENCRYPT).
        :param region_id: unique identifier of the existing region on the main platform.
        :param key: SSL certificate key.
        :param intermediate: intermediate SSL certificate.
        :param cert: SSL certificate body.
        :param source502: path to the 50x error pages source files.
        """
        return self._get(
            "AddRegionReseller",
            params={
                "resellerId": reseller_id,
                "domain": domain,
                "type": type,
                "generateDns": generate_dns,
                "sslType": ssl_type,
                "regionId": region_id,
                "key": key,
                "intermediate": intermediate,
                "cert": cert,
                "source502": source502,
            },
        )

    def AddRegionSsl(
        self,
        region_id: int,
        ssl_type: str,
        domain_id: int = None,
        cert_key: str = None,
        intermediate: str = None,
        cert: str = None,
    ):
        """
        :param region_id: unique identifier of the target region.
        :param ssl_type: SSL certificates type (CUSTOM - manually provided certificates; LETSENCRYPT - automatically issued Let's Encrypt certificates).
        :param domain_id: unique identifier of the target domain name.
        :param cert_key: server key certificate (for CUSTOM sslType only).
        :param intermediate: intermediate certificate CA (for CUSTOM sslType only).
        :param cert: domain certificate (for CUSTOM sslType only).
        """
        return self._get(
            "AddRegionSsl",
            params={
                "regionId": region_id,
                "sslType": ssl_type,
                "domainId": domain_id,
                "cert_key": cert_key,
                "intermediate": intermediate,
                "cert": cert,
            },
        )

    def AddTemplate(
        self,
        registry_id: int,
        repository: str,
        tags: str,
        node_type: str,
        node_mission: str,
        display_name: str,
        engine_type: str = None,
        images_data: str = None,
        auto_update: bool = None,
        keep_selected_tags: bool = None,
        update_default_tag: bool = None,
        skip_tags_from_auto_update: str = None,
    ):
        return self._get(
            "AddTemplate",
            params={
                "registryId": registry_id,
                "repository": repository,
                "tags": tags,
                "nodeType": node_type,
                "nodeMission": node_mission,
                "displayName": display_name,
                "engineType": engine_type,
                "imagesData": images_data,
                "autoUpdate": auto_update,
                "keepSelectedTags": keep_selected_tags,
                "updateDefaultTag": update_default_tag,
                "skipTagsFromAutoUpdate": skip_tags_from_auto_update,
            },
        )

    def AddTemplateRegistry(
        self,
        data: str,
    ):
        return self._get(
            "AddTemplateRegistry",
            params={
                "data": data,
            },
        )

    def AddUserToContainer(
        self,
        node_id: int = None,
        container_id: int = None,
        regenerate_keys: bool = None,
    ):
        return self._get(
            "AddUserToContainer",
            params={
                "nodeId": node_id,
                "containerId": container_id,
                "regenerateKeys": regenerate_keys,
            },
        )

    def AddUsersToGate(
        self,
    ):
        return self._get(
            "AddUsersToGate",
            params={},
        )

    def ApplyFirewallRules(
        self,
    ):
        return self._get(
            "ApplyFirewallRules",
            params={},
        )

    def CheckMigrationEnvPossibility(
        self,
        target_appid: str = None,
        hardware_node_group: str = None,
    ):
        return self._get(
            "CheckMigrationEnvPossibility",
            params={
                "targetAppid": target_appid,
                "hardwareNodeGroup": hardware_node_group,
            },
        )

    def CleanTemplateManifestCache(
        self,
    ):
        return self._get(
            "CleanTemplateManifestCache",
            params={},
        )

    def ClearPool(
        self,
        hnid: int = None,
    ):
        return self._get(
            "ClearPool",
            params={"hnid": hnid},
        )

    def ConvertPasswords(
        self,
    ):
        return self._get(
            "ConvertPasswords",
            params={},
        )

    def DeactivateRegionDomain(
        self,
        region_id: int,
        domain_id: int,
    ):
        return self._get(
            "DeactivateRegionDomain",
            params={
                "regionId": region_id,
                "domainId": domain_id,
            },
        )

    def DeleteEnv(
        self,
        target_appid: str,
        password: str,
    ):
        return self._get(
            "DeleteEnv",
            params={
                "targetAppid": target_appid,
                "password": password,
            },
        )

    def DeleteEnvsByChecksum(
        self,
        checksum: str,
        uid: int,
        target_appid: str,
    ):
        """
        :param checksum: checksum of the request.
        :param uid: unique identifier of the target user.
        :param target_appid: A semicolon-separated list of target environment IDs.
        """
        return self._get(
            "DeleteEnvsByChecksum",
            params={
                "checksum": checksum,
                "uid": uid,
                "targetAppid": target_appid,
            },
        )

    def DeleteEnvsByUidByChecksum(
        self,
        uid: int,
    ):
        """
        :param uid: unique identifier of the target user.
        """
        return self._get(
            "DeleteEnvsByUidByChecksum",
            params={
                "uid": uid,
            },
        )

    def DeleteHDNode(self, hdnodeid: int, force: bool = None):
        return self._get(
            "DeleteHDNode",
            params={
                "hdnodeid": hdnodeid,
                "force": force,
            },
        )

    def EditHdNode(self, hdnode: dict, set_as_docker_host: bool = None):
        return self._get(
            "EditHdNode",
            params={
                "hdnode": hdnode,
                "set_as_docker_host": set_as_docker_host,
            },
        )

    def EditHdNodeGroup(
        self,
        data: dict,
    ):
        return self._get(
            "EditHdNodeGroup",
            params={
                "data": data,
            },
        )

    def EditRegion(self, data: dict, test_authentication: bool = None):
        return self._get(
            "EditRegion",
            params={"data": data, "testAuthentication": test_authentication},
        )

    def EditTemplate(
        self,
        node_type: str,
        tags: str = None,
        display_name: str = None,
        engine_type: str = None,
        images_data: str = None,
        auto_update: bool = None,
        keep_selected_tags: bool = None,
        update_default_tag: bool = None,
        skip_tags_from_auto_update: str = None,
    ):
        return self._get(
            "EditTemplate",
            params={
                "nodeType": node_type,
                "tags": tags,
                "displayName": display_name,
                "engineType": engine_type,
                "imagesData": images_data,
                "autoUpdate": auto_update,
                "keepSelectedTags": keep_selected_tags,
                "updateDefaultTag": update_default_tag,
                "skipTagsFromAutoUpdate": skip_tags_from_auto_update,
            },
        )

    def EditTemplateRegistry(
        self,
        data: str,
    ):
        return self._get(
            "EditTemplateRegistry",
            params={
                "data": data,
            },
        )

    def EvacuateContainers(
        self,
        source_hn_id: str,
        possible_target_node_ids: str = None,
        is_online: bool = None,
    ):
        return self._get(
            "EvacuateContainers",
            params={
                "sourceHnId": source_hn_id,
                "possibleTargetNodeIds": possible_target_node_ids,
                "isOnline": is_online,
            },
        )

    def ExecHnCMD(
        self,
        cmd: str,
        hn_id: int = None,
        infra_only: bool = None,
        run_on_broken: bool = None,
        vz_version: str = None,
        docker_host_only: bool = None,
    ):
        return self._get(
            "ExecHnCMD",
            params={
                "cmd": cmd,
                "hnId": hn_id,
                "infraOnly": infra_only,
                "runOnBroken": run_on_broken,
                "vzVersion": vz_version,
                "dockerHostOnly": docker_host_only,
            },
        )

    def ExecHostCmd(
        self,
        cmd: str,
        host_id: int = None,
        infra_only: bool = None,
        run_on_broken: bool = None,
        vz_version: str = None,
        docker_host_only: bool = None,
    ):
        return self._get(
            "ExecHostCmd",
            params={
                "cmd": cmd,
                "hostId": host_id,
                "infraOnly": infra_only,
                "runOnBroken": run_on_broken,
                "vzVersion": vz_version,
                "dockerHostOnly": docker_host_only,
            },
        )

    def GeneratePool(
        self,
        node_type: str = None,
        hnid: int = None,
    ):
        return self._get(
            "GeneratePool",
            params={
                "nodeType": node_type,
                "hnId": hnid,
            },
        )

    def GetAddHdNodeCmd(
        self,
        hard_node_group: str = None,
    ):
        return self._get(
            "GetAddHdNodeCmd",
            params={
                "hardNodeGroup": hard_node_group,
            },
        )

    def GetAddHostCmd(
        self,
        host_group: str = None,
    ):
        return self._get(
            "GetAddHostCmd",
            params={
                "hostGroup": host_group,
            },
        )

    def GetAllContainers(
        self,
    ):
        return self._get(
            "GetAllContainers",
            params={},
        )

    def GetAllRegionReseller(
        self,
    ):
        return self._get(
            "GetAllRegionReseller",
            params={},
        )

    def GetAllSumStatByUid(
        self,
        duration: int = None,
        endtime: datetime = None,
        uid: int = None,
    ):
        return self._get(
            "GetAllSumStatByUid",
            params={
                "duration": duration,
                "endtime": endtime,
                "uid": uid,
            },
        )

    def GetAppidByDomain(
        self,
        domain: str = None,
    ):
        return self._get(
            "GetAppidByDomain",
            params={
                "domain": domain,
            },
        )

    def GetBillableItems(
        self,
    ):
        return self._get(
            "GetBillableItems",
            params={},
        )

    def GetClusterLoadHistory(self, starttime: datetime, endtime: datetime):
        return self._get(
            "GetClusterLoadHistory",
            params={
                "starttime": starttime,
                "endtime": endtime,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetClusterLoadInfo(
        self,
    ):
        return self._get(
            "GetClusterLoadInfo",
            params={},
        )

    def GetClusterLoadPercent(self, checksum: str):
        return self._get(
            "GetClusterLoadPercent",
            params={"checksum": checksum},
        )

    def GetClusterStatus(
        self,
        check_smtp: bool = None,
        cached: bool = None,
    ):
        return self._get(
            "GetClusterStatus",
            params={
                "checkSMTP": check_smtp,
                "cached": cached,
            },
        )

    def GetClusterUsage(
        self,
    ):
        return self._get(
            "GetClusterUsage",
            params={},
        )

    def GetContainerConfig(self, node_id: int):
        return self._get(
            "GetContainerConfig",
            params={"nodeId": node_id},
        )

    def GetDefaultRegion(
        self,
    ):
        return self._get(
            "GetDefaultRegion",
            params={},
        )

    def GetDefaultTagInfo(self, node_type: str, engine: str = None):
        return self._get(
            "GetDefaultTagInfo",
            params={"nodeType": node_type, "engine": engine},
        )

    def GetDomainByIp(
        self,
        ips: str,
    ):
        return self._get(
            "GetDomainByIp",
            params={
                "ips": ips,
            },
        )

    def GetEngineTypes(
        self,
    ):
        return self._get(
            "GetEngineTypes",
            params={},
        )

    def GetEnvGroupsByUid(
        self,
        uid: int,
    ):
        return self._get(
            "GetEnvGroupsByUid",
            params={
                "uid": uid,
            },
        )

    def GetEnvInfo(
        self,
        target_appid: str,
    ):
        return self._get(
            "GetEnvInfo",
            params={
                "targetAppid": target_appid,
            },
        )

    def GetEnvStat(self, starttime: datetime, endtime: datetime):
        return self._get(
            "GetEnvStat",
            params={
                "starttime": starttime,
                "endtime": endtime,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetEnvironmentGroupPopulations(self, start: datetime, end: datetime):
        """
        rows ordered by time asc not more than 1000 rows

        :param start: slice start in date and time in ISO 8601
        :param end: slice end in date and time in ISO 8601
        """
        return self._get(
            "GetEnvironmentGroupPopulations",
            params={"start": start, "end": end},
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetEnvs(
        self,
        uid: int,
        rights: list[str] = None,
        lazy: bool = None,
        owner_uid: int = None,
        ssh_access_only: bool = None,
    ):
        """
        A list of suitable environments.

        :param uid: unique identifier of the target user.
        :param rights: a comma-separated list of rights to filter environments. The filtering won't be applied if this parameter is not specified (all environments are displayed).
        :param lazy: enables/disables lazy (on-demand) loading.
        :param owner_uid: unique identifier of the target user account.
        :param ssh_access_only: filter to environments with SSH access.
        """
        return self._get(
            "GetEnvs",
            params={
                "uid": uid,
                "rights": rights,
                "lazy": lazy,
                "ownerUid": owner_uid,
                "sshAccessOnly": ssh_access_only,
            },
            delimiter=",",
        )

    def GetEvacuationState(
        self,
        hard_node_id: int,
    ):
        """
        EvacuationState entity or null
        """
        return self._get(
            "GetEvacuationState",
            params={
                "hardNodeId": hard_node_id,
            },
        )

    def GetExtIpPoolInfo(
        self,
        search: dict,
    ):
        return self._get(
            "GetExtIpPoolInfo",
            params={
                "search": search,
            },
        )

    def GetHdNodeGroups(
        self,
    ):
        return self._get(
            "GetHdNodeGroups",
            params={},
        )

    def GetHdNodeStatus(
        self,
    ):
        return self._get(
            "GetHdNodeStatus",
            params={},
        )

    def GetHdNodes(self, ids: str = None):
        return self._get(
            "GetHdNodes",
            params={"ids": ids},
        )

    def GetHdNodesLoad(self, duration: int, hdnodes: str = None):
        return self._get(
            "GetHdNodesLoad", params={"duration": duration, "hdnodes": hdnodes}
        )

    def GetHdNodesLoadInfo(self, ids: str = None):
        return self._get("GetHdNodesLoadInfo", params={"ids": ids})

    def GetHosts(self, ids: str = None):
        return self._get("GetHosts", params={"ids": ids})

    def GetIpPoolInfo(
        self,
        search: dict,
    ):
        return self._get(
            "GetIpPoolInfo",
            params={
                "search": search,
            },
        )

    def GetIpv6Networks(
        self,
    ):
        return self._get(
            "GetIpv6Networks",
            params={},
        )

    def GetIpv6SubnetsInfo(self, search: str = None):
        return self._get(
            "GetIpv6SubnetsInfo",
            params={
                "search": search,
            },
        )

    def GetJelasticAppid(
        self,
    ):
        return self._get(
            "GetJelasticAppid",
            params={},
        )

    def GetJobNames(
        self,
    ):
        return self._get(
            "GetJobNames",
            params={},
        )

    def GetLastHardWareNodeMessage(
        self,
        id: int,
    ):
        return self._get(
            "GetLastHardWareNodeMessage",
            params={
                "id": id,
            },
        )

    def GetNodeInfo(
        self,
        target_appid: str,
        node_id: int,
    ):
        """
        Result of operation or error.

        :param target_appid: appid of user environment
        :param node_id: id of SoftNode that belongs to env
        """
        return self._get(
            "GetNodeInfo",
            params={
                "targetAppid": target_appid,
                "nodeId": node_id,
            },
        )

    def GetNodeMissions(
        self,
    ):
        return self._get(
            "GetNodeMissions",
            params={},
        )

    def GetNodePassword(self, nodeid: int = None):
        return self._get(
            "GetNodePassword",
            params={
                "nodeid": nodeid,
            },
        )

    def GetNodes(
        self,
        hdnodeid: int,
        name: str = None,
        start_row: int = None,
        result_count: int = None,
    ):
        return self._get(
            "GetNodes",
            params={
                "hdnodeid": hdnodeid,
                "name": name,
                "startRow": start_row,
                "resultCount": result_count,
            },
        )

    def GetOOMKilledProcesses(
        self,
        search: dict,
    ):
        return self._get(
            "GetOOMKilledProcesses",
            params={
                "search": search,
            },
        )

    def GetPcsClusterList(
        self,
    ):
        return self._get(
            "GetPcsClusterList",
            params={},
        )

    def GetPoolStatus(
        self,
    ):
        return self._get(
            "GetPoolStatus",
            params={},
        )

    def GetRegion(
        self,
        id: int,
    ):
        return self._get(
            "GetRegion",
            params={
                "id": id,
            },
        )

    def GetRegionDnsRecords(
        self,
        id: int,
    ):
        return self._get(
            "GetRegionDnsRecords",
            params={
                "id": id,
            },
        )

    def GetRegionDomains(self, region_id: int = None):
        """
        param region_id: unique identifier of the target region.
        """
        return self._get(
            "GetRegionDomains",
            params={
                "regionId": region_id,
            },
            delimiter=",",
        )

    def GetRegionResellerByResellerId(
        self,
        id: int,
    ):
        return self._get(
            "GetRegionResellerByResellerId",
            params={
                "id": id,
            },
        )

    def GetRegions(
        self,
    ):
        return self._get(
            "GetRegions",
            params={},
        )

    def GetRepositoryTags(
        self,
        repository: str,
        registry_id: int = None,
    ):
        return self._get(
            "GetRepositoryTags",
            params={
                "repository": repository,
                "registryId": registry_id,
            },
        )

    def GetSoftNodeInfo(
        self,
        node_id: int,
    ):
        return self._get(
            "GetSoftNodeInfo",
            params={
                "nodeId": node_id,
            },
        )

    def GetStandByStatus(
        self,
    ):
        return self._get(
            "GetStandByStatus",
            params={},
        )

    def GetStats(
        self,
        duration: int,
        interval: int,
        target_appid: str,
        endtime: datetime = None,
        nodeid: int = None,
        nodetype: str = None,
        node_group: str = None,
    ):
        return self._get(
            "GetStats",
            params={
                "duration": duration,
                "interval": interval,
                "targetAppid": target_appid,
                "endtime": endtime,
                "nodeid": nodeid,
                "nodetype": nodetype,
                "nodeGroup": node_group,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetSumStat(
        self,
        duration: int = None,
        endtime: datetime = None,
        target_appid: str = None,
    ):
        return self._get(
            "GetSumStat",
            params={
                "duration": duration,
                "endtime": endtime,
                "targetAppid": target_appid,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetSystemLog(
        self,
        search: str,
    ):
        return self._get(
            "GetSystemLog",
            params={
                "search": search,
            },
        )

    def GetTemplateInfo(
        self,
        node_type: str,
    ):
        return self._get(
            "GetTemplateInfo",
            params={
                "nodeType": node_type,
            },
        )

    def GetTemplateLabels(
        self,
        repository: str,
        registry_id: int = None,
        tag: str = None,
    ):
        return self._get(
            "GetTemplateLabels",
            params={
                "repository": repository,
                "registryId": registry_id,
                "tag": tag,
            },
        )

    def GetTemplateRegistries(
        self,
    ):
        return self._get(
            "GetTemplateRegistries",
            params={},
        )

    def GetTemplates(
        self,
        type: str = None,
        published: bool = None,
        lazy: bool = None,
    ):
        return self._get(
            "GetTemplates",
            params={
                "type": type,
                "published": published,
                "lazy": lazy,
            },
        )

    def GetUserActivity(
        self,
        uid: int,
        starttime: datetime,
        endtime: datetime,
        target_appid: str = None,
        start_row: int = None,
        result_count: int = None,
        service_name: str = None,
        search_text: str = None,
        action_types: str = None,
        order_field: str = None,
        order_direction: str = None,
    ):
        """
        param: uid: unique identifier of the target user.
        param: starttime: a start time of a period for which user activity should be shown. In the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        param: endtime: an end time of a period for which user activity should be shown. In the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        param: target_appid: target environment name.
        param: start_row: returns information starting from the specified row in the response (starts with 0, by default).
        param: result_count: returns the specified number of rows from the response (0 – unlimited – by default).
        param: service_name: filters results by the specified service name.
        param: search_text: filters results by the provided string.
        param: action_types: filters results by the action type.
        params order_field: sorts results by the specified field.
        param: order_direction: sorts results in the ascending (ASC) or descending (DESC) order.
        """
        return self._get(
            "GetUserActivity",
            params={
                "uid": uid,
                "starttime": starttime,
                "endtime": endtime,
                "targetAppid": target_appid,
                "startRow": start_row,
                "resultCount": result_count,
                "serviceName": service_name,
                "searchText": search_text,
                "actionTypes": action_types,
                "orderField": order_field,
                "orderDirection": order_direction,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetUsersActivities(
        self,
        starttime: datetime,
        endtime: datetime,
        start_row: int = None,
        result_count: int = None,
    ):
        return self._get(
            "GetUsersActivities",
            params={
                "starttime": starttime,
                "endtime": endtime,
                "startRow": start_row,
                "resultCount": result_count,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def L2Update(
        self,
        hn_id: int,
    ):
        return self._get(
            "L2Update",
            params={
                "hnId": hn_id,
            },
        )

    def MigrateEnv(
        self,
        target_appid: str = None,
        hardware_node_group: str = None,
        is_online: bool = None,
    ):
        return self._get(
            "MigrateEnv",
            params={
                "targetAppid": target_appid,
                "hardwareNodeGroup": hardware_node_group,
                "isOnline": is_online,
            },
        )

    def MigrateNode(
        self,
        nodeid: int,
        hdnodeid: int,
        is_online: bool = None,
        manage_dns_state: bool = None,
    ):
        """
        param nodeid: unique identifier of the target node (container).
        param hdnodeid: unique identifier of the target host.
        param is_online: defines whether to perform online (true) or offline (false) migration.
        param manage_dns_state: defines whether to exclude a target node from DNS for the duration of the operation (true) or not (false, by default). This parameter only works with the sequential processes (isSequential=true) and is ignored otherwise. Enabling the parameter will bring additional delay (as the DNS records have TTL and cannot be disabled instantly), while disabling can cause some of the requests to be lost.
        """
        return self._get(
            "MigrateNode",
            params={
                "nodeid": nodeid,
                "hdnodeid": hdnodeid,
                "isOnline": is_online,
                "manageDNSState": manage_dns_state,
            },
        )

    def RedeployContainers(
        self,
        target_env_name: str,
        tag: str,
        node_group: str = None,
        node_id: int = None,
        use_existing_volumes: bool = None,
        login: str = None,
        password: str = None,
        skip_reinstall: bool = None,
    ):
        return self._get(
            "RedeployContainers",
            params={
                "targetEnvName": target_env_name,
                "tag": tag,
                "nodeGroup": node_group,
                "nodeId": node_id,
                "useExistingVolumes": use_existing_volumes,
                "login": login,
                "password": password,
                "skipReinstall": skip_reinstall,
            },
        )

    def RefreshEmailTemplates(
        self,
        modules: str,
    ):
        return self._get(
            "RefreshEmailTemplates",
            params={
                "modules": modules,
            },
        )

    def RefreshUser(self, language: str = None):
        return self._get(
            "RefreshUser",
            params={
                "language": language,
            },
        )

    def RegeneratePool(self, node_type: str, exclude: str = None):
        return self._get(
            "RegeneratePool",
            params={
                "nodeType": node_type,
                "exclude": exclude,
            },
        )

    def RegisterInfaModule(
        self,
        module: str = None,
        dst_env_name: str = None,
        dry_run: bool = None,
    ):
        return self._get(
            "RegisterInfaModule",
            params={
                "module": module,
                "dstEnvName": dst_env_name,
                "dryRun": dry_run,
            },
        )

    def RemoveExtIps(
        self,
        ips: str = None,
    ):
        return self._get(
            "RemoveExtIps",
            params={
                "ips": ips,
            },
        )

    def RemoveHdNodeGroup(
        self,
        id: int,
    ):
        return self._get(
            "RemoveHdNodeGroup",
            params={
                "id": id,
            },
        )

    def RemoveIpv6Network(
        self,
        id: int,
    ):
        return self._get(
            "RemoveIpv6Network",
            params={
                "id": id,
            },
        )

    def RemoveRegion(
        self,
        id: int,
    ):
        return self._get(
            "RemoveRegion",
            params={
                "id": id,
            },
        )

    def RemoveRegionReseller(
        self, reseller_id: int, remove_dns: bool, region_id: int = None
    ):
        return self._get(
            "RemoveRegionReseller",
            params={
                "resellerId": reseller_id,
                "dstEnvName": remove_dns,
                "regionId": region_id,
            },
        )

    def RemoveRegionSsl(
        self,
        region_id: int,
        domain_id: int = None,
        reseller_id: int = None,
    ):
        """
        param region_id: unique identifier of the target region.
        param domain_id: unique identifier of the target domain name.
        param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "RemoveRegionSsl",
            params={
                "regionId": region_id,
                "domainId": domain_id,
                "resellerId": reseller_id,
            },
        )

    def RemoveTemplate(
        self,
        node_type: str,
    ):
        return self._get(
            "RemoveTemplate",
            params={
                "nodeType": node_type,
            },
        )

    def RemoveTemplateRegistry(
        self,
        id: int,
    ):
        return self._get(
            "RemoveTemplateRegistry",
            params={
                "id": id,
            },
        )

    def ReplaceNodeInEnv(
        self,
        dst_env_name: str = None,
        dst_node_id: int = None,
        src_env_id: str = None,
        src_hn_id: int = None,
    ):
        return self._get(
            "ReplaceNodeInEnv",
            params={
                "dstEnvName": dst_env_name,
                "dstNodeId": dst_node_id,
                "srcEnvId": src_env_id,
                "srcHnId": src_hn_id,
            },
        )

    def ReviveInstallHdNode(
        self,
        id: int,
    ):
        return self._get(
            "ReviveInstallHdNode",
            params={
                "id": id,
            },
        )

    def SearchEnvs(
        self,
        search: dict,
    ):
        return self._get(
            "SearchEnvs",
            params={
                "search": search,
            },
        )

    def SearchNodes(
        self,
        search: dict,
    ):
        return self._get(
            "SearchNodes",
            params={
                "search": search,
            },
        )

    def SetDefaultTemplateTag(self, node_type: str, tag: str):
        return self._get(
            "SetDefaultTemplateTag",
            params={
                "nodeType": node_type,
                "tag": tag,
            },
        )

    def SetEnvNote(self, target_appid: str = None, note: str = None):
        """
        param target_appid: target environment name
        param note: custom note for the target environment
        """
        return self._get(
            "SetEnvNote",
            params={
                "targetAppid": target_appid,
                "note": note,
            },
        )

    def SetEnvStatus(self, target_appid: str, status: int):
        """
        param target_appid: appid of the required environment
        param status: new status for the specified environment whose appid equals to {@code targetAppid}.
        """
        return self._get(
            "SetEnvStatus",
            params={
                "targetAppid": target_appid,
                "status": status,
            },
        )

    def SetEnvsStatus(self, target_appid: str, status: int):
        """
        param target_appid: list of appids separated by commas
        param status: new status for each environment whose appid is in {@code targetAppids}.
        """
        return self._get(
            "SetEnvsStatus",
            params={
                "targetAppid": target_appid,
                "status": status,
            },
        )

    def SetEnvsStatusByUid(self, uid: int, status: int):
        return self._get(
            "SetEnvsStatusByUid",
            params={
                "uid": uid,
                "status": status,
            },
        )

    def SetEnvsStatusByUidByChecksum(self, uid: int, status: int):
        return self._get(
            "SetEnvsStatusByUidByChecksum",
            params={
                "uid": uid,
                "status": status,
            },
        )

    def SetRegionDnsRecords(self, id: int, data: int):
        return self._get(
            "SetRegionDnsRecords",
            params={
                "id": id,
                "data": data,
            },
        )

    def SetRegionPrimaryDomain(self, region_id: int, domain_id: int):
        """
        param region_id: unique identifier of the target region.
        param domain_id: unique identifier of the target domain name.
        """
        return self._get(
            "SetRegionPrimaryDomain",
            params={
                "regionId": region_id,
                "domainId": domain_id,
            },
        )

    def SetStandbyMode(self, enabled: bool):
        return self._get(
            "SetStandbyMode",
            params={
                "enabled": enabled,
            },
        )

    def SetTemplatePublished(self, node_type: str, published: bool):
        return self._get(
            "SetTemplatePublished",
            params={"nodeType": node_type, "published": published},
        )

    def Sleep(
        self,
        starttime: datetime = None,
        endtime: datetime = None,
        deactivate_after: int = None,
    ):
        """
        param starttime: start of the period (date and time in format yyyy-MM-dd HH:mm:ss, timezone GMT+0)
        param endtime: end of the period (date and time in format yyyy-MM-dd HH:mm:ss, timezone GMT+0)
        param deactivate_after: in milliseconds. deactivate only environment inactive more than this time. *
        """
        return self._get(
            "Sleep",
            params={
                "starttime": starttime,
                "endtime": endtime,
                "deactivateAfter": deactivate_after,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def StartEnv(
        self,
        target_appid: str,
    ):
        return self._get(
            "StartEnv(",
            params={
                "targetAppid": target_appid,
            },
        )

    def StopBalanceResources(
        self,
    ):
        return self._get(
            "StopBalanceResources(",
            params={},
        )

    def StopEnv(
        self,
        target_appid: str,
    ):
        return self._get(
            "StopEnv(",
            params={
                "targetAppid": target_appid,
            },
        )

    def StopEvacuation(
        self,
        hard_node_id: int,
    ):
        return self._get(
            "StopEvacuation",
            params={
                "hardNodeId": hard_node_id,
            },
        )

    def SyncCloudlets(self, starttime: datetime, debug: bool = None):
        return self._get(
            "SyncCloudlets(",
            params={
                "starttime": starttime,
                "debug": debug,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def SyncInfaModule(
        self,
        node_group: str,
        dst_env_name: str,
        components: str,
        target_tag: str = None,
    ):
        return self._get(
            "SyncInfaModule",
            params={
                "nodeGroup": node_group,
                "dstEnvName": dst_env_name,
                "components": components,
                "targetTag": target_tag,
            },
        )

    def UpdateRegionSsl(self, region_id: int, domain_id: int = None):
        """
        param region_id: unique identifier of the target region.
        param domain_id: unique identifier of the target domain name.
        """
        return self._get(
            "UpdateRegionSsl",
            params={
                "regionId": region_id,
                "domainId": domain_id,
            },
        )

    def UpdateResellerSsl(self, region_id: int, reseller_id: int):
        return self._get(
            "UpdateResellerSsl",
            params={
                "regionId": region_id,
                "resellerId": reseller_id,
            },
        )

    def UpdateTemplate(self, node_type: int, icons_only: bool = None):
        return self._get(
            "UpdateTemplate",
            params={
                "nodeType": node_type,
                "iconsOnly": icons_only,
            },
        )

    def Validate(
        self,
    ):
        return self._get(
            "Validate",
            params={},
        )

    def ValidateAll(
        self,
    ):
        return self._get(
            "ValidateAll",
            params={},
        )

    def ValidateSsl(
        self,
        domain: str,
        key: str = None,
        intermediate: str = None,
        cert: str = None,
    ):
        return self._get(
            "ValidateSsl",
            params={
                "domain": domain,
                "key": key,
                "intermediate": intermediate,
                "cert": cert,
            },
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
        value: str = None,
    ):
        return self._get(
            "ChangeConfigKey",
            params={
                "type": type,
                "key": key,
                "value": value,
            },
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
        reseller_id: int = None,
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
        start_date: date = None,
        end_date: date = None,
        env_name: str = None,
        node_id: int = None,
        note: str = None,
        value_group: str = None,
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
            datetime_format="%Y-%m-%d",
        )


class _Update(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Update
    """

    _endpoint2 = "update"

    def FixExtDns(
        self,
        uid: int = None,
        target_app_id: str = None,
    ):
        return self._get(
            "FixExtDns",
            params={
                "uid": uid,
                "targetAppIds": target_app_id,
            },
        )

    def RestoreEnv(
        self,
        env_name: str = None,
        uid: int = None,
        region: str = None,
    ):
        return self._get(
            "RestoreEnv",
            params={
                "envName": env_name,
                "uid": uid,
                "region": region,
            },
        )

    def SyncInfraEnv(
        self,
        domain: str = None,
        registry: str = None,
    ):
        return self._get(
            "SyncInfraEnv",
            params={
                "domain": domain,
                "registry": registry,
            },
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
        id: int = None,
    ):
        """
        :param id: identifier of the registry.
        """
        return self._get(
            "SetDefaultRegistry",
            params={
                "id": id,
            },
        )

    def SetDistribution(
        self,
        node_types: str,
        distribution: str = None,
    ):
        """
        :param node_type: templates where distribution should be set.
        :param distribution: zone configuration JSON string, example: {"mode":"STRICT","zones":"windows"}.
        """
        return self._get(
            "SetDistribution",
            params={"nodeTypes": node_types, "distribution": distribution},
        )


class _HostGroup(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.HostGroup
    """

    _endpoint2 = "hostgroup"

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
        port: int = None,
        check_external_ip: bool = None,
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
        )

    def GetHostFirewallSets(self):
        return self._get("GetHostFirewallSets", params={})

    def RemoveLabels(self, ids: str, labels: str):
        return self._get("RemoveLabels", params={"ids": ids, "labels": labels})

    def SetLabels(self, ids: str, labels: str):
        return self._get("SetLabels", params={"ids": ids, "labels": labels})

    def UpdateHostFirewall(
        self,
        host_id: int = None,
        force: bool = None,
        check_external_ip: bool = None,
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
        )


class _Utils(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Utils
    """

    _endpoint2 = "utils"

    def AddSystemExternalDNSRecord(
        self,
        record_data: str,
        name: str,
        ttl: int,
        record_data_type: str,
        ssl_enabled: bool = None,
        enabled: bool = None,
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
        target_app_ids: str = None,
    ):
        return self._get(
            "DeleteBrokenEnvs",
            params={
                "targetAppIds": target_app_ids,
            },
        )

    def EditSystemExternalDNSRecord(
        self,
        id: int,
        record_data: str = None,
        name: str = None,
        ttl: int = None,
        record_data_type: str = None,
        ssl_enabled: bool = None,
        enabled: bool = None,
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
        )

    def ExportEnv(self, target_app_id: str):
        return self._get(
            "ExportEnv",
            params={
                "targetAppId": target_app_id,
            },
        )

    def FixExtDns(self, uid: int = None, target_app_id: str = None):
        return self._get(
            "FixExtDns",
            params={
                "uid": uid,
                "targetAppId": target_app_id,
            },
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
        start_time: datetime,
        end_time: datetime,
    ):
        return self._get(
            "GetBalancerStat",
            params={
                "starttime": start_time,
                "endtime": end_time,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetCloudletsUsage(self):
        return self._get("GetCloudletsUsage", params={})

    def GetDBCreationStat(
        self,
        start_time: datetime,
        end_time: datetime,
    ):
        return self._get(
            "GetDBCreationStat",
            params={
                "startTime": start_time,
                "endTime": end_time,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetErrors(
        self,
        start_time: datetime,
        end_time: datetime,
        start_row: int,
        result_count: int,
        filter: int = None,
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
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetErrorsByDate(
        self,
        start_time: datetime,
        end_time: datetime,
        interval: int,
        filter: int = None,
    ):
        return self._get(
            "GetErrorsByDate",
            params={
                "starttime": start_time,
                "endtime": end_time,
                "interval": interval,
                "filter": filter,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetSystemExternalDNSRecords(self):
        return self._get("GetSystemExternalDNSRecords", params={})

    def GetZone(self):
        return self._get("GetZone", params={})

    def ImportEnv(
        self,
        env_info: str,
        env_name: str = None,
        enable_firewall: bool = None,
    ):
        return self._get(
            "ImportEnv",
            params={
                "envInfo": env_info,
                "envName": env_name,
                "enableFirewall": enable_firewall,
            },
        )

    def InspectEnvs(
        self,
        remove: bool = None,
    ):
        return self._get(
            "InspectEnvs",
            params={
                "remove": remove,
            },
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
        reseller_id: int = None,
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
        )

    def AddProduct(
        self,
        product: dict = None,
        reseller_id: int = None,
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
        )

    def AddServicePlan(
        self,
        service_plan: dict,
        reseller_id: int = None,
        expand_fields: str = None,
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
        reseller_id: int = None,
    ):
        """
        :param id: unique identifier of the target category.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get("DeleteCategory", params={"id": id, "resellerId": reseller_id})

    def DeleteProduct(
        self,
        id: int,
        reseller_id: int = None,
    ):
        """
        :param id: unique identifier of the target product.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get("DeleteProduct", params={"id": id, "resellerId": reseller_id})

    def DeleteServicePlan(
        self,
        id: int,
        reseller_id: int = None,
    ):
        """
        :param id: unique identifier of the target service plan.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "DeleteServicePlan", params={"id": id, "resellerId": reseller_id}
        )

    def EditCategory(self, category: dict, reseller_id: int = None):
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
        )

    def EditProduct(self, category: dict, reseller_id: int = None):
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
        )

    def EditServicePlan(
        self,
        service_plan: dict,
        reseller_id: int = None,
        expend_fields: str = None,
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
        )

    def GetCategories(
        self,
        reseller_id: int = None,
        expend_fields: str = None,
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
        )

    def GetProducts(
        self,
        id: int = None,
        status: list[str] = None,
        reseller_id: int = None,
        subscription_status: list[str] = None,
        expend_fields: str = None,
        start_row: int = None,
        result_count: int = None,
        order_field: str = None,
        order_direction: str = None,
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
        id: int = None,
        has_products: bool = None,
        subscription_status: list[str] = None,
        product_id: int = None,
        expend_fields: str = None,
        reseller_id: int = None,
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
        id: int = None,
        uid: int = None,
        status: list[str] = None,
        reseller_id: int = None,
        product_id: int = None,
        service_plan_id: int = None,
        expend_fields: str = None,
        start_row: int = None,
        result_count: int = None,
        order_field: str = None,
        order_direction: str = None,
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
        reseller_id: int = None,
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
        )

    def SetProductStatus(
        self,
        id: int,
        status: str,
        reseller_id: int = None,
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
        )

    def SetServicePlanStatus(
        self,
        id: int,
        status: str,
        reseller_id: int = None,
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


class _VirtualNetwork(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.VirtualNetwork
    """

    _endpoint2 = "virtualnetwork"

    def AddVirtualNetwork(
        self,
        virtual_network: dict,
    ):
        """
        :param virtual_network: a list of the target virtual networks' unique identifiers.
        """
        return self._get(
            "AddVirtualNetwork",
            params={"virtualNetwork": virtual_network},
        )

    def ApplyVirtualNetworks(
        self,
        host_id: int = None,
    ):
        """
        :param host_id: unique identifier of the target host (all hosts if not defined).
        """
        return self._get(
            "ApplyVirtualNetworks",
            params={
                "hostId": host_id,
            },
        )

    def DeleteVirtualNetworks(
        self,
        ids: int = None,
    ):
        """
        :param ids: a list of the target virtual networks' unique identifiers.
        """
        return self._get(
            "DeleteVirtualNetworks",
            params={
                "ids": ids,
            },
        )

    def GetVirtualNetworks(
        self,
        ids: int = None,
    ):
        """
        :param ids: a list of the target virtual networks' unique identifiers.
        """
        return self._get(
            "GetVirtualNetworks",
            params={
                "ids": ids,
            },
        )
