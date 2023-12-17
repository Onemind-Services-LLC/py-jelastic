from ..abstract import ClientAbstract

__all__ = ["Message"]


class Message(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.message

    """

    _endpoint1 = "message"

    @property
    def Email(self) -> "_Email":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.message.Email

        Ref: https://docs.jelastic.com/api/private/#!/api/message.Email
        """
        return _Email(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Email(Message):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/message.Email
    """

    _endpoint2 = "email"

    def Send(
        self,
        to: str,
        subject: str,
        body: str,
        from_email: str = None,
        reply_to: str = None,
        type: str = None,
        reseller_id: int = None,
    ):
        return self._get(
            "Send",
            params={
                "to": to,
                "subject": subject,
                "body": body,
                "from": from_email,
                "replyTo": reply_to,
                "type": type,
                "resellerId": reseller_id,
            },
        )

    def SendToUser(
        self,
        login: str,
        subject: str,
        body: str,
        from_email: str = None,
        reseller_id: int = None,
    ):
        return self._get(
            "SendToUser",
            params={
                "login": login,
                "subject": subject,
                "body": body,
                "from": from_email,
                "resellerId": reseller_id,
            },
        )
