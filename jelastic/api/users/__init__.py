from datetime import datetime

from ..abstract import ClientAbstract

__all__ = ["Users"]


class Users(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users
    Ref: https://docs.jelastic.com/api/private/#!/api/users
    """

    _endpoint1 = "users"

    @property
    def Registration(self) -> "_Registration":
        """
        Registration of new users.
         >>> from jelastic import Jelastic
         >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
         >>> jelastic.users.Registration
         Ref: https://docs.jelastic.com/api/private/#!/api/users.Registration
        """
        return _Registration(
            session=self._session, token=self._token, debug=self._debug
        )


class _Registration(Users):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.users.Registration
     Ref: https://docs.jelastic.com/api/private/#!/api/users.Registration
    """

    _endpoint2 = "registration"

    def Activate(
        self,
        key: str,
        password: list[str] = None,
        skip_send_email: list[bool] = None,
        code: list[str] = None,
        reseller_id: list[int] = None,
    ):
        """
        param key: activation key received after registration. The activation key is sent to the email address provided during registration.
        param password: password for the new user.
        param skip_send_email: defines whether to send the activation email (false) or not (true).
        param code: custom code to be executed upon activation.
        param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "Activate",
            params={
                "key": key,
                "password": password,
                "skipSendEmail": skip_send_email,
                "code": code,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def CheckEmailExist(
        self,
        email: str,
    ):
        """
        param email: verifiable e-mail address
        """
        return self._get("CheckEmailExist", params={"email": email})

    def CheckEmailRegistration(
        self,
        email: str,
    ):
        """
        param email: verifiable e-mail address
        """
        return self._get("CheckEmailRegistration", params={"email": email})

    def CheckPassword(
        self,
        password: str,
    ):
        return self._get("CheckPassword", params={"password": password})

    def ClearSmsListData(
        self,
        email: str,
    ):
        """
        param email: email to generate confirmation key
        """
        return self._get("ClearSmsListData", params={"email": email})

    def CreateAccount(
        self,
        email: str,
        password: str,
        name: list[str] = None,
        check_email: list[bool] = None,
        welcome: list[str] = None,
        skip_send_email: list[bool] = None,
        reseller_id: list[int] = None,
    ):
        """
        param email: mailing address to which will be sent an activation key (as specified by user). The key activation is valid 24 hours after registration, if the key was not activated during this time, the user is automatically deleted, the key is not valid
        param password: password for the new user.
        param name: user name
        param check_email: verifying the existence of e-mail address (default is false)
        param welcome: optional. if invitation letter should be sent, url to redirect to after activation
        param skip_send_email: defines whether to send the activation email (false) or not (true).
        param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "CreateAccount",
            params={
                "email": email,
                "password": password,
                "name": name,
                "checkEmail": check_email,
                "welcome": welcome,
                "skipSendEmail": skip_send_email,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def CreateAuthKey(
        self,
        login: str,
        solution: str,
        auth_type: list[str] = None,
        expires_at: list[datetime] = None,
        type: list[str] = None,
    ):
        return self._get(
            "CreateAuthKey",
            params={
                "login": login,
                "solution": solution,
                "authType": auth_type,
                "expiresAt": expires_at,
                "type": type,
            },
            delimiter=",",
        )

    def CreateConfirmLinkUserKey(
        self,
        email: str,
        role: str,
        target_app_id: list[str] = None,
        application_right: list[str] = None,
    ):
        """
        param email: email to generate confirmation key
        param role: role that will be applied to a linked user after confirmation
        """
        return self._get(
            "CreateConfirmLinkUserKey",
            params={
                "email": email,
                "role": role,
                "targetAppid": target_app_id,
                "applicationRight": application_right,
            },
            delimiter=",",
        )

    def GeneratePassword(
        self,
        length: list[int] = None,
    ):
        """
        param length: define password length (default value is set by password policy: minLength, can not be less than minLength)
        """
        return self._get("GeneratePassword", params={"length": length})

    def GetSmsListData(
        self,
    ):
        return self._get("GetSmsListData", params={})

    def ResendInvitation(self, welcome: str):
        return self._get("ResendInvitation", params={"welcome": welcome})

    def SendSms(
        self,
        activation_key: str,
        email: str,
        phone: str,
        lang: list[str] = None,
    ):
        """
        param email: email to generate confirmation key
        param phone: phone number of user that receive message with verification code.
        param lang: localization language in standart ISO 639-1
        """
        return self._get(
            "SendSms",
            params={
                "activationKey ": activation_key,
                "email ": email,
                "phone ": phone,
                "lang ": lang,
            },
        )
