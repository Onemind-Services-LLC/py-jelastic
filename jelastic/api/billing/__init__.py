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
    def GroupQuota(self) -> "_GroupQuota":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.GroupQuota

        Ref: https://docs.jelastic.com/api/#!/api/billing.GroupQuota
        """
        return _GroupQuota(session=self._session, token=self._token, debug=self._debug)

    @property
    def Integration(self) -> "_Integration":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Integration

        Ref: https://docs.jelastic.com/api/#!/api/billing.Integration
        """
        return _Integration(session=self._session, token=self._token, debug=self._debug)

    @property
    def PayMethod(self) -> "_PayMethod":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.PayMethod

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.PayMethod
        """
        return _PayMethod(session=self._session, token=self._token, debug=self._debug)

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

    @property
    def Order(self) -> "_Order":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Order

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.Order
        """
        return _Order(session=self._session, token=self._token, debug=self._debug)

    @property
    def Invoice(self) -> "_Invoice":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Invoice

        Ref: https://docs.jelastic.com/api/#!/api/billing.Invoice
        """
        return _Invoice(session=self._session, token=self._token, debug=self._debug)

    @property
    def System(self) -> "_System":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.System

        Ref: https://docs.jelastic.com/api/#!/api/billing.System
        """
        return _System(session=self._session, token=self._token, debug=self._debug)

    @property
    def Utils(self) -> "_Utils":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Utils

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.Utils
        """
        return _Utils(session=self._session, token=self._token, debug=self._debug)


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


class _Invoice(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.Invoice
    """

    _endpoint2 = "invoice"

    def Event(
        self,
        extern_id: str,
        event_type: str,
    ):
        """
        :param extern_id: unique identifier of the document that was returned by external billing system
        :param event_type: invoice event type (EXPIRED or PAID)
        """
        return self._get(
            "Event", params={"externId": extern_id, "eventType": event_type}
        )

    def GetExternalInvoices(
        self,
        limit: list[int] = None,
        owner_uid: list[int] = None,
    ):
        """
        :param limit: the maximum number of invoices returned in the response.
        :param owner_uid: unique identifier of the invoice owner.
        """
        return self._get(
            "ExternalInvoices",
            params={
                "limit": limit,
                "ownerUid": owner_uid,
            },
            delimiter=",",
        )

    def GetInvoices(
        self,
        id: list[int] = None,
        unique_name: list[str] = None,
        type: list[str] = None,
        status: list[str] = None,
        subscription_id: list[int] = None,
        subscription_status: list[str] = None,
        order_fields: list[str] = None,
        order_direction: list[str] = None,
        start_row: list[int] = None,
        result_count: list[int] = None,
        expand_fields: list[str] = None,
    ):
        """
        :param id: unique identifier of the target invoice.
        :param unique_name: a name of the target invoice that is provided to the end-user.
        :param type: invoice type (POST_PAYMENT or SUBSCRIPTION).
        :param status: a semicolon-separated list of invoice statuses.
        :param subscription_id: unique identifier of the target subscription.
        :param subscription_status: a semicolon-separated list of the subscription statuses.
        :param order_fields: sorts results by the specified field.
        :param order_direction: sorts results in the ascending (ASC) or descending (DESC) order.
        :param start_row: returns information starting from the specified row in the response (starts with 0, by default).
        :param result_count: returns the specified number of rows from the response (0 – unlimited – by default).
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group
        """
        return self._get(
            "GetInvoices",
            params={
                "id": id,
                "uniqueName": unique_name,
                "type": type,
                "status": status,
                "subscriptionId": subscription_id,
                "subscriptionStatus": subscription_status,
                "orderFields": order_fields,
                "orderDirection": order_direction,
                "startRow": start_row,
                "resultCount": result_count,
                "expandFields": expand_fields,
            },
            delimiter=",",
        )

    def MakeInvoice(
        self,
        uid: str,
        skip_pay: list[bool] = None,
    ):
        """
        :param uid: a comma-separated list of target POST-paid users' unique identifiers (all, if not set).
        :param skip_pay: a flag that disables (true) or enables (false) auto-pay with a default payment method
        """
        return self._get(
            "MakeInvoice",
            params={
                "uid": uid,
                "skipPay": skip_pay,
            },
            delimiter=",",
        )

    def MarkAsPaid(
        self,
        id: list[int] = None,
        ebs_invoice_id: list[str] = None,
    ):
        """
        :param id: unique identifier of the target invoice.
        :param ebs_invoice_id: unique identifier of the target invoice in the external billing system.
        """
        return self._get(
            "MarkAsPaid",
            params={
                "id": id,
                "ebsInvoiceId": ebs_invoice_id,
            },
            delimiter=",",
        )

    def MarkAsVoid(
        self,
        id: list[int] = None,
        ebs_invoice_id: list[str] = None,
    ):
        """
        :param id: unique identifier of the target invoice.
        :param ebs_invoice_id: unique identifier of the target invoice in the external billing system.
        """
        return self._get(
            "MarkAsVoid",
            params={
                "id": id,
                "ebsInvoiceId": ebs_invoice_id,
            },
            delimiter=",",
        )

    def Pay(
        self,
        id: int,
        payment_method_id: list[str] = None,
        payment_method_type: list[str] = None,
    ):
        """
        :param id: unique identifier of the target invoice.
        :param payment_method_id: unique identifier of the payment method type.
        :param payment_method_type: type of the payment method.
        """
        return self._get(
            "Pay",
            params={
                "id": id,
                "paymentMethodId": payment_method_id,
                "paymentMethodType": payment_method_type,
            },
            delimiter=",",
        )

    def SearchInvoices(
        self,
        search: str,
        expand_fields: list[str] = None,
        reseller_id: list[int] = None,
    ):
        """
        :param search: a search string in the JSON format. For example: {"startDate":"2023-01-23 00:00:00","endDate":"2023-01-30 23:59:59","orderField":"id","orderDirection":"DESC","startRow":0,"resultCount":10}
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "SearchInvoices",
            params={
                "search": search,
                "expandFields": expand_fields,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )


class _GroupQuota(Billing):
    """
    Ref: https://docs.jelastic.com/api/#!/api/billing.GroupQuota
    """

    _endpoint2 = "getQuota"

    def AddGroup(
        self,
        type: str,
        name: str,
        description: list[str] = None,
        source_group_name: list[str] = None,
        domain: list[str] = None,
        conversion_group: list[str] = None,
    ):
        """
        :param type: quota group type.
        :param name: unique name of the target quota group.
        :param description: custom description for the quota group.
        :param source_group_name: name of the quota group to be used as a source for the new group.
        :param domain: domain name of the target platform.
        :param conversion_group: name of the quota group to be used after conversion.
        """
        return self._get(
            "AddGroup",
            params={
                "type": type,
                "name": name,
                "description": description,
                "sourceGroupName": source_group_name,
                "domain": domain,
                "conversionGroup": conversion_group,
            },
            delimiter=",",
        )

    def AddQuota(
        self,
        name: str,
        description: list[str] = None,
        reference_id: list[str] = None,
        default_value: list[int] = None,
        assign_to_group: list[bool] = None,
    ):
        """
        :param name: a name of the quota to be created.
        :param description: custom quota description.
        :param reference_id: reference ID of the quota.
        :param default_value: quota's default value.
        :param assign_to_group: a flag that indicates if this quota could (true) or not (false) be assigned to groups.
        """
        return self._get(
            "AddQuota",
            params={
                "name": name,
                "description": description,
                "referenceId": reference_id,
                "defaultValue": default_value,
                "assignToGroup": assign_to_group,
            },
            delimiter=",",
        )

    def DeleteGroup(self, name: str):
        return self._get("DeleteGroup", params={"name": name})

    def EditGroup(
        self,
        name: str,
        new_name: list[str] = None,
        description: list[str] = None,
        conversion_group: list[str] = None,
    ):
        """
        :param name: unique name of the target quota group.
        :param new_name: a new name for the quota group.
        :param description: custom description for the quota group.
        :param conversion_group: name of the quota group to be used after conversion.
        """
        return self._get(
            "EditGroup",
            params={
                "name": name,
                "newName": new_name,
                "description": description,
                "conversionGroup": conversion_group,
            },
            delimiter=",",
        )

    def EditQuota(
        self,
        name: str,
        reference_id: list[str] = None,
        new_reference_id: list[str] = None,
        description: list[str] = None,
    ):
        return self._get(
            "EditQuota",
            params={
                "name": name,
                "referenceId": reference_id,
                "newReferenceId": new_reference_id,
                "description": description,
            },
            delimiter=",",
        )

    def GetGroupQuotas(self, name: str, quotas_names: list[str] = None):
        return self._get(
            "GetGroupQuotas",
            params={
                "name": name,
                "quotasnames": quotas_names,
            },
            delimiter=",",
        )

    def GetGroups(self):
        return self._get("GetGroups", params={})

    def GetPricingModels(self, group_name: str):
        return self._get("GetPricingModels", params={"groupName": group_name})

    def GetQuotas(self):
        return self._get("GetQuotas", params={})

    def IsDomainBound(self, checksum: list[str] = None):
        return self._get(
            "IsDomainBound",
            params={"checksum": checksum},
            delimiter=",",
        )

    def RemoveGroupQuota(self, group_name: str, quota_name: str):
        return self._get(
            "RemoveGroupQuota",
            params={
                "groupName": group_name,
                "quotaName": quota_name,
            },
        )

    def RemoveQuota(
        self,
        name: str,
        force: list[bool] = None,
        reference_id: list[str] = None,
    ):
        """
        :param name: a name of the quota to be removed.
        :param force: proceeds (true) or interrupts (false) the operation in case of errors.
        :param reference_id: reference ID of the quota.
        """
        return self._get(
            "RemoveQuota",
            params={
                "name": name,
                "force": force,
                "referenceId": reference_id,
            },
            delimiter=",",
        )

    def SetCollaborationGroup(
        self,
        name: str,
    ):
        return self._get("SetCollaborationGroup", params={"name": name})

    def SetDefaultGroup(self, name: str):
        return self._get("DefaultGroup", params={"name": name})

    def SetGroupQuota(
        self,
        group_name: str,
        quota_name: str,
        value: int,
        reference_id: list[str] = None,
    ):
        """
        :param group_name: unique name of the target group.
        :param quota_name: a name of the quota to be adjusted.
        :param value: custom value for the quota.
        :param reference_id: reference ID of the quota.
        """
        return self._get(
            "SetGroupQuota",
            params={
                "groupName": group_name,
                "quotaName": quota_name,
                "value": value,
                "referenceId": reference_id,
            },
            delimiter=",",
        )

    def SetPricingModels(
        self,
        group_name: str,
        data: str,
    ):
        return self._get(
            "SetPricingModel", params={"groupName": group_name, "data": data}
        )

    def SetSignupGroup(self, name: str):
        return self._get("SetSignupGroup", params={"name": name})

    def SetWinDomain(
        self,
        group_name: str,
        win_domain_id: int,
    ):
        return self._get(
            "SetWinDomain",
            params={"groupName": group_name, "winDomainId": win_domain_id},
        )

    def UnassignHdNodeGroup(
        self,
        hardware_node_group: str,
        checksum: str,
    ):
        return self._get(
            "UnassignHdNodeGroup",
            params={
                "hardwareNodeGroup": hardware_node_group,
                "checksum": checksum,
            },
        )


class _Integration(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Integration
    """

    _endpoint = "integration"

    def GetInvoiceUrl(self, invoice_id: int):
        """
        :param invoice_id: unique identifier of the target invoice in the internal billing system.
        """
        return self._get("GetInvoiceUrl", params={"invoiceId": invoice_id})

    def GetSSOUrl(self, path: list[str] = None):
        """
        :param path: destination path within the integrated system.
        """
        return self._get("GetSSOUrl", params={"path": path})


class _PayMethod(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.PayMethod
    """

    _endpoint2 = "payMethod"

    def EnablePayMethod(
        self,
        pay_method_id: str,
        enable: int,
    ):
        """
        :param pay_method_id: payment method ID to be set as default one (see the GetPayMethodList method)
        :param enable: enables (1) or disables (0) the provided payment method
        """
        return self._get(
            "EnablePayMethod", params={"payMethodId": pay_method_id, "enable": enable}
        )

    def GetDefaultPayMethod(self):
        return self._get("GetDefaultPayMethod", params={})

    def GetPublicToken(self):
        return self._get("GetPublicToken", params={})

    def GetValidPayTypes(self):
        return self._get("GetValidPayTypes", params={})

    def RegisterBankCard(
        self,
        first_name: str,
        last_name: str,
        card_number: str,
        card_code: str,
        expire_month: int,
        expire_year: int,
        service_plan_id: int,
    ):
        """
        :param first_name: exactly as on the card
        :param last_name: exactly as on the card
        :param card_number: very big number
        :param card_code: 4 digits.
        :param expire_month: exactly as on the card. from 1 to 12
        :param expire_year: year in format yyyy
        :param service_plan_id: service plan id to buy for check card or 0 then min test pay is used.
        """
        return self._get(
            "RegisterBankCard",
            params={
                "firstName": first_name,
                "lastName": last_name,
                "cardNumber": card_number,
                "cardCode": card_code,
                "expireMonth": expire_month,
                "expireYear": expire_year,
                "servicePlanId": service_plan_id,
            },
        )

    def RegisterPayMethodAndPay(
        self,
        pay_method_type: str,
        service_plan_id: int,
        auto_service_plan_id: list[int] = None,
        auto_refill_min_balance: list[int] = None,
        auto_refill_period: list[str] = None,
    ):
        """
        :param pay_method_type: take value from item of GetValidPayTypes response
        :param auto_service_plan_id: service plan id for auto refill, should 0 or -1 if none
        :param auto_refill_min_balance: min balance threshold when by new service plan
        :param auto_refill_period: accepted string literals "WEEK" and "MONTH"
        """
        return self._get(
            "RegisterPayMethodAndPay",
            params={
                "payMethodType": pay_method_type,
                "servicePlanId": service_plan_id,
                "autoServicePlanId": auto_service_plan_id,
                "autoRefillMinBalance": auto_refill_min_balance,
                "autoRefillPeriod": auto_refill_period,
            },
            delimiter=",",
        )

    def SetDefaultPayMethod(self, pay_method_id: str):
        """
        :param pay_method_id: payment method ID to be set as default one (see the GetPayMethodList method)
        """
        return self._get("SetDefaultPayMethod", params={"payMethodId": pay_method_id})

    def SetupIntent(
        self,
        payment_method_type: list[str] = None,
    ):
        """
        :param payment_method_type: list of payment method keys (optional), for example: card, bancontact, ...
        """
        return self._get(
            "SetupIntent",
            params={"paymentMethodType": payment_method_type},
            delimiter=",",
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


class _Order(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.Order
    """

    _endpoint2 = "order"

    def AddStats(
        self,
        resource_name: str,
        uid: int,
        value: int,
        start_date: list[str] = None,
        end_date: list[str] = None,
        env_name: list[str] = None,
        node_id: list[int] = None,
        note: list[str] = None,
        value_group: list[str] = None,
    ):
        return self._get(
            "AddStats",
            params={
                "resourceName": resource_name,
                "uid": uid,
                "value": value,
                "startDate": start_date,
                "endDate": end_date,
                "envName": env_name,
                "nodeId": node_id,
                "note": note,
                "valueGroup": value_group,
            },
            delimiter=",",
        )

    def EnvResources(
        self,
        start_date: date,
        end_date: date,
    ):
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")
        return self._get(
            "EnvResources",
            params={
                "startDate": start_date,
                "endDate": end_date,
            },
        )

    def EnvsResources(
        self,
        start_date: date,
        end_date: date,
        target_app_id: str,
        checksum: str,
    ):
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")
        return self._get(
            "EnvsResources",
            params={
                "startDate": start_date,
                "endDate": end_date,
                "targetAppId": target_app_id,
                "checksum": checksum,
            },
        )

    def EnvsResourcesByAccount(
        self,
        start_date: date,
        end_date: date,
        uid: int,
        checksum: str,
    ):
        """
        :param checksum: required but not used
        """

        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")
        return self._get(
            "EnvsResourcesByAccount",
            params={
                "startDate": start_date,
                "endDate": end_date,
                "uid": uid,
                "checksum": checksum,
            },
        )

    def GetOptions(
        self,
        target_env_name: str,
        node_group: str,
    ):
        """
        :param target_env_name: env which holds nodeGroup
        :param node_group: Node Group
        """
        return self._get(
            "GetOptions",
            params={
                "targetEnvName": target_env_name,
                "nodeGroup": node_group,
            },
        )

    def SetOptions(
        self,
        target_env_name: str,
        node_group: str,
        options: str,
        node_id: list[int] = None,
    ):
        """
        :param target_env_name: target environment name with the required node group (layer).
        :param node_group: unique identifier of the target node group (layer), e.g. "cp" for the default application server layer.
        :param options: JSON object with the required billing options.
        :param node_id: unique identifier of the node that will be used to identify the target node group (overrides the nodeGroup parameter if both are specified).
        """
        return self._get(
            "SetOptions",
            params={
                "targetEnvName": target_env_name,
                "nodeGroup": node_group,
                "options": options,
                "nodeId": node_id,
            },
            delimiter=",",
        )


class _Utils(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.Utils
    """

    _endpoint2 = "utils"

    def ClearBillingHistory(
        self,
        env_name: str,
        uid: int,
        start_date: str,
        end_date: str,
        checksum: str,
    ):
        return self._get(
            "ClearBillingHistory",
            params={
                "envName": env_name,
                "uid": uid,
                "startDate": start_date,
                "endDate": end_date,
                "checksum": checksum,
            },
        )

    def ClearMonthTraffic(
        self,
        uid: int,
        month_start: str,
        checksum: str,
    ):
        return self._get(
            "ClearMonthTraffic",
            params={
                "uid": uid,
                "monthStart": month_start,
                "checksum": checksum,
            },
        )

    def GetUidUsageByPeriod(
        self,
        uid: int,
        start_date: str,
        end_date: str,
        checksum: str,
    ):
        return self._get(
            "GetUidUsageByPeriod",
            params={
                "uid": uid,
                "startDate": start_date,
                "endDate": end_date,
                "checksum": checksum,
            },
        )

    def SetAccountDate(
        self,
        uid: int,
        date_type: str,
        date_value: str,
        checksum: str,
    ):
        return self._get(
            "SetAccountDate",
            params={
                "uid": uid,
                "dateType": date_type,
                "dateValue": date_value,
                "checksum": checksum,
            },
        )

    def SetBillingHistoryDate(
        self,
        uid: int,
        env_name: str,
        start_date_from: str,
        start_date_to: str,
        date_type: str,
        date_value: str,
        checksum: str,
    ):
        return self._get(
            "SetBillingHistoryDate",
            params={
                "uid": uid,
                "envName": env_name,
                "startDateFrom": start_date_from,
                "startDateTo": start_date_to,
                "dateType": date_type,
                "dateValue": date_value,
                "checksum": checksum,
            },
        )

    def SetMonthTraffic(
        self,
        uid: int,
        month_start: str,
        external_traffic: int,
        checksum: str,
    ):
        return self._get(
            "SetMonthTraffic",
            params={
                "uid": uid,
                "monthStart": month_start,
                "externalTraffic": external_traffic,
                "checksum": checksum,
            },
        )


class _System(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.System
    """

    _endpoint2 = "system"

    def CleanCheckRequestCache(
        self,
        uid: list[int] = None,
        local_only: list[bool] = None,
    ):
        return self._get(
            "CleanCheckRequestCache",
            params={
                "uid": uid,
                "localOnly": local_only,
            },
            delimiter=",",
        )

    def Event(
        self,
        topic: str,
        message: str,
        publish_local: list[bool] = None,
    ):
        return self._get(
            "Event",
            params={
                "topic": topic,
                "message": message,
                "publishLocal": publish_local,
            },
            delimiter=",",
        )

    def GetAPIDescriptions(
        self,
        is_public_only: list[bool] = None,
        is_token: list[bool] = None,
    ):
        return self._get(
            "GetAPIDescriptions",
            params={
                "isPublicOnly": is_public_only,
                "isToken": is_token,
            },
            delimiter=",",
        )

    def GetAutoPercent(self):
        return self._get("GetAutoPercent", params={})

    def GetCacheStats(self):
        return self._get("GetCacheStats", params={})

    def GetCacheStatus(self):
        return self._get("GetCacheStatus", params={})

    def GetInstanceCacheStatus(self):
        return self._get("GetInstanceCacheStatus", params={})

    def GetStatus(self, checksum: int):
        return self._get("GetStatus", params={"checksum": checksum})

    def GetVersion(self):
        return self._get("GetVersion", params={})

    def RefreshEmailTemplates(self):
        return self._get("RefreshEmailTemplates", params={})

    def RefreshUser(self, language: list[str] = None):
        return self._get(
            "RefreshUser",
            params={"language": language},
            delimiter=",",
        )

    def ReloadConfiguration(
        self,
        reseller_id: list[int] = None,
        changed_placeholders: list[str] = None,
    ):
        return self._get(
            "ReloadConfiguration",
            params={
                "resellerId": reseller_id,
                "changedPlaceholders": changed_placeholders,
            },
            delimiter=",",
        )

    def SendEmail(
        self,
        template: str,
        email: list[str] = None,
        language: list[str] = None,
        timeout: list[int] = None,
    ):
        return self._get(
            "SendEmail",
            params={
                "template": template,
                "email": email,
                "language": language,
                "timeout": timeout,
            },
            delimiter=",",
        )

    def Validate(self):
        return self._get("Validate", params={})

    def ValidateAll(self):
        return self._get("ValidateAll", params={})
