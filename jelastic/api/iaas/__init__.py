from ..abstract import ClientAbstract

__all__ = ["IaaS"]


class IaaS(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.iaas

    Ref: https://docs.jelastic.com/api/private/#!/api/iaas
    """

    _endpoint1 = "iaas"

    @property
    def Project(self) -> "_Project":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.iaas.Project

        Ref: https://docs.jelastic.com/api/private/#!/api/iaas.Project
        """
        return _Project(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Project(IaaS):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/iaas.Project
    """

    def Create(
            self,
            host_group: str,
            project_name: str,
            owner_uid: int = None,
            description: str = None,
    ):
        """
        Creates a new Virtuozzo Hybrid Infrastructure project.

        :param host_group: unique identifier of the target host group.
        :param project_name: new project's name.
        :param owner_uid: unique identifier of the project's owner.
        :param description: new project's description.
        """
        return self._get(
            "Create",
            params={
                "hostGroup": host_group,
                "projectName": project_name,
                "ownerUid": owner_uid,
                "description": description,
            },
        )

    def Delete(self, host_group: str, project_id: str, owner_uid: int = None):
        """
        Deletes a specified Virtuozzo Hybrid Infrastructure project.

        :param host_group: unique identifier of the target host group.
        :param project_id: unique identifier of the target project.
        :param owner_uid: unique identifier of the project's owner.
        """
        return self._get(
            "Delete",
            params={
                "hostGroup": host_group,
                "projectId": project_id,
                "ownerUid": owner_uid,
            },
        )

    def Get(self, host_group: str, owner_uid: int = None):
        """
        Returns a list of Virtuozzo Hybrid Infrastructure projects related to the user and host group.

        :param host_group: unique identifier of the target host group.
        :param owner_uid: unique identifier of the project's owner.
        """
        return self._get(
            "Get",
            params={
                "hostGroup": host_group,
                "ownerUid": owner_uid,
            },
        )

    def Update(self, host_group: str, project_id: str, project_name: str, owner_uid: int = None,
                description: str = None):
        """
        Changes the specified project name and description.

        :param host_group: unique identifier of the target host group.
        :param project_id: unique identifier of the target project.
        :param project_name: updated project's name.
        :param owner_uid: unique identifier of the project's owner.
        :param description: updated project's description.
        """
        return self._get(
            "Update",
            params={
                "hostGroup": host_group,
                "projectId": project_id,
                "projectName": project_name,
                "ownerUid": owner_uid,
                "description": description,
            },
        )
