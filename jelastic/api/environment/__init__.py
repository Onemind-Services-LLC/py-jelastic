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
    def Deployment(self) -> "_Node":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.environment.Deployment

        Ref: https://docs.jelastic.com/api/private/#!/api/environment.Deployment
        """
        return _Deployment(session=self._session, token=self._token, debug=self._debug)


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
        key_id: list[int] = None,
        login: list[str] = None,
        password: list[str] = None,
        target_env: list[str] = None,
        context: list[str] = None,
        branch: list[str] = None,
        interval: list[str] = None,
        delay: list[int] = None,
        deploy_now: list[bool] = None,
        hooks: list[str] = None,
        work_dir: list[str] = None,
        target_node_group: list[str] = None,
        is_sequential: list[bool] = None,
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
            delimiter=",",
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
        target_env: list[str] = None,
        login: list[str] = None,
        password: list[str] = None,
        context: list[str] = None,
        branch: list[str] = None,
        interval: list[str] = None,
        delay: list[int] = None,
        deploy_now: list[bool] = None,
        hooks: list[str] = None,
        work_dir: list[str] = None,
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
            delimiter=",",
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
        target_env: list[str] = None,
        key_id: list[int] = None,
        context: list[str] = None,
        branch: list[str] = None,
        interval: list[str] = None,
        delay: list[int] = None,
        deploy_now: list[bool] = None,
        hooks: list[str] = None,
        work_dir: list[str] = None,
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
            delimiter=",",
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
        delay: list[int] = None,
        update: list[bool] = None,
        is_sequential: list[bool] = None,
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
            delimiter=",",
        )

    def BuildProject(
        self,
        env_name: str,
        node_id: int,
        project_id: str,
        update: list[bool] = None,
        skip_publish: list[bool] = None,
        asyncs: list[bool] = None,
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
            delimiter=",",
        )

    def DeployProject(
        self,
        env_name: str,
        node_id: int,
        project_id: str,
        delay: list[int] = None,
        is_sequential: list[bool] = None,
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
            delimiter=",",
        )

    def EditProject(
        self,
        env_name: str,
        node_id: int,
        project_id: int,
        name: str,
        type: str,
        path: str,
        key_id: list[int] = None,
        login: list[str] = None,
        password: list[str] = None,
        env: list[str] = None,
        context: list[str] = None,
        branch: list[str] = None,
        autoupdate: list[bool] = None,
        interval: list[str] = None,
        auto_resolve_conflict: list[bool] = None,
        delay: list[int] = None,
        hooks: list[str] = None,
        work_dir: list[str] = None,
        target_node_group: list[str] = None,
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
            delimiter=",",
        )

    def GetProjectInfo(
        self,
        env_name: str,
        node_id: int,
        project_id: list[int] = None,
        project_name: list[str] = None,
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
            delimiter=",",
        )

    def GetProjects(
        self,
        env_name: str,
        node_group: list[int] = None,
        node_id: list[int] = None,
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
            delimiter=",",
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
            delimiter=",",
        )

    def Update(
        self,
        env_name: str,
        node_id: int,
        project_id: list[int] = None,
        context: list[str] = None,
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
            delimiter=",",
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
        hooks: list[str] = None,
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
            delimiter=",",
        )

    def AddRepo(
        self,
        name: str,
        url: str,
        type: list[str] = None,
        branch: list[str] = None,
        key_id: list[int] = None,
        login: list[str] = None,
        password: list[str] = None,
        description: list[str] = None,
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
            delimiter=",",
        )

    def BuildDeployProject(
        self,
        env_name: str,
        node_id: int,
        project: str,
        skip_update: list[bool] = None,
        delay: list[int] = None,
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
            delimiter=",",
        )

    def BuildProject(
        self,
        env_name: str,
        node_id: int,
        project: str,
        skip_upload: list[bool] = None,
        skip_update: list[bool] = None,
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
            delimiter=",",
        )

    def Deploy(
        self,
        env_name: str,
        repo: str,
        context: str,
        node_group: list[str] = None,
        build_node_id: list[int] = None,
        settings: dict = None,
        hooks: list[str] = None,
        delay: list[int] = None,
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
            delimiter=",",
        )

    def DeployArchive(
        self,
        env_name: str,
        file_url: str,
        file_name: str,
        node_group: list[str] = None,
        context: list[str] = None,
        zdt: list[bool] = None,
        hooks: list[str] = None,
        delay: list[int] = None,
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
            delimiter=",",
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
            delimiter=",",
        )

    def EditBuildProject(
        self,
        env_name: str,
        node_id: int,
        project: str,
        name: list[str] = None,
        repo: list[str] = None,
        deployment: dict = None,
        settings: dict = None,
        hooks: list[str] = None,
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
            delimiter=",",
        )

    def EditProject(
        self,
        env_name: str,
        node_group: str,
        context: str,
        new_context: list[str] = None,
        repo: list[str] = None,
        settings: dict = None,
        hooks: list[str] = None,
        delay: list[int] = None,
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
            delimiter=",",
        )

    def EditRepo(
        self,
        id: int,
        name: list[str] = None,
        type: list[str] = None,
        url: list[str] = None,
        branch: list[str] = None,
        key_id: list[int] = None,
        login: list[str] = None,
        password: list[str] = None,
        description: list[str] = None,
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
            delimiter=",",
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
            delimiter=",",
        )

    def GetBuildProjects(
        self,
        env_name: str,
        node_group: list[str] = None,
        node_id: list[int] = None,
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
            delimiter=",",
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
            delimiter=",",
        )

    def GetHooks(
        self,
        env_name: str,
        node_group: list[str] = None,
        node_id: list[int] = None,
        context: list[str] = None,
        project: list[str] = None,
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
            delimiter=",",
        )

    def GetProjectInfo(
        self,
        env_name: str,
        context: str,
        node_group: list[str] = None,
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
            delimiter=",",
        )

    def GetRepos(
        self,
        id: list[int] = None,
    ):
        """
        param id: unique identifier of the repository.
        """
        return self._get(
            "GetRepos",
            params={
                "id": id,
            },
            delimiter=",",
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
            delimiter=",",
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
        node_group: list[str] = None,
        node_id: list[int] = None,
        context: list[str] = None,
        project: list[str] = None,
        delay: list[str] = None,
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
            delimiter=",",
        )


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
