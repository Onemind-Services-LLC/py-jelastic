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


class _Cluster(Administration):
    _endpoint2 = "cluster"

    def AddActionToIsolationQueue(
            self,
            count: list[int] = None,
            delay: list[int] = None
    ):
        return self._get(
            "AddActionToIsolationQueue",
            params={
                "count": count,
                "delay": delay,
            },
            delimiter=",",
        )

    def AddCartridge(
            self,
            manifest_url: str,
    ):
        return self._get(
            "AddCartridge",
            params={
                "manifestUrl": manifest_url
            },
        )

    def AddCertifiedTemplates(
            self,
            repositories: str,
            publish: list[bool] = None
    ):
        return self._get(
            "AddCertifiedTemplates",
            params={
                "repositories": repositories,
                "publish": publish
            },
            delimiter=",",
        )

    def AddExtIps(
            self,
            ipfrom: str,
            ipto: str,
            regions: str,
    ):
        return self._get(
            "AddExtIps",
            params={
                "ipfrom": ipfrom,
                "ipto": ipto,
                "regions": regions
            },
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
                "customData": custom_data
            },

        )

    def AddHdNode(
            self,
            hdnode: dict,
            set_as_docker_host: list[bool] = None,
            skip_configuration: list[bool] = None
    ):
        return self._get(
            "AddHdNode",
            params={
                "hdnode": hdnode,
                "setAsDockerHost": set_as_docker_host,
                "setAsDockerHost": skip_configuration,
            },
            delimiter=",",
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
            delimiter=",",
        )

    def AddIps(
            self,
            ipfrom: str,
            ipto: str,
            region: str,

    ):
        return self._get(
            "AddIps",
            params={
                "ipfrom": ipfrom,
                "ipto": ipto,
                "region": region
            },
        )

    def AddIpv6Network(
            self,
            region: str,
            network: list[str] = None,

    ):
        return self._get(
            "AddIpv6Network",
            params={
                "network": network,
                "region": region
            },
            delimiter=",",
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
            test_authentication: list[bool] = None,

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
            delimiter=",",
        )

    def AddRegionDomain(
            self,
            region_id: int,
            domain: str,
            primary: list[bool] = None,

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
            delimiter=",",
        )

    def AddRegionReseller(
            self,
            reseller_id: int,
            domain: str,
            type: str,
            generate_dns: bool,
            ssl_type: list[str] = None,
            region_id: list[int] = None,
            key: list[str] = None,
            intermediate: list[str] = None,
            cert: list[str] = None,
            source502: list[str] = None,

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
            delimiter=",",
        )

    def AddRegionSsl(
            self,
            region_id: int,
            ssl_type: str,
            domain_id: list[int] = None,
            cert_key: list[str] = None,
            intermediate: list[str] = None,
            cert: list[str] = None,

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
            delimiter=",",
        )

    def AddTemplate(
            self,
            registry_id: int,
            repository: str,
            tags: str,
            node_type: str,
            node_mission: str,
            display_name: str,
            engine_type: list[str] = None,
            images_data: list[str] = None,
            auto_update: list[bool] = None,
            keep_selected_tags: list[bool] = None,
            update_default_tag: list[bool] = None,
            skip_tags_from_auto_update: list[str] = None,

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
            delimiter=",",
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
            delimiter=",",
        )

    def AddUserToContainer(
            self,
            node_id: list[int] = None,
            container_id: list[int] = None,
            regenerate_keys: list[bool] = None,

    ):
        return self._get(
            "AddUserToContainer",
            params={
                "nodeId": node_id,
                "containerId": container_id,
                "regenerateKeys": regenerate_keys,
            },
            delimiter=",",
        )

    def AddUsersToGate(
            self,
    ):
        return self._get(
            "AddUsersToGate",
            params={
            },
        )

    def ApplyFirewallRules(
            self,
    ):
        return self._get(
            "ApplyFirewallRules",
            params={
            },
        )

    def CheckMigrationEnvPossibility(
            self,
            target_appid: list[str] = None,
            hardware_node_group: list[str] = None,
    ):
        return self._get(
            "CheckMigrationEnvPossibility",
            params={
                "targetAppid": target_appid,
                "hardwareNodeGroup": hardware_node_group,
            },
            delimiter=",",
        )

    def CleanTemplateManifestCache(
            self,
    ):
        return self._get(
            "CleanTemplateManifestCache",
            params={
            },
        )

    def ClearPool(
            self,
            hnid: list[int] = None,
    ):
        return self._get(
            "ClearPool",
            params={
                "hnid": hnid
            },
            delimiter=",",
        )

    def ConvertPasswords(
            self,
    ):
        return self._get(
            "ConvertPasswords",
            params={
            },
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
            uid: int,
            target_appid: str,
    ):
        """
            :param uid: unique identifier of the target user.
            :param target_appid: A semicolon-separated list of target environment IDs.
        """
        return self._get(
            "DeleteEnvsByChecksum",
            params={
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

    def DeleteHDNode(
            self,
            hdnodeid: int,
            force: list[bool] = None
    ):
        return self._get(
            "DeleteHDNode",
            params={
                "hdnodeid": hdnodeid,
                "force": force,
            },
            delimiter=",",
        )

    def EditHdNode(
            self,
            hdnode: dict,
            set_as_docker_host: list[bool] = None
    ):
        return self._get(
            "EditHdNode",
            params={
                "hdnode": hdnode,
                "set_as_docker_host": set_as_docker_host,
            },
            delimiter=",",
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
            delimiter=",",
        )

    def EditRegion(
            self,
            data: dict,
            test_authentication: list[bool] = None
    ):
        return self._get(
            "EditRegion",
            params={
                "data": data,
                "testAuthentication": test_authentication
            },
            delimiter=",",
        )

    def EditTemplate(
            self,
            node_type: str,
            tags: list[str] = None,
            display_name: list[str] = None,
            engine_type: list[str] = None,
            images_data: list[str] = None,
            auto_update: list[bool] = None,
            keep_selected_tags: list[bool] = None,
            update_default_tag: list[bool] = None,
            skip_tags_from_auto_update: list[str] = None,

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
            delimiter=",",
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
            possible_target_node_ids: list[str] = None,
            is_online: list[bool] = None,

    ):
        return self._get(
            "EvacuateContainers",
            params={
                "sourceHnId": source_hn_id,
                "possibleTargetNodeIds": possible_target_node_ids,
                "isOnline": is_online,
            },
            delimiter=",",
        )

    def ExecHnCMD(
            self,
            cmd: str,
            hn_id: list[int] = None,
            infra_only: list[bool] = None,
            run_on_broken: list[bool] = None,
            vz_version: list[str] = None,
            docker_host_only: list[bool] = None,

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
            delimiter=",",
        )

    def ExecHostCmd(
            self,
            cmd: str,
            host_id: list[int] = None,
            infra_only: list[bool] = None,
            run_on_broken: list[bool] = None,
            vz_version: list[str] = None,
            docker_host_only: list[bool] = None,

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
            delimiter=",",
        )

    def GeneratePool(
            self,
            node_type: list[str] = None,
            hnid: list[int] = None,

    ):
        return self._get(
            "GeneratePool",
            params={
                "nodeType": node_type,
                "hnId": hnid,
            },
            delimiter=",",
        )

    def GetAddHdNodeCmd(
            self,
            hard_node_group: list[str] = None,

    ):
        return self._get(
            "GetAddHdNodeCmd",
            params={
                "hardNodeGroup": hard_node_group,
            },
            delimiter=",",
        )

    def GetAddHostCmd(
            self,
            host_group: list[str] = None,

    ):
        return self._get(
            "GetAddHostCmd",
            params={
                "hostGroup": host_group,
            },
            delimiter=",",
        )

    def GetAllContainers(
            self,
    ):
        return self._get(
            "GetAllContainers",
            params={
            },
        )

    def GetAllRegionReseller(
            self,
    ):
        return self._get(
            "GetAllRegionReseller",
            params={
            },
        )

    def GetAllSumStatByUid(
            self,
            duration: list[int] = None,
            endtime: list[datetime] = None,
            uid: list[int] = None,

    ):
        return self._get(
            "GetAllSumStatByUid",
            params={
                "duration": duration,
                "endtime": endtime,
                "uid": uid,
            },
            delimiter=",",
        )

    def GetAppidByDomain(
            self,
            domain: list[str] = None,
    ):
        return self._get(
            "GetAppidByDomain",
            params={
                "domain": domain,
            },
            delimiter=",",
        )

    def GetBillableItems(
            self,
    ):
        return self._get(
            "GetBillableItems",
            params={
            },
        )

    def GetClusterLoadHistory(
            self,
            starttime: datetime,
            endtime: datetime
    ):
        return self._get(
            "GetClusterLoadHistory",
            params={
                "starttime": starttime,
                "endtime": endtime,
            },
        )

    def GetClusterLoadInfo(
            self,
    ):
        return self._get(
            "GetClusterLoadInfo",
            params={
            },
        )

    def GetClusterLoadPercent(
            self,
            checksum: str
    ):
        return self._get(
            "GetClusterLoadPercent",
            params={
                "checksum": checksum
            },
        )

    def GetClusterStatus(
            self,
            check_smtp: list[bool] = None,
            cached: list[bool] = None,
    ):
        return self._get(
            "GetClusterStatus",
            params={
                "checkSMTP": check_smtp,
                "cached": cached,
            },
            delimiter=",",
        )

    def GetClusterUsage(
            self,
    ):
        return self._get(
            "GetClusterUsage",
            params={
            },
        )

    def GetContainerConfig(
            self,
            node_id: int
    ):
        return self._get(
            "GetContainerConfig",
            params={
                "nodeId": node_id
            },
        )

    def GetDefaultRegion(
            self,
    ):
        return self._get(
            "GetDefaultRegion",
            params={
            },
        )

    def GetDefaultTagInfo(
            self,
            node_type: str,
            engine: list[str] = None
    ):
        return self._get(
            "GetDefaultTagInfo",
            params={
                "nodeType": node_type,
                "engine": engine
            },
            delimiter=",",
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
            params={
            },
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

    def GetEnvStat(
            self,
            starttime: datetime,
            endtime: datetime
    ):
        return self._get(
            "GetEnvStat",
            params={
                "starttime": starttime,
                "endtime": endtime,
            },
        )

    def GetEnvironmentGroupPopulations(
            self,
            start: datetime,
            end: datetime
    ):
        """
        rows ordered by time asc not more than 1000 rows

        :param start: slice start in date and time in ISO 8601
        :param end:slice end in date and time in ISO 8601
        """
        return self._get(
            "GetEnvironmentGroupPopulations",
            params={
                "start": start,
                "end": end
            },
        )

    def GetEnvs(
            self,
            uid: int,
            rights: list[str] = None,
            lazy: list[bool] = None,
            owner_uid: list[int] = None,
            ssh_access_only: list[bool] = None

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
            delimiter=",",
        )

    def GetHdNodeGroups(
            self,
    ):
        return self._get(
            "GetHdNodeGroups",
            params={
            },
        )

    def GetHdNodeStatus(
            self,
    ):
        return self._get(
            "GetHdNodeStatus",
            params={
            },
        )

    def GetHdNodes(
            self,
            ids: list[str] = None
    ):
        return self._get(
            "GetHdNodes",
            params={
                "ids": ids
            },
            delimiter=",",
        )

    def GetHdNodesLoad(
            self,
            duration: int,
            hdnodes: list[str] = None
    ):
        return self._get(
            "GetHdNodesLoad",
            params={
                "duration": duration,
                "hdnodes": hdnodes

            },
            delimiter=",",
        )

    def GetHdNodesLoadInfo(
            self,
            ids: list[str] = None
    ):
        return self._get(
            "GetHdNodesLoadInfo",
            params={
                "ids": ids
            },
            delimiter=",",
        )

    def GetHosts(
            self,
            ids: list[str] = None
    ):
        return self._get(
            "GetHosts",
            params={
                "ids": ids
            },
            delimiter=",",
        )

    def GetIpPoolInfo(
            self,
            search: dict,
    ):
        return self._get(
            "GetIpPoolInfo",
            params={
                "search": search,
            },
            delimiter=",",
        )

    def GetIpv6Networks(
            self,
    ):
        return self._get(
            "GetIpv6Networks",
            params={
            },
        )

    def GetIpv6SubnetsInfo(
            self,
            search: list[str] = None
    ):
        return self._get(
            "GetIpv6SubnetsInfo",
            params={
                "search": search,
            },
            delimiter=",",
        )

    def GetJelasticAppid(
            self,
    ):
        return self._get(
            "GetJelasticAppid",
            params={
            },
        )

    def GetJobNames(
            self,
    ):
        return self._get(
            "GetJobNames",
            params={
            },
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
            params={
            },
        )

    def GetNodePassword(
            self,
            nodeid: list[int] = None
    ):
        return self._get(
            "GetNodePassword",
            params={
                "nodeid": nodeid,
            },
            delimiter=",",
        )

    def GetNodes(
            self,
            hdnodeid: int,
            name: list[str] = None,
            start_row: list[int] = None,
            result_count: list[int] = None,
    ):
        return self._get(
            "GetNodes",
            params={
                "hdnodeid": hdnodeid,
                "name": name,
                "startRow": start_row,
                "resultCount": result_count,
            },
            delimiter=",",
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
            delimiter=",",
        )

    def GetPcsClusterList(
            self,
    ):
        return self._get(
            "GetPcsClusterList",
            params={
            },
        )

    def GetPoolStatus(
            self,
    ):
        return self._get(
            "GetPoolStatus",
            params={
            },
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

    def GetRegionDomains(
            self,
            region_id: list[int] = None
    ):
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
            params={
            },
        )

    def GetRepositoryTags(
            self,
            registry_id: list[int] = None,
            repository: list[str] = None,
    ):
        return self._get(
            "GetRepositoryTags",
            params={
                "registryId": registry_id,
                "repository": repository,
            },
            delimiter=",",
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
            params={
            },
        )

    def GetStats(
            self,
            duration: int,
            interval: int,
            target_appid: str,
            endtime: list[datetime] = None,
            nodeid: list[int] = None,
            nodetype: list[str] = None,
            node_group: list[str] = None,
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
            delimiter=",",
        )

    def GetSumStat(
            self,
            duration: list[int] = None,
            endtime: list[datetime] = None,
            target_appid: list[str] = None,
    ):
        return self._get(
            "GetSumStat",
            params={
                "duration": duration,
                "endtime": endtime,
                "targetAppid": target_appid,
            },
            delimiter=",",
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
            registry_id: list[int] = None,
            tag: list[str] = None,
    ):
        return self._get(
            "GetTemplateLabels",
            params={
                "repository": repository,
                "registryId": registry_id,
                "tag": tag,
            },
            delimiter=",",
        )

    def GetTemplateRegistries(
            self,
    ):
        return self._get(
            "GetTemplateRegistries",
            params={
            },
        )

    def GetTemplates(
            self,
            type: list[str] = None,
            published: list[bool] = None,
            lazy: list[bool] = None,
    ):
        return self._get(
            "GetTemplates",
            params={
                "type": type,
                "published": published,
                "lazy": lazy,
            },
            delimiter=",",
        )

    def GetUserActivity(
            self,
            uid: int,
            starttime: datetime,
            endtime: datetime,
            target_appid: list[str] = None,
            start_row: list[int] = None,
            result_count: list[int] = None,
            service_name: list[str] = None,
            search_text: list[str] = None,
            action_types: list[str] = None,
            order_field: list[str] = None,
            order_direction: list[str] = None,
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
            delimiter=",",
        )

    def GetUsersActivities(
            self,
            starttime: datetime,
            endtime: datetime,
            start_row: list[int] = None,
            result_count: list[int] = None,

    ):
        return self._get(
            "GetUsersActivities",
            params={
                "starttime": starttime,
                "endtime": endtime,
                "startRow": start_row,
                "resultCount": result_count,
            },
            delimiter=",",
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
            target_appid: list[str] = None,
            hardware_node_group: list[str] = None,
            is_online: list[bool] = None,

    ):
        return self._get(
            "MigrateEnv",
            params={
                "targetAppid": target_appid,
                "hardwareNodeGroup": hardware_node_group,
                "isOnline": is_online,
            },
            delimiter=",",
        )

    def MigrateNode(
            self,
            nodeid: int,
            hdnodeid: int,
            is_online: list[bool] = None,
            manage_dns_state: list[bool] = None,

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
            delimiter=",",
        )

    def RedeployContainers(
            self,
            target_env_name: str,
            tag: str,
            node_group: list[str] = None,
            node_id: list[int] = None,
            use_existing_volumes: list[bool] = None,
            login: list[str] = None,
            password: list[str] = None,
            skip_reinstall: list[bool] = None,
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
            delimiter=",",
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

    def RefreshUser(
            self,
            language: list[str] = None
    ):
        return self._get(
            "RefreshUser",
            params={
                "language": language,
            },
            delimiter=",",
        )

    def RegeneratePool(
            self,
            node_type: str,
            exclude: list[str] = None
    ):
        return self._get(
            "RegeneratePool",
            params={
                "nodeType": node_type,
                "exclude": exclude,
            },
            delimiter=",",
        )

    def RegisterInfaModule(
            self,
            module: list[str] = None,
            dst_env_name: list[str] = None,
            dry_run: list[bool] = None
    ):
        return self._get(
            "RegisterInfaModule",
            params={
                "module": module,
                "dstEnvName": dst_env_name,
                "dryRun": dry_run,
            },
            delimiter=",",
        )

    def RemoveExtIps(
            self,
            ips: list[str] = None,
    ):
        return self._get(
            "RemoveExtIps",
            params={
                "ips": ips,
            },
            delimiter=",",
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
            self,
            reseller_id: int,
            remove_dns: bool,
            region_id: list[int] = None
    ):
        return self._get(
            "RemoveRegionReseller",
            params={
                "resellerId": reseller_id,
                "dstEnvName": remove_dns,
                "regionId": region_id,
            },
            delimiter=",",
        )

    def RemoveRegionSsl(
            self,
            region_id: int,
            domain_id: list[int] = None,
            reseller_id: list[int] = None,
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
            delimiter=",",
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
            dst_env_name: list[str] = None,
            dst_node_id: list[int] = None,
            src_env_id: list[str] = None,
            src_hn_id: list[int] = None,
    ):
        return self._get(
            "ReplaceNodeInEnv",
            params={
                "dstEnvName": dst_env_name,
                "dstNodeId": dst_node_id,
                "srcEnvId": src_env_id,
                "srcHnId": src_hn_id,
            },
            delimiter=",",
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
            delimiter=",",
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
            delimiter=",",
        )

    def SetDefaultTemplateTag(
            self,
            node_type: str,
            tag: str
    ):
        return self._get(
            "SetDefaultTemplateTag",
            params={
                "nodeType": node_type,
                "tag": tag,
            },
        )

    def SetEnvNote(
            self,
            target_appid: list[str] = None,
            note: list[str] = None
    ):
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
            delimiter=",",
        )

    def SetEnvStatus(
            self,
            target_appid: str,
            status: int
    ):
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

    def SetEnvsStatus(
            self,
            target_appid: str,
            status: int
    ):
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

    def SetEnvsStatusByUid(
            self,
            uid: int,
            status: int
    ):
        return self._get(
            "SetEnvsStatusByUid",
            params={
                "uid": uid,
                "status": status,
            },
        )

    def SetEnvsStatusByUidByChecksum(
            self,
            uid: int,
            status: int
    ):
        return self._get(
            "SetEnvsStatusByUidByChecksum",
            params={
                "uid": uid,
                "status": status,
            },
        )

    def SetRegionDnsRecords(
            self,
            id: int,
            data: int
    ):
        return self._get(
            "SetRegionDnsRecords",
            params={
                "id": id,
                "data": data,
            },
        )

    def SetRegionPrimaryDomain(
            self,
            region_id: int,
            domain_id: int
    ):
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

    def SetStandbyMode(
            self,
            enabled: bool
    ):
        return self._get(
            "SetStandbyMode",
            params={
                "enabled": enabled,
            },
        )

    def SetTemplatePublished(
            self,
            node_type: str,
            published: bool
    ):
        return self._get(
            "SetTemplatePublished",
            params={
                "nodeType": node_type,
                "published": published
            },
        )

    def Sleep(
            self,
            starttime: list[datetime] = None,
            endtime: list[datetime] = None,
            deactivate_after: list[int] = None
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
            delimiter=",",
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
            params={
            },
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
            hard_node_id: str,
    ):
        return self._get(
            "StopEvacuation",
            params={
                "hardNodeId": hard_node_id,
            },
        )

    def SyncCloudlets(
            self,
            starttime: datetime,
            debug: list[bool] = None
    ):
        return self._get(
            "SyncCloudlets(",
            params={
                "starttime": starttime,
                "debug": debug,
            },
        )

    def SyncInfaModule(
            self,
            node_group: str,
            dst_env_name: str,
            components: str,
            target_tag: list[str] = None
    ):
        return self._get(
            "SyncInfaModule",
            params={
                "nodeGroup": node_group,
                "dstEnvName": dst_env_name,
                "components": components,
                "targetTag": target_tag,
            },
            delimiter=",",
        )

    def UpdateRegionSsl(
            self,
            region_id: int,
            domain_id: list[int] = None
    ):
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

    def UpdateResellerSsl(
            self,
            region_id: int,
            reseller_id: int
    ):
        return self._get(
            "UpdateResellerSsl",
            params={
                "regionId": region_id,
                "resellerId": reseller_id,
            },
        )

    def UpdateTemplate(
            self,
            node_type: int,
            icons_only: list[int] = None
    ):
        return self._get(
            "UpdateTemplate",
            params={
                "nodeType": node_type,
                "iconsOnly": icons_only,
            },
            delimiter=",",
        )

    def Validate(
            self,
    ):
        return self._get(
            "Validate",
            params={
            },
        )

    def ValidateAll(
            self,
    ):
        return self._get(
            "ValidateAll",
            params={
            },
        )

    def ValidateSsl(
            self,
            domain: str,
            key: list[str] = None,
            intermediate: list[str] = None,
            cert: list[str] = None
    ):
        return self._get(
            "ValidateSsl",
            params={
                "domain": domain,
                "key": key,
                "intermediate": intermediate,
                "cert": cert,
            },
            delimiter=",",
        )
