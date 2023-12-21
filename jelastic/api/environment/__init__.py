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
        hooks: list[str]= None
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
            delimeter=",",
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
            delimeter=",",
        )
    def BuildDeployProject(
        self,
        env_name: str,
        node_id: int,
        project: str,
        skip_update: list[bool]= None,
        delay: list[int]= None
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
            delimeter=",",
        )
    def BuildProject(
        self,
        env_name: str,
        node_id: int,
        project: str,
        skip_upload: list[bool]= None,
        skip_update: list[bool]= None,
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
            delimeter=",",
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
                "delay": delay
            },
            delimeter=",",
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
                "delay": delay
            },
            delimeter=",",
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
            delimeter=",",
        )
    def EditBuildProject(
        self,
        env_name: str,
        node_id: int,
        project: str,
        name: list[str]=None,
        repo: list[str]=None,
        deployment: dict = None,
        settings: dict = None,
        hooks: list[str]= None
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
            delimeter=",",
        )
    def EditProject(
        self,
        env_name: str,
        node_group: str,
        context: str,
        new_context: list[str]=None,
        repo: list[str]=None,
        settings: dict = None,
        hooks: list[str]= None,
        delay: list[int]= None
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
            delimeter=",",
        )

    def EditRepo(
        self,
        id:int,
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
                "id":id,
                "name": name,
                "type": type,
                "url": url,
                "branch": branch,
                "keyId": key_id,
                "login": login,
                "password": password,
                "description": description,
            },
            delimeter=",",
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
            delimeter=",",
        )
    def GetBuildProjects(
        self,
        env_name: str,
        node_group: list[str]=None,
        node_id: list[int]=None,
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
            delimeter=",",
        )
    def GetDeployments(
        self,
        env_name: str,
        node_group: str
    ):
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
            delimeter=",",
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
            delimeter=",",
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
            delimeter=",",
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
            delimeter=",",
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
            delimeter=",",
        )
    def RemoveRepo(
            self,
            id: int
    ):
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
        new_context:str,
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
            delimeter=",",
        )






