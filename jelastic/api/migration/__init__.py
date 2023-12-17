from ..abstract import ClientAbstract

__all__ = ["Migration"]


class Migration(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.migration
    """
    _endpoint1 = "migration"

    @property
    def Migration(self) -> "_Migration":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.migration.Migration

        https://docs.jelastic.com/api/private/#!/api/migration.Migration
        """
        return _Migration(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Migration(Migration):
    """
    https://docs.jelastic.com/api/private/#!/api/migration.Migration
    """
    _endpoint2 = "migration"

    def GetMigrationOperations(self, search: str = None):
        return self._get(
            "GetMigrationOperations",
            params={
                'search': search
            }
        )

    def Migrate(self):
        return self._get("Migrate")
