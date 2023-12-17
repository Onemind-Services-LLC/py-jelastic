from enum import Enum

from httpx import Client

# Import all API endpoints
from .api import *


class ClientState(Enum):
    # UNOPENED: The client has been instantiated, but has not been used to send a request or been opened by entering
    # the context of a `with` block
    UNOPENED = 1
    # OPENED: The client has either sent a request, or is within a `with` block
    OPENED = 2
    # CLOSED: The client has either exited the `with` block, or `close()` has been called explicitly
    CLOSED = 3


class Jelastic:
    """Jelastic API client, main entry point for all API operations."""

    def __init__(
        self, base_url: str, token: str, version: str = "1.0", debug: bool = False
    ):
        """
        To initialize with API endpoints for the Jelastic API.

        >>> with Jelastic(base_url, token) as client:
        >>>     client.billing.Account.GetAccount()

        :param base_url: Jelastic API base URL
        :param token: Jelastic API token
        :param version: Jelastic API version
        :param debug: Enable debug mode
        """
        if not base_url.startswith("http"):
            base_url = f"https://{base_url}"

        if base_url.endswith("/"):
            base_url = base_url[:-1]

        base_url = f"{base_url}/{version}"
        self._session = Client(base_url=base_url, timeout=None)
        self._state = ClientState.UNOPENED
        self._token = token
        self._debug = debug

    def __enter__(self) -> "Jelastic":
        if self._state != ClientState.UNOPENED:
            message = {
                ClientState.OPENED: "Cannot open a client instance more than once",
                ClientState.CLOSED: "Cannot reopen a client instance, once it has been closed",
            }[self._state]
            raise RuntimeError(message)

        self._state = ClientState.OPENED
        self._session = self._session.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._state = ClientState.CLOSED
        self._session.__exit__(exc_type, exc_val, exc_tb)

    @property
    def administration(self) -> Administration:
        return Administration(
            session=self._session, token=self._token, debug=self._debug
        )

    @property
    def automation(self) -> Automation:
        return Automation(session=self._session, token=self._token, debug=self._debug)

    @property
    def billing(self) -> Billing:
        return Billing(session=self._session, token=self._token, debug=self._debug)

    @property
    def data(self) -> Data:
        return Data(session=self._session, token=self._token, debug=self._debug)

    @property
    def development(self) -> Development:
        return Development(session=self._session, token=self._token, debug=self._debug)

    @property
    def environment(self) -> Environment:
        return Environment(session=self._session, token=self._token, debug=self._debug)

    @property
    def iaas(self) -> IaaS:
        return IaaS(session=self._session, token=self._token, debug=self._debug)

    @property
    def io(self) -> IO:
        return IO(session=self._session, token=self._token, debug=self._debug)

    @property
    def management(self) -> Management:
        return Management(session=self._session, token=self._token, debug=self._debug)

    @property
    def marketplace(self) -> Marketplace:
        return Marketplace(session=self._session, token=self._token, debug=self._debug)

    @property
    def message(self) -> Message:
        return Message(session=self._session, token=self._token, debug=self._debug)

    @property
    def migration(self) -> Migration:
        return Migration(session=self._session, token=self._token, debug=self._debug)

    @property
    def platform(self) -> Platform:
        return Platform(session=self._session, token=self._token, debug=self._debug)

    @property
    def pool(self) -> Pool:
        return Pool(session=self._session, token=self._token, debug=self._debug)

    @property
    def pricing(self) -> Pricing:
        return Pricing(session=self._session, token=self._token, debug=self._debug)

    @property
    def s3(self) -> S3:
        return S3(session=self._session, token=self._token, debug=self._debug)

    @property
    def security(self) -> Security:
        return Security(session=self._session, token=self._token, debug=self._debug)

    @property
    def statistic(self) -> Statistic:
        return Statistic(session=self._session, token=self._token, debug=self._debug)

    @property
    def system(self) -> System:
        return System(session=self._session, token=self._token, debug=self._debug)

    @property
    def thirdparty(self) -> ThirdParty:
        return ThirdParty(session=self._session, token=self._token, debug=self._debug)

    @property
    def users(self) -> Users:
        return Users(session=self._session, token=self._token, debug=self._debug)

    @property
    def utils(self) -> Utils:
        return Utils(session=self._session, token=self._token, debug=self._debug)
