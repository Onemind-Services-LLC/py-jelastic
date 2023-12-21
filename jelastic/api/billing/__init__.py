import json
from datetime import datetime, date
from typing import Literal

from ..abstract import ClientAbstract

__all__ = ["Billing"]

PERIOD = Literal["AGE", "YEAR", "MONTH", "WEEK", "DAY", "HOUR"]


class Billing(ClientAbstract):
    """
    The Billing service provides methods for managing user accounts and their billing information.

    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.billing

    Ref: https://docs.jelastic.com/api/#!/billing
    """

    _endpoint1 = "billing"

    @property
    def Account(self) -> "_Account":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Account

        Ref: https://docs.jelastic.com/api/#!/api/billing.Account
        """
        return _Account(session=self._session, token=self._token, debug=self._debug)

    @property
    def Pricing(self) -> "_Pricing":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Pricing

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.Pricing
        """
        return _Pricing(session=self._session, token=self._token, debug=self._debug)

    @property
    def Reseller(self) -> "_Reseller":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Reseller

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.Reseller
        """
        return _Reseller(session=self._session, token=self._token, debug=self._debug)

    @property
    def ServicePlan(self) -> "_ServicePlan":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.ServicePlan

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.ServicePlan
        """
        return _ServicePlan(session=self._session, token=self._token, debug=self._debug)


class _Account(Billing):
    """
    The methods of this service provide billing information about a user account (such as UID, balance, billing history,
    quotas, etc.) and allow managing it.

    Ref: https://docs.jelastic.com/api/#!/api/billing.Account
    """

    _endpoint2 = "account"

    def AddAccount(self, uid: int):
        """
        Create new trial account in JBilling system.
        """
        return self._get("AddAccount", params={"uid": uid})

    def ChangeEmail(self, login: str, email: str):
        """
        Changes user’s email address.
        """
        return self._get("ChangeEmail", params={"login": login, "email": email})

    def ChangeGroup(
            self,
            group_name: str,
            uids: list[str] = None,
            send_email: bool = False,
            template: str = None,
    ):
        """
        Change account group for selected users
        """
        return self._get(
            "ChangeGroup",
            params={
                "groupName": group_name,
                "uids": uids,
                "sendEmail": send_email,
                "template": template,
            },
        )

    def ChangePhoneNumber(self, login: str, number: str):
        """
        Changes user’s phone number.
        """
        return self._get("ChangePhoneNumber", params={"login": login, "number": number})

    def ChargeAccountByUid(
            self, uid: int, amount: float, description: str, env_name: str = None
    ):
        """
        Charge account by uid.
        """
        return self._get(
            "ChargeAccountByUid",
            params={
                "uid": uid,
                "amount": amount,
                "description": description,
                "envName": env_name,
            },
        )

    def ConvertToCommercial(self, customer: dict):
        """
        Make trial account commercial one. This method register Jbilling account into extern billing system. Commercial
        client can create auto payment, just pay service plans.

        externBillingSystemId need if hoster has multiple billing systems. And its user belongs to one specific system.
        This is one place where it's needed to point it obviously.
        """
        customer = json.dumps(customer)

        return self._get("ConvertToCommercial", params={"customer": customer})

    def ConvertToCommercialAndPay(
            self,
            customer: dict,
            pay_method_type: str,
            service_plan_id: int,
            auto_service_plan_id: int = None,
            auto_refill_main_balance: int = None,
            auto_refill_period: str = None,
    ):
        """
        Make trial account commercial one. This method register Jbilling account into extern billing system. Commercial
        client can create auto payment, just pay service plans.
        """
        customer = json.dumps(customer)

        return self._get(
            "ConvertToCommercialAndPay",
            params={
                "customer": customer,
                "payMethodType": pay_method_type,
                "servicePlanId": service_plan_id,
                "autoServicePlanId": auto_service_plan_id,
                "autoRefillMainBalance": auto_refill_main_balance,
                "autoRefillPeriod": auto_refill_period,
            },
        )

    def ConvertToTrial(
            self,
            template: str,
            uids: list[str] = None,
            start_time: datetime = None,
            end_time: datetime = None,
            start: int = None,
            count: int = None,
            bonus: float = None,
    ):
        """
        Converts non-trial and billing accounts to trial.
        """
        return self._get(
            "ConvertToTrial",
            params={
                "template": template,
                "uids": uids,
                "startTime": start_time,
                "endTime": end_time,
                "start": start,
                "count": count,
                "bonus": bonus,
            },
        )

    def EnableUser(self, uid: int):
        """
        Enables user account.
        """
        return self._get("EnableUser", params={"uid": uid})

    def ExportAccountBillingHistoryByPeriod(
            self,
            start_time: datetime,
            end_time: datetime,
            period: PERIOD = "DAY",
            time_offset: int = None,
            group_nodes: bool = False,
            target_app_id: str = None,
    ):
        """
        Generates a link for downloading the specified account's billing history for the specific period.
        """
        return self._get(
            "ExportAccountBillingHistoryByPeriod",
            params={
                "targetAppid": target_app_id,
                "startTime": start_time,
                "endTime": end_time,
                "period": str(period),
                "timeOffset": time_offset,
                "groupNodes": group_nodes,
            },
        )

    def ExportEnvBillingHistoryByPeriod(
            self,
            start_time: datetime,
            end_time: datetime,
            time_offset: int,
            period: PERIOD = "DAY",
            group_nodes: bool = False,
    ):
        """
        Generates a link for downloading the specified environment's billing history for the specific period.
        """
        return self._get(
            "ExportEnvBillingHistoryByPeriod",
            params={
                "startTime": start_time,
                "endTime": end_time,
                "period": str(period),
                "timeOffset": time_offset,
                "groupNodes": group_nodes,
            },
        )

    def FundAccount(
            self, uid: int, amount: float, is_bonus: bool = False, note: str = None
    ):
        """
        Fund account by uid.

        :param uid: unique identifier of the target user whose balance will be changed
        :param amount: positive value of money
        :param is_bonus: false change bonus balance otherwise change main balance
        :param note: note for transaction
        """
        return self._get(
            "FundAccount",
            params={"uid": uid, "amount": amount, "isBonus": is_bonus, "note": note},
        )

    def FundAndActivateAccount(self, uid: int, amount: float, note: str = None):
        """
        Fund account by uid, activate it and set billing group.

        :param uid: unique identifier of the target user whose balance will be changed
        :param amount: positive value of money
        :param note: note for transaction
        """
        return self._get(
            "FundAndActivateAccount",
            params={"uid": uid, "amount": amount, "note": note},
        )

    def GetAccount(self):
        """
        Returns account information based on the user session.
        """
        return self._get("GetAccount")

    def GetAccountBillingByEngineTypeAndPeriod(
            self,
            start_time: datetime,
            end_time: datetime,
            owner_uid: str = None,
            engine_types: list[str] = None,
            period: PERIOD = "DAY",
            time_offset: int = None,
    ):
        """
        Returns account billing information for the specified period.

        :param owner_uid: owner uid
        :param engine_types: list of engine types
        :param start_time: start time of the period
        :param end_time: end time of the period
        :param period: period of the billing
        :param time_offset: time offset
        """
        start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
        end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")

        return self._get(
            "GetAccountBillingByEngineTypeAndPeriod",
            params={
                "ownerUid": owner_uid,
                "engineTypes": engine_types,
                "startTime": start_time,
                "endTime": end_time,
                "period": period,
                "timeOffset": time_offset,
            },
        )

    def GetAccountBillingHistoryByPeriod(
            self,
            start_time: datetime,
            end_time: datetime,
            period: PERIOD = "DAY",
            time_offset: int = None,
            group_nodes: bool = False,
            target_app_id: str = None,
    ):
        """
        Gets account billing history.
        """
        start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
        end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")

        return self._get(
            "GetAccountBillingHistoryByPeriod",
            params={
                "targetAppid": target_app_id,
                "startTime": start_time,
                "endTime": end_time,
                "period": str(period),
                "timeOffset": time_offset,
                "groupNodes": group_nodes,
            },
        )

    def GetAccounts(
            self,
            lebalance: str = None,
            order_field: str = None,
            order_direction: str = None,
            filter_field: str = None,
            filter_value: str = None,
            start_row: int = None,
            result_count: int = None,
    ):
        """
        Gets accounts.
        """
        return self._get(
            "GetAccounts",
            params={
                "lebalance": lebalance,
                "orderField": order_field,
                "orderDirection": order_direction,
                "filterField": filter_field,
                "filterValue": filter_value,
                "startRow": start_row,
                "resultCount": result_count,
            },
        )

    def GetAccountsByLimits(self, uidslimits: list[str]):
        """
        Gets accounts by limits.
        """
        # Ensure the uidslimits in the correct format
        # Example: '1234:100.00;6789:20.00'
        return self._get(
            "GetAccountsByLimits", params={"uidslimits": uidslimits}, delimiter=";"
        )

    def GetAccountsByPersonalThreshold(self):
        """
        Get accounts for remind which balance less then setted by user.
        """
        return self._get("GetAccountsByPersonalThreshold")

    def GetAccountsByUids(self, uids: list[str], lebalance: str = None):
        """
        Gets accounts by user ids.
        """
        return self._get(
            "GetAccountsByUids", params={"uids": uids, "lebalance": lebalance}
        )

    def GetAccountsForDeactivation(self):
        """
        Get accounts for deactivation. Such as bonus is zero or trial period ended for trial accounts and balance less
        then allowed for billing accounts.
        """
        return self._get("GetAccountsForDeactivation")

    def GetAccountsForDestroying(self):
        """
        Get accounts for destroying which in status inactive more then allowed.
        """
        return self._get("GetAccountsForDestroying")

    def GetAggClusterBillingHistory(
            self,
            start_time: datetime,
            end_time: datetime,
            interval: int,
            sum_fields: list[str],
            is_paid: bool = False,
    ):
        """
        Gets account billing history.
        """
        return self._get(
            "GetAggClusterBillingHistory",
            params={
                "startTime": start_time,
                "endTime": end_time,
                "interval": interval,
                "sumFields": sum_fields,
                "isPaid": is_paid,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetAggExtraBillingHistory(
            self,
            start_time: datetime,
            end_time: datetime,
            interval: int,
            is_paid: bool = False,
            type: str = None,
            names: list[str] = None,
    ):
        return self._get(
            "GetAggExtraBillingHistory",
            params={
                "startTime": start_time,
                "endTime": end_time,
                "interval": interval,
                "isPaid": is_paid,
                "type": type,
                "names": names,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetBillingInfo(self):
        """
        Returns account billing information.
        """
        return self._get("GetBillingInfo")

    def GetClusterBillingHistory(
            self, start_time: datetime, end_time: datetime, interval: int = None
    ):
        """
        Gets account billing history.
        """
        return self._get(
            "GetClusterBillingHistory",
            params={"startTime": start_time, "endTime": end_time, "interval": interval},
        )

    def GetCollaborationQuotas(
            self,
            collaboration_id: int = None,
            owner_uid: int = None,
            quota_names: list[str] = None,
    ):
        """
        Gets list of quotas of the payer user.

        :param collaboration_id: unique identifier of the collaboration.
        :param owner_uid: owner uid
        :param quota_names: list of quota names to get values for
        """
        if not collaboration_id and not owner_uid:
            raise ValueError("Either collaboration ID or owner UID are required")

        if collaboration_id and owner_uid:
            raise ValueError("You can only pass either collaboration ID or owner UID")

        return self._get(
            "GetCollaborationQuotas",
            params={
                "collaborationId": collaboration_id,
                "ownerUid": owner_uid,
                "quotaNames": quota_names,
            },
        )

    def GetCountries(self):
        """
        Returns associative list of country names, regex patterns for VAT (tax payer id) and postal code, phone prefix
        and its two letter codes. Each extern billing could have its own representation so Jbilling settle this.
        """
        return self._get("GetCountries")

    def GetCountryStates(self, country_code: str):
        """
        Returns lists of states (provinces) for the specified country. If conversion to commercial group doesn't
        requires to point client's state then this method returns empty list.
        """
        return self._get("GetCountryStates", params={"ccode": country_code})

    def GetEnvBillingHistoryByPeriod(
            self,
            start_time: datetime,
            end_time: datetime,
            period: PERIOD = "DAY",
            time_offset: int = None,
            group_nodes: bool = False,
    ):
        """
        Gets environment billing history.
        """
        return self._get(
            "GetEnvBillingHistoryByPeriod",
            params={
                "startTime": start_time,
                "endTime": end_time,
                "period": str(period),
                "timeOffset": time_offset,
                "groupNodes": group_nodes,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetExtendedAccountBillingHistoryByPeriod(
            self, start_time: datetime, end_time: datetime, target_app_id: str = None
    ):
        """
        Returns user’s billing history information for the specified period.

        :param start_time: start time of the period
        :param end_time: end time of the period
        :param target_app_id: target environment name
        """
        return self._get(
            "GetExtendedAccountBillingHistoryByPeriod",
            params={
                "starttime": start_time,
                "endtime": end_time,
                "targetAppid": target_app_id,
            },
        )

    def GetExternBillingSystemSession(self):
        """
        Session (some information) to interact with extern billing system as its client. It created automatically and
        garbaged. JBilling cache it and check. If you code fails try to recall this method.
        """
        return self._get("GetExternBillingSystemSession")

    def GetExternBillingSystems(self):
        """
        The platform can work with multiple external billing systems. But each user can only be bound with one.
        Possible values: NullExternBilling, PbasExternBilling, PbaExternBilling.
        """
        return self._get("GetExternBillingSystems")

    def GetExternalUserById(self, id: str):
        return self._get("GetExternalUserById", params={"id": id})

    def GetFundAccountHistory(self, start_time: datetime, end_time: datetime, uid: int):
        """
        Getting Fund history account by uid.
        """
        return self._get(
            "GetFundAccountHistory",
            params={"startTime": start_time, "endTime": end_time, "uid": uid},
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetQuotas(self, quota_names: list[str] = None):
        """
        Returns the values of the specified quotas for the user.

        :param quota_names: list of quota names to get values for
        """
        return self._get("GetQuotas", params={"quotasnames": quota_names})

    def GetSum(self, uid: int, start_time: datetime, end_time: datetime):
        """
        Gets account summary debit and balance for period.
        """
        return self._get(
            "GetSum",
            params={"uid": uid, "startTime": start_time, "endTime": end_time},
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetSumAccountBillingHistory(
            self, uid: int, start_time: datetime, end_time: datetime, bonus: int = None
    ):
        """
        Gets account billing history.
        """
        return self._get(
            "GetSumAccountBillingHistory",
            params={
                "uid": uid,
                "startTime": start_time,
                "endTime": end_time,
                "bonus": bonus,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetSuspendedAccounts(self):
        """
        Get suspended accounts.
        """
        return self._get("GetSuspendedAccounts")

    def RemoveQuota(self, uid: int, name: str):
        return self._get("RemoveQuota", params={"uid": uid, "name": name})

    def ResetTestAccounts(self):
        """
        Resets a list of testing accounts on the platform.
        """
        return self._get("ResetTestAccounts")

    def SetAccountStatus(self, uid: int, status: int):
        """
        Sets account status. If new status is inactive then active environments are remembered and non stopped
        environments are shutdown. At activation all active environments are woken up.
        """
        return self._get("SetAccountStatus", params={"uid": uid, "status": status})

    def SetBillingInfo(self, customer: dict):
        """
        Replaces existing account billing information with the provided value.

        :param customer: JSON object with the client's billing information.
        """
        return self._get("SetBillingInfo", params={"customer": customer})

    def SetFundNote(self, id: int, note: str):
        return self._get("SetFundNote", params={"id": id, "note": note})

    def SetGroup(
            self,
            uid: int,
            group_name: str,
            reset_balance: bool = False,
            reset_bonus: bool = False,
    ):
        """
        Sets group to account.
        """
        return self._get(
            "SetGroup",
            params={
                "uid": uid,
                "groupName": group_name,
                "resetBalance": reset_balance,
                "resetBonus": reset_bonus,
            },
        )

    def SetQuota(self, uid: int, name: str, value: str, reference_id: int = None):
        """
        Changes quota value for the target account.

        :param uid: unique ID of the target user account.
        :param name: a name of the quota to be adjusted.
        :param value: custom value for the quota.
        :param reference_id: reference ID of the quota.
        """
        return self._get(
            "SetQuota",
            params={
                "uid": uid,
                "name": name,
                "value": value,
                "referenceId": reference_id,
            },
        )

    def SetUserNote(self, uid: int, note: str):
        return self._get("SetUserNote", params={"uid": uid, "note": note})

    def SurchargeAccounts(self, start_date: date, end_date: date):
        """
        Surcharge accounts.
        """
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")

        return self._get(
            "SurchargeAccounts", params={"startDate": start_date, "endDate": end_date}
        )

    def SuspendUser(self, uid: int):
        """
        Suspend account. This status deny signin for user.
        """
        return self._get("SuspendUser", params={"uid": uid})

    def UnfundAccount(
            self, uid: int, amount: float, is_bonus: bool = False, note: str = None
    ):
        """
        Unfund account by uid.

        :param uid: unique identifier of the target user whose balance will be changed
        :param amount: positive value of money
        :param is_bonus: false change bonus balance otherwise change main balance
        :param note: note for transaction
        """
        return self._get(
            "UnfundAccount",
            params={"uid": uid, "amount": amount, "isBonus": is_bonus, "note": note},
        )

    def WithdrawAccounts(self, start_date: date, end_date: date):
        """
        Charge accounts for resource usage for the specified period.
        """
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")

        return self._get(
            "WithdrawAccounts", params={"startDate": start_date, "endDate": end_date}
        )


class _Pricing(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.Pricing
    """

    endpoint = "pricing"

    def AddPricing(
            self,
            pricing: dict,
            tariff_ids: str,
            tariff_grid_names: list[str] = None,
    ):
        return self._get(
            "AddPricing",
            params={
                "pricing": pricing,
                "tariffIds": tariff_ids,
                "tariffGridNames": tariff_grid_names,
            },
            delimiter=",",
        )

    def AddResource(self, resource: str):
        return self._get("AddResource", params={"resource": resource})

    def AddTariff(self, tariff: dict):
        return self._get(
            "AddTariff",
            params={"tariff": tariff},
            delimiter=",",
        )

    def AttachTariff(self, uniq_name: str, target_app_id: str):
        return self._get(
            "AttachTariff", params={"uniqName": uniq_name, "targetAppId": target_app_id}
        )

    def AttachTariffGrid(
            self,
            tariff_grid_name: str,
            id: str,
    ):
        return self._get(
            "AttachTariffGrid",
            params={
                "tariffGridName": tariff_grid_name,
                "id": id,
            },
        )

    def CheckHostGroupsAllowed(
            self,
            owner_uid: list[int] = None,
            hardware_node_groups: list[str] = None,
    ):
        """
        :param owner_uid: unique identifier of the target user.
        :param hardware_node_groups: a comma-separated list of the host groups to be checked.
        """
        return self._get(
            "CheckHostGroupsAllowed",
            params={"ownerUid": owner_uid, "hardwareNodeGroups": hardware_node_groups},
            delimiter=",",
        )

    def DeletePricing(self, id: str):
        return self._get("DeletePricing", params={"id": id})

    def DeleteTariff(self, id: str):
        return self._get("DeleteTariff", params={"id": id})

    def DetachTariff(
            self,
            uniq_name: str,
            target_app_id: str,
    ):
        return self._get(
            "DetachTariff", params={"uniqName": uniq_name, "targetAppId": target_app_id}
        )

    def DetachTariffGrid(
            self,
            tariff_grid_name: str,
            id: str,
    ):
        return self._get(
            "DetachTariffGrid", params={"tariffGridName": tariff_grid_name, "id": id}
        )

    def EditPricing(
            self,
            pricing: dict,
    ):
        return self._get(
            "EditPricing",
            params={"pricing": pricing},
            delimiter=",",
        )

    def EditResource(self, resource: str):
        return self._get("EditResource", params={"resource": resource})

    def EditTariff(self, tariff: dict):
        return self._get(
            "EditTariff",
            params={"tariff": tariff},
            delimiter=",",
        )

    def GetCurrencies(self, currency: list[str] = None):
        return self._get(
            "GetCurrencies",
            params={"currency": currency},
            delimiter=",",
        )

    def GetPlatformCurrency(self, reseller_id: list[int] = None):
        return self._get(
            "GetPlatformCurrency",
            params={"resellerId": reseller_id},
            delimiter=",",
        )

    def GetPricing(self, owner_uid: list[int] = None):
        return self._get(
            "GetPricing",
            params={"ownerUid": owner_uid},
            delimiter=",",
        )

    def GetPricingInner(self, reseller_id: list[int] = None):
        """
        :param reseller_id: unique ID of the target reseller platform
        """
        return self._get(
            "GetPricingInner",
            params={"resellerId": reseller_id},
            delimiter=",",
        )

    def GetResources(
            self,
            id: list[int] = None,
            name: list[str] = None,
    ):
        return self._get(
            "GetResources",
            params={"id": id, "name": name},
            delimiter=",",
        )

    def GetTariffsInner(
            self,
            pricing_id: list[str] = None,
            type: list[str] = None,
            reseller_id: list[int] = None,
    ):
        """
        :param pricing_id: pricing model unique ID.
        :param type: a semicolon-separated list of tariff types.
        :param reseller_id: unique ID of the target reseller platform.
        """
        return self._get(
            "GetTariffsInner",
            params={"priceId": pricing_id, "type": type, "resellerId": reseller_id},
            delimiter=",",
        )

    def GetUniqueResourceNames(self):
        return self._get("GetUniqueResourceNames", params={})

    def SetTariffs(
            self,
            pricing_id: str,
            tariff_ids: str,
            tariff_grid_names: list[str] = None,
    ):
        return self._get(
            "SetTariffs",
            params={
                "pricingId": pricing_id,
                "tariffIds": tariff_ids,
                "tariffGridNames": tariff_grid_names,
            },
            delimiter=",",
        )

    def ValidateEnvironment(
            self,
            hardware_node_group: str,
            owner_uid: list[int] = None,
    ):
        return self._get(
            "ValidateEnvironment",
            params={
                "hardwareNodeGroup": hardware_node_group,
                "ownerUid": owner_uid,
            },
            delimiter=",",
        )

    def ValidateNode(
            self,
            uid: int,
            hardware_node_group: str,
            node_type: str,
            fixed_cloud_lets: int,
            flexible_cloud_lets: int,
    ):
        return self._get(
            "ValidateNode",
            params={
                "uid": uid,
                "hardwareNodeGroup": hardware_node_group,
                "nodeType": node_type,
                "fixedCloudlets": fixed_cloud_lets,
                "flexibleCloudlets": flexible_cloud_lets,
            },
        )

    def ValidateNodeInner(
            self,
            uid: int,
            hardware_node_group: str,
            node_type: str,
            fixed_cloud_lets: int,
            flexible_cloud_lets: int,
    ):
        return self._get(
            "ValidateNodeInner",
            params={
                "uid": uid,
                "hardwareNodeGroup": hardware_node_group,
                "nodeType": node_type,
                "fixedCloudlets": fixed_cloud_lets,
                "flexibleCloudlets": flexible_cloud_lets,
            },
        )


class _Reseller(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.Reseller
    """

    def AddReseller(
            self,
            reseller: str,
            platform: str,
            regions: str,
            settings: list[str] = None,
    ):
        """
        :param reseller: JSON representation of the reseller object.
        :param platform: JSON representation of the reseller platform object.
        :param regions: JSON representation of the reseller regions object.
        :param settings: JSON representation of the reseller setting object.
        """
        return self._get(
            "AddReseller",
            params={
                "reseller": reseller,
                "platform": platform,
                "regions": regions,
                "settings": settings,
            },
            delimiter=",",
        )

    def EditReseller(
            self,
            reseller: str,
            platform: str,
            regions: list[str] = None,
    ):
        return self._get(
            "EditReseller",
            params={
                "reseller": reseller,
                "platform": platform,
                "regions": regions,
            },
            delimiter=",",
        )

    def GetAllResellers(self):
        return self._get("GetAllResellers", params={})

    def GetResellerByAppid(self, target_app_id: str):
        return self._get("GetResellerByAppid", params={"targetAppid": target_app_id})

    def GetResellerById(self, id: int):
        return self._get("GetResellerById", params={"id": id})

    def GetResellerByOwnerUid(self, uid: int):
        return self._get("GetResellerByOwnerUid", params={"uid": uid})

    def GetResellerByUid(self, uid: int):
        return self._get("GetResellerByUid", params={"uid": uid})

    def RemoveReseller(self, id: int):
        return self._get("RemoveReseller", params={"id": id})

    def SetResellerStatus(self, id: int, status: str):
        return self._get("SetResellerStatus", params={"id": id, "status": status})


class _ServicePlan(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.ServicePlan
    """

    _endpoint2 = "servicePlan"

    def CreateLevelAutoPay(
            self,
            min_balance: int,
            expires: str,
            service_plan_id: int,
            payment_method_id: str,
            min_period: int,
    ):
        """
        :param min_balance: the value used in the "account.balance < minBalance" expression.
        :param expires: date [and time] (in the UTC ISO 8601 format) when the auto-pay becomes unavailable.
        :param service_plan_id: service plan ID to be paid (for example, $200 one-time fee)
        :param payment_method_id: payment method ID to be used (see the GetPayMethodList method)
        :param min_period: minimal delay (in seconds) between two consecutive auto-pays. 0 means no limit.
        """
        return self._get(
            "CreateLevelAutoPay",
            params={
                "minBalance": min_balance,
                "expires": expires,
                "servicePlanId": service_plan_id,
                "paymentMethodId": payment_method_id,
                "minPeriod": min_period,
            },
        )

    def CreateRegularAutoPay(
            self,
            cron_expression: str,
            expires: str,
            time_zone: str,
            service_plan_id: int,
            payment_method_id: str,
    ):
        """

        :param cron_expression: Year value is optional. '*' means every possible value.
        :param expires: date [and time] (in the UTC ISO 8601 format) when the auto-pay becomes unavailable.
        :param time_zone: time zone for the cron expression. For example, GMT+4.
        :param service_plan_id: service plan ID to be paid (for example, $200 one-time fee)
        :param payment_method_id: payment method ID to be used (see the GetPayMethodList method)
        """
        return self._get(
            "CreateRegularAutoPay",
            params={
                "cronExpression": cron_expression,
                "expires": expires,
                "timeZone": time_zone,
                "servicePlanId": service_plan_id,
                "paymentMethodId": payment_method_id,
            },
        )

    def CreateServicePlan(
            self,
            name: str,
            description: str,
            service_plan_type: str,
            extern_plan_id: str,
    ):
        """
        :param name: unique name of service plan
        :param description: detailed comment about the service plan
        :param service_plan_type: "one-time" or "regular"
        """
        return self._get(
            "CreateServicePlan",
            params={
                "name": name,
                "description": description,
                "servicePlanType": service_plan_type,
                "externPlanId": extern_plan_id,
            },
        )

    def DeleteAutoPay(self, auto_pay_id: int):
        """
        :param auto_pay_id: auto pay id. It can be get with ServicePlanService#GetAutoPays method
        """
        return self._get("DeleteAutoPay", params={"autoPayId": auto_pay_id})

    def DeleteServicePlan(self, service_plan_id: int):
        """
        :param service_plan_id: id of sevice plan to be deleted
        """
        return self._get("DeleteServicePlan", params={"servicePlanId": service_plan_id})

    def EnableServicePlan(self, service_plan_id: int, enabled: int):
        """
        :param service_plan_id: id of the specified service plan
        :param enabled: 1 enabled and 0 = disabled
        """
        return self._get(
            "EnableServicePlan",
            params={"servicePlanId": service_plan_id, "enabled": enabled},
        )

    def ExtendedCreateServicePlan(
            self,
            label: str,
            external_plan_id: str,
            description: str,
            enabled: bool,
            type: str,
            by_default: bool,
            price: str,
    ):
        """
        :param label: name or short description of the service plan
        :param external_plan_id: service plan ID in the external billing system
        :param description: detailed description of the service plan
        :param enabled: enables (1) or disables (0) the service plan
        :param type: service plan type in the external billing system (usually, one-time fee)
        :param by_default: proposes the current service plan to users during the recharge operations by default (1) or not (0). Only one service plan can be set as default.
        :param price: the sum to be refilled on the account balance by this service plan
        """
        return self._get(
            "ExtendedCreateServicePlan",
            params={
                "label": label,
                "externalPlanId": external_plan_id,
                "description": description,
                "enabled": enabled,
                "type": type,
                "byDefault": by_default,
                "price": price,
            },
        )

    def ExtendedGetServicePlans(self):
        return self._get("ExtendedGetServicePlans", params={})

    def ExtendedServicePlanUpdate(
            self,
            id: int,
            label: str,
            external_plan_id: str,
            description: str,
            enabled: bool,
            type: str,
            by_default: bool,
            price: str,
    ):
        """
        :param id: internal service plan ID in the PaaS admin panel
        :param label: name or short description of the service plan
        :param external_plan_id: service plan ID in the external billing system
        :param description: detailed description of the service plan
        :param enabled: enables (1) or disables (0) the service plan
        :param type: service plan type in the external billing system (usually, one-time fee)
        :param by_default: proposes the current service plan to users during the recharge operations by default (1) or not (0). Only one service plan can be set as default.
        :param price: the sum to be refilled on the account balance by this service plan
        """
        return self._get(
            "ExtendedServicePlanUpdate",
            params={
                "id": id,
                "label": label,
                "externalPlanId": external_plan_id,
                "description": description,
                "enabled": enabled,
                "type": type,
                "byDefault": by_default,
                "price": price,
            },
        )

    def GetAutoPayHistory(self, auto_pay_id: int):
        """
        :param auto_pay_id: specified auto pay id
        """
        return self._get("GetAutoPayHistory", params={"autoPayId": auto_pay_id})

    def GetAutoPays(self):
        return self._get("GetAutoPays", params={})

    def GetBoughtServicePlans(self):
        return self._get("GetBoughtServicePlans", params={})

    def GetCurrency(self):
        return self._get("GetCurrency", params={})

    def GetFinalCost(self, service_plan_id: int):
        """
        :param service_plan_id: specified service plan id
        """
        return self._get("GetFinalCost", params={"servicePlanId": service_plan_id})

    def GetPayMethodList(self):
        return self._get("GetPayMethodList", params={})

    def GetPaymentNews(self):
        return self._get("GetPaymentNews", params={})

    def GetServicePlan(self, service_plan_id: int):
        """
        :param service_plan_id: id of service plan to be returned
        """
        return self._get("GetServicePlan", params={"servicePlanId": service_plan_id})

    def GetServicePlanByType(self, plan_type: list[int] = None):
        return self._get("GetServicePlanByType", params={"planType": plan_type})

    def PaymentNewsRead(self, id: int):
        """
        :param id: comma separated ids of payments
        """
        return self._get("PaymentNewsRead", params={"id": id})

    def SetExternPlanId(
            self,
            service_plan_id: int,
            external_plan_id: int,
    ):
        """
        :param service_plan_id: JBilling service plan id
        """
        return self._get(
            "SetExternPlanId",
            params={
                "servicePlanId": service_plan_id,
                "externalPlanId": external_plan_id,
            },
        )

    def UpdateServicePlan(
            self,
            service_plan_id: int,
            name: str,
            description: str,
            extern_service_plan_id: str,
    ):
        """
        :param service_plan_id: id of service plan to be changed
        :param name: new name (unique among the others)
        :param description: detailed description
        """
        return self._get(
            "UpdateServicePlan",
            params={
                "servicePlanId": service_plan_id,
                "name": name,
                "description": description,
                "externServicePlanId": extern_service_plan_id,
            },
        )

