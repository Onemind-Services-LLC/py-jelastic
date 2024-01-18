from ..abstract import ClientAbstract

__all__ = ["Marketplace"]


class Marketplace(ClientAbstract):
    _endpoint1 = "marketplace"

    @property
    def Admin(self) -> "_Admin":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.marketplace.Admin

        Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Admin
        """
        return _Admin(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def App(self) -> "_App":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.marketplace.App
        Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.App
        """
        return _App(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Console(self) -> "_Console":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.marketplace.Console

        Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Console
        """
        return _Console(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Favorite(self) -> "_Favorite":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.marketplace.Favorite
        Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Favorite
        """
        return _Favorite(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Installation(self) -> "_Installation":
        """
        The Installation service provides extensive functionality for users to manage applications installed from the Marketplace or via Import.
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.marketplace.Installation
        Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Installation
        """
        return _Installation(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Jps(self) -> "_Jps":
        """
        The JPS service provides methods for working with custom JPS manifests.
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.marketplace.Jps
        Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Jps
        """
        return _Jps(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Installation(Marketplace):
    """
    The Installation service provides extensive functionality for users to manage applications installed from the Marketplace or via Import.
    Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Installation
    """

    _endpoint2 = "installation"

    def ExecuteAction(
        self,
        app_unique_name: str,
        action: str,
        settings_id: str = "main",
        params: dict = None,
        lang: str = None,
    ):
        """
        :param app_unique_name: unique identifier of the particular installation.
        :param action: unique identifier of the custom action name to be executed.
        :param settings_id: unique identifier of the settings section of the manifest. Default settings form ID is 'main'.
        :param params: JSON object with custom settings for the JPS manifest.
        :param lang: target localization language.
        """
        return self._get(
            "ExecuteAction",
            params={
                "appUniqueName": app_unique_name,
                "action": action,
                "settingsId": settings_id,
                "params": params,
                "lang": lang,
            },
        )

    def GetEnvAppid(
        self,
        app_unique_name: str,
    ):
        """
        param app_unique_name: unique identifier of the particular installation.
        """
        return self._get(
            "GetEnvAppid",
            params={
                "appUniqueName": app_unique_name,
            },
        )

    def GetInfo(
        self,
        app_unique_name: str,
    ):
        """
        param app_unique_name: unique identifier of the particular installation.
        """
        return self._get(
            "GetInfo",
            params={
                "appUniqueName": app_unique_name,
            },
        )

    def GetScriptingAppid(self):
        return self._get("GetScriptingAppid", params={})

    def GetSettings(
        self,
        app_unique_name: str,
        settings_id: list[str] = None,
        lang: list[str] = None,
    ):
        """
        param app_unique_name: unique identifier of the particular installation.
        param settings_id: unique identifier of the settings section of the manifest. Default settings form ID is 'main'.
        param lang: target localization language.
        """
        return self._get(
            "GetSettings",
            params={
                "appUniqueName": app_unique_name,
                "settingsId": settings_id,
                "lang": lang,
            },
            delimiter=",",
        )

    def Uninstall(
        self,
        app_unique_name: str,
        target_app_id: str,
        app_template_id: str,
        force: bool = False,
    ):
        """
        :param app_unique_name: unique identifier of the particular installation.
        :param target_app_id: unique identifier of the target application.
        :param app_template_id: unique identifier of the target application template.
        :param force: defines whether to proceed (true) or interrupt (false) the operation in case of errors.
        """
        return self._get(
            "Uninstall",
            params={
                "appUniqueName": app_unique_name,
                "targetAppId": target_app_id,
                "appTemplateId": app_template_id,
                "force": force,
            },
        )


class _Favorite(Marketplace):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Favorite
    """

    _endpoint2 = "favorite"

    def Add(
        self,
        id: str,
    ):
        """
        param id: unique identifier of the target application.
        """
        return self._get(
            "Add",
            params={
                "id": id,
            },
        )

    def AddManifest(
        self,
        manifest: str,
    ):
        """
        param manifest: custom JPS (manifest body or link).
        """
        return self._get(
            "AddManifest",
            params={
                "manifest": manifest,
            },
        )

    def Delete(
        self,
        id: str,
    ):
        """
        param id: unique identifier of the target application.
        """
        return self._get(
            "Delete",
            params={
                "id": id,
            },
        )

    def GetList(
        self,
        search: list[str] = None,
        lang: list[str] = None,
        checksum: list[str] = None,
    ):
        """
        param search: JSON object with the search parameters
        param lang: target localization language.
        param checksum: hecksum of the Marketplace applications (to verify that you possess the most recent checksum and applications copy). If you send the same 'checksum' parameter as received in the previous response and if this 'checksum' hasn't changed on the server side, then the server assumes you have the latest local copy of applications on the client side. In this case, it will return an empty applications list, speeding up the response time.
        """
        return self._get(
            "Delete",
            params={
                "search": search,
                "lang": lang,
                "checksum": checksum,
            },
        )


class _Console(Marketplace):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Console
    """

    _endpoint2 = "console"

    def ClearLog(
        self,
    ):
        return self._get("ClearLog", params={})

    def ReadLog(
        self,
    ):
        return self._get("ReadLog", params={})

    def WriteLog(self, message: str):
        """
        param message: a custom message to be added to the console log.
        """
        return self._get("WriteLog", params={"message": message})


class _App(Marketplace):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.App
    """

    _endpoint2 = "app"

    def AddApp(self, manifest: str):
        """
        :param manifest: custom personal JPS (manifest body or link) to be added.
        """
        return self._get(
            "AddApp",
            params={
                "manifest": manifest,
            },
        )

    def DeleteApp(self, id: str):
        """
        :param id: unique identifier of the target personal JPS manifest in the Marketplace..
        """
        return self._get(
            "DeleteApp",
            params={
                "id": id,
            },
        )

    def EditApp(self, id: str, manifest: str):
        """
        :param id: unique identifier of the target personal JPS manifest in the Marketplace..
        :param manifest: updated personal JPS (manifest body or link).
        """
        return self._get(
            "EditApp",
            params={
                "id": id,
                "manifest": manifest,
            },
        )

    def GetAddonList(
        self,
        env_name: str,
        node_group: list[str] = None,
        search: dict = None,
    ):
        """
        :param env_name: target environment name.
        :param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        :param search: JSON object with the search parameters. For example (all fields are optional):
        """
        return self._get(
            "GetAddonList",
            params={
                "envName": env_name,
                "nodeGroup": node_group,
                "search": search,
            },
        )

    def GetAppInfo(
        self,
        id: str,
        lang: list[str] = None,
        owner_uid: list[int] = None,
    ):
        """
        :param id: unique identifier of the target JPS manifest in the Marketplace.
        :param lang: target localization language.
        :param owner_uid: unique identifier of the target user account.
        """
        return self._get(
            "GetAppInfo",
            params={
                "id": id,
                "lang": lang,
                "ownerUid": owner_uid,
            },
        )

    def GetCategories(
        self,
    ):
        return self._get(
            "GetCategories",
            params={},
        )

    def GetChecksum(
        self,
    ):
        return self._get(
            "GetChecksum",
            params={},
        )

    def GetList(
        self,
        search: list[str] = None,
    ):
        """
        :param search: JSON object with the search parameters. For example (all fields are optional):
        """
        return self._get(
            "GetList",
            params={"search": search},
        )

    def Install(
        self,
        id: str,
        env_name: str = None,
        settings: dict = None,
        display_name: str = None,
        region: str = None,
        env_groups: list[str] = None,
        owner_uid: int = None,
        nodes: dict = None,
        override_nodes: bool = None,
        skip_email: bool = False,
        skip_node_emails: bool = False,
    ):
        """
        :param id: unique identifier of the target JPS manifest in the Marketplace.
        :param env_name: target environment name.
        :param settings: JSON object with custom settings for the JPS manifest.
        :param display_name: custom alias (display name) for the deployed application.
        :param region: target environment region.
        :param env_groups: target environment group name or JSON array of group names.
        :param owner_uid: unique identifier of the target user account.
        :param nodes: JSON object with a list of environment nodes and their settings. Considered for 'jpsType: install' only.
        :param override_nodes: defines whether to override (true) or merge (false) nodes from the 'nodes' parameter with the nodes specified in the manifest.
        :param skip_email: defines whether to send email after the successful installation (false) or not (true).
        :param skip_node_emails: defines whether to send emails after the new nodes creation (false) or not (true).
        """
        return self._get(
            "Install",
            params={
                "id": id,
                "envName": env_name,
                "settings": settings,
                "displayName": display_name,
                "region": region,
                "envGroups": env_groups,
                "ownerUid": owner_uid,
                "nodes": nodes,
                "overrideNodes": override_nodes,
                "skipEmail": skip_email,
                "skipNodeEmails": skip_node_emails,
            },
        )

    def InstallAddon(
        self,
        env_name: str,
        app_id: str,
        settings: dict = None,
        node_group: list[str] = None,
        skip_email: bool = False,
    ):
        """
        :param env_name: target environment name.
        :param app_id: unique identifier of the target JPS manifest in the Marketplace.
        :param settings: JSON object with custom settings for the JPS manifest.
        :param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        :param skip_email: defines whether to send email after the successful installation (false) or not (true).
        """
        return self._get(
            "InstallAddon",
            params={
                "id": app_id,
                "envName": env_name,
                "settings": settings,
                "nodeGroup": node_group,
                "skipEmail": skip_email,
            },
            delimiter=",",
        )


class _Admin(Marketplace):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Admin
    """

    _endpoint2 = "admin"

    def AddApp(self, env_name: str, manifest: str):
        return self._get(
            "AddApp",
            params={
                "envName": env_name,
                "manifest": manifest,
            },
        )

    def DeleteApp(self, env_name: str, id: int):
        return self._get(
            "DeleteApp",
            params={
                "envName": env_name,
                "id": id,
            },
        )

    def EditApp(self, env_name: str, id: int, manifest: str):
        return self._get(
            "EditApp",
            params={
                "envName": env_name,
                "id": id,
                "manifest": manifest,
            },
        )

    def GetAppManifest(self, env_name: str, id: int):
        return self._get(
            "GetAppManifest",
            params={"envName": env_name, "id": id},
        )

    def GetApps(self, env_name: str, search: list[str] = None):
        return self._get(
            "GetApps",
            params={"envName": env_name, "search": search},
            delimiter=",",
        )

    def GetJpsSamples(self, env_name: str, type: list[str] = None):
        return self._get(
            "GetJpsSamples",
            params={"envName": env_name, "type": type},
            delimiter=",",
        )

    def PublishApp(self, env_name: str, id: int):
        return self._get(
            "PublishApp",
            params={"envName": env_name, "id": id},
        )

    def ScheduleAppsSync(
        self,
        env_name: str,
    ):
        return self._get(
            "ScheduleAppsSync",
            params={
                "envName": env_name,
            },
        )

    def SetSetting(
        self,
        env_name: str,
        name: str,
        values: str,
        override: list[bool] = None,
    ):
        return self._get(
            "SetSetting",
            params={
                "envName": env_name,
                "name": name,
                "values": values,
                "override": override,
            },
            delimiter=",",
        )

    def SyncExternalApps(
        self,
        env_name: str,
    ):
        return self._get(
            "SyncExternalApps",
            params={
                "envName": env_name,
            },
        )

    def SyncSystemApps(
        self,
        env_name: str,
    ):
        return self._get(
            "SyncSystemApps",
            params={
                "envName": env_name,
            },
        )

    def UnpublishApp(self, env_name: str, id: int):
        return self._get(
            "UnpublishApp",
            params={
                "envName": env_name,
                "id": id,
            },
        )

    def UpdateAppRating(
        self,
        env_name: str,
        id: int,
        rating: int,
    ):
        return self._get(
            "UpdateAppRating",
            params={
                "envName": env_name,
                "id": id,
                "rating": rating,
            },
        )

    def UpdateAppVisibilityLevels(
        self,
        env_name: str,
        id: int,
        visibility_levels: str,
    ):
        return self._get(
            "UpdateAppVisibilityLevels",
            params={
                "envName": env_name,
                "id": id,
                "visibilityLevels": visibility_levels,
            },
        )


class _Jps(Marketplace):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Jps
    """

    _endpoint2 = "jps"

    def ExecuteAppAction(
        self,
        app_unique_name: str,
        action: list[str] = None,
        settings_id: list[str] = None,
        params: list[str] = None,
        lang: list[str] = None,
    ):
        return self._get(
            "ExecuteAppAction",
            params={
                "appUniqueName": app_unique_name,
                "action": action,
                "settingsId": settings_id,
                "params": params,
                "lang": lang,
            },
            delimiter=",",
        )

    def GetAppInfo(
        self,
        jps: list[str] = None,
        lang: list[str] = None,
        owner_uid: list[str] = None,
    ):
        """
        param jps: custom JPS (manifest body, link, or application ID from the Marketplace).
        param lang: target installation language.
        param owner_uid: unique identifier of the target user account.
        """
        return self._get(
            "GetAppInfo",
            params={
                "jps": jps,
                "lang": lang,
                "ownerUid": owner_uid,
            },
            delimiter=",",
        )

    def GetAppSettings(
        self,
        app_unique_name: str,
        settings_id: list[str] = None,
        lang: list[str] = None,
    ):
        return self._get(
            "GetAppSettings",
            params={
                "appUniqueName": app_unique_name,
                "settingsId": settings_id,
                "lang": lang,
            },
            delimiter=",",
        )

    def GetEngineVersion(self):
        return self._get("GetEngineVersion", params={})

    def GetScriptingAppid(self):
        return self._get("GetScriptingAppid", params={})

    def Install(
        self,
        jps: str,
        env_name: str = None,
        settings: dict = None,
        node_group: str = None,
        display_name: str = None,
        region: str = None,
        env_groups: list[str] = None,
        owner_uid: int = None,
        logs_path: str = None,
        write_output_tasks: bool = False,
        skip_node_emails: bool = False,
    ):
        """
        param jps: custom JPS (manifest body, link, or application ID from the Marketplace).
        param env_name: target environment name.
        param settings: JSON object with custom settings for the JPS manifest.
        param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        param display_name: custom alias (display name) for the deployed JPS application.
        param region: target environment region.
        param env_groups: target environment group name or JSON array of group names.
        param owner_uid: unique identifier of the target user account.
        param logs_path: a relative path to the JPS installation log file, which is created in the user's application in the Backend-as-a-Service system. 'cs.log' by default.
        param write_output_tasks: defines whether write internal installation events (true) or not (false). It is used with the nested manifest installations.
        param skip_node_emails: defines whether to send emails after the new nodes creation (false) or not (true).
        """
        return self._get(
            "Install",
            params={
                "jps": jps,
                "envName": env_name,
                "settings": settings,
                "nodeGroup": node_group,
                "displayName": display_name,
                "region": region,
                "envGroups": env_groups,
                "ownerUid": owner_uid,
                "logsPath": logs_path,
                "writeOutputTasks": write_output_tasks,
                "skipNodeEmails": skip_node_emails,
            },
        )
