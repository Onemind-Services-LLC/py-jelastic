from ..abstract import ClientAbstract

__all__ = ["Marketplace"]


class Marketplace(ClientAbstract):
    _endpoint1 = "marketplace"

    @property
    def Admin(self) -> "_Admin":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.marketplace.Admin

        Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Admin
        """
        return _Admin(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Admin(Marketplace):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.Admin
    """

    _endpoint2 = "account"

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
