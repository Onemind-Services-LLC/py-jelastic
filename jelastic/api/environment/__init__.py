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
    def Control(self) -> "_Control":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.Control

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.Control
        """
        return _Control(session=self._session, token=self._token, debug=self._debug)


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

    def EnvResources(
            self,
            start_time: datetime,
            end_time: datetime
    ):
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
            }
        )

    def BindSSLCert(
            self,
            env_name: str,
            cert_id: int,
            entry_point: list[str] = None,
            ext_domains: list[str] = None
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
                "extDomains": ext_domains
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
        return self._get("DeleteSSL",
                         params={"envName": env_name
                                 },
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
        return self._get("DisableSSL", params={
            "envName": env_name,
        })

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
                "interm": interm
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
            in_short: list[bool] = None
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

    def GetExtDomains(
            self,
            env_name: str
    ):
        return self._get("GetExtDomains", params={
            "envName": env_name
        })

    def GetSSL(
            self,
            env_name: str
    ):
        return self._get("GetSSL", params={
            "envName": env_name
        })

    def GetSSLCerts(
            self,
            env_name: str,
            ids: list[str] = None
    ):
        return self._get("GetSSLCerts", params={
            "envName": env_name,
            "ids": ids},
                         delimiter=",",
                         )

    def ManageNodeDnsState(
            self,
            env_name: str,
            node_id: list[int] = None,
            enabled: list[bool] = None
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
            self,
            env_name: str,
            source_node_id: int,
            target_node_id: int,
            ips: str
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
                "ips": ips
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
            target_ip: list[str] = None
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
                "targetIp": target_ip
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


class _Control(Environment):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/environment.Control
    """
    _endpoint2 = 'control'

    def AddBackend(
            self,
            env_name: str,
            backend_node_id: int,
            balancer_node_id: int,
    ):
        return self._get(
            "AddBackend",
            params={
                "envName": env_name,
                "backendNodeId": backend_node_id,
                "balancerNodeId": balancer_node_id,
            }
        )

    def AddBackends(
            self,
            env_name: str,
            backend_node_id: str,
            balancer_node_id: str,

    ):
        return self._get(
            'AddBackends',
            params={
                "envName": env_name,
                "backendNodeId": backend_node_id,
                "balancerNodeId": balancer_node_id,
            }
        )

    def AddBalancerNode(
            self,
            env_name: str,
            node_type: str,
            cloud_lets: list[int] = None,
            exp_ip: list[bool] = None,
            flexible_cloud_lets: list[int] = None,
            fixed_cloud_lets: list[int] = None,
            display_name: list[str] = None,
            node_group: list[str] = None,
            disk_limit: list[int] = None,
            tag: list[str] = None,
            metadata: list[str] = None,
            start_service: list[bool] = None,
            exp_ipv6_count: list[int] = None,
            exp_ip_count: list[int] = None,
            node_group_data: list[str] = None,
    ):
        return self._get(
            'AddBalancerNode',
            params={
                "envName": env_name,
                "nodeType": node_type,
                "cloudLets": cloud_lets,
                "expIp": exp_ip,
                "flexibleCloudlets": flexible_cloud_lets,
                'fixedCloudlets': fixed_cloud_lets,
                'displayName': display_name,
                'nodeGroup': node_group,
                'diskLimit': disk_limit,
                'tag': tag,
                'metadata': metadata,
                'startService': start_service,
                'extIpv6Count': exp_ipv6_count,
                'extIpCount': exp_ip_count,
                'nodeGroupData': node_group_data,
            },
            delimiter=",",
        )

    def AddBuildNode(
            self,
            env_name: str,
            node_type: str,
            cloud_lets: list[int] = None,
            node_id: list[int] = None,
            exp_ip: list[bool] = None,
            flexible_cloud_lets: list[int] = None,
            fixed_cloud_lets: list[int] = None,
            display_name: list[str] = None,
            node_group: list[str] = None,
            tag: list[str] = None,
            metadata: list[str] = None,
            start_service: list[bool] = None,
            engine: list[str] = None,
            exp_ipv6_count: list[int] = None,
            exp_ip_count: list[int] = None,
            node_group_data: list[str] = None,
            disk_limit: list[int] = None,
    ):
        return self._get(
            'AddBuildNode',
            params={
                'envName': env_name,
                'nodeType': node_type,
                'cloudlets': cloud_lets,
                'nodeId': node_id,
                'expIp': exp_ip,
                'flexibleCloudlets': flexible_cloud_lets,
                'fixedCloudlets': fixed_cloud_lets,
                'displayName': display_name,
                'nodeGroup': node_group,
                'tag': tag,
                'metadata': metadata,
                'startService': start_service,
                'engine': engine,
                'extIpv6Count': exp_ipv6_count,
                'extIpCount': exp_ip_count,
                'nodeGroupData': node_group_data,
                'diskLimit': disk_limit,
            },
            delimiter=",",
        )

    def AddCacheNode(
            self,
            env_name: str,
            node_type: str,
            cloud_lets: list[int] = None,
            flexible_cloud_lets: list[int] = None,
            fixed_cloud_lets: list[int] = None,
            display_name: list[str] = None,
            node_group: list[str] = None,
            disk_limit: list[int] = None,
            tag: list[str] = None,
            metadata: list[str] = None,
            start_service: list[bool] = None,
            exp_ipv6_count: list[int] = None,
            exp_ip_count: list[int] = None,
            node_group_data: list[str] = None,
    ):
        return self._get(
            'AddCacheNode',
            params={
                'envName': env_name,
                'nodeType': node_type,
                'cloudlets': cloud_lets,
                'flexibleCloudlets': flexible_cloud_lets,
                'fixedCloudlets': fixed_cloud_lets,
                'displayName': display_name,
                'nodeGroup': node_group,
                'diskLimit': disk_limit,
                'tag': tag,
                'metadata': metadata,
                'startService': start_service,
                'expIpv6Count': exp_ipv6_count,
                'expIpCount': exp_ip_count,
                'nodeGroupData': node_group_data,
            },
            delimiter=",",
        )

    def AddComputeNode(
            self,
            env_name: str,
            node_type: str,
            cloud_lets: list[int] = None,
            is_master: list[int] = None,
            exp_ip: list[bool] = None,
            flexible_cloud_lets: list[int] = None,
            fixed_cloud_lets: list[int] = None,
            display_name: list[str] = None,
            node_group: list[str] = None,
            disk_limit: list[int] = None,
            tag: list[str] = None,
            metadata: list[bool] = None,
            start_service: list[bool] = None,
            engine: list[str] = None,
            exp_ipv6_count: list[int] = None,
            exp_ip_count: list[int] = None,
            node_group_data: list[str] = None,
    ):
        return self._get(
            'AddComputeNode',
            params={
                'envName': env_name,
                'nodeType': node_type,
                'cloudlets': cloud_lets,
                'isMaster': is_master,
                'expIp': exp_ip,
                'flexibleCloudlets': flexible_cloud_lets,
                'fixedCloudlets': fixed_cloud_lets,
                'displayName': display_name,
                'nodeGroup': node_group,
                'diskLimit': disk_limit,
                'tag': tag,
                'metadata': metadata,
                'startService': start_service,
                'engine': engine,
                'expIpv6Count': exp_ipv6_count,
                'expIpCount': exp_ip_count,
                'nodeGroupData': node_group_data,
            },
            delimiter=",",
        )

    def AddContainerEnvVars(
            self,
            env_name: str,
            vars: str,
            node_group: list[str] = None,
            node_id: list[int] = None,
    ):
        """
        :param env_name: target environment name.
        :param vars: JSON object with a list of container environment variables, e.g. {"var1":"value1", "var2":"value2"}
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            'AddContainerEnvVars',
            params={
                'envName': env_name,
                'vars': vars,
                'nodeGroup': node_group,
                'nodeId': node_id,
            },
            delimiter=",",
        )

    def AddContainerVolume(
            self,
            env_name: str,
            node_id: int,
            path: str,
    ):
        return self._get(
            'AddContainerVolume',
            params={
                'envName': env_name,
                'nodeId': node_id,
                'path': path,
            }
        )

    def AddContainerVolumeByGroup(
            self,
            env_name: str,
            node_group: str,
            path: str,
    ):
        return self._get(
            'AddContainerVolumeByGroup',
            params={
                'envName': env_name,
                'nodeGroup': node_group,
                'path': path,
            }
        )

    def AddContainerVolumes(
            self,
            env_name: str,
            volumes: str,
            node_group: list[str] = None,
            node_id: list[int] = None,
    ):
        """
        :param env_name: target environment name
        :param volumes: an array of data volumes to be added, e.g. /data/volume or ["/data/volume","/data/volume2", ...]
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            'AddContainerVolumes',
            params={
                'envName': env_name,
                'volumes': volumes,
                'nodeGroup': node_group,
                'nodeId': node_id,
            },
            delimiter=",",
        )

    def AddContext(
            self,
            env_name: str,
            name: str,
            file_name: str,
            type: str,
            node_group: list[str] = None,
    ):
        """
        :param env_name: target environment name
        :param name: context name for the application
        """
        return self._get(
            'AddContext',
            params={
                'envName': env_name,
                'name': name,
                'fileName': file_name,
                'type': type,
                'nodeGroup': node_group,
            },
            delimiter=",",
        )

    def AddDBNode(
            self,
            env_name: str,
            node_type: str,
            cloud_lets: list[int] = None,
            exp_ip: list[bool] = None,
            password: list[str] = None,
            flexible_cloud_lets: list[int] = None,
            fixed_cloud_lets: list[int] = None,
            display_name: list[str] = None,
            node_group: list[str] = None,
            disk_limit: list[int] = None,
            tag: list[str] = None,
            metadata: list[bool] = None,
            start_service: list[bool] = None,
            exp_ipv6_count: list[int] = None,
            exp_ip_count: list[int] = None,
            node_group_data: list[str] = None,
    ):
        return self._get(
            'AddDBNode',
            params={
                'envName': env_name,
                'nodeType': node_type,
                'cloudlets': cloud_lets,
                'expIp': exp_ip,
                'password': password,
                'flexibleCloudlets': flexible_cloud_lets,
                'fixedCloudlets': fixed_cloud_lets,
                'displayName': display_name,
                'nodeGroup': node_group,
                'diskLimit': disk_limit,
                'tag': tag,
                'metadata': metadata,
                'startService': start_service,
                'expIpv6Count': exp_ipv6_count,
                'expIpCount': exp_ip_count,
                'nodeGroupData': node_group_data,
            },
            delimiter=",",
        )

    def AddDockerNode(
            self,
            env_name: str,
            node_type: str,
            metadata: dict,
            cloud_lets: list[int] = None,
            exp_ip: list[bool] = None,
            password: list[str] = None,
            flexible_cloud_lets: list[int] = None,
            fixed_cloud_lets: list[int] = None,
            display_name: list[str] = None,
            node_group: list[str] = None,
            disk_limit: list[int] = None,
            start_service: list[bool] = None,
            exp_ipv6_count: list[int] = None,
            exp_ip_count: list[int] = None,
            node_group_data: list[str] = None,
    ):
        return self._get(
            'AddDockerNode',
            params={
                'envName': env_name,
                'nodeType': node_type,
                'metadata': metadata,
                'cloudlets': cloud_lets,
                'expIp': exp_ip,
                'password': password,
                'flexibleCloudlets': flexible_cloud_lets,
                'fixedCloudlets': fixed_cloud_lets,
                'displayName': display_name,
                'nodeGroup': node_group,
                'diskLimit': disk_limit,
                'startService': start_service,
                'expIpv6Count': exp_ipv6_count,
                'expIpCount': exp_ip_count,
                'nodeGroupData': node_group_data,
            },
            delimiter=",",
        )

    def AddDockerVolume(
            self,
            env_name: str,
            node_id: int,
            path: str,
    ):
        return self._get(
            'AddDockerVolume',
            params={
                'envName': env_name,
                'nodeId': node_id,
                'path': path
            }
        )

    def AddDockerVolumeByGroup(
            self,
            env_name: str,
            node_group: int,
            path: str,
    ):
        return self._get(
            'AddDockerVolumeByGroup',
            params={
                'envName': env_name,
                'nodeGroup': node_group,
                'path': path
            }
        )

    def AddEndpoint(
            self,
            env_name: str,
            node_id: int,
            private_port: int,
            protocol: str,
            name: str,
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        :param private_port: local port on the container to connect to via endpoint.
        :param protocol: connection protocol (“TCP” or “UDP”).
        :param name: custom endpoint name.
        """
        return self._get(
            'AddEndpoint',
            params={
                'envName': env_name,
                'nodeId': node_id,
                'privatePort': private_port,
                'protocol': protocol,
                'name': name,
            }
        )

    def AddEnvPolicy(
            self,
            target_app_id: str,
            policy: str,
    ):
        """
        :param target_app_id: target application identifier of the environment for adding policy.
        :param policy: a comma-separated list of policy. For example: "policy1,policy2".
        """
        return self._get(
            'AddEnvPolicy',
            params={
                'targetAppId': target_app_id,
                'policy': policy,
            }
        )

    def AddEnvProperty(self, properties: str):
        """
        :param properties: JSON object with environment properties. For example: {"customProperty1":"value1","customProperty2":"value2"}
        """
        return self._get(
            'AddEnvProperty',
            params={
                'properties': properties,
            }
        )

    def AddExtraNode(
            self,
            env_name: str,
            node_type: str,
            cloud_lets: list[int] = None,
            exp_ip: list[bool] = None,
            flexible_cloud_lets: list[int] = None,
            fixed_cloud_lets: list[int] = None,
            display_name: list[str] = None,
            node_group: list[str] = None,
            disk_limit: list[int] = None,
            tag: list[str] = None,
            metadata: list[bool] = None,
            start_service: list[bool] = None,
            exp_ipv6_count: list[int] = None,
            exp_ip_count: list[int] = None,
            node_group_data: list[str] = None,
    ):
        return self._get(
            'AddExtraNode',
            params={
                'envName': env_name,
                'nodeType': node_type,
                'cloudlets': cloud_lets,
                'expIp': exp_ip,
                'flexibleCloudlets': flexible_cloud_lets,
                'fixedCloudlets': fixed_cloud_lets,
                'displayName': display_name,
                'nodeGroup': node_group,
                'diskLimit': disk_limit,
                'tag': tag,
                'metadata': metadata,
                'startService': start_service,
                'expIpv6Count': exp_ipv6_count,
                'expIpCount': exp_ip_count,
                'nodeGroupData': node_group_data,
            },
            delimiter=",",
        )

    def AddNode(self,
                env_name: str,
                node_type: str,
                cloud_lets: list[int] = None,
                ext_ip: list[str] = None,
                password: list[str] = None,
                flexible_cloud_lets: list[int] = None,
                fixed_cloud_lets: list[int] = None,
                display_name: list[str] = None,
                metadata: list[str] = None,
                node_group: list[str] = None,
                start_service: list[bool] = None,
                disk_limit: list[int] = None,
                tag: list[str] = None,
                engine: list[str] = None,
                exit_ipv4: list[int] = None,
                exit_ipv6: list[int] = None,
                node_group_data: list[str] = None,
                options: list[str] = None,
                ):
        """
        :param env_name: name of the selected environment
        :param node_type: node type (tomcat7, mysql5, etc)
        :param password: password for specific nodes
        :param flexible_cloud_lets: flexible cloudlets number
        :param fixed_cloud_lets: fixed cloudlets number
        :param display_name: alias for your environment
        :param metadata: docker node metadata
        :param node_group: node group (cp,bl, etc)
        :param start_service: exec docker run
        :param disk_limit: node disk limitation
        :params tag: docker tag
        :param engine:
        :param exit_ipv4: IPv4 count
        :param exit_ipv6: IPv6 count
        """
        return self._get(
            'AddNode',
            params={
                'envName': env_name,
                'nodeType': node_type,
                'cloudLets': cloud_lets,
                'extIp': ext_ip,
                'password': password,
                'flexibleCloudLets': flexible_cloud_lets,
                'fixedCloudLets': fixed_cloud_lets,
                'displayName': display_name,
                'metadata': metadata,
                'nodeGroup': node_group,
                'startService': start_service,
                'diskLimit': disk_limit,
                'tag': tag,
                'engine': engine,
                'extipv4': exit_ipv4,
                'extipv6': exit_ipv6,
                'nodeGroupData': node_group_data,
                'options': options,
            },
            delimiter=",",
        )

    def AddPortRedirect(
            self,
            env_name: str,
            node_id: int,
            src_port: int,
            dst_port: int,
            protocol: str,
            comments: list[str] = None,
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        :param src_port: source port on the container.
        :param dst_port: destination port on the container.
        :param protocol:transport protocol (“TCP” or “UDP”).
        :param comments: custom comment for the redirect.
        """
        return self._get(
            'AddPortRedirect',
            params={
                'envName': env_name,
                'nodeId': node_id,
                'srcPort': src_port,
                'dstPort': dst_port,
                'protocol': protocol,
                'comments': comments,
            },
            delimiter=",",
        )

    def AddStorageNode(
            self,
            env_name: str,
            node_type: str,
            cloud_lets: list[int] = None,
            ext_ip: list[str] = None,
            flexible_cloud_lets: list[int] = None,
            fixed_cloud_lets: list[int] = None,
            display_name: list[str] = None,
            node_group: list[str] = None,
            disk_limit: list[int] = None,
            tag: list[str] = None,
            metadata: list[str] = None,
            start_service: list[bool] = None,
            ext_ipv6_count: list[int] = None,
            ext_ip_count: list[int] = None,
            node_group_data: list[str] = None,
    ):
        return self._get(
            'AddStorageNode',
            params={
                'envName': env_name,
                'nodeType': node_type,
                'cloudlets': cloud_lets,
                'extIp': ext_ip,
                'flexibleCloudLets': flexible_cloud_lets,
                'fixedCloudLets': fixed_cloud_lets,
                'displayName': display_name,
                'nodeGroup': node_group,
                'diskLimit': disk_limit,
                'tag': tag,
                'metadata': metadata,
                'startService': start_service,
                'extIpv6Count': ext_ipv6_count,
                'extIpCount': ext_ip_count,
                'nodeGroupData': node_group_data,
            },
            delimiter=",",
        )

    def AddVdsNode(
            self,
            env_name: str,
            node_type: str,
            cloud_lets: list[int] = None,
            ext_ip: list[str] = None,
            password: list[str] = None,
            flexible_cloud_lets: list[int] = None,
            fixed_cloud_lets: list[int] = None,
            display_name: list[str] = None,
            node_group: list[str] = None,
            disk_limit: list[int] = None,
            tag: list[str] = None,
            metadata: list[str] = None,
            start_service: list[bool] = None,
            ext_ipv6_count: list[int] = None,
            ext_ip_count: list[int] = None,
            node_group_data: list[str] = None,
    ):
        return self._get(
            'AddVdsNode',
            params={
                'envName': env_name,
                'nodeType': node_type,
                'cloudlets': cloud_lets,
                'extIp': ext_ip,
                'password': password,
                'flexibleCloudLets': flexible_cloud_lets,
                'fixedCloudLets': fixed_cloud_lets,
                'displayName': display_name,
                'nodeGroup': node_group,
                'diskLimit': disk_limit,
                'tag': tag,
                'metadata': metadata,
                'startService': start_service,
                'extIpv6Count': ext_ipv6_count,
                'extIpCount': ext_ip_count,
                'nodeGroupData': node_group_data,
            },
            delimiter=",",
        )

    def AddVmNode(
            self,
            env_name: str,
            node_type: str,
            options: str,
            ext_ip: list[str] = None,
            display_name: list[str] = None,
            node_group: list[str] = None,
            disk_limit: list[int] = None,
            ext_ipv6_count: list[int] = None,
            ext_ip_count: list[int] = None,
            node_group_data: list[str] = None,
            password: list[str] = None,
    ):
        return self._get(
            'AddVmNode',
            params={
                'envName': env_name,
                'nodeType': node_type,
                'options': options,
                'extIp': ext_ip,
                'displayName': display_name,
                'nodeGroup': node_group,
                'diskLimit': disk_limit,
                'extIpv6Count': ext_ipv6_count,
                'extIpCount': ext_ip_count,
                'nodeGroupData': node_group_data,
                'password': password,
            },
            delimiter=",",
        )

    def AppendNodes(
            self,
            env_name: str,
            count: int,
            node_type: str,
    ):
        return self._get(
            'AppendNodes',
            params={
                'envName': env_name,
                'count': count,
                'nodeType': node_type,
            }
        )

    def ApplyEnvProperty(
            self,
            env_name: str,
            properties: str,
    ):
        """
        :param env_name: target environment name.
        :param properties: JSON object with environment properties. For example: {"customProperty1":"value1","customProperty2":"value2"}
        """
        return self._get(
            'ApplyEnvProperty',
            params={
                'envName': env_name,
                'properties': properties,
            }
        )

    def ApplyNodeGroupData(
            self,
            env_name: str,
            node_group_data: str,
            data: str,
    ):
        return self._get(
            'ApplyNodeGroupData',
            params={
                'envName': env_name,
                'nodeGroupData': node_group_data,
                'data': data,
            }
        )

    def ApplySoftwarePackageAction(
            self,
            env_name: str,
            keywords: str,
            node_type: list[str] = None,
            action: list[str] = None,
            password: list[str] = None,
            node_group: list[str] = None,
    ):
        return self._get(
            'ApplySoftwarePackageAction',
            params={
                'envName': env_name,
                'keywords': keywords,
                'nodeType': node_type,
                'action': action,
                'password': password,
                'nodeGroup': node_group,
            },
            delimiter=",",
        )

    def AttachEnvGroup(
            self,
            env_name: str,
            env_group_name: str,
    ):
        return self._get(
            'AttachEnvGroup',
            params={
                'envName': env_name,
                'envGroup': env_group_name,
            }
        )

    def BuildCluster(
            self,
            env_name: str,
            node_group: str,
    ):
        return self._get(
            'BuildCluster',
            params={
                'envName': env_name,
                'nodeGroup': node_group
            }
        )

    def CancelTransferRequest(self):
        return self._get(
            'CancelTransferRequest',
            params={}
        )

    def ChangeLimits(self, env_name: str):
        return self._get(
            'ChangeLimits',
            params={'envName': env_name}
        )

    def ChangeLimitsInner(
            self,
            env_name: str,
            uid: int,
            limit_type: list[str] = None,
    ):
        return self._get(
            'ChangeLimitsInner',
            params={
                'envName': env_name,
                'uid': uid,
                'limitType': limit_type,
            }
        )

    def ChangeTopology(
            self,
            env_name: str,
            env: dict,
            nodes: dict,
            action_key: list[str] = None
    ):
        """
        :param env_name: target environment name.
        :param env: JSON object with environment settings:
        :param nodes: JSON object with a list of environment nodes and their settings:
        :param action_key: name of the action and domain name.
        """
        return self._get(
            'ChangeTopology',
            params={
                'envName': env_name,
                'env': env,
                'nodes': nodes,
                'actionkey': action_key,
            },
            delimiter=',',
        )

    def CheckDependencies(
            self,
            env_name: str,
            node_id: list[int] = None,
            filter: list[str] = None,
    ):
        return self._get(
            'CheckDependencies',
            params={
                'envName': env_name,
                'nodeId': node_id,
                'filter': filter,
            },
            delimiter=',',
        )

    def CheckExtIpCount(
            self,
            exp_ipv6: int,
            exp_ipv4: list[int] = None,
            hardware_node_group: list[str] = None,
    ):
        return self._get(
            'CheckExtIpCount',
            params={
                'expIpv6': exp_ipv6,
                'expIpv4': exp_ipv4,
                'hardwareNodeGroup': hardware_node_group,
            },
            delimiter=',',
        )

    def CheckMigrationPossibility(
            self,
            env_name: str,
            hardware_node_group: list[str] = None,
    ):
        """
        :param env_name: target environment name.
        :param hardware_node_group: unique identifier of the target region (host group).
        """
        return self._get(
            'CheckMigrationPossibility',
            params={
                'envName': env_name,
                'hardwareNodeGroup': hardware_node_group,
            },
            delimiter=',',
        )

    def ClearLog(
            self,
            env_name: str,
            node_id: int,
            path: str
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        :param path: path to the target log file.
        """
        return self._get(
            'ClearLog',
            params={
                'envName': env_name,
                'nodeId': node_id,
                'path': path,
            }
        )

    def CloneEnv(
            self,
            src_env_name: str,
            dit_env_name: str,
            use_external_mounts: list[bool] = None,
    ):
        """
        :param src_env_name: source environment name (one that is going to be cloned).
        :param dit_env_name: destination (cloned) environment name.
        :param use_external_mounts: defines whether to copy external mounts on the clone (true) or not (false).
        """
        return self._get(
            'CloneEnv',
            params={
                'srcEnvName': src_env_name,
                'ditEnvName': dit_env_name,
                'useExternalMounts': use_external_mounts,
            },
            delimiter=",",
        )

    def CloneNode(
            self,
            env_name: str,
            count: int,
            node_group: str,
            node_id: list[int] = None,
    ):
        return self._get(
            'CloneNode',
            params={
                'envName': env_name,
                'count': count,
                'nodeGroup': node_group,
                'nodeId': node_id,
            }
        )

    def ConfirmTransferRequest(self, key: str):
        """
        :param key: disposable confirmation key
        """
        return self._get(
            'ConfirmTransferRequest',
            params={
                'key': key,
            }
        )

    def CreateEnv(
            self,
            env_name: str,
            settings: dict,
            owner_uid: list[int] = None,
            hardware_node_group: list[str] = None,
            env_groups: list[str] = None,
    ):
        """
        :param env_name: domain of the environment
        :param settings: settings of the environment
        :param owner_uid: unique identifier of the environment's owner
        """
        return self._get(
            'CreateEnv',
            params={
                'envName': env_name,
                'settings': settings,
                'ownerUid': owner_uid,
                'hardwareNodeGroups': hardware_node_group,
                'envGroups': env_groups,
            },
            delimiter=",",
        )

    def CreateEnvironment(
            self,
            env: dict,
            nodes: dict,
            action_key: list[str] = None,
            owner_uid: list[int] = None,
            env_groups: list[str] = None,
    ):
        """
        :param env: JSON object with environment settings:
        :param nodes: JSON object with a list of environment nodes and their settings:
        :param action_key: name of the action and domain name.
        :param owner_uid: unique identifier of the environment owner (if installing as collaborator on another user account).
        :param env_groups: target group name or JSON array of group names.
        """
        return self._get(
            'CreateEnvironment',
            params={
                'env': env,
                'nodes': nodes,
                'actionKey': action_key,
                'ownerUid': owner_uid,
                'envGroups': env_groups,
            },
            delimiter=",",
        )

    def DeleteEnv(
            self,
            env_name: str,
            password: list[str] = None,
    ):
        """
        :param env_name: target environment name.
        :param password: current user password or environment name to confirm environment deletion (depending on the 'environment.delete.confirm.type' quota).
        """
        return self._get(
            'DeleteEnv',
            params={
                'envName': env_name,
                'password': password,
            },
            delimiter=",",
        )

    def DeleteExportedFiles(
            self,
            env_name: str,
            file_name: str,
    ):
        """
        :param env_name: application identifier of the environment
        :param file_name: settings for export
        """
        return self._get(
            'DeleteExportedFiles',
            params={
                'envName': env_name,
                'fileName': file_name,
            }
        )

    def DeployApp(
            self,
            env_name: str,
            file_url: str,
            file_name: str,
            context: list[str] = None,
            atomic_deploy: list[bool] = None,
            delay: list[int] = None,
            node_group: list[str] = None,
            hooks: list[str] = None,
            is_sequential: list[bool] = None,
    ):
        """
        :param env_name: target environment name.
        :param file_url: URL to the application archive to be deployed.
        :param file_name: name of the application archive from the Deployment Manager to be deployed.
        :param context: custom context for the application (ROOT by default).
        :param atomic_deploy: defines whether to use zero-downtime deployment for PHP (true) or not (false).
        :param delay: delay (in seconds) between two consecutive deployments when using the sequential deployment type (I.e. when deployment is performed on servers one-by-one to ensure uptime).
        :param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        :param hooks: JSON object with custom scripts (actual content) to be executed before and after the build/deployment operations. For example: {"preDeploy":"script", "postDeploy":"script", "preBuild":"script", "postBuild":"script"}.
        :param is_sequential: defines whether to deploy the project on application servers one-by-one to ensure uptime (true) or simultaneously (false).
        """
        return self._get(
            'DeployApp',
            params={
                'envName': env_name,
                'fileUrl': file_url,
                'fileName': file_name,
                'context': context,
                'atomicDeploy': atomic_deploy,
                'delay': delay,
                'nodeGroup': node_group,
                'hooks': hooks,
                'isSequential': is_sequential,
            },
            delimiter=",",
        )

    def DetachEnvGroup(
            self,
            env_name: str,
            env_group: str,
    ):
        """
        :param env_name: target environment name.
        :param env_group: target group name or JSON array of group names.
        """
        return self._get(
            'DetachEnvGroup',
            params={
                'envName': env_name,
                'envGroup': env_group,
            }
        )

    def DisableReplication(
            self,
            env_name: str,
            node_group: str,
    ):
        return self._get(
            'DisableReplication',
            params={
                'envName': env_name,
                'nodeGroup': node_group,
            }
        )

    def EditEndpoint(
            self,
            env_name: str,
            id: int,
            name: str,
            private_port: int,
            protocol: str,
    ):
        """
        :param env_name: target environment name.
        :param id: unique identifier of the target endpoint.
        :param name: custom endpoint name.
        :param private_port: local port on the container to connect to via endpoint.
        :param protocol: transport protocol (“TCP” or “UDP”).
        """
        return self._get(
            'EditEndpoint',
            params={
                'envName': env_name,
                'id': id,
                'name': name,
                'privatePort': private_port,
                'protocol': protocol,
            }
        )

    def EditEnvSettings(
            self,
            env_name: str,
            settings: dict,
    ):
        """
        :param settings: {"engine":string,"sslstate":boolean}
        """
        return self._get(
            'EditEnvSettings',
            params={
                'envName': env_name,
                'settings': settings,
            },
            delimiter=",",
        )

    def EditNodeGroup(
            self,
            env_name: str,
            node_group: dict,
    ):
        """
        :param env_name: target environment name.
        :param node_group: JSON object with node group (layer) settings:
        """
        return self._get(
            'EditNodeGroup',
            params={
                'envName': env_name,
                'nodeGroup': node_group,
            },
            delimiter=",",
        )

    def EditRegistryCredentials(
            self,
            filter: dict,
            user: list[str] = None,
            password: list[str] = None,
    ):
        """
        :param filter: JSON object to list parameters that need to be updated:
        :param user: new username to access remote registry.
        :param password: new password to access remote registry.
        """
        return self._get(
            'EditRegistryCredentials',
            params={
                'filter': filter,
                'user': user,
                'password': password,
            },
            delimiter=",",
        )

    def ExecCmd(
            self,
            env_name: str,
            node_type: str,
            command_list: dict,
            say_yes: list[bool] = None,
                ):
        return self._get(
            'ExecCmd',
            params={
                'envName': env_name,
                'nodeType': node_type,
                'commandList': command_list,
                'sayYes': say_yes,
            },
            delimiter=",",
        )

    def ExecCmdByGroup(
            self,
            env_name: str,
            node_group: str,
            command_list: dict,
            say_yes: list[bool] = None,
            Async: list[bool] = None,
                ):
        """
        :param env_name: target environment name.
        :param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        :param command_list: JSON object with a list of commands to execute on the layer:
        :param say_yes: defines whether to automatically confirm any operation if prompted (true) or not (false).
        :param Async: defines whether to run provided commands simultaneously (true) or one-by-one (false).
        """
        return self._get(
            'ExecCmdByGroup',
            params={
                'envName': env_name,
                'nodeGroup': node_group,
                'commandList': command_list,
                'sayYes': say_yes,
                'async': Async,
            },
            delimiter=",",
        )
    def ExecCmdById(
            self,
            env_name: str,
            node_id: int,
            command_list: dict,
            say_yes: list[bool] = None,
                    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        :param command_list: JSON object with a list of commands to execute on the node:
        :param say_yes: defines whether to automatically confirm any operation if prompted (true) or not (false).
        """
        return self._get(
            'ExecCmdById',
            params={
                'envName': env_name,
                'nodeId': node_id,
                'commandList': command_list,
                'sayYes': say_yes,
            },
            delimiter=",",
        )

    def ExecCmdByType(
            self,
            env_name: str,
            node_type: str,
            command_list: dict,
            say_yes: list[bool] = None,
                    ):
        return self._get(
            'ExecCmdByType',
            params={
                'envName': env_name,
                'nodeType': node_type,
                'commandList': command_list,
                'sayYes': say_yes,
            },
            delimiter=",",
        )

    def ExecCmdInner(
            self,
            env_name: str,
            target_app_id: str,
            session: str,
            command_list: dict,
            node_type: list[str] = None,
            node_id: list[int] = None,
            user_name: list[str] = None,
            say_yes: list[bool] = None,
            node_group: list[str] = None,
            Async: list[bool] = None,
                     ):
        return self._get(
            'ExecCmdInner',
            params={
                'envName': env_name,
                'targetAppId': target_app_id,
                'session':session,
                'commandList': command_list,
                'nodeType': node_type,
                'nodeId': node_id,
                'userName': user_name,
                'sayYes': say_yes,
                'nodeGroup': node_group,
                'async': Async,
            },
            delimiter=",",
        )

    def ExecDockerRunCmd(
            self,
            env_name: str,
            node_id: int
                         ):
        return self._get(
            'ExecDockerRunCmd',
            params={
                'envName': env_name,
                'nodeId': node_id,
            }
        )

    def Export(
            self,
            env_name: str,
            settings: str,
               ):
        return self._get(
            'Export',
            params={
                'envName': env_name,
                'settings': settings,
            }
        )

    def Finish(self):
        pass

    def FireWallStatus(self):
        pass

    def GetActiveEnvs(self):
        pass

    def GetAllSumStatByUid(self):
        pass

    def GetBasicEnvsInfo(self):
        pass

    def GetContainerEntryPoint(self):
        pass

    def GetContainerEnvVars(self):
        pass

    def GetContainerEnvVarsByGroup(self):
        pass

    def GetContainerManifest(self):
        pass

    def GetContainerNodeTags(self):
        pass

    def GetContainerRunCmd(self):
        pass

    def GetContainerRunConfig(self):
        pass

    def GetContainerTags(self):
        pass

    def GetContainerVolumesByGroup(self):
        pass

    def GetContainerVolumesById(self):
        pass

    def GetDockerConfig(self):
        pass

    def GetDockerEntryPoint(self):
        pass

    def GetDockerRunCmd(self):
        pass

    def GetDomainsList(self):
        pass

    def GetEndpoints(self):
        pass

    def GetEngineList(self):
        pass

    def GetEngineTypes(self):
        pass

    def GetEnvInfo(self):
        pass

    def GetEnvProperty(self):
        pass

    def GetEnvs(self):
        pass

    def GetEnvsByCriteria(self):
        pass

    def GetEnvsInfo(self):
        pass

    def GetLogs(self):
        pass

    def GetLogsList(self):
        pass

    def GetNodeGroups(self):
        pass

    def GetNodeInfo(self):
        pass

    def GetNodeMissions(self):
        pass

    def GetNodeSSHKey(self):
        pass

    def GetNodeTags(self):
        pass

    def GetRegions(self):
        pass

    def GetRegionsInner(self):
        pass

    def GetRegistryInfo(self):
        pass

    def GetSSHAccessInfo(self):
        pass

    def GetSharedEnvsByUid(self):
        pass

    def GetSoftwarePackages(self):
        pass

    def GetStats(self):
        pass

    def GetSumStat(self):
        pass

    def GetTemplateManifest(self):
        pass

    def GetTemplates(self):
        pass

    def GetTransferRequest(self):
        pass

    def InstallPackageByGroup(self):
        pass

    def InstallPackageById(self):
        pass

    def InstallSoftwarePackage(self):
        pass

    def LinkDockerNodes(self):
        pass

    def LinkNode(self):
        pass

    def LinkNodes(self):
        pass

    def ManageEnvAttributes(self):
        pass

    def Migrate(self):
        pass

    def ReadLog(self):
        pass

    def RedeployContainerById(self):
        pass

    def RedeployContainers(self):
        pass

    def RedeployContainersByGroup(self):
        pass

    def RemoveApp(self):
        pass

    def RemoveContainerEnvVars(self):
        pass

    def RemoveContainerVolume(self):
        pass

    def RemoveContainerVolumeByGroup(self):
        pass

    def RemoveContainerVolumes(self):
        pass

    def RemoveDockerVolume(self):
        pass

    def RemoveDockerVolumeByGroup(self):
        pass

    def RemoveEndpoint(self):
        pass

    def RemoveEnvPolicy(self):
        pass

    def RemoveEnvProperty(self):
        pass

    def RemoveLog(self):
        pass

    def RemoveNode(self):
        pass

    def RenameApp(self):
        pass

    def ReplicateNodes(self):
        pass

    def ResetContainerPassword(self):
        pass

    def ResetContainerPasswordById(self):
        pass

    def ResetContainerPasswordByType(self):
        pass

    def ResetContainersPasswordByGroup(self):
        pass

    def ResetNodePassword(self):
        pass

    def ResetNodePasswordById(self):
        pass

    def ResetNodePasswordByType(self):
        pass

    def ResetServicePassword(self):
        pass

    def RestartContainer(self):
        pass

    def RestartContainerById(self):
        pass

    def RestartContainerByType(self):
        pass

    def RestartContainersByGroup(self):
        pass

    def RestartNodeById(self):
        pass

    def RestartNodes(self):
        pass

    def RestartNodesByGroup(self):
        pass

    def RestartNodesByType(self):
        pass

    def RestartServices(self):
        pass

    def RestoreDump(self):
        pass

    def SendEnvCreatedEmail(self):
        pass

    def SendTransferRequest(self):
        pass

    def SetCloudletsCount(self):
        pass

    def SetCloudletsCountByGroup(self):
        pass

    def SetCloudletsCountById(self):
        pass

    def SetCloudletsCountByType(self):
        pass

    def SetContainerEntryPoint(self):
        pass

    def SetContainerEnvVars(self):
        pass

    def SetContainerEnvVarsByGroup(self):
        pass

    def SetContainerRunCmd(self):
        pass

    def SetDiskLimitByGroup(self):
        pass

    def SetDiskLimitById(self):
        pass

    def SetDockerEntryPoint(self):
        pass

    def SetDockerEnvVars(self):
        pass

    def SetDockerRunCmd(self):
        pass

    def SetDockerVolumesFrom(self):
        pass

    def SetEngineByGroup(self):
        pass

    def SetEnvDisplayName(self):
        pass

    def SetEnvGroup(self):
        pass

    def SetNodeDisplayName(self):
        pass

    def SetNodeGroupDisplayName(self):
        pass

    def SetSLBAccessEnabled(self):
        pass

    def SkipMessage(self):
        pass

    def SleepEnv(self):
        pass

    def StartEnv(self):
        pass

    def StopEnv(self):
        pass

    def UninstallSoftwarePackage(self):
        pass

    def UnlinkDockerNodes(self):
        pass

    def UnpackDocker(self):
        pass
