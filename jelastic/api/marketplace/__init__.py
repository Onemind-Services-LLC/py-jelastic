from ..abstract import ClientAbstract

__all__ = ["Marketplace"]


class Marketplace(ClientAbstract):
    _endpoint1 = "marketplace"

    @property
    def App(self) -> "_App":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.marketplace.App
        Ref: https://docs.jelastic.com/api/private/#!/api/marketplace.App
        """
        return _App(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


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
        envName: str,
        node_group: list[str] = None,
        search: list[str] = None,
    ):
        """
        :param envName: target environment name.
        :param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        :param search: JSON object with the search parameters. For example (all fields are optional):
        """
        return self._get(
            "GetAddonList",
            params={
                "envName": envName,
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
        env_name: list[str] = None,
        settings: list[str] = None,
        display_name: list[str] = None,
        region: list[str] = None,
        env_groups: list[str] = None,
        owner_uid: list[int] = None,
        nodes: list[str] = None,
        override_nodes: list[bool] = None,
        skip_email: list[bool] = None,
        skip_node_emails: list[bool] = None,
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
            delimiter=",",
        )

    def InstallAddon(
        self,
        id: str,
        settings: list[str] = None,
        node_group: list[str] = None,
        skip_email: list[bool] = None,
    ):
        """
        :param id: unique identifier of the target JPS manifest in the Marketplace.
        :param settings: JSON object with custom settings for the JPS manifest.
        :param node_group: unique identifier of the target node group (layer), e.g. “cp” for the default application server layer.
        :param skip_email: defines whether to send email after the successful installation (false) or not (true).
        """
        return self._get(
            "InstallAddon",
            params={
                "id": id,
                "settings": settings,
                "nodeGroup": node_group,
                "skipEmail": skip_email,
            },
            delimiter=",",
        )
