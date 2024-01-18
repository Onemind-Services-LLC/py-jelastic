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
    def Build(self) -> "_Build":
        """
        This service provides methods to manage Java project deployment from the version control system (VCS) repositories. The process requires a dedicated Maven build automation node that will build and deploy Java projects. With Maven, you can add any public or private project directly from your VCS repository (Git or SVN) using the appropriate link type: http, https, git (or svn). After the addition, Java projects can be deployed to the appropriate application servers.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.Build

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.Build
        """
        return _Build(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Binder(self) -> "_Binder":
        """
        With the platform, you can set your own external domain name for your projects instead of using the default
        hosting provider domain name. Binding can be done in two ways: by adding a CNAME record or by setting A Records.
        A CNAME specifies an alias for a canonical name record in a Domain Name System (DNS) database. If you don't
        have your own Public IP, your URL is an alias for a single canonical name that is associated with a common
        platform IP address in the DNS database. In this case, it's recommended to set your own custom domain by adding
        a CNAME record.
        A Record is an entry in your DNS zone file that maps each domain name to an IP address. When you type
        www.mycustomsite.com, the browser goes to the nameserver for mycustomsite.com and asks for the A Record. This
        record must point to an IP address - it will be the IP address of your web server. Setting your own custom
        external domain name using A Record is more appropriate if you have a personal Public IP address.
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

    @property
    def Deployment(self) -> "_Deployment":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.Deployment

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.Deployment
        """
        return _Deployment(session=self._session, token=self._token, debug=self._debug)

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

    @property
    def Group(self) -> "_Group":
        """
        Categorize environments in the account with the help of the group management API. Such user-defined groups can filter the environment list, allowing a clear-cut view of the projects. Learn more in the documentation.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.Group

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.Group
        """
        return _Group(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def NodeGroup(self) -> "_NodeGroup":
        """
        The nodeGroup API service is used to manage data (parameters) and custom options of the environment layers.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.NodeGroup

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.NodeGroup
        """
        return _NodeGroup(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Security(self) -> "_Security":
        """
        This service is responsible for managing the environment firewall feature. You can get a rules list, manage specific rules, and enable/disable firewalls for environments. Learn more in the documentation.

         >>> from jelastic import Jelastic
         >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
         >>> jelastic.environment.Security

         Ref: https://docs.jelastic.com/api/private/#!/api/environment.Security
        """
        return _Security(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def System(self) -> "_System":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.System

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.System
        """
        return _System(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Tracking(self) -> "_Tracking":
        """
        This service is responsible for the monitoring of actions performed by the user. Learn more in the documentation.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.Tracking

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.Tracking
        """
        return _Tracking(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Trigger(self) -> "_Trigger":
        """
                This service implements the environment's trigger handling and management functionality. There are two types of triggers:

        auto-scaling - custom conditions for nodes' addition (scale out) and removal (scale in) based on the load, which allows implementing automatic horizontal scaling. Learn more in the documentation.
        load alert - custom conditions for email notifications based on the nodes' load, i.e. a particular resource type is above/below the stated value for the designated period.

                 >>> from jelastic import Jelastic
                 >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
                 >>> jelastic.environment.Trigger

                 Ref: https://docs.jelastic.com/api/private/#!/api/environment.Trigger
        """
        return _Trigger(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Vcs(self) -> "_Vcs":
        """
        This service is the tool for managing your VCS (version control system) projects. Configure periodic automatic deployment of the committed changes, and you can work with GIT/SVN repository only. Just commit the updated code to your VCS project. The platform will detect changes and automatically push them to the assigned environment. In contrast to the GIT hooks, the auto-deploy feature does not require configuration on the GIT side and works with SVN.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.Vcs

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.Vcs
        """
        return _Vcs(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Windows(self) -> "_Windows":
        """
        Service provides a flexible structure to manage Environment, obtain statistic information etc.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.Windows

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.Windows
        """
        return _Windows(
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


class _Build(Environment):
    """
    This service provides methods to manage Java project deployment from the version control system (VCS) repositories. The process requires a dedicated Maven build automation node that will build and deploy Java projects. With Maven, you can add any public or private project directly from your VCS repository (Git or SVN) using the appropriate link type: http, https, git (or svn). After the addition, Java projects can be deployed to the appropriate application servers.
     resources that grouped by account.

     Ref: https://docs.jelastic.com/api/private/#!/api/environment.Build
    """

    _endpoint2 = "build"

    def AddProject(
        self,
        autoupdate: bool,
        auto_resolve_conflict: bool,
        env_name: str,
        node_id: int,
        name: str,
        type: str,
        path: str,
        key_id: int = None,
        login: str = None,
        password: str = None,
        target_env: str = None,
        context: str = None,
        branch: str = None,
        interval: str = None,
        delay: int = None,
        deploy_now: bool = None,
        hooks: str = None,
        work_dir: str = None,
        target_node_group: str = None,
        is_sequential: bool = None,
    ):
        return self._get(
            "AddProject",
            params={
                "autoUpdate": autoupdate,
                "autoResolveConflict": auto_resolve_conflict,
                "envName": env_name,
                "nodeId": node_id,
                "name": name,
                "type": type,
                "path": path,
                "keyId": key_id,
                "login": login,
                "password": password,
                "targetEnv": target_env,
                "context": context,
                "branch": branch,
                "interval": interval,
                "delay": delay,
                "deployNow": deploy_now,
                "hooks": hooks,
                "workDir": work_dir,
                "targetNodeGroup": target_node_group,
                "isSequential": is_sequential,
            },
        )

    def AddProjectWithCreds(
        self,
        autoupdate: bool,
        auto_resolve_conflict: bool,
        env_name: str,
        node_id: int,
        name: str,
        type: str,
        path: str,
        target_env: str = None,
        login: str = None,
        password: str = None,
        context: str = None,
        branch: str = None,
        interval: str = None,
        delay: int = None,
        deploy_now: bool = None,
        hooks: str = None,
        work_dir: str = None,
    ):
        """
        param autoupdate: defines whether to enable (true) or disable (false) automatic project updates (only upon code changes in the remote repository); auto-update frequency is set with the interval parameter.
        param auto_resolve_conflict: defines whether to automatically resolve (true) or not (false) merge conflicts (by updating the contradictory files to the repository version, i.e. locally made changes are discarded).
        param env_name: source environment name (with a build node).
        param node_id: unique identifier of the build node.
        param name: project name.
        param type: VCS repository type ("GIT" or "SVN").
        param path: URL to the repository (including protocol).
        param target_env: target environment name (with a Java application server).
        param login: login for authentication in VCS.
        param password: password or token for authentication in VCS.
        param context: custom context name for the deployed project (ROOT by default).
        param branch: remote repository branch (master by default).
        param interval: delay (in minutes) for automatic project updates.
        param delay: delay (in seconds) between two consecutive deployments when using the sequential deployment type (I.e. when deployment is performed on servers one-by-one to ensure uptime).
        param deploy_now: defines whether to just create (false) or create and immediately deploy (true) the project.
        param hooks: JSON object with custom scripts (actual content) to be executed before and after the build/deployment operations. For example: {"preDeploy":"script", "postDeploy":"script", "preBuild":"script", "postBuild":"script"}.
        param work_dir: relative path to the repository subdirectory with application source code.
        """
        return self._get(
            "AddProjectWithCreds",
            params={
                "autoUpdate": autoupdate,
                "autoResolveConflict": auto_resolve_conflict,
                "envName": env_name,
                "nodeId": node_id,
                "name": name,
                "type": type,
                "path": path,
                "targetEnv": target_env,
                "login": login,
                "password": password,
                "context": context,
                "branch": branch,
                "interval": interval,
                "delay": delay,
                "deployNow": deploy_now,
                "hooks": hooks,
                "workDir": work_dir,
            },
        )

    def AddProjectWithKey(
        self,
        autoupdate: bool,
        auto_resolve_conflict: bool,
        env_name: str,
        node_id: int,
        name: str,
        type: str,
        path: str,
        target_env: str = None,
        key_id: int = None,
        context: str = None,
        branch: str = None,
        interval: str = None,
        delay: int = None,
        deploy_now: bool = None,
        hooks: str = None,
        work_dir: str = None,
    ):
        """
        param autoupdate: Defines whether to enable (true) or disable (false) automatic project updates (only upon code changes in the remote repository); auto-update frequency is set with the interval parameter.
        param auto_resolve_conflict: defines whether to automatically resolve (true) or not (false) merge conflicts (by updating the contradictory files to the repository version, i.e. locally made changes are discarded).
        param env_name: source environment name (with a build node).
        param node_id: unique identifier of the build node.
        param name: project name.
        param type: VCS repository type ("GIT" or "SVN").
        param path: URL to the repository (including protocol).
        param target_env: target environment name (with a Java application server).
        param key_id: unique identifier of a private SSH key on the account. It can be found in the dashboard (account Settings > SSH Keys > Private Keys) or fetched with the Management > Account > GetSSHKeys method.
        param context: custom context name for the deployed project (ROOT by default).
        param branch: remote repository branch (master by default).
        param interval: delay (in minutes) for automatic project updates.
        param delay: delay (in seconds) between two consecutive deployments when using the sequential deployment type (I.e. when deployment is performed on servers one-by-one to ensure uptime).
        param deploy_now: defines whether to just create (false) or create and immediately deploy (true) the project.
        param hooks: JSON object with custom scripts (actual content) to be executed before and after the build/deployment operations. For example: {"preDeploy":"script", "postDeploy":"script", "preBuild":"script", "postBuild":"script"}.
        param work_dir: relative path to the repository subdirectory with application source code.
        """
        return self._get(
            "AddProjectWithKey",
            params={
                "autoUpdate": autoupdate,
                "autoResolveConflict": auto_resolve_conflict,
                "envName": env_name,
                "nodeId": node_id,
                "name": name,
                "type": type,
                "path": path,
                "targetEnv": target_env,
                "keyId": key_id,
                "context": context,
                "branch": branch,
                "interval": interval,
                "delay": delay,
                "deployNow": deploy_now,
                "hooks": hooks,
                "workDir": work_dir,
            },
        )

    def BuildDeploy(self, env_name: str, project_name: str):
        """
        param env_name: source environment name (with a build node).
        param project_name: project name.
        """
        return self._get(
            "BuildDeploy",
            params={
                "envName": env_name,
                "projectName": project_name,
            },
        )

    def BuildDeployProject(
        self,
        env_name: str,
        node_id: int,
        project_id: str,
        delay: int = None,
        update: bool = None,
        is_sequential: bool = None,
    ):
        """
        param env_name: target environment name.
        param node_id: unique identifier of the build node.
        param project_id: unique identifier of the added project that should be built and deployed.
        param delay: delay (in seconds) between two consecutive deployments when using the sequential deployment type (I.e. when deployment is performed on servers one-by-one to ensure uptime).
        param update: defines whether to update (true) or not (false) the project before deployment.
        param is_sequential: defines whether to deploy project on application servers one-by-one to ensure uptime (true) or simultaneously (false).
        """
        return self._get(
            "BuildDeployProject",
            params={
                "envName": env_name,
                "nodeid": node_id,
                "projectid": project_id,
                "delay": delay,
                "update": update,
                "isSequential": is_sequential,
            },
        )

    def BuildProject(
        self,
        env_name: str,
        node_id: int,
        project_id: str,
        update: bool = None,
        skip_publish: bool = None,
        asyncs: bool = None,
    ):
        """
        param env_name: source environment name (with a build node).
        param node_id: unique identifier of the build node.
        param project_id: unique identifier of the added project that should be built.
        param update: defines whether to update (true) or not (false) the project before building.
        param skip_publish: defines whether to add built project to the Deployment Manager (false) or not (true).
        param asyncs: defines whether to build projects asynchronously (true) or not (false).
        """
        return self._get(
            "BuildProject",
            params={
                "envName": env_name,
                "nodeid": node_id,
                "projectid": project_id,
                "update": update,
                "skipPublish": skip_publish,
                "async": asyncs,
            },
        )

    def DeployProject(
        self,
        env_name: str,
        node_id: int,
        project_id: str,
        delay: int = None,
        is_sequential: bool = None,
    ):
        """
        param env_name: source environment name (with a build node).
        param node_id: unique identifier of the build node.
        param project_id: unique identifier of the built project that should be deployed.
        param delay: delay (in seconds) between two consecutive deployments when using the sequential deployment type (I.e. when deployment is performed on servers one-by-one to ensure uptime).
        param is_sequential: defines whether to use sequential (true) or simultaneous (false) deployment type; the former can ensure uptime, and the latter is faster.
        """
        return self._get(
            "DeployProject",
            params={
                "envName": env_name,
                "nodeid": node_id,
                "projectid": project_id,
                "delay": delay,
                "isSequential": is_sequential,
            },
        )

    def EditProject(
        self,
        env_name: str,
        node_id: int,
        project_id: int,
        name: str,
        type: str,
        path: str,
        key_id: int = None,
        login: str = None,
        password: str = None,
        env: str = None,
        context: str = None,
        branch: str = None,
        autoupdate: bool = None,
        interval: str = None,
        auto_resolve_conflict: bool = None,
        delay: int = None,
        hooks: str = None,
        work_dir: str = None,
        target_node_group: str = None,
    ):
        """
        param env_name: source environment name (with a build node).
        param node_id: unique identifier of the build node.
        param project_id: unique identifier of the project.
        param name: project name.
        param type: VCS repository type (“GIT” or “SVN”).
        param path: URL to the repository (including protocol).
        param key_id: unique identifier of a private SSH key on the account. It can be found in the dashboard (account Settings > SSH Keys > Private Keys) or fetched with the Management > Account > GetSSHKeys method.
        param login: login for authentication in VCS.
        param password: password or token for authentication in VCS.
        param env: target environment name (with a Java application server).
        param context: custom context name for the deployed project (ROOT by default).
        param branch: remote repository branch (master by default).
        param autoupdate: defines whether to enable (true) or disable (false) automatic project updates (only upon code changes in the remote repository); auto-update frequency is set with the interval parameter.
        param interval: delay (in minutes) for automatic project updates.
        param auto_resolve_conflict: defines whether to automatically resolve (true) or not (false) merge conflicts (by updating the contradictory files to the repository version, i.e. locally made changes are discarded).
        param delay:  delay (in seconds) between two consecutive deployments when using the sequential deployment type (I.e. when deployment is performed on servers one-by-one to ensure uptime).
        param hooks: JSON object with custom scripts (actual content) to be executed before and after the build/deployment operations. For example: {"preDeploy":"script", "postDeploy":"script", "preBuild":"script", "postBuild":"script"}.
        param work_dir: relative path to the repository subdirectory with application source code.
        param target_node_group: target node group (layer) with Java application servers.
        """
        return self._get(
            "EditProject",
            params={
                "envName": env_name,
                "nodeid": node_id,
                "projectid": project_id,
                "name": name,
                "type": type,
                "path": path,
                "keyId": key_id,
                "login": login,
                "password": password,
                "env": env,
                "context": context,
                "branch": branch,
                "autoUpdate": autoupdate,
                "interval": interval,
                "autoResolveConflict": auto_resolve_conflict,
                "delay": delay,
                "hooks": hooks,
                "workDir": work_dir,
                "targetNodeGroup": target_node_group,
            },
        )

    def GetProjectInfo(
        self,
        env_name: str,
        node_id: int,
        project_id: int = None,
        project_name: str = None,
    ):
        """
        param env_name: source environment name (with a build node).
        param node_id: unique identifier of the build node.
        param project_id: unique identifier of the project.
        param project_name: project name.
        """
        return self._get(
            "GetProjectInfo",
            params={
                "envName": env_name,
                "nodeid": node_id,
                "projectid": project_id,
                "projectName": project_name,
            },
        )

    def GetProjects(
        self,
        env_name: str,
        node_group: str = None,
        node_id: int = None,
    ):
        """
        param env_name: source environment name (with a build node).
        param node_group: unique identifier of the node group with a build node.
        param node_id: unique identifier of the build node.
        """
        return self._get(
            "GetProjects",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "nodeid": node_id,
            },
        )

    def RemoveProject(
        self,
        env_name: str,
        nodeid: int,
        projectid: int,
    ):
        """
        param env_name: source environment name (with a build node).
        param nodeid: unique identifier of the build node.
        param projectid: unique identifier of the project.
        """
        return self._get(
            "RemoveProject",
            params={
                "envName": env_name,
                "nodeid": nodeid,
                "projectid": projectid,
            },
        )

    def Update(
        self,
        env_name: str,
        node_id: int,
        project_id: int = None,
        context: str = None,
    ):
        """
        param env_name: source environment name (with a build node).
        param nodeid: unique identifier of the build node.
        param projectid: unique identifier of the project.
        param context: custom context name for the deployed project (ROOT by default).
        """
        return self._get(
            "Update",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "projectId": project_id,
                "context": context,
            },
        )


class _Deployment(Environment):
    """
    The Deployment API methods implement extensive Deployment Manager functionality, including application installation (from archive packages and remote Git/SVN repositories) and management (update, rename, context undeploy, etc.). If working with Java projects from the VCS repository, a special Maven build node is used for the source's compilation, which requires separate API methods.

    Based on this, three method types can be distinguished the below-listed methods can be conditionally divided into three groups:

    for Maven build node - AddBuildProject, EditBuildProject, GetBuildProjectInfo, RemoveBuildProject, GetBuildProjects, BuildProject, BuildDeployProject, DeployProject, Update
    for Deployment Manager - Deploy, DeployArchive, AddRepo, EditRepo, GetRepos, RemoveRepo
    for already deployed projects - EditProject, GetProjectInfo, RenameContext, Undeploy, Update

    Ref: https://docs.jelastic.com/api/private/#!/api/environment.Deployment
    """

    _endpoint2 = "deployment"

    def AddBuildProject(
        self,
        env_name: str,
        node_id: int,
        name: str,
        repo: str,
        deployment: dict = None,
        settings: dict = None,
        hooks: str = None,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_id: unique identifier of the build node.
        param name: project name.
        param repo: unique identifier of a repository in the Deployment Manager (e.g. 1 or {"id":1}) or JSON object with repository access details {"url":"...", ["login":"..."], ["password":"..."], ["branch":"..."], ["type":"GIT/SVN"], ["keyId":1]}
        param deployment: JSON object with deployment data:
        param settings: JSON object with additional deployment settings:
        param hooks: JSON object with custom scripts (actual content) to be executed before and after the build/deployment operations. For example: {"preDeploy":"script", "postDeploy":"script", "preBuild":"script", "postBuild":"script"}.
        """
        return self._get(
            "AddBuildProject",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "name": name,
                "repo": repo,
                "deployment": deployment,
                "settings": settings,
                "hooks": hooks,
            },
        )

    def AddRepo(
        self,
        name: str,
        url: str,
        type: str = None,
        branch: str = None,
        key_id: int = None,
        login: str = None,
        password: str = None,
        description: str = None,
    ):
        """
        param name: project name.
        param url: URL to the repository with the project sources.
        param type: VCS repository type ("GIT" or "SVN").
        param branch: remote repository branch (master by default).
        param key_id: unique identifier of a private SSH key on the account. It can be found in the dashboard (account Settings > SSH Keys > Private Keys) or fetched with the GetSSHKeys method.
        param login: login for authentication in VCS.
        param password: password or token for authentication in VCS.
        param description: custom description for the project.
        """
        return self._get(
            "AddRepo",
            params={
                "name": name,
                "url": url,
                "type": type,
                "branch": branch,
                "keyId": key_id,
                "login": login,
                "password": password,
                "description": description,
            },
        )

    def BuildDeployProject(
        self,
        env_name: str,
        node_id: int,
        project: str,
        skip_update: bool = None,
        delay: bool = None,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_id: unique identifier of the build node.
        param project: unique identifier or name of the project.
        param skip_update: defines whether to update (false) or not (true) the project from the VCS source files.
        param delay: delay (in seconds) between two consecutive deployments when using the sequential deployment type (i.e. when deployment is performed on servers one-by-one to ensure uptime).
        """
        return self._get(
            "BuildDeployProject",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "project": project,
                "skipUpdate": skip_update,
                "delay": delay,
            },
        )

    def BuildProject(
        self,
        env_name: str,
        node_id: int,
        project: str,
        skip_upload: bool = None,
        skip_update: bool = None,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_id: unique identifier of the build node.
        param project: unique identifier or name of the project.
        param skip_update: defines whether to update (false) or not (true) the project from the VCS source files.
        param skip_upload: defines whether to add built project to the Deployment Manager (false) or not (true).
        """
        return self._get(
            "BuildProject",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "project": project,
                "skipUpload": skip_upload,
                "skipUpdate": skip_update,
            },
        )

    def Deploy(
        self,
        env_name: str,
        repo: str,
        context: str,
        node_group: str = None,
        build_node_id: int = None,
        settings: dict = None,
        hooks: str = None,
        delay: int = None,
    ):
        """
        param env_name: target environment name (with a build node).
        param repo: unique identifier of a repository in the Deployment Manager (e.g. 1 or {"id":1}) or JSON object with repository access details {"url":"...", ["login":"..."], ["password":"..."], ["branch":"..."], ["type":"GIT/SVN"], ["keyId":1]}
        param context: target context name of the deployed project.
        param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        param build_node_id: unique identifier of a Maven build node (for Java-based projects only).
        param settings: JSON object with the deployment settings:
        param hooks: JSON object with custom scripts (actual content) to be executed before and after the build/deployment operations. For example: {"preDeploy":"script", "postDeploy":"script", "preBuild":"script", "postBuild":"script"}.
        param delay: delay (in seconds) between two consecutive deployments when using the sequential deployment type (i.e. when deployment is performed on servers one-by-one to ensure uptime).

        """
        return self._get(
            "Deploy",
            params={
                "envName": env_name,
                "repo": repo,
                "context": context,
                "nodeGroup": node_group,
                "buildNodeId": build_node_id,
                "settings": settings,
                "hooks": hooks,
                "delay": delay,
            },
        )

    def DeployArchive(
        self,
        env_name: str,
        file_url: str,
        file_name: str,
        node_group: str = None,
        context: str = None,
        zdt: bool = None,
        hooks: str = None,
        delay: int = None,
    ):
        """
        param env_name: target environment name (with a build node).
        param file_url: URL to the archive file.
        param file_name: archive file name from the Deployment Manager storage.
        param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        param context: custom context name for the deployed project (ROOT by default).
        param zdt: defines whether to use zero-downtime deployment for PHP (true) or not (false).
        param hooks: JSON object with custom scripts (actual content) to be executed before and after the build/deployment operations. For example: {"preDeploy":"script", "postDeploy":"script", "preBuild":"script", "postBuild":"script"}.
        param delay: delay (in seconds) between two consecutive deployments when using the sequential deployment type (i.e. when deployment is performed on servers one-by-one to ensure uptime).

        """
        return self._get(
            "DeployArchive",
            params={
                "envName": env_name,
                "fileUrl": file_url,
                "fileName": file_name,
                "nodeGroup": node_group,
                "context": context,
                "zdt": zdt,
                "hooks": hooks,
                "delay": delay,
            },
        )

    def DeployProject(
        self,
        env_name: str,
        node_id: int,
        project: str,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_id: unique identifier of the build node.
        param project: unique identifier or name of the project.
        """
        return self._get(
            "DeployProject",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "project": project,
            },
        )

    def EditBuildProject(
        self,
        env_name: str,
        node_id: int,
        project: str,
        name: str = None,
        repo: str = None,
        deployment: dict = None,
        settings: dict = None,
        hooks: str = None,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_id: unique identifier of the build node.
        param project: unique identifier or name of the project
        param name:New project name.
        param repo: unique identifier of a repository in the Deployment Manager (e.g. 1 or {"id":1}) or JSON object with repository access details {"url":"...", ["login":"..."], ["password":"..."], ["branch":"..."], ["type":"GIT/SVN"], ["keyId":1]}
        param deployment: JSON object with deployment data:
        param settings: JSON object with additional deployment settings:
        param hooks: JSON object with custom scripts (actual content) to be executed before and after the build/deployment operations. For example: {"preDeploy":"script", "postDeploy":"script", "preBuild":"script", "postBuild":"script"}.
        """
        return self._get(
            "EditBuildProject",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "project": project,
                "name": name,
                "repo": repo,
                "deployment": deployment,
                "settings": settings,
                "hooks": hooks,
            },
        )

    def EditProject(
        self,
        env_name: str,
        node_group: str,
        context: str,
        new_context: str = None,
        repo: str = None,
        settings: dict = None,
        hooks: str = None,
        delay: int = None,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        param context: target context name of the deployed project.
        param new_context: new context name for the project (could be the same as Context).
        param repo: unique identifier of a repository in the Deployment Manager (e.g. 1 or {"id":1}) or JSON object with repository access details {"url":"...", ["login":"..."], ["password":"..."], ["branch":"..."], ["type":"GIT/SVN"], ["keyId":1]}
        param deployment: JSON object with deployment data:
        param settings: JSON object with additional deployment settings:
        param hooks: JSON object with custom scripts (actual content) to be executed before and after the build/deployment operations. For example: {"preDeploy":"script", "postDeploy":"script", "preBuild":"script", "postBuild":"script"}.
        param delay: delay (in seconds) between two consecutive deployments when using the sequential deployment type (I.e. when deployment is performed on servers one-by-one to ensure uptime).
        """
        return self._get(
            "EditProject",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "context": context,
                "newContext": new_context,
                "repo": repo,
                "settings": settings,
                "hooks": hooks,
                "delay": delay,
            },
        )

    def EditRepo(
        self,
        id: int,
        name: str = None,
        type: str = None,
        url: str = None,
        branch: str = None,
        key_id: int = None,
        login: str = None,
        password: str = None,
        description: str = None,
    ):
        """
        param id : unique identifier of the repository to be edited.
        param name: project name.
        param url: URL to the repository with the project sources.
        param type: VCS repository type ("GIT" or "SVN").
        param branch: remote repository branch (master by default).
        param key_id: unique identifier of a private SSH key on the account. It can be found in the dashboard (account Settings > SSH Keys > Private Keys) or fetched with the GetSSHKeys method.
        param login: login for authentication in VCS.
        param password: password or token for authentication in VCS.
        param description: custom description for the project.
        """
        return self._get(
            "EditRepo",
            params={
                "id": id,
                "name": name,
                "type": type,
                "url": url,
                "branch": branch,
                "keyId": key_id,
                "login": login,
                "password": password,
                "description": description,
            },
        )

    def GetBuildProjectInfo(
        self,
        env_name: str,
        node_id: int,
        project: str,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_id: unique identifier of the build node.
        param project: unique identifier or name of the project
        """
        return self._get(
            "GetBuildProjectInfo",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "project": project,
            },
        )

    def GetBuildProjects(
        self,
        env_name: str,
        node_group: str = None,
        node_id: int = None,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        param node_id: unique identifier of the build node.
        """
        return self._get(
            "GetBuildProjects",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "nodeId": node_id,
            },
        )

    def GetDeployments(self, env_name: str, node_group: str):
        """
        param env_name: target environment name (with a build node).
        param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        """
        return self._get(
            "GetDeployments",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
            },
        )

    def GetHooks(
        self,
        env_name: str,
        node_group: str = None,
        node_id: int = None,
        context: str = None,
        project: str = None,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        param node_id: unique identifier of the target node (container).
        param context: target context name of the deployed project.
        param project: unique identifier or name of the project.
        """
        return self._get(
            "GetHooks",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "nodeId": node_id,
                "context": context,
                "project": project,
            },
        )

    def GetProjectInfo(
        self,
        env_name: str,
        context: str,
        node_group: str = None,
    ):
        """
        param env_name: target environment name (with a build node).
        param context: target context name of the deployed project.
        param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        """
        return self._get(
            "GetProjectInfo",
            params={
                "envName": env_name,
                "context": context,
                "nodeGroup": node_group,
            },
        )

    def GetRepos(
        self,
        id: int = None,
    ):
        """
        param id: unique identifier of the repository.
        """
        return self._get(
            "GetRepos",
            params={
                "id": id,
            },
        )

    def RemoveBuildProject(
        self,
        env_name: str,
        node_id: str,
        project: str,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_id: unique identifier of the target node (container).
        param project: unique identifier or name of the project.
        """
        return self._get(
            "RemoveBuildProject",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "project": project,
            },
        )

    def RemoveRepo(self, id: int):
        """
        param id: unique identifier of the repository.
        """
        return self._get(
            "RemoveRepo",
            params={
                "id": id,
            },
        )

    def RenameContext(
        self,
        env_name: str,
        node_group: str,
        old_context: str,
        new_context: str,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        param old_context: target context name of the deployed project.
        param new_context: new context name for the project (could be the same as Context).
        """
        return self._get(
            "RenameContext",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "oldContext": old_context,
                "newContext": new_context,
            },
        )

    def Undeploy(
        self,
        env_name: str,
        node_group: str,
        context: str,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        param context: target context name of the deployed project.
        """
        return self._get(
            "Undeploy",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "context": context,
            },
        )

    def Update(
        self,
        env_name: str,
        node_group: str = None,
        node_id: int = None,
        context: str = None,
        project: str = None,
        delay: str = None,
    ):
        """
        param env_name: target environment name (with a build node).
        param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        param node_id: unique identifier of the target node (container).
        param context: target context name of the deployed project.
        param project: unique identifier or name of the project.
        param delay: delay (in seconds) between two consecutive deployments when using the sequential deployment type (I.e. when deployment is performed on servers one-by-one to ensure uptime).
        """
        return self._get(
            "Update",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "nodeId": node_id,
                "context": context,
                "project": project,
                "delay": delay,
            },
        )


class _Binder(Environment):
    """
    With the platform, you can set your own external domain name for your projects instead of using the default hosting provider domain name. Binding can be done in two ways: by adding a CNAME record or by setting A Records.

     A CNAME specifies an alias for a canonical name record in a Domain Name System (DNS) database. If you don't have your own Public IP, your URL is an alias for a single canonical name that is associated with a common platform IP address in the DNS database. In this case, it's recommended to set your own custom domain by adding a CNAME record.

     A Record is an entry in your DNS zone file that maps each domain name to an IP address. When you type www.mycustomsite.com, the browser goes to the nameserver for mycustomsite.com and asks for the A Record. This record must point to an IP address - it will be the IP address of your web server. Setting your own custom external domain name using A Record is more appropriate if you have a personal Public IP address.

     Also, you can bind Custom SSL to your custom domain.

     Ref: https://docs.jelastic.com/api/private/#!/api/environment.Binder
    """

    _endpoint2 = "binder"

    def AddDomains(
        self,
        env_name: str,
        domains: list[str] = None,
        node_group: str = None,
        node_id: int = None,
        subdomain: str = None,
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
        interm: str = None,
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
        )

    def AttachExtIp(
        self,
        env_name: str,
        nodeid: int,
        type: str = None,
    ):
        return self._get(
            "AttachExtIp",
            params={
                "envName": env_name,
                "nodeid": nodeid,
                "type": type,
            },
        )

    def BindExtDomain(
        self,
        env_name: str,
        extdomain: str,
        cert_id: int = None,
    ):
        return self._get(
            "BindExtDomain",
            params={
                "envName": env_name,
                "extdomain": extdomain,
                "certId": cert_id,
            },
        )

    def BindExtDomains(
        self,
        env_name: str,
        extdomains: list[str] = None,
        cert_id: int = None,
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
        entry_point: str = None,
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
        region: str = None,
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
        key: str = None,
        cert: str = None,
        interm: str = None,
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
        node_group: str = None,
        node_id: int = None,
        in_short: bool = None,
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
        self, env_name: str, node_id: int = None, enabled: bool = None
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
        )

    def MoveExtIps(
        self,
        env_name: str,
        source_node_id: int,
        target_node_id: int,
        ips: list[str] = None,
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
            delimiter=",",
        )

    def RemoveDomains(
        self,
        env_name: str,
        domains: list[str] = None,
        node_group: str = None,
        node_id: int = None,
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
        ids: list[str] = None,
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
            delimiter=",",
        )

    def SetExtIpCount(
        self,
        env_name: str,
        type: str,
        count: int,
        node_group: str = None,
        node_id: int = None,
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
        source_ip: str = None,
        target_ip: str = None,
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

    _endpoint2 = "control"

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
            },
        )

    def AddBackends(
        self,
        env_name: str,
        backend_node_id: str,
        balancer_node_id: str,
    ):
        return self._get(
            "AddBackends",
            params={
                "envName": env_name,
                "backendNodeId": backend_node_id,
                "balancerNodeId": balancer_node_id,
            },
        )

    def AddBalancerNode(
        self,
        env_name: str,
        node_type: str,
        cloud_lets: int = None,
        exp_ip: bool = None,
        flexible_cloud_lets: int = None,
        fixed_cloud_lets: int = None,
        display_name: str = None,
        node_group: str = None,
        disk_limit: int = None,
        tag: str = None,
        metadata: str = None,
        start_service: bool = None,
        exp_ipv6_count: int = None,
        exp_ip_count: int = None,
        node_group_data: str = None,
    ):
        return self._get(
            "AddBalancerNode",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "cloudLets": cloud_lets,
                "expIp": exp_ip,
                "flexibleCloudlets": flexible_cloud_lets,
                "fixedCloudlets": fixed_cloud_lets,
                "displayName": display_name,
                "nodeGroup": node_group,
                "diskLimit": disk_limit,
                "tag": tag,
                "metadata": metadata,
                "startService": start_service,
                "extIpv6Count": exp_ipv6_count,
                "extIpCount": exp_ip_count,
                "nodeGroupData": node_group_data,
            },
        )

    def AddBuildNode(
        self,
        env_name: str,
        node_type: str,
        cloud_lets: int = None,
        node_id: int = None,
        exp_ip: bool = None,
        flexible_cloud_lets: int = None,
        fixed_cloud_lets: int = None,
        display_name: str = None,
        node_group: str = None,
        tag: str = None,
        metadata: str = None,
        start_service: bool = None,
        engine: str = None,
        exp_ipv6_count: int = None,
        exp_ip_count: int = None,
        node_group_data: str = None,
        disk_limit: int = None,
    ):
        return self._get(
            "AddBuildNode",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "cloudlets": cloud_lets,
                "nodeId": node_id,
                "expIp": exp_ip,
                "flexibleCloudlets": flexible_cloud_lets,
                "fixedCloudlets": fixed_cloud_lets,
                "displayName": display_name,
                "nodeGroup": node_group,
                "tag": tag,
                "metadata": metadata,
                "startService": start_service,
                "engine": engine,
                "extIpv6Count": exp_ipv6_count,
                "extIpCount": exp_ip_count,
                "nodeGroupData": node_group_data,
                "diskLimit": disk_limit,
            },
        )

    def AddCacheNode(
        self,
        env_name: str,
        node_type: str,
        cloud_lets: int = None,
        flexible_cloud_lets: int = None,
        fixed_cloud_lets: int = None,
        display_name: str = None,
        node_group: str = None,
        disk_limit: int = None,
        tag: str = None,
        metadata: str = None,
        start_service: bool = None,
        exp_ipv6_count: int = None,
        exp_ip_count: int = None,
        node_group_data: str = None,
    ):
        return self._get(
            "AddCacheNode",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "cloudlets": cloud_lets,
                "flexibleCloudlets": flexible_cloud_lets,
                "fixedCloudlets": fixed_cloud_lets,
                "displayName": display_name,
                "nodeGroup": node_group,
                "diskLimit": disk_limit,
                "tag": tag,
                "metadata": metadata,
                "startService": start_service,
                "expIpv6Count": exp_ipv6_count,
                "expIpCount": exp_ip_count,
                "nodeGroupData": node_group_data,
            },
        )

    def AddComputeNode(
        self,
        env_name: str,
        node_type: str,
        cloud_lets: int = None,
        is_master: int = None,
        exp_ip: bool = None,
        flexible_cloud_lets: int = None,
        fixed_cloud_lets: int = None,
        display_name: str = None,
        node_group: str = None,
        disk_limit: int = None,
        tag: str = None,
        metadata: bool = None,
        start_service: bool = None,
        engine: str = None,
        exp_ipv6_count: int = None,
        exp_ip_count: int = None,
        node_group_data: str = None,
    ):
        return self._get(
            "AddComputeNode",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "cloudlets": cloud_lets,
                "isMaster": is_master,
                "expIp": exp_ip,
                "flexibleCloudlets": flexible_cloud_lets,
                "fixedCloudlets": fixed_cloud_lets,
                "displayName": display_name,
                "nodeGroup": node_group,
                "diskLimit": disk_limit,
                "tag": tag,
                "metadata": metadata,
                "startService": start_service,
                "engine": engine,
                "expIpv6Count": exp_ipv6_count,
                "expIpCount": exp_ip_count,
                "nodeGroupData": node_group_data,
            },
        )

    def AddContainerEnvVars(
        self,
        env_name: str,
        vars: dict,
        node_group: str = None,
        node_id: int = None,
    ):
        """
        :param env_name: target environment name.
        :param vars: JSON object with a list of container environment variables, e.g. {"var1":"value1", "var2":"value2"}
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "AddContainerEnvVars",
            params={
                "envName": env_name,
                "vars": vars,
                "nodeGroup": node_group,
                "nodeId": node_id,
            },
        )

    def AddContainerVolume(
        self,
        env_name: str,
        node_id: int,
        path: str,
    ):
        return self._get(
            "AddContainerVolume",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "path": path,
            },
        )

    def AddContainerVolumeByGroup(
        self,
        env_name: str,
        node_group: str,
        path: str,
    ):
        return self._get(
            "AddContainerVolumeByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "path": path,
            },
        )

    def AddContainerVolumes(
        self,
        env_name: str,
        volumes: str,
        node_group: str = None,
        node_id: int = None,
    ):
        """
        :param env_name: target environment name
        :param volumes: an array of data volumes to be added, e.g. /data/volume or ["/data/volume","/data/volume2", ...]
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "AddContainerVolumes",
            params={
                "envName": env_name,
                "volumes": volumes,
                "nodeGroup": node_group,
                "nodeId": node_id,
            },
        )

    def AddContext(
        self,
        env_name: str,
        name: str,
        file_name: str,
        type: str,
        node_group: str = None,
    ):
        """
        :param env_name: target environment name
        :param name: context name for the application
        """
        return self._get(
            "AddContext",
            params={
                "envName": env_name,
                "name": name,
                "fileName": file_name,
                "type": type,
                "nodeGroup": node_group,
            },
        )

    def AddDBNode(
        self,
        env_name: str,
        node_type: str,
        cloud_lets: int = None,
        exp_ip: bool = None,
        password: str = None,
        flexible_cloud_lets: int = None,
        fixed_cloud_lets: int = None,
        display_name: str = None,
        node_group: str = None,
        disk_limit: int = None,
        tag: str = None,
        metadata: bool = None,
        start_service: bool = None,
        exp_ipv6_count: int = None,
        exp_ip_count: int = None,
        node_group_data: str = None,
    ):
        return self._get(
            "AddDBNode",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "cloudlets": cloud_lets,
                "expIp": exp_ip,
                "password": password,
                "flexibleCloudlets": flexible_cloud_lets,
                "fixedCloudlets": fixed_cloud_lets,
                "displayName": display_name,
                "nodeGroup": node_group,
                "diskLimit": disk_limit,
                "tag": tag,
                "metadata": metadata,
                "startService": start_service,
                "expIpv6Count": exp_ipv6_count,
                "expIpCount": exp_ip_count,
                "nodeGroupData": node_group_data,
            },
        )

    def AddDockerNode(
        self,
        env_name: str,
        node_type: str,
        metadata: dict,
        cloud_lets: int = None,
        exp_ip: bool = None,
        password: str = None,
        flexible_cloud_lets: int = None,
        fixed_cloud_lets: int = None,
        display_name: str = None,
        node_group: str = None,
        disk_limit: int = None,
        start_service: bool = None,
        exp_ipv6_count: int = None,
        exp_ip_count: int = None,
        node_group_data: str = None,
    ):
        return self._get(
            "AddDockerNode",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "metadata": metadata,
                "cloudlets": cloud_lets,
                "expIp": exp_ip,
                "password": password,
                "flexibleCloudlets": flexible_cloud_lets,
                "fixedCloudlets": fixed_cloud_lets,
                "displayName": display_name,
                "nodeGroup": node_group,
                "diskLimit": disk_limit,
                "startService": start_service,
                "expIpv6Count": exp_ipv6_count,
                "expIpCount": exp_ip_count,
                "nodeGroupData": node_group_data,
            },
        )

    def AddDockerVolume(
        self,
        env_name: str,
        node_id: int,
        path: str,
    ):
        return self._get(
            "AddDockerVolume",
            params={"envName": env_name, "nodeId": node_id, "path": path},
        )

    def AddDockerVolumeByGroup(
        self,
        env_name: str,
        node_group: int,
        path: str,
    ):
        return self._get(
            "AddDockerVolumeByGroup",
            params={"envName": env_name, "nodeGroup": node_group, "path": path},
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
            "AddEndpoint",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "privatePort": private_port,
                "protocol": protocol,
                "name": name,
            },
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
            "AddEnvPolicy",
            params={
                "targetAppId": target_app_id,
                "policy": policy,
            },
        )

    def AddEnvProperty(self, properties: str):
        """
        :param properties: JSON object with environment properties. For example: {"customProperty1":"value1","customProperty2":"value2"}
        """
        return self._get(
            "AddEnvProperty",
            params={
                "properties": properties,
            },
        )

    def AddExtraNode(
        self,
        env_name: str,
        node_type: str,
        cloud_lets: int = None,
        exp_ip: bool = None,
        flexible_cloud_lets: int = None,
        fixed_cloud_lets: int = None,
        display_name: str = None,
        node_group: str = None,
        disk_limit: int = None,
        tag: str = None,
        metadata: bool = None,
        start_service: bool = None,
        exp_ipv6_count: int = None,
        exp_ip_count: int = None,
        node_group_data: str = None,
    ):
        return self._get(
            "AddExtraNode",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "cloudlets": cloud_lets,
                "expIp": exp_ip,
                "flexibleCloudlets": flexible_cloud_lets,
                "fixedCloudlets": fixed_cloud_lets,
                "displayName": display_name,
                "nodeGroup": node_group,
                "diskLimit": disk_limit,
                "tag": tag,
                "metadata": metadata,
                "startService": start_service,
                "expIpv6Count": exp_ipv6_count,
                "expIpCount": exp_ip_count,
                "nodeGroupData": node_group_data,
            },
        )

    def AddNode(
        self,
        env_name: str,
        node_type: str,
        cloud_lets: int = None,
        ext_ip: str = None,
        password: str = None,
        flexible_cloud_lets: int = None,
        fixed_cloud_lets: int = None,
        display_name: str = None,
        metadata: str = None,
        node_group: str = None,
        start_service: bool = None,
        disk_limit: int = None,
        tag: str = None,
        engine: str = None,
        exit_ipv4: int = None,
        exit_ipv6: int = None,
        node_group_data: str = None,
        options: str = None,
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
            "AddNode",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "cloudLets": cloud_lets,
                "extIp": ext_ip,
                "password": password,
                "flexibleCloudLets": flexible_cloud_lets,
                "fixedCloudLets": fixed_cloud_lets,
                "displayName": display_name,
                "metadata": metadata,
                "nodeGroup": node_group,
                "startService": start_service,
                "diskLimit": disk_limit,
                "tag": tag,
                "engine": engine,
                "extipv4": exit_ipv4,
                "extipv6": exit_ipv6,
                "nodeGroupData": node_group_data,
                "options": options,
            },
        )

    def AddPortRedirect(
        self,
        env_name: str,
        node_id: int,
        src_port: int,
        dst_port: int,
        protocol: str,
        comments: str = None,
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        :param src_port: source port on the container.
        :param dst_port: destination port on the container.
        :param protocol: transport protocol (“TCP” or “UDP”).
        :param comments: custom comment for the redirect.
        """
        return self._get(
            "AddPortRedirect",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "srcPort": src_port,
                "dstPort": dst_port,
                "protocol": protocol,
                "comments": comments,
            },
        )

    def AddStorageNode(
        self,
        env_name: str,
        node_type: str,
        cloud_lets: int = None,
        ext_ip: str = None,
        flexible_cloud_lets: int = None,
        fixed_cloud_lets: int = None,
        display_name: str = None,
        node_group: str = None,
        disk_limit: int = None,
        tag: str = None,
        metadata: str = None,
        start_service: bool = None,
        ext_ipv6_count: int = None,
        ext_ip_count: int = None,
        node_group_data: str = None,
    ):
        return self._get(
            "AddStorageNode",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "cloudlets": cloud_lets,
                "extIp": ext_ip,
                "flexibleCloudLets": flexible_cloud_lets,
                "fixedCloudLets": fixed_cloud_lets,
                "displayName": display_name,
                "nodeGroup": node_group,
                "diskLimit": disk_limit,
                "tag": tag,
                "metadata": metadata,
                "startService": start_service,
                "extIpv6Count": ext_ipv6_count,
                "extIpCount": ext_ip_count,
                "nodeGroupData": node_group_data,
            },
        )

    def AddVdsNode(
        self,
        env_name: str,
        node_type: str,
        cloud_lets: int = None,
        ext_ip: str = None,
        password: str = None,
        flexible_cloud_lets: int = None,
        fixed_cloud_lets: int = None,
        display_name: str = None,
        node_group: str = None,
        disk_limit: int = None,
        tag: str = None,
        metadata: str = None,
        start_service: bool = None,
        ext_ipv6_count: int = None,
        ext_ip_count: int = None,
        node_group_data: str = None,
    ):
        return self._get(
            "AddVdsNode",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "cloudlets": cloud_lets,
                "extIp": ext_ip,
                "password": password,
                "flexibleCloudLets": flexible_cloud_lets,
                "fixedCloudLets": fixed_cloud_lets,
                "displayName": display_name,
                "nodeGroup": node_group,
                "diskLimit": disk_limit,
                "tag": tag,
                "metadata": metadata,
                "startService": start_service,
                "extIpv6Count": ext_ipv6_count,
                "extIpCount": ext_ip_count,
                "nodeGroupData": node_group_data,
            },
        )

    def AddVmNode(
        self,
        env_name: str,
        node_type: str,
        options: str,
        ext_ip: str = None,
        display_name: str = None,
        node_group: str = None,
        disk_limit: int = None,
        ext_ipv6_count: int = None,
        ext_ip_count: int = None,
        node_group_data: str = None,
        password: str = None,
    ):
        return self._get(
            "AddVmNode",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "options": options,
                "extIp": ext_ip,
                "displayName": display_name,
                "nodeGroup": node_group,
                "diskLimit": disk_limit,
                "extIpv6Count": ext_ipv6_count,
                "extIpCount": ext_ip_count,
                "nodeGroupData": node_group_data,
                "password": password,
            },
        )

    def AppendNodes(
        self,
        env_name: str,
        count: int,
        node_type: str,
    ):
        return self._get(
            "AppendNodes",
            params={
                "envName": env_name,
                "count": count,
                "nodeType": node_type,
            },
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
            "ApplyEnvProperty",
            params={
                "envName": env_name,
                "properties": properties,
            },
        )

    def ApplyNodeGroupData(
        self,
        env_name: str,
        node_group_data: str,
        data: str,
    ):
        return self._get(
            "ApplyNodeGroupData",
            params={
                "envName": env_name,
                "nodeGroupData": node_group_data,
                "data": data,
            },
        )

    def ApplySoftwarePackageAction(
        self,
        env_name: str,
        keywords: str,
        node_type: str = None,
        action: str = None,
        password: str = None,
        node_group: str = None,
    ):
        return self._get(
            "ApplySoftwarePackageAction",
            params={
                "envName": env_name,
                "keywords": keywords,
                "nodeType": node_type,
                "action": action,
                "password": password,
                "nodeGroup": node_group,
            },
        )

    def AttachEnvGroup(
        self,
        env_name: str,
        env_group_name: str,
    ):
        return self._get(
            "AttachEnvGroup",
            params={
                "envName": env_name,
                "envGroup": env_group_name,
            },
        )

    def BuildCluster(
        self,
        env_name: str,
        node_group: str,
    ):
        return self._get(
            "BuildCluster", params={"envName": env_name, "nodeGroup": node_group}
        )

    def CancelTransferRequest(self):
        return self._get("CancelTransferRequest", params={})

    def ChangeLimits(self, env_name: str):
        return self._get("ChangeLimits", params={"envName": env_name})

    def ChangeLimitsInner(
        self,
        env_name: str,
        uid: int,
        limit_type: str = None,
    ):
        return self._get(
            "ChangeLimitsInner",
            params={
                "envName": env_name,
                "uid": uid,
                "limitType": limit_type,
            },
        )

    def ChangeTopology(
        self, env_name: str, env: dict, nodes: dict, action_key: str = None
    ):
        """
        :param env_name: target environment name.
        :param env: JSON object with environment settings:
        :param nodes: JSON object with a list of environment nodes and their settings:
        :param action_key: name of the action and domain name.
        """
        return self._get(
            "ChangeTopology",
            params={
                "envName": env_name,
                "env": env,
                "nodes": nodes,
                "actionkey": action_key,
            },
        )

    def CheckDependencies(
        self,
        env_name: str,
        node_id: int = None,
        filter: str = None,
    ):
        return self._get(
            "CheckDependencies",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "filter": filter,
            },
        )

    def CheckExtIpCount(
        self,
        exp_ipv6: int,
        exp_ipv4: int = None,
        hardware_node_group: str = None,
    ):
        return self._get(
            "CheckExtIpCount",
            params={
                "expIpv6": exp_ipv6,
                "expIpv4": exp_ipv4,
                "hardwareNodeGroup": hardware_node_group,
            },
        )

    def CheckMigrationPossibility(
        self,
        env_name: str,
        hardware_node_group: str = None,
    ):
        """
        :param env_name: target environment name.
        :param hardware_node_group: unique identifier of the target region (host group).
        """
        return self._get(
            "CheckMigrationPossibility",
            params={
                "envName": env_name,
                "hardwareNodeGroup": hardware_node_group,
            },
        )

    def ClearLog(self, env_name: str, node_id: int, path: str):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        :param path: path to the target log file.
        """
        return self._get(
            "ClearLog",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "path": path,
            },
        )

    def CloneEnv(
        self,
        src_env_name: str,
        dit_env_name: str,
        use_external_mounts: bool = None,
    ):
        """
        :param src_env_name: source environment name (one that is going to be cloned).
        :param dit_env_name: destination (cloned) environment name.
        :param use_external_mounts: defines whether to copy external mounts on the clone (true) or not (false).
        """
        return self._get(
            "CloneEnv",
            params={
                "srcEnvName": src_env_name,
                "ditEnvName": dit_env_name,
                "useExternalMounts": use_external_mounts,
            },
        )

    def CloneNode(
        self,
        env_name: str,
        count: int,
        node_group: str,
        node_id: int = None,
    ):
        return self._get(
            "CloneNode",
            params={
                "envName": env_name,
                "count": count,
                "nodeGroup": node_group,
                "nodeId": node_id,
            },
        )

    def ConfirmTransferRequest(self, key: str):
        """
        :param key: disposable confirmation key
        """
        return self._get(
            "ConfirmTransferRequest",
            params={
                "key": key,
            },
        )

    def CreateEnv(
        self,
        env_name: str,
        settings: dict,
        owner_uid: int = None,
        hardware_node_group: str = None,
        env_groups: str = None,
    ):
        """
        :param env_name: domain of the environment
        :param settings: settings of the environment
        :param owner_uid: unique identifier of the environment's owner
        """
        return self._get(
            "CreateEnv",
            params={
                "envName": env_name,
                "settings": settings,
                "ownerUid": owner_uid,
                "hardwareNodeGroups": hardware_node_group,
                "envGroups": env_groups,
            },
        )

    def CreateEnvironment(
        self,
        env: dict,
        nodes: dict,
        action_key: str = None,
        owner_uid: int = None,
        env_groups: str = None,
    ):
        """
        :param env: JSON object with environment settings:
        :param nodes: JSON object with a list of environment nodes and their settings:
        :param action_key: name of the action and domain name.
        :param owner_uid: unique identifier of the environment owner (if installing as collaborator on another user account).
        :param env_groups: target group name or JSON array of group names.
        """
        return self._get(
            "CreateEnvironment",
            params={
                "env": env,
                "nodes": nodes,
                "actionKey": action_key,
                "ownerUid": owner_uid,
                "envGroups": env_groups,
            },
        )

    def DeleteEnv(
        self,
        env_name: str,
        password: str = None,
    ):
        """
        :param env_name: target environment name.
        :param password: current user password or environment name to confirm environment deletion (depending on the 'environment.delete.confirm.type' quota).
        """
        return self._get(
            "DeleteEnv",
            params={
                "envName": env_name,
                "password": password,
            },
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
            "DeleteExportedFiles",
            params={
                "envName": env_name,
                "fileName": file_name,
            },
        )

    def DeployApp(
        self,
        env_name: str,
        file_url: str,
        file_name: str,
        context: str = None,
        atomic_deploy: bool = None,
        delay: int = None,
        node_group: str = None,
        hooks: str = None,
        is_sequential: bool = None,
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
            "DeployApp",
            params={
                "envName": env_name,
                "fileUrl": file_url,
                "fileName": file_name,
                "context": context,
                "atomicDeploy": atomic_deploy,
                "delay": delay,
                "nodeGroup": node_group,
                "hooks": hooks,
                "isSequential": is_sequential,
            },
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
            "DetachEnvGroup",
            params={
                "envName": env_name,
                "envGroup": env_group,
            },
        )

    def DisableReplication(
        self,
        env_name: str,
        node_group: str,
    ):
        return self._get(
            "DisableReplication",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
            },
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
            "EditEndpoint",
            params={
                "envName": env_name,
                "id": id,
                "name": name,
                "privatePort": private_port,
                "protocol": protocol,
            },
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
            "EditEnvSettings",
            params={
                "envName": env_name,
                "settings": settings,
            },
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
            "EditNodeGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
            },
        )

    def EditRegistryCredentials(
        self,
        filter: dict,
        user: str = None,
        password: str = None,
    ):
        """
        :param filter: JSON object to list parameters that need to be updated:
        :param user: new username to access remote registry.
        :param password: new password to access remote registry.
        """
        return self._get(
            "EditRegistryCredentials",
            params={
                "filter": filter,
                "user": user,
                "password": password,
            },
        )

    def ExecCmd(
        self,
        env_name: str,
        node_type: str,
        command_list: list[dict],
        say_yes: bool = True,
    ):
        return self._get(
            "ExecCmd",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "commandList": command_list,
                "sayYes": say_yes,
            },
        )

    def ExecCmdByGroup(
        self,
        env_name: str,
        node_group: str,
        command_list: list[dict],
        say_yes: bool = True,
        asynchronous: bool = False,
    ):
        """
        :param env_name: target environment name.
        :param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        :param command_list: JSON object with a list of commands to execute on the layer:
        :param say_yes: defines whether to automatically confirm any operation if prompted (true) or not (false).
        :param Async: defines whether to run provided commands simultaneously (true) or one-by-one (false).
        """
        return self._get(
            "ExecCmdByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "commandList": command_list,
                "sayYes": say_yes,
                "async": asynchronous,
            },
        )

    def ExecCmdById(
        self,
        env_name: str,
        node_id: int,
        command_list: list[dict],
        say_yes: bool = True,
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        :param command_list: JSON object with a list of commands to execute on the node:
        :param say_yes: defines whether to automatically confirm any operation if prompted (true) or not (false).
        """
        return self._get(
            "ExecCmdById",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "commandList": command_list,
                "sayYes": say_yes,
            },
        )

    def ExecCmdByType(
        self,
        env_name: str,
        node_type: str,
        command_list: list[dict],
        say_yes: bool = True,
    ):
        return self._get(
            "ExecCmdByType",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "commandList": command_list,
                "sayYes": say_yes,
            },
        )

    def ExecCmdInner(
        self,
        env_name: str,
        target_app_id: str,
        command_list: list[dict],
        node_type: str = None,
        node_id: int = None,
        user_name: str = None,
        node_group: str = None,
        asynchronous: bool = None,
        say_yes: bool = True,
    ):
        return self._get(
            "ExecCmdInner",
            params={
                "envName": env_name,
                "targetAppid": target_app_id,
                "commandList": command_list,
                "nodeType": node_type,
                "nodeId": node_id,
                "userName": user_name,
                "nodeGroup": node_group,
                "async": asynchronous,
                "sayYes": say_yes,
            },
        )

    def ExecDockerRunCmd(self, env_name: str, node_id: int):
        return self._get(
            "ExecDockerRunCmd",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def ExportEnv(
        self,
        env_name: str,
        settings: str,
    ):
        """
        :param env_name: application identifier of the environment
        :param settings: settings for export
        """
        return self._get(
            "ExportEnv",
            params={
                "envName": env_name,
                "settings": settings,
            },
        )

    def Finish(
        self,
        env_name: str,
    ):
        return self._get("Finish", params={"envName": env_name})

    def FireWallStatus(
        self,
        env_name: str,
        node_id: int,
    ):
        return self._get(
            "FireWallStatus",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def GetActiveEnvs(
        self,
        env_name: str,
        domain: str,
        start_time: datetime,
        end_time: datetime,
        checksum: str,
    ):
        return self._get(
            "GetActiveEnvs",
            params={
                "envName": env_name,
                "domain": domain,
                "starttime": start_time,
                "endtime": end_time,
                "checksum": checksum,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetAllSumStatByUid(
        self,
        duration: int = None,
        end_time: datetime = None,
    ):
        """
        :param duration: period (in seconds) to show statistics for.
        :param end_time: end time (UTC) in the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00" (duration must be passed).
        """
        return self._get(
            "GetAllSumStatByUid",
            params={
                "duration": duration,
                "endtime": end_time,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetBasicEnvsInfo(self, owner_uid: int = None):
        """
        :param owner_uid: unique identifier of the target user account.
        """
        return self._get(
            "GetBasicEnvsInfo",
            params={
                "ownerUid": owner_uid,
            },
        )

    def GetContainerEntryPoint(self, env_name: str, node_id: int):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "GetContainerEntryPoint",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def GetContainerEnvVars(
        self,
        env_name: str,
        node_id: int,
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "GetContainerEnvVars",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def GetContainerEnvVarsByGroup(
        self,
        env_name: str,
        node_group: str,
    ):
        """
        :param env_name: target environment name.
        :param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        """
        return self._get(
            "GetContainerEnvVarsByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
            },
        )

    def GetContainerManifest(
        self,
        image: str,
        registry: str = None,
        user_name: str = None,
        password: str = None,
        ignore_format: bool = None,
    ):
        """
        :param image: container's Docker image and tag, e.g. "alpine:latest".
        :param registry: custom remote registry, where the container image is stored (Docker Hub by default).
        :param user_name: username for authentication at the remote registry.
        :param password: password for authentication at the remote registry.
        :param ignore_format: defines whether to ignore image format (true) or not (false).
        """
        return self._get(
            "GetContainerManifest",
            params={
                "image": image,
                "registry": registry,
                "userName": user_name,
                "password": password,
                "ignoreFormat": ignore_format,
            },
        )

    def GetContainerNodeTags(self, env_name: str, node_id: int):
        """
        :params env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "GetContainerNodeTags",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def GetContainerRunCmd(self, env_name: str, node_id: int):
        """
        :params env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "GetContainerRunCmd",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def GetContainerRunConfig(self, env_name: str, node_id: int):
        """
        :params env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "GetContainerRunConfig",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def GetContainerTags(
        self,
        image: str,
        registry: str = None,
        user_name: str = None,
        password: str = None,
    ):
        """
        :params image: container's Docker image and tag, e.g. "alpine:latest".
        :param registry: custom remote registry, where the container image is stored (Docker Hub by default).
        :param user_name: username for authentication at the remote registry.
        :param password: password for authentication at the remote registry.
        """
        return self._get(
            "GetContainerTags",
            params={
                "image": image,
                "registry": registry,
                "userName": user_name,
                "password": password,
            },
        )

    def GetContainerVolumesByGroup(
        self,
        env_name: str,
        node_group: str,
    ):
        """
        :params env_name: target environment name.
        :param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        """
        return self._get(
            "GetContainerVolumesByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
            },
        )

    def GetContainerVolumesById(
        self,
        env_name: str,
        node_id: int,
    ):
        """
        :params env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "GetContainerVolumesById",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def GetDockerConfig(
        self,
        env_name: str,
        node_id: int,
    ):
        return self._get(
            "GetDockerConfig",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def GetDockerEntryPoint(
        self,
        env_name: str,
        node_id: int,
    ):
        return self._get(
            "GetDockerEntryPoint",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def GetDockerRunCmd(
        self,
        env_name: str,
        node_id: int,
    ):
        return self._get(
            "GetDockerRunCmd",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def GetDomainsList(
        self,
        env_name: str,
        checksum: str,
    ):
        return self._get(
            "GetDomainsList",
            params={
                "envName": env_name,
                "checksum": checksum,
            },
        )

    def GetEndpoints(
        self,
        env_name: str,
        node_id: int = None,
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "GetEndpoints",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
            delimiter=",",
        )

    def GetEngineList(
        self,
        type: str = None,
    ):
        """
        :param type: type of the engine (java/php/ruby/js)
        """
        return self._get(
            "GetEngineList",
            params={
                "type": type,
            },
        )

    def GetEngineTypes(self):
        return self._get("GetEngineTypes", params={})

    def GetEnvInfo(
        self,
        env_name: str,
        lazy: bool = None,
    ):
        """
        :param env_name: target environment name.
        :param lazy: defines whether to load only the main environment metadata, e.g. name, alias, domain, etc., (true) or all the environment information (false).
        """
        return self._get(
            "GetEnvInfo",
            params={
                "envName": env_name,
                "lazy": lazy,
            },
        )

    def GetEnvProperty(
        self,
        env_name: str,
        property_keys: list[str] = None,
    ):
        """
        :param env_name: target environment name.
        :param property_keys: a comma-separated list of property keys (all properties if “null” or “empty”). For example: "customProperty1,customProperty2".
        """
        return self._get(
            "GetEnvProperty",
            params={
                "envName": env_name,
                "propertyKeys": property_keys,
            },
            delimiter=",",
        )

    def GetEnvs(
        self,
        lazy: bool = None,
        owner_uid: int = None,
    ):
        """
        :param lazy: defines whether to load only the main environment metadata, e.g. name, alias, domain, etc., (true) or all the environment information (false).
        :param owner_uid: unique identifier of the target user account.
        """
        return self._get(
            "GetEnvs",
            params={
                "lazy": lazy,
                "ownerUid": owner_uid,
            },
        )

    def GetEnvsByCriteria(
        self,
        criteria: dict,
        lazy: bool = None,
    ):
        return self._get(
            "GetEnvsByCriteria",
            params={
                "criteria": criteria,
                "lazy": lazy,
            },
        )

    def GetEnvsInfo(
        self,
        env_name: str,
        target_app_id: str = None,
    ):
        return self._get(
            "GetEnvsInfo",
            params={
                "envName": env_name,
                "targetAppid": target_app_id,
            },
        )

    def GetLogs(
        self,
        env_name: str,
        node_id: int,
        path: str = None,
    ):
        return self._get(
            "GetLogs",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "path": path,
            },
        )

    def GetLogsList(
        self,
        env_name: str,
        node_id: int,
        path: str = None,
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        :params path: custom path to the log files (/var/log by default).
        """
        return self._get(
            "GetLogsList",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "path": path,
            },
        )

    def GetNodeGroups(
        self,
        env_name: str,
    ):
        """
        :param env_name: target environment name
        """
        return self._get(
            "GetNodeGroups",
            params={
                "envName": env_name,
            },
        )

    def GetNodeInfo(
        self,
        node_id: str,
    ):
        """
        :param node_id: node identifier
        """
        return self._get(
            "GetNodeInfo",
            params={
                "GetNodeInfo": node_id,
            },
        )

    def GetNodeMissions(self):
        return self._get("GetNodeMissions", params={})

    def GetNodeSSHKey(
        self,
        env_name: str,
        node_id: int,
        uid: int,
        skip_node_type_check: bool = None,
    ):
        """
        :param node_id: unique identifier of the software node.
        :param skip_node_type_check: ignore 'jelastic.ssh.nodetype.restriction.list'
        """
        return self._get(
            "GetNodeSSHKey",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "uid": uid,
                "skipNodeTypeCheck": skip_node_type_check,
            },
        )

    def GetNodeTags(
        self,
        env_name: str,
        node_id: int,
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "GetNodeTags",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def GetRegions(self):
        return self._get("GetRegions", params={})

    def GetRegionsInner(
        self,
        group_name: str,
        is_enabled: bool = None,
    ):
        """
        :param group_name: unique identifier of the target user group.
        :param is_enabled: defines whether to include only active regions (true) or not (false).
        """
        return self._get(
            "GetRegionsInner",
            params={
                "groupName": group_name,
                "isEnabled": is_enabled,
            },
        )

    def GetRegistryInfo(
        self,
        env_name: str,
        node_group: str,
    ):
        """
        :param env_name: target environment name.
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        """
        return self._get(
            "GetRegistryInfo",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
            },
        )

    def GetSSHAccessInfo(self, node_id: int):
        """
        :param node_id: unique identifier of the target node (container).
        """
        return self._get(
            "GetSSHAccessInfo",
            params={
                "nodeId": node_id,
            },
        )

    def GetSharedEnvsByUid(self, uid: int):
        """
        :param uid: identifier of the target user
        """
        return self._get(
            "GetSharedEnvsByUid",
            params={
                "uid": uid,
            },
        )

    def GetSoftwarePackages(
        self,
        env_name: str,
        node_type: str = None,
        node_group: str = None,
    ):
        """
        :param env_name: target environment name.
        :param node_type: unique identifier of the target node type (software stack), e.g. “tomcat11” for the Tomcat 11 stack.
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        """
        return self._get(
            "GetSoftwarePackages",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "nodeGroup": node_group,
            },
        )

    def GetStats(
        self,
        env_name: str,
        duration: int,
        interval: int,
        end_time: datetime = None,
        node_id: int = None,
        node_type: str = None,
        node_group: str = None,
    ):
        """
        :param env_name: target environment name.
        :param duration: period (in seconds) to show statistics for.
        :param interval: interval (in seconds) to divide the stated period (duration).
        :param end_time: end time (UTC) in the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00" (duration must be passed).
        :node_id: unique identifier of the target node (container).
        :node_type: unique identifier of the target node type (software stack), e.g. “tomcat11” for the Tomcat 11 stack. Required if nodeid is not specified.
        :node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        """
        return self._get(
            "GetStats",
            params={
                "envName": env_name,
                "duration": duration,
                "interval": interval,
                "endtime": end_time,
                "nodeid": node_id,
                "nodetype": node_type,
                "nodeGroup": node_group,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetSumStat(
        self,
        env_name: str,
        duration: int,
        end_time: datetime = None,
    ):
        """
        :param env_name: target environment name
        :params duration: period (in seconds) to show statistics for.
        :param end_time: end time (UTC) in the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00" (duration must be passed).
        """
        return self._get(
            "GetSumStat",
            params={
                "envName": env_name,
                "duration": duration,
                "endtime": end_time,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetTemplateManifest(
        self,
        node_type: str,
        tag: str,
    ):
        """
        :param node_type: unique identifier of the target node type (software stack), e.g. “tomcat11” for the Tomcat 11 stack.
        :param tag: target tag for the template.
        """
        return self._get(
            "GetTemplateManifest",
            params={
                "nodeType": node_type,
                "tag": tag,
            },
        )

    def GetTemplates(
        self,
        type: str = None,
        owner_uid: int = None,
    ):
        """
        :param type: filter the list by the template type (ALL,NATIVE,CARTRIDGE,DOCKERIZED)
        :param owneer_uid: filter the list by the templates available for the specific user.
        """
        return self._get(
            "GetTemplates",
            params={
                "type": type,
                "ownerUid": owner_uid,
            },
        )

    def GetTransferRequest(self):
        return self._get("GetTransferRequest", params={})

    def InstallPackageByGroup(
        self,
        env_name: str,
        node_group: str,
        package_name: str,
    ):
        """
        :param env_name: environment name or appid
        :param node_group: node group (cp, bl, nosql, sql)
        """
        return self._get(
            "InstallPackageByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "packageName": package_name,
            },
        )

    def InstallPackageById(
        self,
        env_name: str,
        package_name: str,
        node_id: int = None,
    ):
        """
        :param env_name: environment name or appid
        :node_id: id of node
        """
        return self._get(
            "InstallPackageById",
            params={
                "envName": env_name,
                "packageName": package_name,
                "nodeId": node_id,
            },
        )

    def InstallSoftwarePackage(
        self,
        env_name: str,
        keyword: str,
        node_type: str = None,
        node_group: str = None,
    ):
        return self._get(
            "InstallSoftwarePackage",
            params={
                "envName": env_name,
                "keyword": keyword,
                "nodeType": node_type,
                "nodeGroup": node_group,
            },
        )

    def LinkDockerNodes(
        self,
        env_name: str,
        source_node_id: int,
        target_node_id: int,
        alias: str,
        is_auto_restart: bool = None,
        group_alias: str = None,
    ):
        return self._get(
            "LinkDockerNodes",
            params={
                "envName": env_name,
                "sourceNodeId": source_node_id,
                "targetNodeId": target_node_id,
                "alias": alias,
                "isAutoRestart": is_auto_restart,
                "groupAlias": group_alias,
            },
        )

    def LinkNode(
        self,
        env_name: str,
        child_node_id: int,
        parent_node_id: int,
    ):
        return self._get(
            "LinkNode",
            params={
                "envName": env_name,
                "childNodeId": child_node_id,
                "parentNodeId": parent_node_id,
            },
        )

    def LinkNodes(
        self,
        env_name: str,
        child_node: str,
        parent_node: str,
    ):
        return self._get(
            "LinkNodes",
            params={
                "envName": env_name,
                "childNode": child_node,
                "parentNode": parent_node,
            },
        )

    def ManageEnvAttributes(
        self,
        target_app_id: str,
        attributes: str,
    ):
        """
        :param target_app_id: target environment name.
        :param attributes: JSON object with required attributes. For example: "{'key1': 'value1', 'key2': null}".
        """
        return self._get(
            "ManageEnvAttributes",
            params={
                "targetAppId": target_app_id,
                "attributes": attributes,
            },
        )

    def Migrate(
        self,
        env_name: str,
        hardware_node_group: str = None,
        is_on_line: bool = None,
    ):
        """
        :param env_name: target environment name.
        :param hardware_node_group: unique identifier of the target user region (host group).
        :param is_on_line: defines whether to perform online migration (true) or offline (false).
        """
        return self._get(
            "Migrate",
            params={
                "envName": env_name,
                "hardwareNodeGroup": hardware_node_group,
                "isOnLine": is_on_line,
            },
        )

    def ReadLog(
        self,
        env_name: str,
        node_id: int,
        path: str,
        From: int = None,
        count: int = None,
    ):
        """
        :param env_name: target environment name
        :param node_id: unique identifier of the target node (container).
        :param path: path to the required log file.
        :param From: index number of a symbol to start returning log file data from (all preceding symbols are skipped); from start of the file if not specified.
        :param count: number of symbols to return (all subsequent symbols are skipped); till the end of the file if not specified.
        """
        return self._get(
            "ReadLog",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "path": path,
                "from": From,
                "count": count,
            },
        )

    def RedeployContainerById(
        self,
        env_name: str,
        node_id: int,
        tag: str,
        use_existing_volumes: bool = None,
        login: str = None,
        password: str = None,
        manage_dns_state: bool = None,
    ):
        """
        :param env_name: target environment name
        :param node_id: unique identifier of the target node (container).
        :param tag: target tag for the container redeploy.
        :param use_existing_volumes: defines whether to keep existing volumes data (true) or erase any custom data (false).
        :param login: new username to access remote registry.
        :param password: new password to access remote registry.
        :param manage_dns_state: defines whether to exclude a target node from DNS for the duration of the operation (true) or not (false, by default). This parameter only works with the sequential processes (isSequential=true) and is ignored otherwise. Enabling the parameter will bring additional delay (as the DNS records have TTL and cannot be disabled instantly), while disabling can cause some of the requests to be lost.
        """
        return self._get(
            "RedeployContainerById",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "tag": tag,
                "useExistingVolumes": use_existing_volumes,
                "login": login,
                "password": password,
                "manageDNSState": manage_dns_state,
            },
        )

    def RedeployContainers(
        self,
        env_name: str,
        tag: str,
        node_group: str = None,
        node_id: int = None,
        use_existing_volumes: bool = None,
        login: str = None,
        password: str = None,
        manage_dns_state: bool = None,
    ):
        """
        :param env_name: target environment name.
        :param tag: target tag for the container redeploy.
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        :param node_id: unique identifier of the target node (container).
        :param use_existing_volumes: defines whether to keep existing volumes data (true) or erase any custom data (false).
        :param login: new username to access remote registry
        :param password: new password to access remote registry.
        :param manage_dns_state: defines whether to exclude a target node from DNS for the duration of the operation (true) or not (false, by default). This parameter only works with the sequential processes (isSequential=true) and is ignored otherwise. Enabling the parameter will bring additional delay (as the DNS records have TTL and cannot be disabled instantly), while disabling can cause some of the requests to be lost.
        """
        return self._get(
            "RedeployContainers",
            params={
                "envName": env_name,
                "tag": tag,
                "nodeGroup": node_group,
                "nodeId": node_id,
                "useExistingVolumes": use_existing_volumes,
                "login": login,
                "password": password,
                "manageDNSState": manage_dns_state,
            },
        )

    def RedeployContainersByGroup(
        self,
        env_name: str,
        node_group: str,
        tag: str,
        is_sequential: bool = None,
        use_existing_volumes: bool = None,
        delay: int = None,
        login: str = None,
        password: str = None,
        manage_dns_state: bool = None,
    ):
        """
        :params env_name: target environment name.
        :params node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        :params tag: target tag for the container redeploy.
        :params is_sequential: defines whether to redeploy containers one-by-one to ensure uptime (true) or simultaneously (false).
        :params use_existing_volumes: defines whether to keep existing volumes data (true) or erase any custom data (false).
        :params delay: delay (in seconds) between two consecutive redeploys when using the sequential restart type (I.e. when redeploy is performed on servers one-by-one to ensure uptime).
        :params login: new username to access remote registry.
        :params password: new password to access remote registry.
        :params manage_dns_state: defines whether to exclude a target node from DNS for the duration of the operation (true) or not (false, by default). This parameter only works with the sequential processes (isSequential=true) and is ignored otherwise. Enabling the parameter will bring additional delay (as the DNS records have TTL and cannot be disabled instantly), while disabling can cause some of the requests to be lost.
        """
        return self._get(
            "RedeployContainersByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "tag": tag,
                "isSequential": is_sequential,
                "useExistingVolumes": use_existing_volumes,
                "delay": delay,
                "login": login,
                "password": password,
                "manageDNSState": manage_dns_state,
            },
        )

    def RemoveApp(
        self,
        env_name: str,
        context: str,
        node_group: str = None,
    ):
        """
        :params env_name: target environment name.
        :params context: application context to be removed.
        :params node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        """
        return self._get(
            "RemoveApp",
            params={
                "envName": env_name,
                "context": context,
                "nodeGroup": node_group,
            },
        )

    def RemoveContainerEnvVars(
        self,
        env_name: str,
        vars: str,
        node_group: str = None,
        node_id: int = None,
    ):
        """
        :params env_name: target environment name.
        :params vars: JSON array with a list of container environment variables, e.g. ["var1", "var2"].
        :params node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        :params node_id: unique identifier of the target node (container).
        """
        return self._get(
            "RemoveContainerEnvVars",
            params={
                "envName": env_name,
                "vars": vars,
                "nodeGroup": node_group,
                "nodeId": node_id,
            },
        )

    def RemoveContainerVolume(
        self,
        env_name: str,
        node_id: int,
        path: str,
    ):
        return self._get(
            "RemoveContainerVolume",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "path": path,
            },
        )

    def RemoveContainerVolumeByGroup(
        self,
        env_name: str,
        node_group: str,
        path: str,
    ):
        return self._get(
            "RemoveContainerVolumeByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "path": path,
            },
        )

    def RemoveContainerVolumes(
        self,
        env_name: str,
        volumes: str,
        node_group: str = None,
        node_id: int = None,
    ):
        """
        :params env_name: target environment name
        :param volumes: JSON array of data volumes to be removed, e.g. /data/volume or ["/data/volume","/data/volume2", ...].
        :params node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.e
        :params node_id: unique identifier of the target node (container).
        """
        return self._get(
            "RemoveContainerVolumes",
            params={
                "envName": env_name,
                "volumes": volumes,
                "nodeGroup": node_group,
                "nodeId": node_id,
            },
        )

    def RemoveDockerVolume(
        self,
        env_name: str,
        node_id: int,
        path: str,
    ):
        return self._get(
            "RemoveDockerVolume",
            params={"envName": env_name, "nodeId": node_id, "path": path},
        )

    def RemoveDockerVolumeByGroup(
        self,
        env_name: str,
        node_group: str,
        path: str,
    ):
        return self._get(
            "RemoveDockerVolumeByGroup",
            params={"envName": env_name, "nodeGroup": node_group, "path": path},
        )

    def RemoveEndpoint(
        self,
        env_name: str,
        id: int,
    ):
        """
        :param env_name: target environment name.
        :param id: unique identifier of the target endpoint.
        """
        return self._get(
            "RemoveEndpoint",
            params={
                "envName": env_name,
                "id": id,
            },
        )

    def RemoveEnvPolicy(
        self,
        target_app_id: str,
        policy: list[str],
    ):
        """
        :param target_app_id: target application identifier of the environment for removing policy.
        :param policy: comma-separated list of policy. For example: "policy1,policy2".
        """
        return self._get(
            "RemoveEnvPolicy",
            params={
                "targetAppId": target_app_id,
                "policy": policy,
            },
            delimiter=",",
        )

    def RemoveEnvProperty(
        self,
        env_name: str,
        property_keys: list[str],
    ):
        """
        :param env_name: target environment name
        :param property_keys: comma-separated list of property keys. For example: "customProperty1,customProperty2".
        """
        return self._get(
            "RemoveEnvProperty",
            params={
                "envName": env_name,
                "propertyKeys": property_keys,
            },
            delimiter=",",
        )

    def RemoveLog(
        self,
        env_name: str,
        node_id: int,
        path: str,
    ):
        """
        :param env_name: target environment name
        :param node_id: unique identifier of the target node (container).
        :param path: path to the required log file.
        """
        return self._get(
            "RemoveLog",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "path": path,
            },
        )

    def RemoveNode(self, env_name: str, node_id: int):
        return self._get(
            "RemoveNode",
            params={
                "envName": env_name,
                "nodeId": node_id,
            },
        )

    def RenameApp(
        self,
        env_name: str,
        old_context: str,
        new_context: str,
        node_group: str = None,
    ):
        """
        :param env_name: target environment name.
        :param old_context: current context name of the application.
        :param new_context: new context name for the application.
        :node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        """
        return self._get(
            "RenameApp",
            params={
                "envName": env_name,
                "oldContext": old_context,
                "newContext": new_context,
                "nodeGroup": node_group,
            },
        )

    def ReplicateNodes(self, env_name: str, nodes: str):
        return self._get("ReplicateNodes", params={"envName": env_name, "nodes": nodes})

    def ResetContainerPassword(
        self,
        env_name: str,
        node_id: int,
        password: str = None,
    ):
        return self._get(
            "ResetContainerPassword",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "password": password,
            },
        )

    def ResetContainerPasswordById(
        self,
        env_name: str,
        node_id: int,
        password: str = None,
    ):
        return self._get(
            "ResetContainerPasswordById",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "password": password,
            },
        )

    def ResetContainerPasswordByType(
        self,
        env_name: str,
        node_type: str,
        password: str = None,
    ):
        return self._get(
            "ResetContainerPasswordByType",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "password": password,
            },
        )

    def ResetContainersPasswordByGroup(
        self,
        env_name: str,
        node_group: str,
        password: str = None,
    ):
        return self._get(
            "ResetContainersPasswordByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "password": password,
            },
        )

    def ResetNodePassword(
        self,
        env_name: str,
        node_group: str = None,
        node_id: int = None,
        password: str = None,
    ):
        """
        :param env_name: target environment name.
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        :param node_id: unique identifier of the target node (container)
        :param password: a new OS password for user container(s).
        """
        return self._get(
            "ResetNodePassword",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "nodeId": node_id,
                "password": password,
            },
        )

    def ResetNodePasswordById(
        self,
        env_name: str,
        node_id: int,
        password: str = None,
    ):
        return self._get(
            "ResetNodePasswordById",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "password": password,
            },
        )

    def ResetNodePasswordByType(
        self,
        env_name: str,
        node_type: str,
        password: str = None,
    ):
        return self._get(
            "ResetNodePasswordByType",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "password": password,
            },
        )

    def ResetServicePassword(
        self,
        env_name: str,
        node_group: str = None,
        node_id: int = None,
        password: str = None,
    ):
        """
        :param env_name: target environment name.
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        :param node_id: unique identifier of the target node (container)
        :param password: a new OS password for user container(s)  service..
        """
        return self._get(
            "ResetServicePassword",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "nodeId": node_id,
                "password": password,
            },
        )

    def RestartContainer(
        self,
        env_name: str,
        node_id: int,
        manage_dns_state: bool = None,
    ):
        return self._get(
            "RestartContainer",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "manageDNSState": manage_dns_state,
            },
        )

    def RestartContainerById(
        self,
        env_name: str,
        node_id: int,
        manage_dns_state: bool = None,
    ):
        return self._get(
            "RestartContainerById",
            params={
                "envName": env_name,
                "nodeid": node_id,
                "manageDNSState": manage_dns_state,
            },
        )

    def RestartContainerByType(
        self,
        env_name: str,
        node_type: str,
        manage_dns_state: bool = None,
    ):
        return self._get(
            "RestartContainerByType",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "manageDNSState": manage_dns_state,
            },
        )

    def RestartContainersByGroup(
        self,
        env_name: str,
        node_group: str,
        delay: int = None,
        is_sequential: bool = None,
        manage_dns_state: bool = None,
    ):
        return self._get(
            "RestartContainersByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "delay": delay,
                "isSequential": is_sequential,
                "manageDNSState": manage_dns_state,
            },
        )

    def RestartNodeById(
        self,
        env_name: str,
        node_id: int,
        manage_dns_state: bool = None,
    ):
        return self._get(
            "RestartNodeById",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "manageDNSState": manage_dns_state,
            },
        )

    def RestartNodes(
        self,
        env_name: str,
        node_group: str = None,
        node_id: int = None,
        delay: int = None,
        is_sequential: bool = False,
        manage_dns_state: bool = False,
    ):
        """
        :param env_name: target environment name.
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        :param node_id: unique identifier of the target node (container).
        :param delay: delay (in seconds) between two consecutive restarts when using the sequential restart type (I.e. when restart is performed on servers one-by-one to ensure uptime).
        :param is_sequential: defines whether to restart containers one-by-one to ensure uptime (true) or simultaneously (false).
        :param manage_dns_state: defines whether to exclude a target node from DNS for the duration of the operation (true) or not (false, by default). This parameter only works with the sequential processes (isSequential=true) and is ignored otherwise. Enabling the parameter will bring additional delay (as the DNS records have TTL and cannot be disabled instantly), while disabling can cause some of the requests to be lost.
        """
        return self._get(
            "RestartNodes",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "nodeId": node_id,
                "delay": delay,
                "isSequential": is_sequential,
                "manageDNSState": manage_dns_state,
            },
        )

    def RestartNodesByGroup(
        self,
        env_name: str,
        node_group: str,
        delay: int = None,
        is_sequential: bool = None,
        manage_dns_state: bool = None,
    ):
        return self._get(
            "RestartNodesByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "delay": delay,
                "isSequential": is_sequential,
                "manageDNSState": manage_dns_state,
            },
        )

    def RestartNodesByType(
        self,
        env_name: str,
        node_type: str,
        manage_dns_state: bool = None,
    ):
        return self._get(
            "RestartNodesByType",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "manageDNSState": manage_dns_state,
            },
        )

    def RestartServices(
        self,
        env_name: str,
        node_group: str = None,
        node_id: int = None,
        delay: int = None,
        is_sequential: bool = None,
        manage_dns_state: bool = None,
    ):
        """
        :param env_name: target environment name.
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        :param node_id: unique identifier of the target node (container).
        :param delay: delay (in seconds) between two consecutive restarts when using the sequential restart type (I.e. when restart is performed on servers one-by-one to ensure uptime).
        :param is_sequential: defines whether to restart containers one-by-one to ensure uptime (true) or simultaneously (false).
        :param manage_dns_state: defines whether to exclude a target node from DNS for the duration of the operation (true) or not (false, by default). This parameter only works with the sequential processes (isSequential=true) and is ignored otherwise. Enabling the parameter will bring additional delay (as the DNS records have TTL and cannot be disabled instantly), while disabling can cause some of the requests to be lost.
        """
        return self._get(
            "RestartServices",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "nodeId": node_id,
                "delay": delay,
                "isSequential": is_sequential,
                "manageDNSState": manage_dns_state,
            },
        )

    def RestoreDump(
        self,
        env_name: str,
        node_type: str,
        db_name: str,
        password: str,
        dump_url: str,
        user: str = None,
    ):
        """
        :param env_name: target environment name.
        :param node_type: unique identifier of the target node type (software stack), e.g. “tomcat11” for the Tomcat 11 stack.
        :param db_name: target database name.
        :param password: password to access database.
        :param dump_url: URL to the database dump file.
        :param user: username to access database.
        """
        return self._get(
            "RestoreDump",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "dbName": db_name,
                "password": password,
                "dumpUrl": dump_url,
                "user": user,
            },
        )

    def SendEnvCreatedEmail(
        self,
        is_import: bool = None,
    ):
        return self._get(
            "SendEnvCreatedEmail",
            params={
                "isImport": is_import,
            },
        )

    def SendTransferRequest(
        self,
        env_name: str,
        email: str,
    ):
        """
        :param env_name: application identifier of the environment
        :param email: email of the user which is going to be an owner
        """
        return self._get(
            "SendTransferRequest",
            params={
                "envName": env_name,
                "email": email,
            },
        )

    def SetCloudletsCount(
        self,
        env_name: str,
        node_type: str,
        flexible_cloudlets: int,
        fixed_cloudlets: int,
    ):
        """
        :param env_name: target environment name
        :param node_type: unique identifier of the target node type (software stack), e.g. “tomcat11” for the Tomcat 11 stack. Required if nodeid is not specified.
        :param flexible_cloudlets: a number of dynamic (flexible) cloudlets to be set for the layer.
        :param fixed_cloudlets: a number of reserved (fixed) cloudlets to be set for the layer.
        """
        return self._get(
            "SetCloudletsCount",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "flexibleCloudlets": flexible_cloudlets,
                "fixedCloudlets": fixed_cloudlets,
            },
        )

    def SetCloudletsCountByGroup(
        self,
        env_name: str,
        node_group: str,
        flexible_cloudlets: int,
        fixed_cloudlets: int,
        delay: int = None,
    ):
        return self._get(
            "SetCloudletsCountByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "flexibleCloudlets": flexible_cloudlets,
                "fixedCloudlets": fixed_cloudlets,
                "delay": delay,
            },
        )

    def SetCloudletsCountById(
        self,
        env_name: str,
        node_id: int,
        flexible_cloudlets: int,
        fixed_cloudlets: int,
    ):
        """
        :param env_name: target environment name
        :param node_id: unique identifier of the target node (container). If not defined, the cloudlet count will be set for all compute Nodes of the environment.
        :param flexible_cloudlets: a number of dynamic cloudlets to be set.
        :param fixed_cloudlets: a number of reserved cloudlets to be set.
        """
        return self._get(
            "SetCloudletsCountById",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "flexibleCloudlets": flexible_cloudlets,
                "fixedCloudlets": fixed_cloudlets,
            },
        )

    def SetCloudletsCountByType(
        self,
        env_name: str,
        node_type: str,
        flexible_cloudlets: int,
        fixed_cloudlets: int,
    ):
        return self._get(
            "SetCloudletsCountByType",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "flexibleCloudlets": flexible_cloudlets,
                "fixedCloudlets": fixed_cloudlets,
            },
        )

    def SetContainerEntryPoint(
        self,
        env_name: str,
        node_id: int,
        data: str = None,
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        :param data: Entry point data, e.g. "/bin/sh -c"
        """
        return self._get(
            "SetContainerEntryPoint",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "data": data,
            },
        )

    def SetContainerEnvVars(
        self,
        env_name: str,
        node_id: int,
        var: dict,
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        :param var: JSON object with a list of container environment variables, e.g {"var1":"value1", "var2":"value2"}.
        """
        var = json.dumps(var)
        return self._get(
            "SetContainerEnvVars",
            params={"envName": env_name, "nodeId": node_id, "vars": var},
        )

    def SetContainerEnvVarsByGroup(
        self,
        env_name: str,
        node_group: str,
        data: dict,
    ):
        """
        :param env_name: target environment name
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer
        :param data: JSON object with a list of container environment variables, e.g. {"var1":"value1", "var2":"value2"}.
        """
        data = json.dumps(data)

        return self._get(
            "SetContainerEnvVarsByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "data": data,
            },
        )

    def SetContainerRunCmd(
        self,
        env_name: str,
        node_id: int,
        data: str = None,
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        :param data: run command data, e.g. "service tomcat start"
        """
        return self._get(
            "SetContainerRunCmd",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "data": data,
            },
        )

    def SetDiskLimitByGroup(
        self,
        env_name: str,
        node_group: str,
        limit: int,
    ):
        return self._get(
            "SetDiskLimitByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "limit": limit,
            },
        )

    def SetDiskLimitById(
        self,
        env_name: str,
        node_id: int,
        limit: int,
    ):
        return self._get(
            "SetDiskLimitById",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "limit": limit,
            },
        )

    def SetDockerEntryPoint(
        self,
        env_name: str,
        node_id: int,
        data: str = None,
    ):
        """
        :param data: entry point
        """
        return self._get(
            "SetDockerEntryPoint",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "data": data,
            },
        )

    def SetDockerEnvVars(
        self,
        env_name: str,
        node_id: int,
        data: str,
    ):
        """
        :param data: list of container environment variables in json format
        """
        return self._get(
            "SetDockerEnvVars",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "data": data,
            },
        )

    def SetDockerRunCmd(
        self,
        env_name: str,
        node_id: int,
        data: str = None,
    ):
        """
        :param data: run command
        """
        return self._get(
            "SetDockerRunCmd",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "data": data,
            },
        )

    def SetDockerVolumesFrom(
        self,
        env_name: str,
        node_id: int,
        data: str,
    ):
        """
        :param data: json array of volumes e.g. [{"readOnly":false,"sourceNodeId":80579}]
        """
        return self._get(
            "SetDockerVolumesFrom",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "data": data,
            },
        )

    def SetEngineByGroup(
        self,
        env_name: str,
        node_group: str,
        engine: str,
    ):
        return self._get(
            "SetEngineByGroup",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "engine": engine,
            },
        )

    def SetEnvDisplayName(
        self,
        env_name: str,
        display_name: str = None,
    ):
        """
        :param env_name: target environment name.
        :param dispplay_name: new display name of the environment
        """
        return self._get(
            "SetEnvDisplayName",
            params={
                "envName": env_name,
                "displayName": display_name,
            },
        )

    def SetEnvGroup(
        self,
        env_name: str,
        env_group: str,
    ):
        return self._get(
            "SetEnvGroup",
            params={
                "envName": env_name,
                "envGroup": env_group,
            },
        )

    def SetNodeDisplayName(
        self,
        env_name: str,
        node_id: int = None,
        display_name: str = None,
    ):
        """
        :param env_name: target environment name.
        :param node_id: unique identifier of the target node (container).
        :param display_name: new display name of the node.t
        """
        return self._get(
            "SetNodeDisplayName",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "displayName": display_name,
            },
        )

    def SetNodeGroupDisplayName(
        self,
        env_name: str,
        node_group: str = None,
        display_name: str = None,
    ):
        """
        :param env_name: target environment name.
        :param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        :param display_name: new display name of the node.t
        """
        return self._get(
            "SetNodeGroupDisplayName",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "displayName": display_name,
            },
        )

    def SetSLBAccessEnabled(
        self,
        env_name: str,
        node_group: str,
        enabled: bool,
    ):
        return self._get(
            "SetSLBAccessEnabled",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "enabled": enabled,
            },
        )

    def SkipMessage(
        self,
        env_name: str,
        node_id: int,
        id: int,
    ):
        """
        :param env_name: target environment name
        :param node_id: unique identifier of the target node (container).
        :param id: unique identifier of the target message.
        """
        return self._get(
            "SkipMessage",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "id": id,
            },
        )

    def SleepEnv(self, env_name: str):
        return self._get(
            "SleepEnv",
            params={
                "envName": env_name,
            },
        )

    def StartEnv(self, env_name: str):
        return self._get(
            "StartEnv",
            params={
                "envName": env_name,
            },
        )

    def StopEnv(self, env_name: str):
        return self._get(
            "StopEnv",
            params={
                "envName": env_name,
            },
        )

    def UninstallSoftwarePackage(
        self,
        env_name: str,
        keyword: str,
        node_type: str = None,
        node_group: str = None,
    ):
        return self._get(
            "UninstallSoftwarePackage",
            params={
                "envName": env_name,
                "keyword": keyword,
                "nodeType": node_type,
                "nodeGroup": node_group,
            },
        )

    def UnlinkDockerNodes(
        self,
        env_name: str,
        source_node_id: int,
        target_node_id: int,
        alias: str,
        is_auto_restart: bool = None,
    ):
        return self._get(
            "UnlinkDockerNodes",
            params={
                "envName": env_name,
                "sourceNodeId": source_node_id,
                "targetNodeId": target_node_id,
                "alias": alias,
                "isAutoRestart": is_auto_restart,
            },
        )

    def UnpackDocker(
        self,
        env_name: str,
        node_id: int,
        folders: str,
        tag: str = None,
    ):
        return self._get(
            "UnpackDocker",
            params={
                "envName": env_name,
                "nodeID": node_id,
                "folders": folders,
                "tag": tag,
            },
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
        node_group: str = None,
        node_id: int = None,
        keyword: str = None,
        filter: str = None,
        is_dir: bool = None,
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
        )

    def AddMountPointByGroup(
        self,
        env_name: str,
        node_group: str,
        path: str,
        source_path: str,
        protocol: str = None,
        source_host: str = None,
        source_node_id: int = None,
        name: str = None,
        read_only: bool = None,
        source_address_type: str = None,
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
        )

    def AddMountPointById(
        self,
        env_name: str,
        node_id: int,
        path: str,
        source_path: str,
        protocol: str = None,
        source_host: str = None,
        source_node_id: int = None,
        name: str = None,
        read_only: bool = None,
        source_address_type: str = None,
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
        )

    def Append(
        self,
        env_name: str,
        path: str,
        body: str = None,
        node_type: str = None,
        node_group: str = None,
        master_only: bool = None,
        node_id: int = None,
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
        mount_points: str = None,
    ):
        return self._get(
            "CloneMountPoints",
            params={
                "envName": env_name,
                "nodeId": node_id,
                "sourceNodeId": source_node_id,
                "mountPoints": mount_points,
            },
        )

    def Copy(
        self,
        env_name: str,
        src: str,
        dest: str,
        node_type: str = None,
        node_group: str = None,
        master_only: bool = None,
        node_id: int = None,
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
        )

    def Create(
        self,
        env_name: str,
        path: str,
        node_type: str = None,
        node_group: str = None,
        master_only: bool = None,
        isdir: bool = None,
        node_id: int = None,
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
        )

    def Delete(
        self,
        env_name: str,
        path: str,
        node_type: str = None,
        node_group: str = None,
        master_only: bool = None,
        node_id: int = None,
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
        )

    def GetExportedList(
        self,
        env_name: str,
        node_id: int,
        path: str = None,
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
        )

    def GetFavorites(
        self,
        env_name: str,
        node_group: str = None,
        node_id: int = None,
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
        )

    def GetList(
        self,
        env_name: str,
        path: str = None,
        node_type: str = None,
        node_group: str = None,
        node_id: int = None,
        filter: int = None,
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
        )

    def GetMountPoints(
        self,
        env_name: str,
        node_group: str = None,
        node_id: int = None,
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
        node_type: str = None,
        node_group: str = None,
        node_id: int = None,
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
        node_type: str = None,
        node_group: str = None,
        node_id: int = None,
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
        node_type: str = None,
        node_group: str = None,
        master_only: bool = None,
        node_id: int = None,
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
        )

    def ReplaceInBody(
        self,
        env_name: str,
        path: str,
        pattern: str,
        replacement: str,
        nth: int = None,
        node_type: str = None,
        node_group: str = None,
        master_only: bool = None,
        node_id: int = None,
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
        node_type: str = None,
        node_group: str = None,
        master_only: bool = None,
        node_id: int = None,
        overwrite: bool = None,
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
        )

    def Write(
        self,
        env_name: str,
        path: str,
        body: str = None,
        node_type: str = None,
        node_group: str = None,
        master_only: bool = False,
        node_id: int = None,
        is_append_mode: bool = False,
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
        )


class _Group(Environment):
    """
    Categorize environments in the account with the help of the group management API. Such user-defined groups can filter the environment list, allowing a clear-cut view of the projects.

     Ref: https://docs.jelastic.com/api/private/#!/api/environment.Group
    """

    _endpoint2 = "group"

    def AttachEnv(
        self,
        env_name: str,
        env_group: list[str],
        target_appid: str = None,
        owner_uid: int = None,
    ):
        """
        param env_name: source environment name.
        param env_group: a comma-separated list of the target environment group names.
        param target_appid: if specified, redefines the target environment. For example, to the environment shared via the collaboration feature.
        param owner_uid: unique identifier of the target account’s owner. Required if the operation is performed by the collaboration member on the shared account.
        """
        return self._get(
            "AttachEnv",
            params={
                "envName": env_name,
                "envGroup": env_group,
                "targetAppid": target_appid,
                "ownerUid": owner_uid,
            },
            delimiter=",",
        )

    def CreateGroup(
        self,
        env_name: str,
        env_group: list[str] = None,
        data: dict = None,
        owner_uid: int = None,
    ):
        """
        param env_name: source environment name.
        param env_group: a comma-separated list of the target environment group names.
        param data : JSON object with the new group settings:
        param owner_uid: unique identifier of the target account’s owner. Required if the operation is performed by the collaboration member on the shared account.
        """
        return self._get(
            "CreateGroup",
            params={
                "envName": env_name,
                "envGroup": env_group,
                "data": data,
                "ownerUid": owner_uid,
            },
            delimiter=",",
        )

    def DetachEnv(
        self,
        env_name: str,
        env_group: list[str],
        target_appid: str = None,
        owner_uid: int = None,
    ):
        """
        param env_name: source environment name.
        param env_group: a comma-separated list of the target environment group names.
        param target_appid: if specified, redefines the target environment. For example, to the environment shared via the collaboration feature.
        param owner_uid: unique identifier of the target account’s owner. Required if the operation is performed by the collaboration member on the shared account.
        """
        return self._get(
            "DetachEnv",
            params={
                "envName": env_name,
                "envGroup": env_group,
                "targetAppid": target_appid,
                "ownerUid": owner_uid,
            },
            delimiter=",",
        )

    def EditGroup(
        self,
        env_name: str,
        src_group_name: str,
        dst_group_name: str = None,
        data: dict = None,
        owner_uid: int = None,
    ):
        """
        param env_name: source environment name.
        param src_group_name: target environment group name.
        param dst_group_name: New environment group name (renames srcGroupName).
        param data : JSON object with the new group settings:
        param owner_uid: unique identifier of the target account’s owner. Required if the operation is performed by the collaboration member on the shared account.
        """
        return self._get(
            "EditGroup",
            params={
                "envName": env_name,
                "srcGroupName": src_group_name,
                "dstGroupName": dst_group_name,
                "data": data,
                "ownerUid": owner_uid,
            },
        )

    def GetGroups(self, env_name: str, target_appid: str = None, owner_uid: int = None):
        """
        param env_name: source environment name.
        param target_appid: if specified, redefines the target environment. For example, to the environment shared via the collaboration feature.
        param owner_uid: unique identifier of the target account’s owner. Required if the operation is performed by the collaboration member on the shared account.
        """
        return self._get(
            "GetGroups",
            params={
                "envName": env_name,
                "targetAppid": target_appid,
                "ownerUid": owner_uid,
            },
        )

    def RemoveGroup(self, env_name: str, env_group: list[str], owner_uid: int = None):
        """
        param env_name: source environment name.
        param env_group: a comma-separated list of the target environment group names.
        param owner_uid: unique identifier of the target account’s owner. Required if the operation is performed by the collaboration member on the shared account.
        """
        return self._get(
            "RemoveGroup",
            params={
                "envName": env_name,
                "envGroup": env_group,
                "ownerUid": owner_uid,
            },
            delimiter=",",
        )

    def SetEnv(
        self,
        env_name: str,
        env_group: list[str],
        target_appid: str = None,
    ):
        """
        param env_name: source environment name.
        param env_group: a comma-separated list of the target environment group names.
        param target_appid: if specified, redefines the target environment. For example, to the environment shared via the collaboration feature.
        """
        return self._get(
            "SetEnv",
            params={
                "envName": env_name,
                "envGroup": env_group,
                "targetAppid": target_appid,
            },
            delimiter=",",
        )

    def SetIsolationEnabled(
        self, env_name: str, group_name: str, enabled: bool, owner_uid: list[int] = None
    ):
        """
        param env_name: source environment name.
        param group_name: target environment group name.
        param enabled: defines whether isolate (true) or not (false) environments within the group.
        param owner_uid: unique identifier of the target account’s owner. Required if the operation is performed by the collaboration member on the shared account.
        """
        return self._get(
            "SetIsolationEnabled",
            params={
                "envName": env_name,
                "groupName": group_name,
                "enabled": enabled,
                "ownerUid": owner_uid,
            },
            delimiter=",",
        )


class _NodeGroup(Environment):
    """
    The nodeGroup API service is used to manage data (parameters) and custom options of the environment layers.

    Ref: https://docs.jelastic.com/api/private/#!/api/environment.NodeGroup
    """

    _endpoint2 = "nodegroup"

    def ApplyData(
        self,
        env_name: str,
        node_group: str,
        data: dict,
    ):
        """
        param env_name: target environment name.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param data: JSON object with the node group data (parameters), e.g. {"redeployContainerDelay":20, "customProperty":"value"}.
        """
        return self._get(
            "ApplyData",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "data": data,
            },
        )

    def Get(
        self,
        env_name: str,
        node_group: str,
    ):
        """
        param env_name: target environment name.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        """
        return self._get(
            "Get",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
            },
        )

    def SetSLBAccessEnabled(
        self,
        env_name: str,
        node_group: str,
        enabled: bool,
    ):
        """
        param env_name: target environment name.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param enabled: defines whether allow (true) or deny (false) access to the layer via Shared Load Balancer.
        """
        return self._get(
            "SetSLBAccessEnabled",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "enabled": enabled,
            },
        )


class _Security(Environment):
    """
    This service is responsible for managing the environment firewall feature. You can get a rules list, manage specific rules, and enable/disable firewalls for environments. Learn more in the documentation.

    Ref: https://docs.jelastic.com/api/private/#!/api/environment.Security
    """

    _endpoint2 = "security"

    def AddRule(
        self,
        env_name: str,
        rule: dict,
        node_group: str = None,
    ):
        """
        param env_name: target environment name.
        param rule: JSON object with a new firewall rule:
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        """
        return self._get(
            "AddRule",
            params={
                "envName": env_name,
                "rule": rule,
                "nodeGroup": node_group,
            },
        )

    def AddRules(
        self,
        env_name: str,
        rules: str,
        node_group: str = None,
    ):
        """
        param env_name: target environment name.
        param rule: JSON object with a new firewall rule:
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        """
        return self._get(
            "AddRules",
            params={
                "envName": env_name,
                "rules": rules,
                "nodeGroup": node_group,
            },
        )

    def EditRule(
        self,
        env_name: str,
        rule: dict,
    ):
        """
        param env_name: target environment name.
        param rule: JSON object with a new firewall rule:
        """
        return self._get(
            "EditRule",
            params={
                "envName": env_name,
                "rule": rule,
            },
        )

    def GetRules(
        self,
        env_name: str,
        node_group: str = None,
        direction: str = None,
    ):
        """
        param env_name: target environment name.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param direction: filters returned list to show just inbound (INPUT or IN) or outbound (OUTPUT or OUT) rules
        """
        return self._get(
            "GetRules",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "direction": direction,
            },
        )

    def RegenerateIsolationSets(
        self,
    ):
        return self._get(
            "RegenerateIsolationSets",
            params={},
        )

    def RemoveRule(self, env_name: str, id: int):
        """
        param env_name: target environment name
        param id: Unique identifier of the target firewall rule.
        """
        return self._get(
            "RemoveRule",
            params={
                "envName": env_name,
                "id": id,
            },
        )

    def RemoveRules(self, env_name: str, ids: list[int]):
        """
        param env_name: target environment name
        param id: Unique identifier of the target firewall rule.
        """
        return self._get(
            "RemoveRules",
            params={
                "envName": env_name,
                "ids": ids,
            },
            delimiter=",",
        )

    def SetFirewallEnabled(
        self,
        env_name: str,
        enabled: bool,
    ):
        """
        param env_name: target environment name
        param enabled: defines whether to enable (true) or disable (false) the environment firewall feature.
        """
        return self._get(
            "SetFirewallEnabled",
            params={
                "envName": env_name,
                "enabled": enabled,
            },
        )

    def SetRuleEnabled(
        self,
        env_name: str,
        id: int,
        enabled: bool,
    ):
        """
        param env_name: target environment name
        param id: Unique identifier of the target firewall
        param enabled: defines whether to enable (true) or disable (false) the environment firewall feature.
        """
        return self._get(
            "SetRuleEnabled",
            params={
                "envName": env_name,
                "id": id,
                "enabled": enabled,
            },
        )

    def SetRules(
        self,
        env_name: str,
        rules: str,
        node_group: str = None,
    ):
        """
        param env_name: target environment name.
        param rule: JSON object with an array of firewall rules to be set instead of the existing ones.
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        """
        return self._get(
            "SetRules",
            params={
                "envName": env_name,
                "rules": rules,
                "nodeGroup": node_group,
            },
        )


class _System(Environment):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/environment.System
    """

    _endpoint2 = "system"

    def CheckDBConnection(self, checksum: str):
        return self._get(
            "CheckDBConnection",
            params={
                "checksum": checksum,
            },
        )

    def CheckError(self, code: int = None):
        return self._get(
            "CheckError",
            params={
                "code": code,
            },
        )

    def CleanCheckRequestCache(self, uid: int = None):
        return self._get(
            "CleanCheckRequestCache",
            params={
                "uid": uid,
            },
        )

    def CleanCheckRequestCacheInner(self, uid: int = None):
        return self._get(
            "CleanCheckRequestCacheInner",
            params={
                "uid": uid,
            },
        )

    def CleanTemplateManifestCache(
        self,
    ):
        return self._get(
            "CleanTemplateManifestCache",
            params={},
        )

    def DeleteOldEnvs(self, updatedon: str, status: str, debug: bool, checksum: str):
        return self._get(
            "DeleteOldEnvs",
            params={
                "updatedon": updatedon,
                "status": status,
                "debug": debug,
                "checksum": checksum,
            },
        )

    def Event(self, message: str, publish_local: bool = None):
        return self._get(
            "Event",
            params={
                "message": message,
                "publishLocal": publish_local,
            },
        )

    def FixDuplicates(self, debug: bool = None):
        return self._get(
            "FixDuplicates",
            params={
                "debug": debug,
            },
        )

    def FixStuckEnvs(
        self,
        checksum: str,
    ):
        return self._get(
            "FixStuckEnvs",
            params={
                "checksum": checksum,
            },
        )

    def GetAPIDescriptions(self, is_public_only: bool = None, is_token: bool = None):
        return self._get(
            "GetAPIDescriptions",
            params={
                "isPublicOnly": is_public_only,
                "isToken": is_token,
            },
        )

    def GetAllAPIDescriptions(self, is_public_only: bool = None, is_token: bool = None):
        return self._get(
            "GetAllAPIDescriptions",
            params={
                "isPublicOnly": is_public_only,
                "isToken": is_token,
            },
        )

    def GetBillableItems(
        self,
    ):
        return self._get(
            "GetBillableItems",
            params={},
        )

    def GetCacheStats(
        self,
    ):
        return self._get(
            "GetCacheStats",
            params={},
        )

    def GetCacheStatus(
        self,
    ):
        return self._get(
            "GetCacheStatus",
            params={},
        )

    def GetContCountStatus(self, starttime: datetime, endtime: datetime):
        return self._get(
            "GetContCountStatus",
            params={"starttime": starttime, "endtime": endtime},
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetInstanceCacheStatus(
        self,
    ):
        return self._get(
            "GetInstanceCacheStatus",
            params={},
        )

    def GetIpsByType(self, checksum: str, node_type: str, hnip: str = None):
        return self._get(
            "GetIpsByType",
            params={"checksum": checksum, "nodeType": node_type, "hnip": hnip},
        )

    def GetKeyword(
        self,
        checksum: str,
    ):
        return self._get(
            "GetKeyword",
            params={
                "checksum": checksum,
            },
        )

    def GetPlatformStatus(self, checksum: str, check_smtp: bool = None):
        return self._get(
            "GetPlatformStatus",
            params={"checksum": checksum, "checkSMTP": check_smtp},
        )

    def GetStatCollectorStatus(
        self,
    ):
        return self._get(
            "GetStatCollectorStatus",
            params={},
        )

    def GetVersion(
        self,
    ):
        return self._get(
            "GetVersion",
            params={},
        )

    def RefreshEmailTemplates(
        self,
    ):
        return self._get(
            "RefreshEmailTemplates",
            params={},
        )

    def RefreshUser(self, language: str = None):
        return self._get("RefreshUser", params={"language": language})

    def RegisterEnvContainer(
        self,
        env_name: str,
        node_type: str,
        ip_address: str,
        env_id: str,
        ct_id: str,
        passwd: str,
        hn_ip_address: str,
    ):
        return self._get(
            "RegisterEnvContainer",
            params={
                "envName": env_name,
                "nodeType": node_type,
                "ipAddress": ip_address,
                "envId": env_id,
                "ctId": ct_id,
                "passwd": passwd,
                "hnIpAddress": hn_ip_address,
            },
        )

    def ReloadConfiguration(
        self,
        reseller_id: int = None,
        changed_placeholders: str = None,
    ):
        return self._get(
            "ReloadConfiguration",
            params={
                "resellerId": reseller_id,
                "changedPlaceholders": changed_placeholders,
            },
        )

    def SendEmail(
        self,
        templates: str,
        email: str = None,
        language: str = None,
        timeout: int = None,
    ):
        return self._get(
            "SendEmail",
            params={
                "templates": templates,
                "email": email,
                "language": language,
                "timeout": timeout,
            },
        )

    def SurchargeBillableItems(self, starttime: datetime, endtime: datetime):
        return self._get(
            "SurchargeBillableItems",
            params={"startTime": starttime, "endTime": endtime},
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def SynchEnvs(
        self,
        checksum: str,
    ):
        return self._get(
            "SynchEnvs",
            params={
                "checksum": checksum,
            },
        )


class _Tracking(Environment):
    """
    This service is responsible for the monitoring of actions performed by the user. Learn more in the documentation.

    Ref: https://docs.jelastic.com/api/private/#!/api/environment.Tracking
    """

    _endpoint2 = "tracking"

    def GetAction(
        self,
        id: int = None,
    ):
        """
        param id: unique identifier of the target action. An error occurs if the specified action does not exist or does not belong to the current user.
        """
        return self._get(
            "GetAction",
            params={
                "id": id,
            },
        )

    def GetActions(self, start_time: datetime, end_time: list[datetime] = None):
        return self._get(
            "GetActions",
            params={
                "starttime": start_time,
                "endtime": end_time,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetAllServiceName(
        self,
        add_services_wildcard: bool = None,
        type: str = None,
    ):
        return self._get(
            "GetAllServiceName",
            params={"addServicesWildcard": add_services_wildcard, "type": type},
        )

    def GetCurrentActions(
        self,
    ):
        return self._get("GetCurrentActions", params={})

    def GetEnvActions(
        self,
        start_time: datetime,
        end_time: list[datetime] = None,
        offset: int = None,
        count: int = None,
    ):
        return self._get(
            "GetEnvActions",
            params={
                "starttime": start_time,
                "endtime": end_time,
                "offset": offset,
                "count": count,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetServerUTCTime(
        self,
    ):
        return self._get("GetServerUTCTime", params={})

    def GetUidActions(
        self,
        count: int = None,
        start_time: datetime = None,
        end_time: datetime = None,
        action_types: str = None,
    ):
        """
        param count: returns the specified number of actions from the response (10 by default).
        param start_time: start time (UTC) of a period for which actions should be shown. In the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        param end_time: end time (UTC) of a period for which actions should be shown. In the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        param action_types: a comma-separated list of action types to return (supported values: PUBLIC, SYSTEM).
        """
        return self._get(
            "GetUidActions",
            params={
                "count": count,
                "starttime": start_time,
                "endtime": end_time,
                "actionTypes": action_types,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetUidActionsAdmin(
        self,
        uid: int,
        start_row: int,
        start_time: datetime,
        end_time: datetime,
        result_count: int = None,
        servicename: str = None,
        order_field: str = None,
        order_direction: str = None,
        search_text: str = None,
    ):
        """
        param start_row: returns information starting from the specified row in the response (starts with 0, by default).
        param start_time: start time in the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        param end_time: end time in the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        param servicename: name of the service and corresponding method, e.g. "AccountService.SetQuota".
        param order_field: oder results by the field name.
        param order_direction: order direction "asc" or "desc".
        param search_text: optional parameter for filtering by the specified text.
        """
        return self._get(
            "GetUidActionsAdmin",
            params={
                "uid": uid,
                "startRow": start_row,
                "starttime": start_time,
                "endtime": end_time,
                "resultCount": result_count,
                "servicename": servicename,
                "orderField": order_field,
                "orderDirection": order_direction,
                "searchText": search_text,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def SearchActions(self, session: str, search: dict):
        """
        param session: user session or personal access token.
        param search: JSON object with the search parameters:
        """
        return self._get("SearchActions", params={"session": session, "search": search})

    def StoreAuditAdminActions(self, session: str, trackedevent: dict):
        """
        param session: user session or personal access token.
        param trackedevent: JSON
        """
        return self._get(
            "StoreAuditAdminActions",
            params={"session": session, "trackedevent": trackedevent},
        )

    def StoreUserActions(self, session: str, tracked_action_event: dict):
        """
        param session: user session or personal access token.
        param trackedActionEvent: JSON
        """
        return self._get(
            "StoreUserActions",
            params={"session": session, "trackedActionEvent": tracked_action_event},
        )


class _Trigger(Environment):
    """
        This service implements the environment's trigger handling and management functionality. There are two types of triggers:

    auto-scaling - custom conditions for nodes' addition (scale out) and removal (scale in) based on the load, which allows implementing automatic horizontal scaling. Learn more in the documentation.
    load alert - custom conditions for email notifications based on the nodes' load, i.e. a particular resource type is above/below the stated value for the designated period.

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.Trigger
    """

    _endpoint2 = "trigger"

    def AddAutoScalingTrigger(
        self,
        env_name: str,
        data: dict,
    ):
        """
        param env_name: target environment name.
        param data: JSON object with trigger's configuration.
        """
        return self._get(
            "AddAutoScalingTrigger",
            params={
                "envName": env_name,
                "data": data,
            },
        )

    def AddLoadAlertTrigger(
        self,
        env_name: str,
        data: dict,
    ):
        """
        param env_name: target environment name.
        param data: JSON object with trigger's configuration.
        """
        return self._get(
            "AddLoadAlertTrigger",
            params={
                "envName": env_name,
                "data": data,
            },
        )

    def AddTrigger(
        self,
        env_name: str,
        data: dict,
    ):
        """
        param env_name: target environment name.
        param data: JSON object with trigger's configuration.
        """
        return self._get(
            "AddTrigger",
            params={
                "envName": env_name,
                "data": data,
            },
        )

    def AutoScalingHistory(
        self,
        env_name: str,
        start_row: int,
        result_count: int,
        trigger_id: int = None,
        action_types: list[str] = None,
        start_time: datetime = None,
        end_time: datetime = None,
        order_field: str = None,
        order_direction: str = None,
        skip_results: str = None,
        node_group: str = None,
        resource_types: list[str] = None,
        trigger_log_id: int = None,
    ):
        """
        param env_name: target environment name.
        param start_row: returns information starting from the specified row in the response (starts with 0, by default).
        param result_count: returns the specified number of rows from the response (10 by default).
        param trigger_id: unique identifier of the target auto-scaling trigger.
        param action_types: a semicolon-separated list of triggers' action types (for filtering). (supported values: ADDNODE, REMOVENODE).
        param start_time: start time (UTC) of a period for which actions should be shown. In the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        param end_time: end time (UTC) of a period for which actions should be shown. In the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        param order_field: sorts results by the specified field.
        param order_direction: sorts results in the ascending (ASC) or descending (DESC) order.
        param skip_results: skips results with matching text (for filtering).
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param resource_type: a semicolon-separated list of triggers' resource types (for filtering).
        param trigger_log_id: unique identifier of the target log file.
        """
        return self._get(
            "AutoScalingHistory",
            params={
                "envName": env_name,
                "startRow": start_row,
                "resultCount": result_count,
                "triggerId": trigger_id,
                "actionTypes": action_types,
                "startTime": start_time,
                "endTime": end_time,
                "orderField": order_field,
                "orderDirection": order_direction,
                "skipResults": skip_results,
                "nodeGroup": node_group,
                "resourceTypes": resource_types,
                "triggerLogId": trigger_log_id,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def DeleteAutoScalingTrigger(
        self,
        env_name: str,
        id: int,
    ):
        """
        param env_name: target environment name.
        param id : unique identifier of the target auto-scaling trigger
        """
        return self._get(
            "DeleteAutoScalingTrigger",
            params={
                "envName": env_name,
                "id": id,
            },
        )

    def DeleteLoadAlertTrigger(
        self,
        env_name: str,
        id: int,
    ):
        """
        param env_name: target environment name.
        param id : unique identifier of the target load alert trigger.
        """
        return self._get(
            "DeleteLoadAlertTrigger",
            params={
                "envName": env_name,
                "id": id,
            },
        )

    def DeleteTrigger(
        self,
        env_name: str,
        id: int,
    ):
        return self._get(
            "DeleteTrigger",
            params={
                "envName": env_name,
                "id": id,
            },
        )

    def EditAutoScalingTrigger(self, env_name: str, id: int, data: str):
        """
        param env_name: target environment name.
        param id : unique identifier of the target load alert trigger.
        param data : JSON object with trigger's configuration.
        """
        return self._get(
            "EditAutoScalingTrigger",
            params={"envName": env_name, "id": id, "data": data},
        )

    def EditLoadAlertTrigger(self, env_name: str, id: int, data: str):
        """
        param env_name: target environment name.
        param id : unique identifier of the target load alert trigger.
        param data : JSON object with trigger's configuration.
        """
        return self._get(
            "EditLoadAlertTrigger",
            params={"envName": env_name, "id": id, "data": data},
        )

    def EditTrigger(self, env_name: str, id: int, data: str):
        return self._get(
            "EditTrigger",
            params={"envName": env_name, "id": id, "data": data},
        )

    def GetAutoScalingTriggers(self, env_name: str, action_types: list[str] = None):
        """
        param env_name: target environment name
        param action_types: a semicolon-separated list of the trigger action types (for filtering).
        """
        return self._get(
            "GetAutoScalingTriggers",
            params={
                "envName": env_name,
                "actionTypes": action_types,
            },
            delimiter=",",
        )

    def GetLoadAlertTriggers(self, env_name: str, action_types: list[str] = None):
        """
        param env_name: target environment name
        param action_types: a semicolon-separated list of the trigger action types (for filtering).
        """
        return self._get(
            "GetLoadAlertTriggers",
            params={
                "envName": env_name,
                "actionTypes": action_types,
            },
            delimiter=",",
        )

    def GetTriggerLogs(
        self,
        env_name: str,
        start_row: int,
        result_count: int,
        trigger_id: list[int] = None,
        action_types: list[str] = None,
        start_time: datetime = None,
        end_time: datetime = None,
        order_field: str = None,
        order_direction: str = None,
        skip_results: str = None,
        node_group: str = None,
        resource_types: list[str] = None,
        trigger_log_id: int = None,
    ):
        """
        param env_name: target environment name.
        param start_row: returns information starting from the specified row in the response (starts with 0, by default).
        param result_count: returns the specified number of rows from the response (10 by default).
        param trigger_id: unique identifier of the target auto-scaling trigger.
        param action_types: a semicolon-separated list of triggers' action types (for filtering). (supported values: ADDNODE, REMOVENODE).
        param start_time: start time (UTC) of a period for which actions should be shown. In the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        param end_time: end time (UTC) of a period for which actions should be shown. In the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        param order_field: sorts results by the specified field.
        param order_direction: sorts results in the ascending (ASC) or descending (DESC) order.
        param skip_results: skips results with matching text (for filtering).
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param resource_type: a semicolon-separated list of triggers' resource types (for filtering).
        param trigger_log_id: unique identifier of the target log file.
        """
        return self._get(
            "GetTriggerLogs",
            params={
                "envName": env_name,
                "startRow": start_row,
                "resultCount": result_count,
                "triggerId": trigger_id,
                "actionTypes": action_types,
                "startTime": start_time,
                "endTime": end_time,
                "orderField": order_field,
                "orderDirection": order_direction,
                "skipResults": skip_results,
                "nodeGroup": node_group,
                "resourceTypes": resource_types,
                "triggerLogId": trigger_log_id,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetTriggers(self, env_name: str, action_types: list[str] = None):
        """
        param env_name: target environment name
        param action_types: a semicolon-separated list of the trigger action types (for filtering).
        """
        return self._get(
            "GetTriggers",
            params={
                "envName": env_name,
                "actionTypes": action_types,
            },
            delimiter=",",
        )

    def LoadAlertHistory(
        self,
        env_name: str,
        start_row: int,
        result_count: int,
        trigger_id: int = None,
        action_types: list[str] = None,
        start_time: datetime = None,
        end_time: datetime = None,
        order_field: str = None,
        order_direction: str = None,
        skip_results: str = None,
        node_group: str = None,
        resource_types: list[str] = None,
        trigger_log_id: int = None,
    ):
        """
        param env_name: target environment name.
        param start_row: returns information starting from the specified row in the response (starts with 0, by default).
        param result_count: returns the specified number of rows from the response (10 by default).
        param trigger_id: unique identifier of the target auto-scaling trigger.
        param action_types: a semicolon-separated list of triggers' action types (for filtering). (supported values: ADDNODE, REMOVENODE).
        param start_time: start time (UTC) of a period for which actions should be shown. In the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        param end_time: end time (UTC) of a period for which actions should be shown. In the format “yyyy-MM-dd hh:mm:ss”, e.g. "2022-11-16 00:00:00".
        param order_field: sorts results by the specified field.
        param order_direction: sorts results in the ascending (ASC) or descending (DESC) order.
        param skip_results: skips results with matching text (for filtering).
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param resource_type: a semicolon-separated list of triggers' resource types (for filtering).
        param trigger_log_id: unique identifier of the target log file.
        """
        return self._get(
            "LoadAlertHistory",
            params={
                "envName": env_name,
                "startRow": start_row,
                "resultCount": result_count,
                "triggerId": trigger_id,
                "actionTypes": action_types,
                "startTime": start_time,
                "endTime": end_time,
                "orderField": order_field,
                "orderDirection": order_direction,
                "skipResults": skip_results,
                "nodeGroup": node_group,
                "resourceTypes": resource_types,
                "triggerLogId": trigger_log_id,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def SetAutoScalingTriggerEnabled(self, env_name: str, id: int, enabled: bool):
        return self._get(
            "SetAutoScalingTriggerEnabled",
            params={"envName": env_name, "id": id, "enabled": enabled},
        )

    def SetLoadAlertTriggerEnabled(self, env_name: str, id: int, enabled: bool):
        return self._get(
            "SetLoadAlertTriggerEnabled",
            params={"envName": env_name, "id": id, "enabled": enabled},
        )

    def SetTriggerEnabled(self, env_name: str, id: int, enabled: bool):
        return self._get(
            "SetTriggerEnabled",
            params={"envName": env_name, "id": id, "enabled": enabled},
        )


class _Vcs(Environment):
    """
    This service is the tool for managing your VCS (version control system) projects. Configure periodic automatic deployment of the committed changes, and you can work with GIT/SVN repository only. Just commit the updated code to your VCS project. The platform will detect changes and automatically push them to the assigned environment. In contrast to the GIT hooks, the auto-deploy feature does not require configuration on the GIT side and works with SVN.

    Ref: https://docs.jelastic.com/api/private/#!/api/environment.Vcs
    """

    _endpoint2 = "vcs"

    def CreateProject(
        self,
        env_name: str,
        type: str,
        context: str,
        url: str,
        branch: str = None,
        key_id: int = None,
        login: str = None,
        password: str = None,
        auto_update: bool = None,
        interval: str = None,
        auto_resolve_conflict: bool = None,
        zdt: bool = None,
        update_now: bool = None,
        node_group: str = None,
        hooks: str = None,
        delay: int = None,
        repo_hash: str = None,
    ):
        """
        param env_name: target environment name.
        param type: VCS repository type ("GIT" or "SVN").
        param context: custom context name for the deployed project (ROOT by default).
        param url: URL to the repository (including protocol).
        param branch: remote repository branch (master by default).
        param key_id: unique identifier of a private SSH key on the account. It can be found in the dashboard (account Settings > SSH Keys > Private Keys) or fetched with the Management > Account > GetSSHKeys method.
        param login: login for authentication in VCS.
        param password: password or token for authentication in VCS.
        param auto_update: defines whether to enable (true) or disable (false) automatic project updates (only upon code changes in the remote repository); auto-update frequency is set with the interval parameter.
        param interval: delay (in minutes) for automatic project updates.
        param auto_resolve_conflict: defines whether to automatically resolve (true) or not (false) merge conflicts (by updating the contradictory files to the repository version, i.e. locally made changes are discarded).
        param zdt: defines whether to use zero-downtime deployment for PHP (true) or not (false).
        param update_now: defines whether to deploy your project immediately after its creation (true) or postpone this operation (false).
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param hooks: JSON object with custom scripts (actual content) to be executed before and after the build/deployment operations. For example: {"preDeploy":"script", "postDeploy":"script", "preBuild":"script", "postBuild":"script"}.
        param delay: delay (in seconds) between two consecutive deployments when using the sequential deployment type (i.e. when deployment is performed on servers one-by-one to ensure uptime).
        param repo_hash: target repository hash.
        """
        return self._get(
            "CreateProject",
            params={
                "envName": env_name,
                "type": type,
                "context": context,
                "url": url,
                "branch": branch,
                "keyId": key_id,
                "login": login,
                "password": password,
                "autoupdate": auto_update,
                "interval": interval,
                "autoResolveConflict": auto_resolve_conflict,
                "zdt": zdt,
                "updateNow": update_now,
                "nodeGroup": node_group,
                "hooks": hooks,
                "delay": delay,
                "repoHash": repo_hash,
            },
        )

    def DeleteProject(
        self,
        env_name: str,
        context: str,
        node_group: str = None,
    ):
        """
        param env_name: target environment name.
        param context: custom context name for the deployed project (ROOT by default).
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        """
        return self._get(
            "DeleteProject",
            params={
                "envName": env_name,
                "context": context,
                "nodeGroup": node_group,
            },
        )

    def EditProject(
        self,
        env_name: str,
        type: str,
        oldcontext: str,
        newcontext: str,
        url: str,
        branch: str,
        auto_update: bool,
        auto_resolve_conflict: bool,
        zdt: bool,
        key_id: int = None,
        login: str = None,
        password: str = None,
        interval: str = None,
        node_group: str = None,
        hooks: list[str] = None,
        delay: int = None,
        repo_hash: str = None,
    ):
        """
        param env_name: target environment name.
        param type: VCS repository type ("GIT" or "SVN").
        param oldcontext: context name of the existing project.
        param newcontext: new context name for the edited project.
        param url: URL to the repository (including protocol).
        param branch: remote repository branch (master by default).
        param key_id: unique identifier of a private SSH key on the account. It can be found in the dashboard (account Settings > SSH Keys > Private Keys) or fetched with the Management > Account > GetSSHKeys method.
        param login: login for authentication in VCS.
        param password: password or token for authentication in VCS.
        param auto_update: defines whether to enable (true) or disable (false) automatic project updates (only upon code changes in the remote repository); auto-update frequency is set with the interval parameter.
        param interval: delay (in minutes) for automatic project updates.
        param auto_resolve_conflict: defines whether to automatically resolve (true) or not (false) merge conflicts (by updating the contradictory files to the repository version, i.e. locally made changes are discarded).
        param zdt: defines whether to use zero-downtime deployment for PHP (true) or not (false).
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param hooks: JSON object with custom scripts (actual content) to be executed before and after the build/deployment operations. For example: {"preDeploy":"script", "postDeploy":"script", "preBuild":"script", "postBuild":"script"}.
        param delay: delay (in seconds) between two consecutive deployments when using the sequential deployment type (i.e. when deployment is performed on servers one-by-one to ensure uptime).
        param repo_hash: target repository hash.
        """
        return self._get(
            "EditProject",
            params={
                "envName": env_name,
                "type": type,
                "oldcontext": oldcontext,
                "newcontext": newcontext,
                "url": url,
                "branch": branch,
                "autoupdate": auto_update,
                "autoResolveConflict": auto_resolve_conflict,
                "zdt": zdt,
                "keyId": key_id,
                "login": login,
                "password": password,
                "interval": interval,
                "nodeGroup": node_group,
                "hooks": hooks,
                "delay": delay,
                "repoHash": repo_hash,
            },
        )

    def GetProject(
        self,
        env_name: str,
        context: str = None,
        node_group: str = None,
    ):
        """
        param env_name: target environment name.
        param context: custom context name for the deployed project (ROOT by default).
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        """
        return self._get(
            "GetProject",
            params={
                "envName": env_name,
                "context": context,
                "nodeGroup": node_group,
            },
        )

    def Update(
        self,
        env_name: str,
        context: str,
        node_group: str = None,
        delay: int = None,
    ):
        """
        param env_name: target environment name.
        param context: custom context name for the deployed project (ROOT by default).
        param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        param delay: delay (in seconds) between two consecutive restarts when using the sequential restart type (i.e. when restart is performed on servers one-by-one to ensure uptime).
        """
        return self._get(
            "Update",
            params={
                "envName": env_name,
                "context": context,
                "nodeGroup": node_group,
                "delay": delay,
            },
        )


class _Windows(Environment):
    """
    Service provides a flexible structure to manage Environment, obtain statistic information etc.

     Ref: https://docs.jelastic.com/api/private/#!/api/environment.Windows
    """

    _endpoint2 = "windows"

    def AddDomain(
        self,
        name: str,
        username: str,
        password: str,
        dns_server: str = None,
    ):
        """
        param password: password of the domain user
        """
        return self._get(
            "AddDomain",
            params={
                "name": name,
                "username": username,
                "password": password,
                "dnsServer": dns_server,
            },
        )

    def EditDomain(
        self,
        id: int,
        name: str = None,
        username: str = None,
        old_password: str = None,
        password: str = None,
        dns_server: str = None,
    ):
        return self._get(
            "EditDomain",
            params={
                "id": id,
                "name": name,
                "username": username,
                "oldPassword": old_password,
                "password": password,
                "dnsServer": dns_server,
            },
        )

    def GetList(self):
        return self._get("GetList", params={})

    def IsDomainExists(
        self,
        id: int,
        checksum: str = None,
    ):
        return self._get("IsDomainExists", params={"id": id, "checksum": checksum})

    def RemoveDomain(
        self,
        id: int,
    ):
        return self._get(
            "RemoveDomain",
            params={
                "id": id,
            },
        )
