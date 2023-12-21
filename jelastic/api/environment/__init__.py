import json
from datetime import date, datetime
from typing import Literal

from ..abstract import ClientAbstract

__all__ = ["Environment"]

EVENT_TYPE = Literal["SEND_NOTIFICATION", "OOM_KILLER", "CUSTOM_NODE_EVENT"]


class Environment(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.environment

    Ref: https://docs.jelastic.com/api/#!/environment
    """

    _endpoint1 = "environment"

    @property
    def Billing(self) -> "_Billing":
        """
        Service provides information about consumed resources by OS nodes of the platform environments or consumed
        resources that grouped by account.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.Billing

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.Billing
        """
        return _Billing(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Export(self) -> "_Export":
        """
        This service provides API methods for exporting environments on the accounts as downloadable manifests for
        future imports. Learn more in the documentation.


        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.Export

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.Export
        """
        return _Export(session=self._session, token=self._token, debug=self._debug)

    @property
    def JError(self) -> "_JError":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.JError

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.JError
        """
        return _JError(session=self._session, token=self._token, debug=self._debug)

    @property
    def Node(self) -> "_Node":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.Node

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.Node
        """
        return _Node(session=self._session, token=self._token, debug=self._debug)

    @property
    def Binder(self) -> "_Binder":
        """
         With the platform, you can set your own external domain name for your projects instead of using the default hosting provider domain name. Binding can be done in two ways: by adding a CNAME record or by setting A Records.
         A CNAME specifies an alias for a canonical name record in a Domain Name System (DNS) database. If you don't have your own Public IP, your URL is an alias for a single canonical name that is associated with a common platform IP address in the DNS database. In this case, it's recommended to set your own custom domain by adding a CNAME record.
         A Record is an entry in your DNS zone file that maps each domain name to an IP address. When you type www.mycustomsite.com, the browser goes to the nameserver for mycustomsite.com and asks for the A Record. This record must point to an IP address - it will be the IP address of your web server. Setting your own custom external domain name using A Record is more appropriate if you have a personal Public IP address.
        Also, you can bind Custom SSL to your custom domain.

         >>> from jelastic import Jelastic
         >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
         >>> jelastic.environment.Binder

         Ref: https://docs.jelastic.com/api/private/#!/api/environment.Binder
        """
        return _Binder(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def File(self) -> "_File":
        """
        The File Manager API service gives you access to the container’s home directory and your environment's configuration files. You can read, write, create, delete, and adjust your application files and settings.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.File

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.File
        """
        return _File(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Billing(Environment):
    """
    Service provides information about consumed resources by OS nodes of the platform environments or consumed
    resources that grouped by account.

    Ref: https://docs.jelastic.com/api/private/#!/api/environment.Billing
    """

    _endpoint2 = "billing"

    def AddStats(
        self,
        resource_name: str,
        uid: int,
        start_date: date,
        end_date: date,
        env_name: str,
        node_id: int,
        value: float,
        note: str = None,
        value_group: str = None,
    ):
        return self._get(
            "AddStats",
            params={
                "resourceName": resource_name,
                "uid": uid,
                "startDate": start_date,
                "endDate": end_date,
                "envName": env_name,
                "nodeId": node_id,
                "value": value,
                "note": note,
                "valueGroup": value_group,
            },
            datetime_format="%Y-%m-%d",
        )

    def EnvResources(self, start_time: datetime, end_time: datetime):
        """
        Calculate resources usage of one environment for the given period.
        """
        return self._get(
            "EnvResources",
            params={
                "starttime": start_time,
                "endtime": end_time,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def EnvsResources(
        self,
        start_time: datetime,
        end_time: datetime,
        target_app_id: str,
        checksum: str,
    ):
        """
        Calculate environments resources for the given period.

        The method is protected by checksum validation. the checksum is calculated as MD5 function from a string of
        concatenation appid, starttime, endtime, targetAppid and privateApiKey. Checksum is compared with result MD5
        function.
        """
        return self._get(
            "EnvsResources",
            params={
                "starttime": start_time,
                "endtime": end_time,
                "targetAppid": target_app_id,
                "checksum": checksum,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def EnvsResourcesByAccount(
        self, start_time: datetime, end_time: datetime, uid: int, checksum: str
    ):
        """
        Calculate environments resources for the given period.
        """
        return self._get(
            "EnvsResourcesByAccount",
            params={
                "starttime": start_time,
                "endtime": end_time,
                "uid": uid,
                "checksum": checksum,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetOptions(self, target_env_name: str, node_group: str):
        """
        Gets billing options for nodeGroup.
        """
        return self._get(
            "GetOptions",
            params={
                "targetEnvName": target_env_name,
                "nodeGroup": node_group,
            },
        )

    def SetOptions(
        self, target_env_name: str, node_group: str, options: dict, node_id: int = None
    ):
        """
        Sets billing options for the node group (layer) to help the platform identify installed license types.

        :param target_env_name: target environment name with the required node group (layer).
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application
            server layer.
        :param options: JSON object with the required billing options.
        :param node_id: unique identifier of the node that will be used to identify the target node group
            (overrides the nodeGroup parameter if both are specified).
        """
        options = json.dumps(options)
        return self._get(
            "SetOptions",
            params={
                "targetEnvName": target_env_name,
                "nodeGroup": node_group,
                "options": options,
                "nodeId": node_id,
            },
        )


class _Export(Environment):
    """
    This service provides API methods for exporting environments on the accounts as downloadable manifests for future
    imports. Learn more in the documentation.

    Ref: https://docs.jelastic.com/api/private/#!/api/environment.Export
    """

    _endpoint2 = "export"

    def Create(self, settings: dict):
        """
        Creates a manifest file based on the existing environment (a JSON file with the topology and other settings)
        and stores it within the corresponding environment.

        :param settings: JSON object with export settings: {"config": true, "data": true}
        """
        return self._get(
            "Create",
            params={
                "settings": json.dumps(settings),
            },
        )

    def Delete(self, id: str):
        """
        Deletes a manifest file from the corresponding environment.

        :param id: unique identifier of the manifest file.
        """
        return self._get(
            "Delete",
            params={
                "id": id,
            },
        )

    def DeleteExportedData(self, env_name: str, file_name: str):
        """
        Deletes the exported data.

        :param env_name: target environment name.
        :param file_name: filename to be removed.
        """
        return self._get(
            "DeleteExportedData", params={"envName": env_name, "fileName": file_name}
        )

    def GetList(self, env_name: str):
        """
        Returns a list of all the exported copies of the environment.

        :param env_name: target environment name.
        """
        return self._get("GetList", params={"envName": env_name})

    def GetManifest(self, env_name: str, id: str):
        """
        Returns a manifest file of the exported environment.

        :param env_name: target environment name.
        :param id: Unique identifier of the exported environment manifest.
        """
        return self._get("GetManifest", params={"envName": env_name, "id": id})


class _JError(Environment):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/environment.JError
    """

    _endpoint2 = "jerror"

    def Error(
        self,
        action_name: str,
        call_parameters: str,
        error_code: int,
        priority: int,
        email: str = None,
        error_message: str = None,
    ):
        return self._get(
            "Error",
            params={
                "actionName": action_name,
                "callParameters": call_parameters,
                "errorCode": error_code,
                "priority": priority,
                "email": email,
                "errorMessage": error_message,
            },
        )


class _Node(Environment):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/environment.Node
    """

    def SendEvent(self, params: dict, event_name: EVENT_TYPE):
        """
        Sends a predefined event using IP authorization.

        :param params: JSON object with parameters for Cloud Scripting
        :param event_name: the name of the required event;
        """
        params = json.dumps(params)
        return self._get(
            "SendEvent", params={"params": params, "eventName": event_name}
        )

    def SendNotification(self, message: str, name: str = None):
        """
        Sends an email notification to the node owner using IP authorization.

        :param message: body of the message
        :param name: title of the message
        """
        return self._get("SendNotification", params={"name": name, "message": message})


class _Binder(Environment):
    """
    With the platform, you can set your own external domain name for your projects instead of using the default hosting provider domain name. Binding can be done in two ways: by adding a CNAME record or by setting A Records.

     A CNAME specifies an alias for a canonical name record in a Domain Name System (DNS) database. If you don't have your own Public IP, your URL is an alias for a single canonical name that is associated with a common platform IP address in the DNS database. In this case, it's recommended to set your own custom domain by adding a CNAME record.

     A Record is an entry in your DNS zone file that maps each domain name to an IP address. When you type www.mycustomsite.com, the browser goes to the nameserver for mycustomsite.com and asks for the A Record. This record must point to an IP address - it will be the IP address of your web server. Setting your own custom external domain name using A Record is more appropriate if you have a personal Public IP address.

     Also, you can bind Custom SSL to your custom domain.

     Ref: https://docs.jelastic.com/api/private/#!/api/environment.Binder
    """

    _endpoint2 = "Binder"

    def AddDomains(
        self,
        env_name: str,
        domains: str,
        node_group: list[str] = None,
        node_id: list[int] = None,
        subdomain: list[str] = None,
    ):
        """
        param domains: a comma- or semicolon-separated list of domains (e.g. domain1,domain2 or domain1;domain2).
        param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        param node_id: unique identifier of the target node (container).
        param subdomain: defines whether the layer/node subdomain should be attached via "-" (false) or "." (true, by default).
        """
        return self._get(
            "AddDomains",
            params={
                "envName": env_name,
                "domains": domains,
                "nodeGroup": node_group,
                "nodeId": node_id,
                "subdomain": subdomain,
            },
            delimiter=",",
        )

    def AddSSLCert(
        self,
        env_name: str,
        key: str,
        cert: str,
        interm: list[str] = None,
    ):
        """
        param key: private key (can be either key body or link to download it).
        param cert: domain certificate (can be either certificate body or link to download it).
        param interm: intermediate certificate (CA) (can be either intermediate body or link to download it).
        """
        return self._get(
            "AddSSLCert",
            params={
                "envName": env_name,
                "key": key,
                "cert": cert,
                "interm": interm,
            },
            delimiter=",",
        )

    def AttachExtIp(
        self,
        env_name: str,
        nodeid: int,
        type: list[str] = None,
    ):
        return self._get(
            "AttachExtIp",
            params={
                "envName": env_name,
                "nodeid": nodeid,
                "type": type,
            },
            delimiter=",",
        )

    def BindExtDomain(
        self,
        env_name: str,
        extdomain: str,
        cert_id: list[int] = None,
    ):
        return self._get(
            "BindExtDomain",
            params={
                "envName": env_name,
                "extdomain": extdomain,
                "certId": cert_id,
            },
            delimiter=",",
        )

    def BindExtDomains(
        self,
        env_name: str,
        extdomains: str,
        cert_id: list[int] = None,
    ):
        """
        param extdomain: a comma-separated list of external domains to be bound to the environment.
        param cert_id: unique identifier of the SSL certificate.
        """
        return self._get(
            "BindExtDomains",
            params={
                "envName": env_name,
                "extdomains": extdomains,
                "certId": cert_id,
            },
            delimiter=",",
        )

    def BindSSL(
        self,
        env_name: str,
        cert_key: str,
        cert: str,
        intermediate: str,
    ):
        return self._get(
            "BindSSL",
            params={
                "envName": env_name,
                "cert_key": cert_key,
                "cert": cert,
                "intermediate": intermediate,
            },
        )

    def BindSSLCert(
        self,
        env_name: str,
        cert_id: int,
        entry_point: list[str] = None,
        ext_domains: list[str] = None,
    ):
        """
        param cert_id: unique identifier of the SSL certificate.
        param entry_point: entry point can be either "ENV" (for all environments domains, by default) or "SLB" (for environment domains specified in the extDomains parameter).
        param ext_domains: a comma-separated list of external domains to be bound with the SSL certificate.
        """
        return self._get(
            "BindSSLCert",
            params={
                "envName": env_name,
                "certId": cert_id,
                "entryPoint": entry_point,
                "extDomains": ext_domains,
            },
            delimiter=",",
        )

    def CheckDomain(
        self,
        env_name: str,
        domain: str,
        region: list[str] = None,
    ):
        """
        param domain: domain name to be checked.
        param region: unique name of a region to be checked.
        """
        return self._get(
            "CheckDomain",
            params={
                "envName": env_name,
                "domain": domain,
                "region": region,
            },
            delimiter=",",
        )

    def CheckExtDomain(
        self,
        env_name: str,
        extdomains: str,
    ):
        """
        param extdomains: external domain name to be checked.
        """
        return self._get(
            "CheckExtDomain",
            params={
                "envName": env_name,
                "extdomains": extdomains,
            },
        )

    def DeleteSSL(
        self,
        env_name: str,
    ):
        return self._get(
            "DeleteSSL",
            params={"envName": env_name},
        )

    def DetachExtIp(
        self,
        env_name: str,
        nodeid: int,
        ip: str,
    ):
        """
        param nodeid: unique identifier of the target node (container).
        param ip: IP address that should be removed from the node.
        """
        return self._get(
            "DetachExtIp",
            params={
                "envName": env_name,
                "nodeid": nodeid,
                "ip": ip,
            },
        )

    def DisableSSL(
        self,
        env_name: str,
    ):
        return self._get(
            "DisableSSL",
            params={
                "envName": env_name,
            },
        )

    def EditSSLCert(
        self,
        env_name: str,
        id: int,
        key: list[str] = None,
        cert: list[str] = None,
        interm: list[str] = None,
    ):
        """
        param id: unique identifier of the target SSL certificate.
        param key: private key (can be either key body or link to download it).
        param cert: domain certificate (can be either certificate body or link to download it).
        param interm: intermediate certificate (CA) (can be intermediate body or link to download it); if set to "*", "null", or "none", the intermediate certificate will be removed from the platform database.
        """
        return self._get(
            "EditSSLCert",
            params={
                "envName": env_name,
                "id": id,
                "key": key,
                "cert": cert,
                "interm": interm,
            },
            delimiter=",",
        )

    def GetDomainInfo(
        self,
        env_name: str,
        domain: str,
    ):
        """
        Returns environment appid if environment found by domain.

        param domain: domain of the environment for search
        """
        return self._get(
            "GetDomainInfo",
            params={
                "envName": env_name,
                "domain": domain,
            },
        )

    def GetDomains(
        self,
        env_name: str,
        node_group: list[str] = None,
        node_id: list[int] = None,
        in_short: list[bool] = None,
    ):
        """
        param node_group: unique identifier of the target node group (layer) for filtering, e.g. "cp" for the default application server layer.
        param node_id: unique identifier of the target node (container) for filtering. It has priority over the nodeGroup parameter.
        param in_short: defines whether domains should be presented in the short (true, by default) or extended (false) form.
        """
        return self._get(
            "GetDomains",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "nodeId": node_id,
                "inShort": in_short,
            },
            delimiter=",",
        )

    def GetExtDomains(self, env_name: str):
        return self._get("GetExtDomains", params={"envName": env_name})

    def GetSSL(self, env_name: str):
        return self._get("GetSSL", params={"envName": env_name})

    def GetSSLCerts(self, env_name: str, ids: list[str] = None):
        return self._get(
            "GetSSLCerts",
            params={"envName": env_name, "ids": ids},
            delimiter=",",
        )

    def ManageNodeDnsState(
        self, env_name: str, node_id: list[int] = None, enabled: list[bool] = None
    ):
        """
        param env_name: target environment name.
        param node_id: unique identifier of the target node (container).
        param enabled: defines whether to enable (true) or disable (false) DNS records for the target node.
        """
        return self._get(
            "ManageNodeDnsState",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "enabled": enabled,
            },
            delimiter=",",
        )

    def MoveExtIps(
        self, env_name: str, source_node_id: int, target_node_id: int, ips: str
    ):
        """
        param env_name: source environment name.
        param source_node_id: unique identifier of the source node (from the source environment).
        param target_node_id: unique identifier of the target node (could be from the same or different environment on the account).
        param ips: a comma- or semicolon-separated list of IP addresses that should be transferred (use "*" to move all the source node external IP addresses).
        """
        return self._get(
            "MoveExtIps",
            params={
                "envName": env_name,
                "sourceNodeId": source_node_id,
                "targetNodeId": target_node_id,
                "ips": ips,
            },
        )

    def RemoveDomains(
        self,
        env_name: str,
        domains: str,
        node_group: list[str] = None,
        node_id: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param domains: a comma- or semicolon-separated list of domains (e.g. domain1,domain2 or domain1;domain2); provide "*" to remove all custom domains.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "RemoveDomains",
            params={
                "envName": env_name,
                "domains": domains,
                "nodeGroup": node_group,
                "node_id": node_id,
            },
            delimiter=",",
        )

    def RemoveExtDomains(
        self,
        env_name: str,
        extdomain: str,
    ):
        """
        param env_name: target environment name.
        param extdomain: external domain name to be detached.
        """
        return self._get(
            "RemoveExtDomains",
            params={
                "envName": env_name,
                "extdomain": extdomain,
            },
        )

    def RemoveSSL(
        self,
        env_name: str,
    ):
        """
        param env_name: target environment name.
        """
        return self._get(
            "RemoveSSL",
            params={
                "envName": env_name,
            },
        )

    def RemoveSSLCerts(
        self,
        env_name: str,
        ids: str,
    ):
        """
        param env_name: target environment name.
        param ids: a comma-separated list of certificate IDs (e.g. id1,id2,id3); provide "*" to remove all certificates.
        """
        return self._get(
            "RemoveSSLCerts",
            params={
                "envName": env_name,
                "ids": ids,
            },
        )

    def SetExtIpCount(
        self,
        env_name: str,
        type: str,
        count: int,
        node_group: list[str] = None,
        node_id: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param type: external IP address type ("ipv4" or "ipv6").
        param count: number of IPs to add per container - requires the multiple IPs feature enabled on the account.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "SetExtIpCount",
            params={
                "envName": env_name,
                "type": type,
                "count": count,
                "nodeGroup": node_group,
                "node_id": node_id,
            },
            delimiter=",",
        )

    def SwapExtDomains(
        self,
        env_name: str,
        targetappid: str,
    ):
        """
        param env_name: target environment name.
        param targetappid: Target (second) environment name.
        """
        return self._get(
            "SwapExtDomains",
            params={
                "envName": env_name,
                "targetappid": targetappid,
            },
        )

    def SwapExtIps(
        self,
        env_name: str,
        source_node_id: int,
        target_node_id: int,
        source_ip: list[str] = None,
        target_ip: list[str] = None,
    ):
        """
        param env_name: source environment name.
        param source_node_id: unique identifier of the source node (from the source environment).
        param target_node_id: unique identifier of the target node (could be from the same or different environment on the account).
        param source_ip: source IP address that should be swapped (if not specified, all external IPs from source node are transferred to the target).
        param target_ip: target IP address that should be swapped (if not specified, all external IPs from target node are transferred to the source).
        """
        return self._get(
            "SwapExtIps",
            params={
                "envName": env_name,
                "sourceNodeId": source_node_id,
                "targetNodeId": target_node_id,
                "sourceIp": source_ip,
                "targetIp": target_ip,
            },
            delimiter=",",
        )

    def UnbindSSLCert(
        self,
        env_name: str,
        extdomains: list[str] = None,
    ):
        """
        param env_name: target environment name.
        param extdomain: a comma-separated list of external domains to be unbound (if not specified, SSL certificates are unbound from the environment).
        """
        return self._get(
            "UnbindSSLCert",
            params={
                "envName": env_name,
                "extDomains": extdomains,
            },
            delimiter=",",
        )


class _File(Environment):
    """
    The File Manager API service gives you access to the container’s home directory and your environment's configuration files. You can read, write, create, delete, and adjust your application files and settings.

     Ref: https://docs.jelastic.com/api/private/#!/api/environment.File
    """

    _endpoint2 = "file"

    def AddFavorite(
        self,
        env_name: str,
        path: str,
        node_group: list[str] = None,
        node_id: list[int] = None,
        keyword: list[str] = None,
        filter: list[str] = None,
        is_dir: list[bool] = None,
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the file or directory for quick access.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param node_id: unique identifier of the target node (container).
        param keyword: custom name of the favorite shortcut.
        param filter: regex expression to filter a list of files displayed via the shortcut (up to 255 characters).
        param is_dir: defines whether shortcut points to the directory (true) or file (false).
        """
        return self._get(
            "AddFavorite",
            params={
                "envName": env_name,
                "path": path,
                "nodeGroup": node_group,
                "nodeId": node_id,
                "keyword": keyword,
                "filter": filter,
                "isDir": is_dir,
            },
            delimiter=",",
        )

    def AddMountPointByGroup(
        self,
        env_name: str,
        node_group: str,
        path: str,
        source_path: str,
        protocol: list[str] = None,
        source_host: list[str] = None,
        source_node_id: list[int] = None,
        name: list[str] = None,
        read_only: list[bool] = None,
        source_address_type: list[str] = None,
    ):
        """
        param env_name: target environment name.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param path: absolute path to the local folder where remote data will be shown at
        param source_path: absolute path to the files on your remote node/server where the data is physically stored.
        param source_host: host or IP address of the remote server where the data is physically stored.
        param source_node_id: unique identifier of the remote node where the data is physically stored.
        param name: custom name for the mount point (local folder name is used if not specified).
        param read_only: defines access rights for the mounted files - read only (true) or read and write (false).
        param source_address_type: source address type ("IP" or 0 | "DOMAIN" or 1 | "NODE_GROUP" or 2).
        """
        return self._get(
            "AddMountPointByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "path": path,
                "sourcePath": source_path,
                "protocol": protocol,
                "sourceHost": source_host,
                "sourceNodeId": source_node_id,
                "name": name,
                "readOnly": read_only,
                "sourceAddressType": source_address_type,
            },
            delimiter=",",
        )

    def AddMountPointById(
        self,
        env_name: str,
        node_id: int,
        path: str,
        source_path: str,
        protocol: list[str] = None,
        source_host: list[str] = None,
        source_node_id: list[int] = None,
        name: list[str] = None,
        read_only: list[bool] = None,
        source_address_type: list[str] = None,
    ):
        """
        param env_name: target environment name.
        param node_id : unique identifier of the target node (container).
        param path: absolute path to the local folder where remote data will be shown at
        param source_path: absolute path to the files on your remote node/server where the data is physically stored.
        param source_host: host or IP address of the remote server where the data is physically stored.
        param source_node_id: unique identifier of the remote node where the data is physically stored.
        param name: custom name for the mount point (local folder name is used if not specified).
        param read_only: defines access rights for the mounted files - read only (true) or read and write (false).
        param source_address_type: source address type ("IP" or 0 | "DOMAIN" or 1 | "NODE_GROUP" or 2).
        """
        return self._get(
            "AddMountPointById",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "path": path,
                "sourcePath": source_path,
                "protocol": protocol,
                "sourceHost": source_host,
                "sourceNodeId": source_node_id,
                "name": name,
                "readOnly": read_only,
                "sourceAddressType": source_address_type,
            },
            delimiter=",",
        )

    def Append(
        self,
        env_name: str,
        path: str,
        body: list[str] = None,
        node_type: list[str] = None,
        node_group: list[str] = None,
        master_only: list[bool] = None,
        node_id: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the file, where the text should be added.
        param body: text that should be added to the file.
        param node_type: unique identifier of the target node type (software stack), e.g. "tomcat11" for the Tomcat 11 stack.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param master_only: defines whether to execute the command on the master/primary node only (true) or on all nodes in the layer (false).
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "Append",
            params={
                "envName": env_name,
                "path": path,
                "body": body,
                "nodeType": node_type,
                "nodeGroup": node_group,
                "masterOnly": master_only,
                "nodeId": node_id,
            },
            delimiter=",",
        )

    def CheckCrossMount(self, env_name: str, node_id: int, source_node_id: int):
        """
        param env_name: target environment name.
        param node_id : unique identifier of the target node (container).
        param source_node_id: unique identifier of the remote node where the data is physically stored.
        """
        return self._get(
            "CheckCrossMount",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "sourceNodeId": source_node_id,
            },
        )

    def CloneMountPoints(
        self,
        env_name: str,
        node_id: int,
        source_node_id: int,
        mount_points: list[str] = None,
    ):
        return self._get(
            "CloneMountPoints",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "sourceNodeId": source_node_id,
                "mountPoints": mount_points,
            },
            delimiter=",",
        )

    def Copy(
        self,
        env_name: str,
        src: str,
        dest: str,
        node_type: list[str] = None,
        node_group: list[str] = None,
        master_only: list[bool] = None,
        node_id: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param src: absolute path to the source file that should be copied.
        param dest: absolute path to the destination, where the file copy should be placed.
        param node_type: unique identifier of the target node type (software stack), e.g. "tomcat11" for the Tomcat 11 stack.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param master_only: defines whether to execute the command on the master/primary node only (true) or on all nodes in the layer (false).
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "Copy",
            params={
                "envName": env_name,
                "src": src,
                "dest": dest,
                "nodeType": node_type,
                "nodeGroup": node_group,
                "masterOnly": master_only,
                "nodeId": node_id,
            },
            delimiter=",",
        )

    def Create(
        self,
        env_name: str,
        path: str,
        node_type: list[str] = None,
        node_group: list[str] = None,
        master_only: list[bool] = None,
        isdir: list[bool] = None,
        node_id: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the file that should be created.
        param node_type: unique identifier of the target node type (software stack), e.g. "tomcat11" for the Tomcat 11 stack.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param master_only: defines whether to execute the command on the master/primary node only (true) or on all nodes in the layer (false).
        param isdir: defines whether to create directory (true) or file (false).
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "Create",
            params={
                "envName": env_name,
                "path": path,
                "nodeType": node_type,
                "nodeGroup": node_group,
                "masterOnly": master_only,
                "isdir": isdir,
                "nodeId": node_id,
            },
            delimiter=",",
        )

    def Delete(
        self,
        env_name: str,
        path: str,
        node_type: list[str] = None,
        node_group: list[str] = None,
        master_only: list[bool] = None,
        node_id: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the file that should be created.
        param node_type: unique identifier of the target node type (software stack), e.g. "tomcat11" for the Tomcat 11 stack.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param master_only: defines whether to execute the command on the master/primary node only (true) or on all nodes in the layer (false).
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "Delete",
            params={
                "envName": env_name,
                "path": path,
                "nodeType": node_type,
                "nodeGroup": node_group,
                "masterOnly": master_only,
                "nodeId": node_id,
            },
            delimiter=",",
        )

    def GetExportedList(
        self,
        env_name: str,
        node_id: int,
        path: list[str] = None,
    ):
        """
        param env_name: target environment name.
        param node_id: unique identifier of the target node (container).
        param path: absolute path to the file that should be created.
        """
        return self._get(
            "GetExportedList",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "path": path,
            },
            delimiter=",",
        )

    def GetFavorites(
        self,
        env_name: str,
        node_group: list[str] = None,
        node_id: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "GetFavorites",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "nodeId": node_id,
            },
            delimiter=",",
        )

    def GetList(
        self,
        env_name: str,
        path: list[str] = None,
        node_type: list[str] = None,
        node_group: list[str] = None,
        node_id: list[int] = None,
        filter: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the directory with files.
        param node_type: unique identifier of the target node type (software stack), e.g. "tomcat11" for the Tomcat 11 stack.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param node_id: unique identifier of the target node (container).
        param filter: regex expression to filter the list of returned files (up to 255 characters).
        """
        return self._get(
            "GetList",
            params={
                "envName": env_name,
                "path": path,
                "nodeType": node_type,
                "nodeGroup": node_group,
                "nodeId": node_id,
                "filter": filter,
            },
            delimiter=",",
        )

    def GetMountPoints(
        self,
        env_name: str,
        node_group: list[str] = None,
        node_id: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "GetMountPoints",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "nodeId": node_id,
            },
            delimiter=",",
        )

    def PrepareMountPoints(self, env_name: str, data: str):
        return self._get(
            "PrepareMountPoints",
            params={"envName": env_name, "data": data},
        )

    def Read(
        self,
        env_name: str,
        path: str,
        node_type: list[str] = None,
        node_group: list[str] = None,
        node_id: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the directory with files.
        param node_type: unique identifier of the target node type (software stack), e.g. "tomcat11" for the Tomcat 11 stack.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "Read",
            params={
                "envName": env_name,
                "path": path,
                "nodeType": node_type,
                "nodeGroup": node_group,
                "nodeId": node_id,
            },
            delimiter=",",
        )

    def RemoveExport(
        self,
        env_name: str,
        node_id: int,
        path: str,
        client_node_id: int,
        client_path: str,
    ):
        """
        param env_name: target environment name.
        param node_id: unique identifier of the target node (container).
        param path: absolute path to the directory with files.
        param client_node_id: unique identifier of the remote client node.
        param client_path: absolute path to the directory on the remote client node through which local files can be accessed.
        """
        return self._get(
            "RemoveExport",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "path": path,
                "clientNodeId": client_node_id,
                "clientPath": client_path,
            },
        )

    def RemoveFavorite(
        self,
        env_name: str,
        path: str,
        node_type: list[str] = None,
        node_group: list[str] = None,
        node_id: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the directory with files.
        param node_type: unique identifier of the target node type (software stack), e.g. "tomcat11" for the Tomcat 11 stack.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "RemoveFavorite",
            params={
                "envName": env_name,
                "path": path,
                "nodeType": node_type,
                "nodeGroup": node_group,
                "nodeId": node_id,
            },
            delimiter=",",
        )

    def RemoveMountPointByGroup(
        self,
        env_name: str,
        path: str,
        node_group: str,
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the directory with files.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        """
        return self._get(
            "RemoveMountPointByGroup",
            params={
                "envName": env_name,
                "path": path,
                "nodeGroup": node_group,
            },
        )

    def RemoveMountPointById(
        self,
        env_name: str,
        path: str,
        node_id: str,
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the directory with files.
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "RemoveMountPointById",
            params={
                "envName": env_name,
                "path": path,
                "nodeId": node_id,
            },
        )

    def Rename(
        self,
        env_name: str,
        old_path: str,
        new_path: str,
        node_type: list[str] = None,
        node_group: list[str] = None,
        master_only: list[bool] = None,
        node_id: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param old_path: absolute path to the file to be renamed.
        param new_path: absolute path with the new filename.
        param node_type: unique identifier of the target node type (software stack), e.g. "tomcat11" for the Tomcat 11 stack.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param master_only: defines whether to execute the command on the master/primary node only (true) or on all nodes in the layer (false).
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "Rename",
            params={
                "envName": env_name,
                "oldPath": old_path,
                "newPath": new_path,
                "nodeType": node_type,
                "nodeGroup": node_group,
                "masterOnly": master_only,
                "nodeId": node_id,
            },
            delimiter=",",
        )

    def ReplaceInBody(
        self,
        env_name: str,
        path: str,
        pattern: str,
        replacement: str,
        nth: list[int] = None,
        node_type: list[str] = None,
        node_group: list[str] = None,
        master_only: list[bool] = None,
        node_id: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the file that should be created.
        param pattern: regex expression (in a SED-compatible format) to locate text for replacement.
        param replacement: replacement text (in a plain text format).
        param nth: maximum number of entries for replacement.
        param node_type: unique identifier of the target node type (software stack), e.g. "tomcat11" for the Tomcat 11 stack.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param master_only: defines whether to execute the command on the master/primary node only (true) or on all nodes in the layer (false).
        param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "ReplaceInBody",
            params={
                "envName": env_name,
                "path": path,
                "pattern": pattern,
                "replacement": replacement,
                "nth": nth,
                "nodeType": node_type,
                "nodeGroup": node_group,
                "masterOnly": master_only,
                "nodeId": node_id,
            },
            delimiter=",",
        )

    def UnpackById(
        self, env_name: str, path: str, node_id: str, source_path: str, dest_path: str
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the directory with files.
        param node_id: unique identifier of the target node (container).
        param source_path: absolute path to the target archive file.
        param dest_path: absolute path to extract files to.
        """
        return self._get(
            "UnpackById",
            params={
                "envName": env_name,
                "path": path,
                "nodeId": node_id,
                "sourcePath": source_path,
                "destPath": dest_path,
            },
        )

    def UnpackByType(
        self, env_name: str, path: str, node_type: str, source_path: str, dest_path: str
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the directory with files.
        param node_type: unique identifier of the target node type (software stack), e.g. "tomcat11" for the Tomcat 11 stack.
        param source_path: absolute path to the target archive file.
        param dest_path: absolute path to extract files to.
        """
        return self._get(
            "UnpackByType",
            params={
                "envName": env_name,
                "path": path,
                "nodeType": node_type,
                "sourcePath": source_path,
                "destPath": dest_path,
            },
        )

    def Upload(
        self,
        env_name: str,
        source_path: str,
        dest_path: str,
        node_type: list[str] = None,
        node_group: list[str] = None,
        master_only: list[bool] = None,
        node_id: list[int] = None,
        overwrite: list[bool] = None,
    ):
        """
        param env_name: target environment name.
        param source_path: URL of the target file to be uploaded.
        param dest_path: absolute path (on the target container) to save uploaded file at.
        param node_type: unique identifier of the target node type (software stack), e.g. "tomcat11" for the Tomcat 11 stack.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param master_only: defines whether to execute the command on the master/primary node only (true) or on all nodes in the layer (false).
        param node_id: unique identifier of the target node (container).
        param overwrite: defines whether to overwrite (true) or skip (false) file if it already exists at the destination directory.
        """
        return self._get(
            "Upload",
            params={
                "envName": env_name,
                "sourcePath": source_path,
                "destPath": dest_path,
                "nodeType": node_type,
                "nodeGroup": node_group,
                "masterOnly": master_only,
                "nodeId": node_id,
                "overwrite": overwrite,
            },
            delimiter=",",
        )

    def Write(
        self,
        env_name: str,
        path: str,
        body: list[str] = None,
        node_type: list[str] = None,
        node_group: list[str] = None,
        master_only: list[bool] = None,
        node_id: list[int] = None,
        is_append_mode: list[int] = None,
    ):
        """
        param env_name: target environment name.
        param path: absolute path to the file that should be created.
        param body: text that should be written to the file.
        param node_type: unique identifier of the target node type (software stack), e.g. "tomcat11" for the Tomcat 11 stack.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param master_only: defines whether to execute the command on the master/primary node only (true) or on all nodes in the layer (false).
        param node_id: unique identifier of the target node (container).
        param is_append_mode: defines whether to overwrite the file content (false) or append the existing text (false)
        """
        return self._get(
            "Write",
            params={
                "envName": env_name,
                "path": path,
                "body": body,
                "nodeType": node_type,
                "nodeGroup": node_group,
                "masterOnly": master_only,
                "nodeId": node_id,
                "isAppendMode": is_append_mode,
            },
            delimiter=",",
        )