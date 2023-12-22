from ..abstract import ClientAbstract

__all__ = ["Marketplace"]


class Marketplace(ClientAbstract):
    _endpoint1 = "marketplace"
    @property
    def Installation(self) -> "_Installation":
        """
        The Installation service provides extensive functionality for users to manage applications installed from the Marketplace or via Import.
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.marketplace.Installation
        Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Installation
        """
        return _Installation(
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
        action: list[str]=None,
        settings_id: list[str]=None,
        params: list[str]=None,
        lang: list[str]=None,
    ):
        """
        param app_unique_name: unique identifier of the particular installation.
        param action: unique identifier of the custom action name to be executed.
        param settings_id: unique identifier of the settings section of the manifest. Default settings form ID is 'main'.
        param params: JSON object with custom settings for the JPS manifest.
        param lang: target localization language.
        """
        return self._get(
            "ExecuteAction",
            params={
                "appUniqueName": app_unique_name,
                "action": action,
                "settingsId": settings_id,
                "params": params,
                "lang": lang,
            }, delimiter=",",
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
            }
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
            }
        )
    def GetScriptingAppid(
        self):
        return self._get(
            "GetScriptingAppid",
            params={}
        )
    def GetSettings(
        self,
        app_unique_name: str,
        settings_id: list[str]=None,
        lang: list[str]=None,
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
            }, delimiter=",",
        )
    def Uninstall(
        self,
        app_unique_name: str,
        force: list[bool]=None,
    ):
        """
        param app_unique_name: unique identifier of the particular installation.
        param force: defines whether to proceed (true) or interrupt (false) the operation in case of errors.
        """
        return self._get(
            "Uninstall",
            params={
                "appUniqueName": app_unique_name,
                "force": force,
            }, delimiter=",",
        )





