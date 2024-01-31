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

    def AddPolicy(
        self,
        role: str,
        object: str,
        rights: str,
        ruk: str = None,
    ):
        """
        :param role: name of the role
        :param object: object access
        :param rights: the rights of access
        """
        return self._get(
            "AddPolicy",
            params={"role": role, "object": object, "rights": rights, "ruk": ruk},
        )

    def ApplyRole(
        self,
        role: str,
        subject: str,
        ruk: str = None,
    ):
        """
        :param subject: subject access
        """
        return self._get(
            "ApplyRole",
            params={"role": role, "subject": subject, "ruk": ruk},
        )

    def CheckRights(
        self,
        subject: str,
        object: str,
        rights: str,
        ruk: str = None,
    ):
        """
        :param subject: the subject of access
        :param object: object access
        :param rights: the rights of access
        """
        return self._get(
            "CheckRights",
            params={"subject": subject, "object": object, "rights": rights, "ruk": ruk},
        )

    def CreateRole(
        self,
        role: str,
        ruk: str = None,
    ):
        """
        :param role: the name of (owner reserved the name, means the owner of the facility)
        """
        return self._get(
            "CreateRole",
            params={"role": role, "ruk": ruk},
        )

    def DeleteRole(
        self,
        role: str,
        ruk: str = None,
    ):
        """
        :param role: role name
        """
        return self._get(
            "DeleteRole",
            params={"role": role, "ruk": ruk},
        )

    def GetObjectsByRole(
        self,
        role: str,
        ruk: str = None,
    ):
        """
        :param role: the name of the role
        """
        return self._get(
            "GetObjectsByRole",
            params={"role": role, "ruk": ruk},
        )

    def GetPolicy(
        self,
        role: str,
        object: str = None,
        ruk: str = None,
    ):
        """
        :param role: name of the role
        :param object: object access
        """
        return self._get(
            "GetPolicy",
            params={"role": role, "object": object, "ruk": ruk},
        )

    def GetRights(
        self,
        subject: str,
        object: str,
        ruk: str = None,
    ):
        """
        :param subject: the subject of access
        :param object: object access
        """
        return self._get(
            "GetRights",
            params={"subject": subject, "object": object, "ruk": ruk},
        )

    def GetRightsByObject(
        self,
        object: str,
        ruk: str = None,
    ):
        """
        :param object: object access
        """
        return self._get(
            "GetRightsByObject",
            params={"object": object, "ruk": ruk},
        )

    def GetRightsBySubject(
        self,
        subject: str,
        ruk: str = None,
    ):
        """
        :param subject: the subject of access
        """
        return self._get(
            "GetRightsBySubject",
            params={"subject": subject, "ruk": ruk},
        )

    def GetRoles(
        self,
        ruk: str = None,
    ):
        return self._get("GetRoles", params={"ruk": ruk})

    def GetRolesByObject(
        self,
        object: str,
        ruk: str = None,
    ):
        """
        :param object: object access
        """
        return self._get(
            "GetRolesByObject",
            params={"object": object, "ruk": ruk},
        )

    def GetRolesBySubject(
        self,
        subject: str,
        ruk: str = None,
    ):
        """
        :param subject: the subject of access
        """
        return self._get(
            "GetRolesBySubject",
            params={"subject": subject, "ruk": ruk},
        )

    def GetSubjectsByRole(
        self,
        role: str,
        ruk: str = None,
    ):
        """
        :param role: the name of the role
        """
        return self._get(
            "GetSubjectsByRole",
            params={"role": role, "ruk": ruk},
        )

    def RemovePolicy(
        self,
        role: str,
        object: str,
        ruk: str = None,
    ):
        """
        :param role: name of the role
        :param object: object access
        """
        return self._get(
            "RemovePolicy",
            params={"role": role, "object": object, "ruk": ruk},
        )

    def RemoveRights(
        self,
        subject: str,
        object: str,
        ruk: str = None,
    ):
        """
        :param subject: subject access
        :param object: object access
        """
        return self._get(
            "RemoveRights",
            params={"subject": subject, "object": object, "ruk": ruk},
        )

    def RemoveRightsByObject(
        self,
        object: str,
        ruk: str = None,
    ):
        """
        :param object: object access
        """
        return self._get(
            "RemoveRightsByObject",
            params={"object": object, "ruk": ruk},
        )

    def RemoveRightsBySubject(
        self,
        subject: str,
        ruk: str = None,
    ):
        """
        :param subject: subject access
        """
        return self._get(
            "RemoveRightsBySubject",
            params={"subject": subject, "ruk": ruk},
        )

    def RemoveRole(
        self,
        role: str,
        subject: str,
        ruk: str = None,
    ):
        """
        :param role: name of the role
        :param subject: subject access
        """
        return self._get(
            "RemoveRole",
            params={"role": role, "subject": subject, "ruk": ruk},
        )

    def SetRights(
        self,
        object: str,
        subject: str,
        rights: str,
        ruk: str = None,
    ):
        """
        :param object: object access
        :param subject: subject access
        :param rights: permissions
        """
        return self._get(
            "SetRights",
            params={"object": object, "subject": subject, "rights": rights, "ruk": ruk},
        )


class _License(Security):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/security.License
    """

    _endpoint2 = "license"

    def Activate(
        self,
        serial: str = None,
        generate_smtp_creds: bool = None,
        ruk: str = None,
    ):
        return self._get(
            "Activate",
            params={
                "serial": serial,
                "generateSMTPCreds": generate_smtp_creds,
                "ruk": ruk,
            },
        )

    def GenerateSMTPSettings(
        self,
        ruk: str = None,
    ):
        return self._get(
            "GenerateSMTPSettings",
            params={"ruk": ruk},
        )

    def GetVZLicense(
        self,
        vz_type: str = None,
        ruk: str = None,
    ):
        return self._get(
            "GetVZLicense",
            params={"vzType": vz_type, "ruk": ruk},
        )

    def Validate(
        self,
        ruk: str = None,
    ):
        return self._get("Validate", params={"ruk": ruk})

    def ValidateServices(
        self,
        ruk: str = None,
    ):
        return self._get("ValidateServices", params={"ruk": ruk})

    def Welcome(
        self,
        allow_info_sharing: bool,
        ruk: str = None,
    ):
        return self._get(
            "ValidateServices",
            params={"allowInfoSharing": allow_info_sharing, "ruk": ruk},
        )
