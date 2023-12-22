from ..abstract import ClientAbstract

__all__ = ["Marketplace"]


class Marketplace(ClientAbstract):
    _endpoint1 = "marketplace"
    @property
    def Jps(self) -> "_Jps":
        """
        The JPS service provides methods for working with custom JPS manifests.
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.marketplace.Jps
        Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Jps
        """
        return _Jps(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Jps(Marketplace):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Jps
    """
    _endpoint2 = "jps"

    def ExecuteAppAction(
        self,
        app_unique_name: str,
        action: list[str]=None,
        settings_id: list[str]=None,
        params: list[str]=None,
        lang: list[str]=None,
    ):
        return self._get(
            "ExecuteAppAction",
            params={
                "appUniqueName": app_unique_name,
                "action": action,
                "settingsId": settings_id,
                "params": params,
                "lang": lang,
            }, delimiter=",",
        )
    def GetAppInfo(
        self,
        jps: list[str]=None,
        lang: list[str]=None,
        owner_uid: list[str]=None,
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
            }, delimiter=",",
        )
    def GetAppSettings(
        self,
        app_unique_name: str,
        settings_id: list[str]=None,
        lang: list[str]=None,
    ):
        return self._get(
            "GetAppSettings",
            params={
                "appUniqueName": app_unique_name,
                "settingsId": settings_id,
                "lang": lang,
            }, delimiter=",",
        )
    def GetEngineVersion(
        self):
        return self._get(
            "GetEngineVersion",
            params={
            }
        )
    def GetScriptingAppid(
        self):
        return self._get(
            "GetScriptingAppid",
            params={
            }
        )
    def Install(
        self,
        jps: str,
        env_name: list[str]=None,
        settings: list[str]=None,
        node_group: list[str]=None,
        display_name: list[str]=None,
        region: list[str]=None,
        env_groups: list[str]=None,
        owner_uid: list[int]=None,
        logs_path: list[str]=None,
        write_output_tasks: list[bool]=None,
        skip_node_emails: list[bool]=None,
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
                "settingsId": settings,
                "nodeGroup": node_group,
                "displayName": display_name,
                "region": region,
                "envGroups": env_groups,
                "ownerUid": owner_uid,
                "logsPath": logs_path,
                "writeOutputTasks": write_output_tasks,
                "skipNodeEmails": skip_node_emails,
            }, delimiter=",",
        )

    def Uninstall(
            self,
            app_unique_name: str,
            force: list[bool] = None,
    ):
        return self._get(
            "Uninstall",
            params={
                "appUniqueName": app_unique_name,
                "force": force,
            }, delimiter=",",
        )






