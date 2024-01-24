from typing import Any
from ..abstract import ClientAbstract

__all__ = ["Development"]


class Development(ClientAbstract):
    _endpoint1 = "development"

    @property
    def Applications(self) -> "_Applications":
        """
        Service Management applications. Used to create new applications and settings.

         >>> from jelastic import Jelastic
         >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
         >>> jelastic.development.Applications

         Ref: https://docs.jelastic.com/api/private/#!/api/development.Applications
        """
        return _Applications(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Scripting(self) -> "_Scripting":
        """
        Service Management applications. Used to create new applications and settings.

         >>> from jelastic import Jelastic
         >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
         >>> jelastic.development.Scripting

         Ref: https://docs.jelastic.com/api/private/#!/api/development.Scripting
        """
        return _Scripting(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Applications(Development):
    """
    Service Management applications. Used to create new applications and settings.

    Ref: https://docs.jelastic.com/api/private/#!/api/development.Applications
    """

    _endpoint2 = "applications"

    def AddAppToPool(
            self,
            name: str,
            target_appid: str,
    ):
        return self._get(
            "AddAppToPool",
            params={
                "name": name,
                "targetAppid": target_appid,
            },
        )

    def AllowAppAccess(
            self,
            target_appid: str,
            allow_appid: str,
    ):
        """
        :param target_appid: the application identifier to which you can access using the session received in another application. You can list separated by commas multiple applications. In targetAppid can specify only the application ID for which you have the rights owner (owner) or admin (administrator)
        :param allow_appid: application Identifier session which can be used in the identifier specified in targetAppid. In allowAppid can specify any existing application ID
        """
        return self._get(
            "AllowAppAccess",
            params={
                "targetAppid": target_appid,
                "allowAppid": allow_appid,
            },
        )

    def ChangeAppInfo(self, target_appid: str, field: str, value: str = None):
        """
        :param target_appid: id editable applications
        :param field: the name of the edited field. Valid values are:
        :param value: new value field
        """
        return self._get(
            "ChangeAppInfo",
            params={
                "targetAppid": target_appid,
                "field": field,
                "value": value,
            },
        )

    def ChangeSolutionInfo(
            self,
            target_appid: str,
            field: str,
            value: str,
    ):
        return self._get(
            "ChangeSolutionInfo",
            params={
                "targetAppid": target_appid,
                "field": field,
                "value": value,
            },
        )

    def CleanOwnerCache(
            self,
            user_id: int = None,
            clean_all_apps: bool = None,
    ):
        return self._get(
            "CleanOwnerCache",
            params={
                "userId": user_id,
                "cleanAllApps": clean_all_apps,
            },
        )

    def CloneApp(
            self,
            target_appid: str,
            name: str = None,
    ):
        return self._get(
            "CloneApp",
            params={
                "targetAppid": target_appid,
                "name": name,
            },
        )

    def ConfirmAppTransferRequest(
            self,
            key: str,
    ):
        """
        :param key: disposable confirmation key
        """
        return self._get(
            "ConfirmAppTransferRequest",
            params={
                "key": key,
            },
        )

    def CreateAppsPool(
            self,
            name: str,
    ):
        return self._get(
            "CreateAppsPool",
            params={
                "name": name,
            },
        )

    def CreateConfirmAppTransferKey(
            self,
            email: str,
    ):
        """
        param email: email to generate confirmation key
        """
        return self._get(
            "CreateConfirmAppTransferKey",
            params={
                "email": email,
            },
        )

    def CreatePersistence(
            self,
            target_appid: str,
            config: str = None,
    ):
        """
        param target_appid: unique identifier of the target application.
        param config: JSON object with the persistence configurations.
        """
        return self._get(
            "CreatePersistence",
            params={
                "targetAppid": target_appid,
                "config": config,
            },
        )

    def CreateSolution(
            self,
            target_appid: str,
    ):
        return self._get(
            "CreateSolution",
            params={
                "targetAppid": target_appid,
            },
        )

    def DeleteApp(
            self,
            password: str,
            target_appid: str,
    ):
        """
        param password: the user password (for this method to re-authentication)
        param target_appid: id remove applications
        """
        return self._get(
            "DeleteApp",
            params={
                "password": password,
                "targetAppid": target_appid,
            },
        )

    def DeleteAppsPool(
            self,
            name: str,
    ):
        return self._get(
            "DeleteAppsPool",
            params={
                "name": name,
            },
        )

    def DeleteSolution(
            self,
            target_appid: str,
    ):
        return self._get(
            "DeleteSolution",
            params={
                "targetAppid": target_appid,
            },
        )

    def ExportAppPersistance(
            self,
            target_appid: str,
    ):
        return self._get(
            "ExportAppPersistance",
            params={
                "targetAppid": target_appid,
            },
        )

    def ExportAppResources(
            self,
            target_appid: str,
    ):
        return self._get(
            "ExportAppResources",
            params={
                "targetAppid": target_appid,
            },
        )

    def FindSolutions(
            self,
            keywords: str = None,
            description: str = None,
            froms: int = None,
            count: int = None,
    ):
        return self._get(
            "FindSolutions",
            params={
                "keywords": keywords,
                "description": description,
                "froms": froms,
                "count": count,
            },
        )

    def GenerateApp(
            self,
            name: str,
            description: str = None,
            domain: str = None,
            keywords: str = None,
            config: str = None,
    ):
        """
        param name: the name of the application (max. 128 characters)
        param description: description of application (max. 512 characters)
        param domain: address that hosts the application (max. 256 characters). You can specify the domain and IP address (in the format xxx.xxx.xxx.xxx). Address mainly indicated for web applications, but it is possible for the desktop. If you want to allow the use of an ID to multiple addresses, they are listed separated by commas
        """
        return self._get(
            "GenerateApp",
            params={
                "name": name,
                "description": description,
                "domain": domain,
                "keywords": keywords,
                "config": config,
            },
        )

    def GenerateAppWithAppID(
            self,
            name: str,
            idapp: str,
            description: str = None,
            domain: str = None,
            keywords: str = None,
            config: str = None,
    ):
        """
        param name: the name of the application (max. 128 characters)
        param description: description of application (max. 512 characters)
        param domain: address that hosts the application (max. 256 characters). You can specify the domain and IP address (in the format xxx.xxx.xxx.xxx). Address mainly indicated for web applications, but it is possible for the desktop. If you want to allow the use of an ID to multiple addresses, they are listed separated by commas
        """
        return self._get(
            "GenerateAppWithAppID",
            params={
                "name": name,
                "idapp": idapp,
                "description": description,
                "domain": domain,
                "keywords": keywords,
                "config": config,
            },
        )

    def GenerateSharedApp(
            self,
            owner_login: str,
            name: str,
            description: str = None,
            domain: str = None,
            keywords: str = None,
            config: str = None,
    ):
        """
        param owner_login: login of the environment's owner
        param name: the name of the application (max. 128 characters)
        param description: description of application (max. 512 characters)
        param domain: address that hosts the application (max. 256 characters). You can specify the domain and IP address (in the format xxx.xxx.xxx.xxx). Address mainly indicated for web applications, but it is possible for the desktop. If you want to allow the use of an ID to multiple addresses, they are listed separated by commas
        """
        return self._get(
            "GenerateSharedApp",
            params={
                "ownerLogin": owner_login,
                "name": name,
                "description": description,
                "domain": domain,
                "keywords": keywords,
                "config": config,
            },
        )

    def GetApp(
            self,
            target_appid: str,
    ):
        return self._get(
            "GetApp",
            params={
                "targetAppid": target_appid,
            },
        )

    def GetAppAccess(
            self,
            target_appid: str,
    ):
        return self._get(
            "GetAppAccess",
            params={
                "targetAppid": target_appid,
            },
        )

    def GetAppHome(
            self,
    ):
        return self._get("GetAppHome", params={})

    def GetAppPermission(
            self,
            target_appid: str,
    ):
        """
        param target_appid: the application identifier for which information is requested
        """
        return self._get(
            "GetAppPermission",
            params={
                "targetAppid": target_appid,
            },
        )

    def GetApps(
            self,
            target_appid: str = None,
    ):
        """
        param target_appid: the application identifier for which information is requested
        """
        return self._get(
            "GetApps",
            params={
                "targetAppid": target_appid,
            },
        )

    def GetAppsByLogin(
            self,
            login: str,
    ):
        return self._get(
            "GetAppsByLogin",
            params={
                "login": login,
            },
        )

    def GetAppsPools(
            self,
            name: str = None,
    ):
        return self._get(
            "GetAppsPools",
            params={
                "name": name,
            },
        )

    def GetConfirmAppTransferKey(self):
        return self._get("GetConfirmAppTransferKey", params={})

    def GetConfirmAppTransferKeys(
            self,
            appid: list[str] = None,
    ):
        """
        param appid: comma-separated list of environment identifiers
        """
        return self._get(
            "GetConfirmAppTransferKeys",
            params={
                "appids": appid,
            },
            delimiter=",",
        )

    def GetSharedAppsByLogin(
            self,
            login: str,
    ):
        """
        param login: login of the target user
        """
        return self._get(
            "GetSharedAppsByLogin",
            params={
                "login": login,
            },
        )

    def GetSharedAppsByOwnerLogin(
            self,
            owner_login: str,
            login: str,
    ):
        return self._get(
            "GetSharedAppsByOwnerLogin",
            params={
                "ownerLogin": owner_login,
                "login": login,
            },
        )

    def GetSharedAppsByOwnerLogins(
            self,
            owner_login: str,
            logins: str,
    ):
        return self._get(
            "GetSharedAppsByOwnerLogins",
            params={
                "ownerLogin": owner_login,
                "logins": logins,
            },
        )

    def GetSolution(
            self,
            target_appid: str,
    ):
        return self._get(
            "GetSolution",
            params={
                "targetAppid": target_appid,
            },
        )

    def GetSolutions(
            self,
            target_appid: str = None,
    ):
        return self._get(
            "GetSolutions",
            params={
                "targetAppid": target_appid,
            },
        )

    def GetUserAppPermission(
            self,
            target_appid: str,
            rights: str = None,
    ):
        return self._get(
            "GetUserAppPermission",
            params={
                "targetAppid": target_appid,
                "rights": rights,
            },
        )

    def ImportAppPersistance(
            self,
            path: str,
            target_appid: str = None,
    ):
        return self._get(
            "ImportAppPersistance",
            params={
                "path": path,
                "targetAppid": target_appid,
            },
        )

    def ImportAppResources(
            self,
            path: str,
            target_appid: str = None,
    ):
        return self._get(
            "ImportAppResources",
            params={
                "path": path,
                "targetAppid": target_appid,
            },
        )

    def IsAppsInstalled(
            self,
    ):
        return self._get("IsAppsInstalled", params={})

    def RebuildApp(
            self,
            target_appid: str,
    ):
        return self._get(
            "RebuildApp",
            params={
                "targetAppid": target_appid,
            },
        )

    def RemoveAppAccess(self, target_appid: str, allow_appid: str):
        return self._get(
            "RemoveAppAccess",
            params={"targetAppid": target_appid, "allowAppid": allow_appid},
        )

    def RemoveAppFromPool(
            self,
            name: str,
            target_appid: str,
    ):
        return self._get(
            "RemoveAppFromPool",
            params={
                "name": name,
                "targetAppid": target_appid,
            },
        )

    def SetAppPermission(
            self,
            target_appid: str,
            login: str,
            rights: str = None,
    ):
        return self._get(
            "SetAppPermission",
            params={
                "targetAppid": target_appid,
                "login": login,
                "rights": rights,
            },
        )


class _Scripting(Development):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/development.Scripting
    """

    _endpoint2 = "scripting"

    def Build(
            self,
            script: str,
            app_id: str = None,
    ):
        return self._get(
            "Build",
            params={
                "script": script,
                "appid": app_id,
            },
        )

    def BuildStubs(self,app_id: str = None,):
        return self._get(
            "BuildStubs",
            params={"appid": app_id,},
        )

    def ChangeScript(
            self,
            name: str,
            field: str,
            value: str = None,
            app_id: str = None,
    ):
        return self._get(
            "ChangeScript",
            params={
                "name": name,
                "field": field,
                "value": value,
                "appid": app_id,
            },
        )

    def CreateScript(
            self,
            name: str,
            type: str,
            code: str = None,
            annotations: str = None,
            app_id: str = None,
    ):
        return self._get(
            "CreateScript",
            params={
                "name": name,
                "type": type,
                "code": code,
                "annotations": annotations,
                "appid": app_id,
            },
        )

    def DeleteScript(self, name: str,app_id: str = None,):
        return self._get(
            "DeleteScript",
            params={
                "name": name,
                "appid": app_id,
            },
        )

    def Eval(
            self,
            script: str,
            params: Any = None,
            app_id: str = None,
    ):
        return self._get(
            "Eval",
            params={
                "script": script,
                "params": params,
                "appid": app_id,
            },
        )

    def EvalCode(
            self,
            code: str,
            type: str,
            annotations: str = None,
            params: Any = None,
            app_id: str = None,
    ):
        return self._get(
            "EvalCode",
            params={
                "code": code,
                "type": type,
                "annotations": annotations,
                "params": params,
                "appid": app_id,
            },
        )

    def ExportScripts(self, overwrite: bool = None,app_id: str = None,):
        return self._get(
            "ExportScripts",
            params={
                "overwrite": overwrite,
                "appid": app_id,
            },
        )

    def GetEngineInfo(self,app_id: str = None,):
        return self._get(
            "GetEngineInfo",
            params={"appid": app_id,},
        )

    def GetScript(self, name: str,app_id: str = None,):
        return self._get(
            "GetScript",
            params={
                "name": name,
                "appid": app_id,
            },
        )

    def GetScripts(
            self,
            type: str = None,
            From: int = None,
            count: int = None,
            app_id: str = None,
    ):
        return self._get(
            "GetScripts",
            params={
                "type": type,
                "from": From,
                "count": count,
                "appid": app_id,
            },
        )
