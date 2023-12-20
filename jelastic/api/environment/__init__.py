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
        key_id:list[int]=None,
        login:list[str]=None,
        password:list[str]=None,
        target_env: list[str]=None,
        context:list[str]=None,
        branch:list[str]=None,
        interval:list[str]=None,
        delay:list[int]=None,
        deploy_now:list[bool]=None,
        hooks:list[str]=None,
        work_dir:list[str]=None,
        target_node_group:list[str]=None,
        is_sequential:list[bool]=None
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

    def BuildDeploy(
            self,
            env_name: str,
            project_name:str
    ):
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
            project_id:str,
            delay: list[int] = None,
            update:list[bool] = None,
            is_sequential: list[bool] = None

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
                "isSequential":is_sequential
            },
            delimiter=",",
        )

    def BuildProject(
            self,
            env_name: str,
            node_id: int,
            project_id:str,
            update:list[bool] = None,
            skip_publish:list[bool] = None,
            asyncs: list[bool] = None

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
                "skipPublish":skip_publish,
                "async":asyncs
            },
            delimiter=",",
        )
    def DeployProject(
            self,
            env_name: str,
            node_id: int,
            project_id:str,
            delay: list[int] = None,
            is_sequential: list[bool] = None


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
                "isSequential":is_sequential
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
        key_id:list[int]=None,
        login:list[str]=None,
        password:list[str]=None,
        env: list[str]=None,
        context:list[str]=None,
        branch:list[str]=None,
        autoupdate: list[bool] = None,
        interval:list[str]=None,
        auto_resolve_conflict: list[bool] = None,
        delay:list[int]=None,
        hooks:list[str]=None,
        work_dir:list[str]=None,
        target_node_group:list[str]=None,
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
        project_id: list[int]=None,
        project_name: list[str]=None
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
        node_group: list[int]=None,
        node_id: list[int]=None,

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
        project_id: list[int]=None,
        context: list[str]=None,
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
