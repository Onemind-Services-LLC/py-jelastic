from typing import Literal
from ..abstract import ClientAbstract

__all__ = ["Security"]

MODE = Literal["STRONG", "MODERATE", "WEAK"]


class Security(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.security

    Ref: https://docs.jelastic.com/api/#!/security
    """

    _endpoint1 = "security"

    @property
    def AccessControl(self) -> "_AccessControl":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.security.AccessControl

        Ref: https://docs.jelastic.com/api/private/#!/api/security.AccessControl
        """
        return _AccessControl(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def License(self) -> "_License":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.security.License

        Ref: https://docs.jelastic.com/api/private/#!/api/security.License
        """
        return _License(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _AccessControl(Security):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/security.AccessControl
    """

    _endpoint2 = "accesscontrol"

    def AddPolicy(self, role: str, object: str, rights: str):
        """
        :param role: name of the role
        :param object: object access
        :param rights: the rights of access
        """
        return self._get(
            "AddPolicy", params={"role": role, "object": object, "rights": rights}
        )

    def ApplyRole(
        self,
        role: str,
        subject: str,
    ):
        """
        :param subject: subject access
        """
        return self._get(
            "ApplyRole",
            params={
                "role": role,
                "subject": subject,
            },
        )

    def CheckRights(self, subject: str, object: str, rights: str):
        """
        :param subject: the subject of access
        :param object: object access
        :param rights: the rights of access
        """
        return self._get(
            "CheckRights",
            params={"subject": subject, "object": object, "rights": rights},
        )

    def CreateRole(
        self,
        role: str,
    ):
        """
        :param role: the name of (owner reserved the name, means the owner of the facility)
        """
        return self._get(
            "CreateRole",
            params={
                "role": role,
            },
        )

    def DeleteRole(
        self,
        role: str,
    ):
        """
        :param role: role name
        """
        return self._get(
            "DeleteRole",
            params={
                "role": role,
            },
        )

    def GetObjectsByRole(
        self,
        role: str,
    ):
        """
        :param role: the name of the role
        """
        return self._get(
            "GetObjectsByRole",
            params={
                "role": role,
            },
        )

    def GetPolicy(
        self,
        role: str,
        object: list[str] = None,
    ):
        """
        :param role: name of the role
        :param object: object access
        """
        return self._get(
            "GetPolicy",
            params={
                "role": role,
                "object": object,
            },
            delimiter=",",
        )

    def GetRights(
        self,
        subject: str,
        object: str,
    ):
        """
        :param subject: the subject of access
        :param object: object access
        """
        return self._get(
            "GetRights",
            params={
                "subject": subject,
                "object": object,
            },
        )

    def GetRightsByObject(
        self,
        object: str,
    ):
        """
        :param object: object access
        """
        return self._get(
            "GetRightsByObject",
            params={
                "object": object,
            },
        )

    def GetRightsBySubject(
        self,
        subject: str,
    ):
        """
        :param subject: the subject of access
        """
        return self._get(
            "GetRightsBySubject",
            params={
                "subject": subject,
            },
        )

    def GetRoles(self):
        return self._get("GetRoles", params={})

    def GetRolesByObject(
        self,
        object: str,
    ):
        """
        :param object: object access
        """
        return self._get(
            "GetRolesByObject",
            params={
                "object": object,
            },
        )

    def GetRolesBySubject(
        self,
        subject: str,
    ):
        """
        :param subject: the subject of access
        """
        return self._get(
            "GetRolesBySubject",
            params={
                "subject": subject,
            },
        )

    def GetSubjectsByRole(
        self,
        role: str,
    ):
        """
        :param role: the name of the role
        """
        return self._get(
            "GetSubjectsByRole",
            params={
                "role": role,
            },
        )

    def RemovePolicy(
        self,
        role: str,
        object: str,
    ):
        """
        :param role: name of the role
        :param object: object access
        """
        return self._get(
            "RemovePolicy",
            params={
                "role": role,
                "object": object,
            },
        )

    def RemoveRights(
        self,
        subject: str,
        object: str,
    ):
        """
        :param subject: subject access
        :param object: object access
        """
        return self._get(
            "RemoveRights",
            params={
                "subject": subject,
                "object": object,
            },
        )

    def RemoveRightsByObject(
        self,
        object: str,
    ):
        """
        :param object: object access
        """
        return self._get(
            "RemoveRightsByObject",
            params={
                "object": object,
            },
        )

    def RemoveRightsBySubject(
        self,
        subject: str,
    ):
        """
        :param subject: subject access
        """
        return self._get(
            "RemoveRightsBySubject",
            params={
                "subject": subject,
            },
        )

    def RemoveRole(
        self,
        role: str,
        subject: str,
    ):
        """
        :param role: name of the role
        :param subject: subject access
        """
        return self._get(
            "RemoveRole",
            params={
                "role": role,
                "subject": subject,
            },
        )

    def SetRights(
        self,
        object: str,
        subject: str,
        rights: str,
    ):
        """
        :param object: object access
        :param subject: subject access
        :param rights: permissions
        """
        return self._get(
            "SetRights",
            params={
                "object": object,
                "subject": subject,
                "rights": rights,
            },
        )


class _License(Security):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/security.License
    """

    _endpoint2 = "license"

    def Activate(
        self,
        serial: list[str] = None,
        generate_smtp_creds: list[bool] = None,
    ):
        return self._get(
            "Activate",
            params={
                "serial": serial,
                "generateSMTPCreds": generate_smtp_creds,
            },
            delimiter=",",
        )

    def GenerateSMTPSettings(self):
        return self._get(
            "GenerateSMTPSettings",
            params={},
        )

    def GetVZLicense(
        self,
        vz_type: list[str] = None,
    ):
        return self._get(
            "GetVZLicense",
            params={
                "vzType": vz_type,
            },
        )

    def Validate(self):
        return self._get("Validate", params={})

    def ValidateServices(self):
        return self._get("ValidateServices", params={})

    def Welcome(self, allow_info_sharing: bool):
        return self._get(
            "ValidateServices", params={"allowInfoSharing": allow_info_sharing}
        )
