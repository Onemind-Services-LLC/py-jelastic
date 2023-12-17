from ..abstract import ClientAbstract

__all__ = ["Pricing"]


class Pricing(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.pricing

    Ref: https://docs.jelastic.com/api/private/#!/api/pricing
    """

    _endpoint1 = "pricing"

    @property
    def Option(self) -> "_Option":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.pricing.Option

        Ref: https://docs.jelastic.com/api/private/#!/api/pricing.Option
        """
        return _Option(session=self._session, token=self._token, debug=self._debug)

    @property
    def Tariff(self) -> "_Tariff":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.pricing.Tariff

        Ref: https://docs.jelastic.com/api/private/#!/api/pricing.Tariff
        """

        return _Tariff(session=self._session, token=self._token, debug=self._debug)


class _Option(Pricing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/pricing.Option
    """

    _endpoint2 = "option"

    def Create(self, tariff_option: dict, reseller_id: int = None):
        """
        Creates a new tariff option TariffOption for the main platform or reseller. It should be unique by name

        :param tariff_option: JSON representation of object which needs to be created.
        :param reseller_id: unique identifier of a reseller
        """
        return self._get(
            "Create", params={"tariffOption": tariff_option, "resellerId": reseller_id}
        )

    def Delete(self, name: str, reseller_id: int = None):
        """
        Deletes a tariff option TariffOption for the main platform or reseller.

        :param name: name of a tariff option
        :param reseller_id: unique identifier of a reseller
        """
        return self._get("Delete", params={"name": name, "resellerId": reseller_id})

    def Edit(self, tariff_option: dict, reseller_id: int = None):
        """
        Modifies a tariff option TariffOption for the main platform or reseller. It should be unique by name

        :param tariff_option: JSON representation of object which needs to be created.
        :param reseller_id: unique identifier of a reseller
        """
        return self._get(
            "Edit", params={"tariffOption": tariff_option, "resellerId": reseller_id}
        )

    def Get(self, reseller_id: int = None):
        """
        :param reseller_id: unique identifier of a reseller
        """
        return self._get("Get", params={"resellerId": reseller_id})


class _Tariff(Pricing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/pricing.Tariff
    """

    _endpoint2 = "tariff"

    def CreateGrid(self, tariff_grid: dict, reseller_id: int = None):
        """
        Creates a new tariff grid TariffGrid for the main platform or reseller. It should be unique by name

        :param tariff_grid: JSON representation of object which needs to be created.
        :param reseller_id: unique identifier of a reseller
        """
        return self._get(
            "CreateGrid", params={"tariffGrid": tariff_grid, "resellerId": reseller_id}
        )

    def CreateGridItem(self, grid_item: dict, reseller_id: int = None):
        """
        Creates a new tariff grid item TariffGridItem for the main platform or reseller. It should be unique by name

        :param grid_item: JSON representation of object which needs to be created.
        :param reseller_id: unique identifier of a reseller
        """
        return self._get(
            "CreateGridItem", params={"gridItem": grid_item, "resellerId": reseller_id}
        )

    def DeleteGrid(self, name: str, reseller_id: int = None):
        """
        Deletes a tariff grid TariffGrid by its name.

        :param name: name of the grid
        :param reseller_id: unique identifier of a reseller
        """
        return self._get("DeleteGrid", params={"name": name, "resellerId": reseller_id})

    def DeleteGridItem(self, name: str, reseller_id: int = None):
        """
        Deletes a tariff grid item TariffGridItem by its name.

        :param name: name of the grid item
        :param reseller_id: unique identifier of a reseller
        """
        return self._get(
            "DeleteGridItem", params={"name": name, "resellerId": reseller_id}
        )

    def EditGrid(self, tariff_grid: dict, reseller_id: int = None):
        """
        Modifies a tariff grid TariffGrid for the main platform or reseller. It should be unique by name

        :param tariff_grid: JSON representation of object which needs to be created.
        :param reseller_id: unique identifier of a reseller
        """
        return self._get(
            "EditGrid", params={"tariffGrid": tariff_grid, "resellerId": reseller_id}
        )

    def EditGridItem(self, grid_item: dict, reseller_id: int = None):
        """
        Modifies a tariff grid item TariffGridItem for the main platform or reseller. It should be unique by name

        :param grid_item: JSON representation of object which needs to be created.
        :param reseller_id: unique identifier of a reseller
        """
        return self._get(
            "EditGridItem", params={"gridItem": grid_item, "resellerId": reseller_id}
        )

    def GetGridItems(self, name: str, reseller_id: int = None):
        """
        Gets a list of tariff grid items TariffGridItem by grid name.

        :param name: name of the grid
        :param reseller_id: unique identifier of a reseller
        """
        return self._get(
            "GetGridItems", params={"name": name, "resellerId": reseller_id}
        )

    def GetGrids(self, names: list[str] = None, reseller_id: int = None):
        """
        Gets a list of tariff grids TariffGrid for the main platform or reseller.

        :param names: name(s) of the grid(s)
        :param reseller_id: unique identifier of a reseller
        """
        return self._get("GetGrids", params={"names": names, "resellerId": reseller_id})
