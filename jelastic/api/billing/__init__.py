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
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
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
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Account

        Ref: https://docs.jelastic.com/api/#!/api/billing.Account
        """
        return _Account(
            session=self._session, token=self._token, debug=self._debug, ruk=self._ruk
        )

    @property
    def GroupQuota(self) -> "_GroupQuota":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.GroupQuota

        Ref: https://docs.jelastic.com/api/#!/api/billing.GroupQuota
        """
        return _GroupQuota(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def Integration(self) -> "_Integration":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Integration

        Ref: https://docs.jelastic.com/api/#!/api/billing.Integration
        """
        return _Integration(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def PayMethod(self) -> "_PayMethod":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.PayMethod

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.PayMethod
        """
        return _PayMethod(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def Pricing(self) -> "_Pricing":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Pricing

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.Pricing
        """
        return _Pricing(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def Reseller(self) -> "_Reseller":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Reseller

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.Reseller
        """
        return _Reseller(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def ServicePlan(self) -> "_ServicePlan":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.ServicePlan

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.ServicePlan
        """
        return _ServicePlan(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def Order(self) -> "_Order":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Order

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.Order
        """
        return _Order(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def Invoice(self) -> "_Invoice":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Invoice

        Ref: https://docs.jelastic.com/api/#!/api/billing.Invoice
        """
        return _Invoice(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def System(self) -> "_System":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.System

        Ref: https://docs.jelastic.com/api/#!/api/billing.System
        """
        return _System(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def Utils(self) -> "_Utils":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Utils

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.Utils
        """
        return _Utils(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )

    @property
    def Subscription(self) -> "_Subscription":
        """
        The methods of this service provide billing information about a user account (such as UID, balance, billing history,
        quotas, etc.) and allow managing it.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.billing.Subscription

        Ref: https://docs.jelastic.com/api/private/#!/api/billing.Subscription
        """
        return _Subscription(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )


class _Account(Billing):
    """
    The methods of this service provide billing information about a user account (such as UID, balance, billing history,
    quotas, etc.) and allow managing it.

    Ref: https://docs.jelastic.com/api/#!/api/billing.Account
    """

    _endpoint2 = "account"

    def AddAccount(self, uid: int, ruk: str = None):
        """
        Create new trial account in JBilling system.
        """
        return self._get("AddAccount", params={"uid": uid, "ruk": ruk})

    def ChangeEmail(self, login: str, email: str, ruk: str = None):
        """
        Changes user’s email address.
        """
        return self._get(
            "ChangeEmail", params={"login": login, "email": email, "ruk": ruk}
        )

    def ChangeGroup(
        self,
        group_name: str,
        uids: list[str] = None,
        send_email: bool = False,
        template: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def ChangePhoneNumber(self, login: str, number: str, ruk: str = None):
        """
        Changes user’s phone number.
        """
        return self._get(
            "ChangePhoneNumber", params={"login": login, "number": number, "ruk": ruk}
        )

    def ChargeAccountByUid(
        self,
        uid: int,
        amount: float,
        description: str,
        env_name: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def ConvertToCommercial(self, customer: dict, ruk: str = None):
        """
        Make trial account commercial one. This method register Jbilling account into extern billing system. Commercial
        client can create auto payment, just pay service plans.

        externBillingSystemId need if hoster has multiple billing systems. And its user belongs to one specific system.
        This is one place where it's needed to point it obviously.
        """
        customer = json.dumps(customer)

        return self._get(
            "ConvertToCommercial", params={"customer": customer, "ruk": ruk}
        )

    def ConvertToCommercialAndPay(
        self,
        customer: dict,
        pay_method_type: str,
        service_plan_id: int,
        auto_service_plan_id: int = None,
        auto_refill_main_balance: int = None,
        auto_refill_period: str = None,
        ruk: str = None,
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
                "ruk": ruk,
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
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def EnableUser(self, uid: int, ruk: str = None):
        """
        Enables user account.
        """
        return self._get("EnableUser", params={"uid": uid, "ruk": ruk})

    def ExportAccountBillingHistoryByPeriod(
        self,
        start_time: datetime,
        end_time: datetime,
        period: PERIOD = "DAY",
        time_offset: int = None,
        group_nodes: bool = False,
        target_app_id: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def ExportEnvBillingHistoryByPeriod(
        self,
        start_time: datetime,
        end_time: datetime,
        time_offset: int,
        period: PERIOD = "DAY",
        group_nodes: bool = False,
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def FundAccount(
        self,
        uid: int,
        amount: float,
        is_bonus: bool = False,
        note: str = None,
        ruk: str = None,
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
            params={
                "uid": uid,
                "amount": amount,
                "isBonus": is_bonus,
                "note": note,
                "ruk": ruk,
            },
        )

    def FundAndActivateAccount(
        self, uid: int, amount: float, note: str = None, ruk: str = None
    ):
        """
        Fund account by uid, activate it and set billing group.

        :param uid: unique identifier of the target user whose balance will be changed
        :param amount: positive value of money
        :param note: note for transaction
        """
        return self._get(
            "FundAndActivateAccount",
            params={"uid": uid, "amount": amount, "note": note, "ruk": ruk},
        )

    def GetAccount(self, ruk: str = None):
        """
        Returns account information based on the user session.
        """
        return self._get("GetAccount", params={"ruk": ruk})

    def GetAccountBillingByEngineTypeAndPeriod(
        self,
        start_time: datetime,
        end_time: datetime,
        owner_uid: str = None,
        engine_types: list[str] = None,
        period: PERIOD = "DAY",
        time_offset: int = None,
        ruk: str = None,
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
                "ruk": ruk,
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
        ruk: str = None,
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
                "ruk": ruk,
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
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetAccountsByLimits(self, uidslimits: list[str], ruk: str = None):
        """
        Gets accounts by limits.
        """
        # Ensure the uidslimits in the correct format
        # Example: '1234:100.00;6789:20.00'
        return self._get(
            "GetAccountsByLimits",
            params={"uidslimits": uidslimits, "ruk": ruk},
            delimiter=";",
        )

    def GetAccountsByPersonalThreshold(self, ruk: str = None):
        """
        Get accounts for remind which balance less then setted by user.
        """
        return self._get("GetAccountsByPersonalThreshold", params={"ruk": ruk})

    def GetAccountsByUids(
        self, uids: list[str], lebalance: str = None, ruk: str = None
    ):
        """
        Gets accounts by user ids.
        """
        return self._get(
            "GetAccountsByUids",
            params={"uids": uids, "lebalance": lebalance, "ruk": ruk},
        )

    def GetAccountsForDeactivation(self, ruk: str = None):
        """
        Get accounts for deactivation. Such as bonus is zero or trial period ended for trial accounts and balance less
        then allowed for billing accounts.
        """
        return self._get("GetAccountsForDeactivation", params={"ruk": ruk})

    def GetAccountsForDestroying(self, ruk: str = None):
        """
        Get accounts for destroying which in status inactive more then allowed.
        """
        return self._get("GetAccountsForDestroying", params={"ruk": ruk})

    def GetAggClusterBillingHistory(
        self,
        start_time: datetime,
        end_time: datetime,
        interval: int,
        sum_fields: list[str],
        is_paid: bool = False,
        ruk: str = None,
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
                "ruk": ruk,
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
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetBillingInfo(self, ruk: str = None):
        """
        Returns account billing information.
        """
        return self._get("GetBillingInfo", params={"ruk": ruk})

    def GetClusterBillingHistory(
        self,
        start_time: datetime,
        end_time: datetime,
        interval: int = None,
        ruk: str = None,
    ):
        """
        Gets account billing history.
        """
        return self._get(
            "GetClusterBillingHistory",
            params={
                "startTime": start_time,
                "endTime": end_time,
                "interval": interval,
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetCollaborationQuotas(
        self,
        collaboration_id: int = None,
        owner_uid: int = None,
        quota_names: list[str] = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetCountries(self, ruk: str = None):
        """
        Returns associative list of country names, regex patterns for VAT (tax payer id) and postal code, phone prefix
        and its two letter codes. Each extern billing could have its own representation so Jbilling settle this.
        """
        return self._get("GetCountries", params={"ruk": ruk})

    def GetCountryStates(self, country_code: str, ruk: str = None):
        """
        Returns lists of states (provinces) for the specified country. If conversion to commercial group doesn't
        requires to point client's state then this method returns empty list.
        """
        return self._get("GetCountryStates", params={"ccode": country_code, "ruk": ruk})

    def GetEnvBillingHistoryByPeriod(
        self,
        start_time: datetime,
        end_time: datetime,
        period: PERIOD = "DAY",
        time_offset: int = None,
        group_nodes: bool = False,
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetExtendedAccountBillingHistoryByPeriod(
        self,
        start_time: datetime,
        end_time: datetime,
        target_app_id: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%dT%H:%M:%SZ",
        )

    def GetExternBillingSystemSession(self, ruk: str = None):
        """
        Session (some information) to interact with extern billing system as its client. It created automatically and
        garbaged. JBilling cache it and check. If you code fails try to recall this method.
        """
        return self._get("GetExternBillingSystemSession", params={"ruk": ruk})

    def GetExternBillingSystems(self, ruk: str = None):
        """
        The platform can work with multiple external billing systems. But each user can only be bound with one.
        Possible values: NullExternBilling, PbasExternBilling, PbaExternBilling.
        """
        return self._get("GetExternBillingSystems", params={"ruk": ruk})

    def GetExternalUserById(self, id: str, ruk: str = None):
        return self._get("GetExternalUserById", params={"id": id, "ruk": ruk})

    def GetFundAccountHistory(
        self, start_time: datetime, end_time: datetime, uid: int, ruk: str = None
    ):
        """
        Getting Fund history account by uid.
        """
        return self._get(
            "GetFundAccountHistory",
            params={
                "startTime": start_time,
                "endTime": end_time,
                "uid": uid,
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetQuotas(self, quota_names: list[str] = None, ruk: str = None):
        """
        Returns the values of the specified quotas for the user.

        :param quota_names: list of quota names to get values for
        """
        return self._get("GetQuotas", params={"quotasnames": quota_names, "ruk": ruk})

    def GetSum(
        self, uid: int, start_time: datetime, end_time: datetime, ruk: str = None
    ):
        """
        Gets account summary debit and balance for period.
        """
        return self._get(
            "GetSum",
            params={
                "uid": uid,
                "startTime": start_time,
                "endTime": end_time,
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetSumAccountBillingHistory(
        self,
        uid: int,
        start_time: datetime,
        end_time: datetime,
        bonus: int = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def GetSuspendedAccounts(self, ruk: str = None):
        """
        Get suspended accounts.
        """
        return self._get("GetSuspendedAccounts", params={"ruk": ruk})

    def RemoveQuota(self, uid: int, name: str, ruk: str = None):
        return self._get("RemoveQuota", params={"uid": uid, "name": name, "ruk": ruk})

    def ResetTestAccounts(self, ruk: str = None):
        """
        Resets a list of testing accounts on the platform.
        """
        return self._get("ResetTestAccounts", params={"ruk": ruk})

    def SetAccountStatus(self, uid: int, status: int, ruk: str = None):
        """
        Sets account status. If new status is inactive then active environments are remembered and non stopped
        environments are shutdown. At activation all active environments are woken up.
        """
        return self._get(
            "SetAccountStatus",
            params={"uid": uid, "status": status, "ruk": ruk},
        )

    def SetBillingInfo(self, customer: dict, ruk: str = None):
        """
        Replaces existing account billing information with the provided value.

        :param customer: JSON object with the client's billing information.
        """
        return self._get("SetBillingInfo", params={"customer": customer, "ruk": ruk})

    def SetFundNote(self, id: int, note: str, ruk: str = None):
        return self._get("SetFundNote", params={"id": id, "note": note, "ruk": ruk})

    def SetGroup(
        self,
        uid: int,
        group_name: str,
        reset_balance: bool = False,
        reset_bonus: bool = False,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def SetQuota(
        self, uid: int, name: str, value: str, reference_id: int = None, ruk: str = None
    ):
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
                "ruk": ruk,
            },
        )

    def SetUserNote(self, uid: int, note: str, ruk: str = None):
        return self._get("SetUserNote", params={"uid": uid, "note": note, "ruk": ruk})

    def SurchargeAccounts(self, start_date: date, end_date: date, ruk: str = None):
        """
        Surcharge accounts.
        """
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")

        return self._get(
            "SurchargeAccounts",
            params={"startDate": start_date, "endDate": end_date, "ruk": ruk},
        )

    def SuspendUser(self, uid: int, ruk: str = None):
        """
        Suspend account. This status deny signin for user.
        """
        return self._get("SuspendUser", params={"uid": uid, "ruk": ruk})

    def UnfundAccount(
        self,
        uid: int,
        amount: float,
        is_bonus: bool = False,
        note: str = None,
        ruk: str = None,
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
            params={
                "uid": uid,
                "amount": amount,
                "isBonus": is_bonus,
                "note": note,
                "ruk": ruk,
            },
        )

    def WithdrawAccounts(self, start_date: date, end_date: date, ruk: str = None):
        """
        Charge accounts for resource usage for the specified period.
        """
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")

        return self._get(
            "WithdrawAccounts",
            params={"startDate": start_date, "endDate": end_date, "ruk": ruk},
        )


class _Invoice(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.Invoice
    """

    _endpoint2 = "invoice"

    def Event(self, extern_id: str, event_type: str, ruk: str = None):
        """
        :param extern_id: unique identifier of the document that was returned by external billing system
        :param event_type: invoice event type (EXPIRED or PAID)
        """
        return self._get(
            "Event", params={"externId": extern_id, "eventType": event_type, "ruk": ruk}
        )

    def GetExternalInvoices(
        self, limit: int = None, owner_uid: int = None, ruk: str = None
    ):
        """
        :param limit: the maximum number of invoices returned in the response.
        :param owner_uid: unique identifier of the invoice owner.
        """
        return self._get(
            "ExternalInvoices",
            params={"limit": limit, "ownerUid": owner_uid, "ruk": ruk},
        )

    def GetInvoices(
        self,
        id: int = None,
        unique_name: str = None,
        type: str = None,
        status: str = None,
        subscription_id: int = None,
        subscription_status: str = None,
        order_fields: str = None,
        order_direction: str = None,
        start_row: int = None,
        result_count: int = None,
        expand_fields: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def MakeInvoice(self, uid: str, skip_pay: bool = None, ruk: str = None):
        """
        :param uid: a comma-separated list of target POST-paid users' unique identifiers (all, if not set).
        :param skip_pay: a flag that disables (true) or enables (false) auto-pay with a default payment method
        """
        return self._get(
            "MakeInvoice",
            params={"uid": uid, "skipPay": skip_pay, "ruk": ruk},
        )

    def MarkAsPaid(self, id: int = None, ebs_invoice_id: str = None, ruk: str = None):
        """
        :param id: unique identifier of the target invoice.
        :param ebs_invoice_id: unique identifier of the target invoice in the external billing system.
        """
        return self._get(
            "MarkAsPaid",
            params={"id": id, "ebsInvoiceId": ebs_invoice_id, "ruk": ruk},
        )

    def MarkAsVoid(self, id: int = None, ebs_invoice_id: str = None, ruk: str = None):
        """
        :param id: unique identifier of the target invoice.
        :param ebs_invoice_id: unique identifier of the target invoice in the external billing system.
        """
        return self._get(
            "MarkAsVoid",
            params={"id": id, "ebsInvoiceId": ebs_invoice_id, "ruk": ruk},
        )

    def Pay(
        self,
        id: int,
        payment_method_id: str = None,
        payment_method_type: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def SearchInvoices(
        self,
        search: str,
        expand_fields: str = None,
        reseller_id: int = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )


class _GroupQuota(Billing):
    """
    Ref: https://docs.jelastic.com/api/#!/api/billing.GroupQuota
    """

    _endpoint2 = "groupquota"

    def AddGroup(
        self,
        type: str,
        name: str,
        description: str = None,
        source_group_name: str = None,
        domain: str = None,
        conversion_group: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def AddQuota(
        self,
        name: str,
        description: str = None,
        reference_id: str = None,
        default_value: int = None,
        assign_to_group: bool = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def DeleteGroup(self, name: str, ruk: str = None):
        return self._get("DeleteGroup", params={"name": name, "ruk": ruk})

    def EditGroup(
        self,
        name: str,
        new_name: str = None,
        description: str = None,
        conversion_group: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def EditQuota(
        self,
        name: str,
        reference_id: str = None,
        new_reference_id: str = None,
        description: str = None,
        ruk: str = None,
    ):
        """
        param name: unique a name of the quota to be adjusted.
        param reference_id: reference ID of the quota.
        param description: custom quota description.
        """
        return self._get(
            "EditQuota",
            params={
                "name": name,
                "referenceId": reference_id,
                "newReferenceId": new_reference_id,
                "description": description,
                "ruk": ruk,
            },
        )

    def GetGroupQuotas(self, name: str, quotas_names: str = None, ruk: str = None):
        return self._get(
            "GetGroupQuotas",
            params={"name": name, "quotasnames": quotas_names, "ruk": ruk},
        )

    def GetGroups(self, ruk: str = None):
        return self._get("GetGroups", params={"ruk": ruk})

    def GetPricingModels(self, group_name: str, ruk: str = None):
        return self._get(
            "GetPricingModels", params={"groupName": group_name, "ruk": ruk}
        )

    def GetQuotas(self, ruk: str = None):
        return self._get("GetQuotas", params={"ruk": ruk})

    def IsDomainBound(self, checksum: str = None, ruk: str = None):
        return self._get("IsDomainBound", params={"checksum": checksum, "ruk": ruk})

    def RemoveGroupQuota(self, group_name: str, quota_name: str, ruk: str = None):
        return self._get(
            "RemoveGroupQuota",
            params={"groupName": group_name, "quotaName": quota_name, "ruk": ruk},
        )

    def RemoveQuota(
        self, name: str, force: bool = None, reference_id: str = None, ruk: str = None
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
                "ruk": ruk,
            },
        )

    def SetCollaborationGroup(self, name: str, ruk: str = None):
        return self._get("SetCollaborationGroup", params={"name": name, "ruk": ruk})

    def SetDefaultGroup(self, name: str, ruk: str = None):
        return self._get("DefaultGroup", params={"name": name, "ruk": ruk})

    def SetGroupQuota(
        self,
        group_name: str,
        quota_name: str,
        value: int,
        reference_id: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def SetPricingModels(self, group_name: str, data: str, ruk: str = None):
        return self._get(
            "SetPricingModel",
            params={"groupName": group_name, "data": data, "ruk": ruk},
        )

    def SetSignupGroup(self, name: str, ruk: str = None):
        return self._get("SetSignupGroup", params={"name": name, "ruk": ruk})

    def SetWinDomain(self, group_name: str, win_domain_id: int, ruk: str = None):
        return self._get(
            "SetWinDomain",
            params={"groupName": group_name, "winDomainId": win_domain_id, "ruk": ruk},
        )

    def UnassignHdNodeGroup(
        self, hardware_node_group: str, checksum: str, ruk: str = None
    ):
        return self._get(
            "UnassignHdNodeGroup",
            params={
                "hardwareNodeGroup": hardware_node_group,
                "checksum": checksum,
                "ruk": ruk,
            },
        )


class _Integration(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Integration
    """

    _endpoint = "integration"

    def GetInvoiceUrl(self, invoice_id: int, ruk: str = None):
        """
        :param invoice_id: unique identifier of the target invoice in the internal billing system.
        """
        return self._get("GetInvoiceUrl", params={"invoiceId": invoice_id, "ruk": ruk})

    def GetSSOUrl(self, path: str = None, ruk: str = None):
        """
        :param path: destination path within the integrated system.
        """
        return self._get("GetSSOUrl", params={"path": path, "ruk": ruk})


class _PayMethod(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.PayMethod
    """

    _endpoint2 = "paymethod"

    def EnablePayMethod(self, pay_method_id: str, enable: int, ruk: str = None):
        """
        :param pay_method_id: payment method ID to be set as default one (see the GetPayMethodList method)
        :param enable: enables (1) or disables (0) the provided payment method
        """
        return self._get(
            "EnablePayMethod",
            params={"payMethodId": pay_method_id, "enable": enable, "ruk": ruk},
        )

    def GetDefaultPayMethod(self, ruk: str = None):
        return self._get("GetDefaultPayMethod", params={"ruk": ruk})

    def GetPublicToken(self, ruk: str = None):
        return self._get("GetPublicToken", params={"ruk": ruk})

    def GetValidPayTypes(self, ruk: str = None):
        return self._get("GetValidPayTypes", params={"ruk": ruk})

    def RegisterBankCard(
        self,
        first_name: str,
        last_name: str,
        card_number: str,
        card_code: str,
        expire_month: int,
        expire_year: int,
        service_plan_id: int,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def RegisterPayMethodAndPay(
        self,
        pay_method_type: str,
        service_plan_id: int,
        auto_service_plan_id: int = None,
        auto_refill_min_balance: int = None,
        auto_refill_period: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def SetDefaultPayMethod(self, pay_method_id: str, ruk: str = None):
        """
        :param pay_method_id: payment method ID to be set as default one (see the GetPayMethodList method)
        """
        return self._get(
            "SetDefaultPayMethod", params={"payMethodId": pay_method_id, "ruk": ruk}
        )

    def SetupIntent(self, payment_method_type: str = None, ruk: str = None):
        """
        :param payment_method_type: list of payment method keys (optional), for example: card, bancontact, ...
        """
        return self._get(
            "SetupIntent", params={"paymentMethodType": payment_method_type, "ruk": ruk}
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
        tariff_grid_names: str = None,
        ruk: str = None,
    ):
        return self._get(
            "AddPricing",
            params={
                "pricing": pricing,
                "tariffIds": tariff_ids,
                "tariffGridNames": tariff_grid_names,
                "ruk": ruk,
            },
        )

    def AddResource(self, resource: str, ruk: str = None):
        return self._get("AddResource", params={"resource": resource, "ruk": ruk})

    def AddTariff(self, tariff: dict, ruk: str = None):
        return self._get("AddTariff", params={"tariff": tariff, "ruk": ruk})

    def AttachTariff(self, uniq_name: str, target_app_id: str, ruk: str = None):
        return self._get(
            "AttachTariff",
            params={"uniqName": uniq_name, "targetAppId": target_app_id, "ruk": ruk},
        )

    def AttachTariffGrid(self, tariff_grid_name: str, id: str, ruk: str = None):
        return self._get(
            "AttachTariffGrid",
            params={"tariffGridName": tariff_grid_name, "id": id, "ruk": ruk},
        )

    def CheckHostGroupsAllowed(
        self, owner_uid: int = None, hardware_node_groups: str = None, ruk: str = None
    ):
        """
        :param owner_uid: unique identifier of the target user.
        :param hardware_node_groups: a comma-separated list of the host groups to be checked.
        """
        return self._get(
            "CheckHostGroupsAllowed",
            params={
                "ownerUid": owner_uid,
                "hardwareNodeGroups": hardware_node_groups,
                "ruk": ruk,
            },
        )

    def DeletePricing(self, id: str, ruk: str = None):
        return self._get("DeletePricing", params={"id": id, "ruk": ruk})

    def DeleteTariff(self, id: str, ruk: str = None):
        return self._get("DeleteTariff", params={"id": id, "ruk": ruk})

    def DetachTariff(self, uniq_name: str, target_app_id: str, ruk: str = None):
        return self._get(
            "DetachTariff",
            params={"uniqName": uniq_name, "targetAppId": target_app_id, "ruk": ruk},
        )

    def DetachTariffGrid(self, tariff_grid_name: str, id: str, ruk: str = None):
        return self._get(
            "DetachTariffGrid",
            params={"tariffGridName": tariff_grid_name, "id": id, "ruk": ruk},
        )

    def EditPricing(self, pricing: dict, ruk: str = None):
        return self._get("EditPricing", params={"pricing": pricing, "ruk": ruk})

    def EditResource(self, resource: str, ruk: str = None):
        return self._get("EditResource", params={"resource": resource, "ruk": ruk})

    def EditTariff(self, tariff: dict, ruk: str = None):
        return self._get("EditTariff", params={"tariff": tariff, "ruk": ruk})

    def GetCurrencies(self, currency: str = None, ruk: str = None):
        return self._get("GetCurrencies", params={"currency": currency, "ruk": ruk})

    def GetPlatformCurrency(self, reseller_id: int = None, ruk: str = None):
        return self._get(
            "GetPlatformCurrency", params={"resellerId": reseller_id, "ruk": ruk}
        )

    def GetPricing(self, owner_uid: int = None, ruk: str = None):
        return self._get("GetPricing", params={"ownerUid": owner_uid, "ruk": ruk})

    def GetPricingInner(self, reseller_id: int = None, ruk: str = None):
        """
        :param reseller_id: unique ID of the target reseller platform
        """
        return self._get(
            "GetPricingInner", params={"resellerId": reseller_id, "ruk": ruk}
        )

    def GetResources(self, id: int = None, name: str = None, ruk: str = None):
        return self._get("GetResources", params={"id": id, "name": name, "ruk": ruk})

    def GetTariffsInner(
        self,
        pricing_id: str = None,
        type: str = None,
        reseller_id: int = None,
        ruk: str = None,
    ):
        """
        :param pricing_id: pricing model unique ID.
        :param type: a semicolon-separated list of tariff types.
        :param reseller_id: unique ID of the target reseller platform.
        """
        return self._get(
            "GetTariffsInner",
            params={
                "priceId": pricing_id,
                "type": type,
                "resellerId": reseller_id,
                "ruk": ruk,
            },
        )

    def GetUniqueResourceNames(self, ruk: str = None):
        return self._get("GetUniqueResourceNames", params={"ruk": ruk})

    def SetTariffs(
        self,
        pricing_id: str,
        tariff_ids: str,
        tariff_grid_names: str = None,
        ruk: str = None,
    ):
        return self._get(
            "SetTariffs",
            params={
                "pricingId": pricing_id,
                "tariffIds": tariff_ids,
                "tariffGridNames": tariff_grid_names,
                "ruk": ruk,
            },
        )

    def ValidateEnvironment(
        self, hardware_node_group: str, owner_uid: int = None, ruk: str = None
    ):
        return self._get(
            "ValidateEnvironment",
            params={
                "hardwareNodeGroup": hardware_node_group,
                "ownerUid": owner_uid,
                "ruk": ruk,
            },
        )

    def ValidateNode(
        self,
        uid: int,
        hardware_node_group: str,
        node_type: str,
        fixed_cloud_lets: int,
        flexible_cloud_lets: int,
        ruk: str = None,
    ):
        return self._get(
            "ValidateNode",
            params={
                "uid": uid,
                "hardwareNodeGroup": hardware_node_group,
                "nodeType": node_type,
                "fixedCloudlets": fixed_cloud_lets,
                "flexibleCloudlets": flexible_cloud_lets,
                "ruk": ruk,
            },
        )

    def ValidateNodeInner(
        self,
        uid: int,
        hardware_node_group: str,
        node_type: str,
        fixed_cloud_lets: int,
        flexible_cloud_lets: int,
        ruk: str = None,
    ):
        return self._get(
            "ValidateNodeInner",
            params={
                "uid": uid,
                "hardwareNodeGroup": hardware_node_group,
                "nodeType": node_type,
                "fixedCloudlets": fixed_cloud_lets,
                "flexibleCloudlets": flexible_cloud_lets,
                "ruk": ruk,
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
        settings: str = None,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def EditReseller(
        self, reseller: str, platform: str = None, regions: str = None, ruk: str = None
    ):
        return self._get(
            "EditReseller",
            params={
                "reseller": reseller,
                "platform": platform,
                "regions": regions,
                "ruk": ruk,
            },
        )

    def GetAllResellers(self, ruk: str = None):
        return self._get("GetAllResellers", params={"ruk": ruk})

    def GetResellerByAppid(self, target_app_id: str, ruk: str = None):
        return self._get(
            "GetResellerByAppid", params={"targetAppid": target_app_id, "ruk": ruk}
        )

    def GetResellerById(self, id: int, ruk: str = None):
        return self._get("GetResellerById", params={"id": id, "ruk": ruk})

    def GetResellerByOwnerUid(self, uid: int, ruk: str = None):
        return self._get("GetResellerByOwnerUid", params={"uid": uid, "ruk": ruk})

    def GetResellerByUid(self, uid: int, ruk: str = None):
        return self._get("GetResellerByUid", params={"uid": uid, "ruk": ruk})

    def RemoveReseller(self, id: int, ruk: str = None):
        return self._get("RemoveReseller", params={"id": id, "ruk": ruk})

    def SetResellerStatus(self, id: int, status: str, ruk: str = None):
        return self._get(
            "SetResellerStatus", params={"id": id, "status": status, "ruk": ruk}
        )


class _ServicePlan(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.ServicePlan
    """

    _endpoint2 = "serviceplan"

    def CreateLevelAutoPay(
        self,
        min_balance: int,
        expires: datetime,
        service_plan_id: int,
        payment_method_id: str,
        min_period: int,
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def CreateRegularAutoPay(
        self,
        cron_expression: str,
        expires: datetime,
        time_zone: str,
        service_plan_id: int,
        payment_method_id: str,
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def CreateServicePlan(
        self,
        name: str,
        description: str,
        service_plan_type: str,
        extern_plan_id: str,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def DeleteAutoPay(self, auto_pay_id: int, ruk: str = None):
        """
        :param auto_pay_id: auto pay id. It can be get with ServicePlanService#GetAutoPays method
        """
        return self._get("DeleteAutoPay", params={"autoPayId": auto_pay_id, "ruk": ruk})

    def DeleteServicePlan(self, service_plan_id: int, ruk: str = None):
        """
        :param service_plan_id: id of sevice plan to be deleted
        """
        return self._get(
            "DeleteServicePlan", params={"servicePlanId": service_plan_id, "ruk": ruk}
        )

    def EnableServicePlan(self, service_plan_id: int, enabled: int, ruk: str = None):
        """
        :param service_plan_id: id of the specified service plan
        :param enabled: 1 enabled and 0 = disabled
        """
        return self._get(
            "EnableServicePlan",
            params={"servicePlanId": service_plan_id, "enabled": enabled, "ruk": ruk},
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
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def ExtendedGetServicePlans(self, ruk: str = None):
        return self._get("ExtendedGetServicePlans", params={"ruk": ruk})

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
        ruk: str = None,
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
                "ruk": ruk,
            },
        )

    def GetAutoPayHistory(self, auto_pay_id: int, ruk: str = None):
        """
        :param auto_pay_id: specified auto pay id
        """
        return self._get(
            "GetAutoPayHistory", params={"autoPayId": auto_pay_id, "ruk": ruk}
        )

    def GetAutoPays(self, ruk: str = None):
        return self._get("GetAutoPays", params={"ruk": ruk})

    def GetBoughtServicePlans(self, ruk: str = None):
        return self._get("GetBoughtServicePlans", params={"ruk": ruk})

    def GetCurrency(self, ruk: str = None):
        return self._get("GetCurrency", params={"ruk": ruk})

    def GetFinalCost(self, service_plan_id: int, ruk: str = None):
        """
        :param service_plan_id: specified service plan id
        """
        return self._get(
            "GetFinalCost", params={"servicePlanId": service_plan_id, "ruk": ruk}
        )

    def GetPayMethodList(self, ruk: str = None):
        return self._get("GetPayMethodList", params={"ruk": ruk})

    def GetPaymentNews(self, ruk: str = None):
        return self._get("GetPaymentNews", params={"ruk": ruk})

    def GetServicePlan(self, service_plan_id: int, ruk: str = None):
        """
        :param service_plan_id: id of service plan to be returned
        """
        return self._get(
            "GetServicePlan", params={"servicePlanId": service_plan_id, "ruk": ruk}
        )

    def GetServicePlanByType(self, plan_type: str = None, ruk: str = None):
        return self._get(
            "GetServicePlanByType", params={"planType": plan_type, "ruk": ruk}
        )

    def PaymentNewsRead(self, id: str, ruk: str = None):
        """
        :param id: comma separated ids of payments
        """
        return self._get("PaymentNewsRead", params={"id": id, "ruk": ruk})

    def SetExternPlanId(
        self, service_plan_id: int, external_plan_id: str, ruk: str = None
    ):
        """
        :param service_plan_id: JBilling service plan id
        """
        return self._get(
            "SetExternPlanId",
            params={
                "servicePlanId": service_plan_id,
                "externalPlanId": external_plan_id,
                "ruk": ruk,
            },
        )

    def UpdateServicePlan(
        self,
        service_plan_id: int,
        name: str,
        description: str,
        extern_service_plan_id: str,
        ruk: str = None,
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
                "ruk": ruk,
            },
        )


class _Order(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.Order
    """

    _endpoint2 = "order"

    def GetFraudCheckUrl(self, ruk: str = None):
        return self._get("GetFraudCheckUrl", params={"ruk": ruk})

    def GetHistoryUrl(self, ruk: str = None):
        return self._get("GetHistoryUrl", params={"ruk": ruk})

    def GetOrders(self, status: str, ruk: str = None):
        return self._get(
            "GetOrders",
            params={"status": status, "ruk": ruk},
        )

    def GetUrlSupplyingCookiesForHistoryUrl(self, ruk: str = None):
        return self._get("GetUrlSupplyingCookiesForHistoryUrl", params={"ruk": ruk})

    def OrderEvent(self, extern_order_id: str, event_type: str, ruk: str = None):
        """
        :param extern_order_id: id of document in ebs which was returned
        :param event_type: APPROVED or DECLINED
        """
        return self._get(
            "OrderEvent",
            params={
                "externOrderId": extern_order_id,
                "eventType": event_type,
                "ruk": ruk,
            },
        )

    def PayServicePlan(self, service_plan_id: int, pay_method_id: str, ruk: str = None):
        """
        :param service_plan_id: service plan ID to be paid (for example, $200 one-time fee)
        :param pay_method_id: payment method ID to be used (see the GetPayMethodList method)
        """
        return self._get(
            "PayServicePlan",
            params={
                "servicePlanId": service_plan_id,
                "payMethodId": pay_method_id,
                "ruk": ruk,
            },
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
        start_date: datetime,
        end_date: datetime,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "ClearBillingHistory",
            params={
                "envName": env_name,
                "uid": uid,
                "startDate": start_date,
                "endDate": end_date,
                "checksum": checksum,
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def ClearMonthTraffic(
        self, uid: int, month_start: str, checksum: str, ruk: str = None
    ):
        return self._get(
            "ClearMonthTraffic",
            params={
                "uid": uid,
                "monthStart": month_start,
                "checksum": checksum,
                "ruk": ruk,
            },
        )

    def GetUidUsageByPeriod(
        self,
        uid: int,
        start_date: datetime,
        end_date: datetime,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "GetUidUsageByPeriod",
            params={
                "uid": uid,
                "startDate": start_date,
                "endDate": end_date,
                "checksum": checksum,
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d %H:%M:%S",
        )

    def SetAccountDate(
        self, uid: int, date_type: str, date_value: str, checksum: str, ruk: str = None
    ):
        return self._get(
            "SetAccountDate",
            params={
                "uid": uid,
                "dateType": date_type,
                "dateValue": date_value,
                "checksum": checksum,
                "ruk": ruk,
            },
        )

    def SetBillingHistoryDate(
        self,
        uid: int,
        env_name: str,
        start_date_from: date,
        start_date_to: date,
        date_type: str,
        date_value: str,
        checksum: str,
        ruk: str = None,
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
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d",
        )

    def SetMonthTraffic(
        self,
        uid: int,
        month_start: str,
        external_traffic: int,
        checksum: str,
        ruk: str = None,
    ):
        return self._get(
            "SetMonthTraffic",
            params={
                "uid": uid,
                "monthStart": month_start,
                "externalTraffic": external_traffic,
                "checksum": checksum,
                "ruk": ruk,
            },
        )


class _System(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.System
    """

    _endpoint2 = "system"

    def CleanCheckRequestCache(
        self, uid: int = None, local_only: bool = None, ruk: str = None
    ):
        return self._get(
            "CleanCheckRequestCache",
            params={"uid": uid, "localOnly": local_only, "ruk": ruk},
        )

    def Event(
        self, topic: str, message: str, publish_local: bool = None, ruk: str = None
    ):
        return self._get(
            "Event",
            params={
                "topic": topic,
                "message": message,
                "publishLocal": publish_local,
                "ruk": ruk,
            },
        )

    def GetAPIDescriptions(
        self, is_public_only: bool = None, is_token: bool = None, ruk: str = None
    ):
        return self._get(
            "GetAPIDescriptions",
            params={"isPublicOnly": is_public_only, "isToken": is_token, "ruk": ruk},
        )

    def GetAutoPercent(self, ruk: str = None):
        return self._get("GetAutoPercent", params={"ruk": ruk})

    def GetCacheStats(self, ruk: str = None):
        return self._get("GetCacheStats", params={"ruk": ruk})

    def GetCacheStatus(self, ruk: str = None):
        return self._get("GetCacheStatus", params={"ruk": ruk})

    def GetInstanceCacheStatus(self, ruk: str = None):
        return self._get("GetInstanceCacheStatus", params={"ruk": ruk})

    def GetStatus(self, checksum: str, ruk: str = None):
        return self._get("GetStatus", params={"checksum": checksum, "ruk": ruk})

    def GetVersion(self, ruk: str = None):
        return self._get("GetVersion", params={"ruk": ruk})

    def RefreshEmailTemplates(self, ruk: str = None):
        return self._get("RefreshEmailTemplates", params={"ruk": ruk})

    def RefreshUser(self, language: str = None, ruk: str = None):
        return self._get("RefreshUser", params={"language": language, "ruk": ruk})

    def ReloadConfiguration(
        self, reseller_id: int = None, changed_placeholders: str = None, ruk: str = None
    ):
        return self._get(
            "ReloadConfiguration",
            params={
                "resellerId": reseller_id,
                "changedPlaceholders": changed_placeholders,
                "ruk": ruk,
            },
        )

    def SendEmail(
        self,
        template: str,
        email: str = None,
        language: str = None,
        timeout: int = None,
        ruk: str = None,
    ):
        return self._get(
            "SendEmail",
            params={
                "template": template,
                "email": email,
                "language": language,
                "timeout": timeout,
                "ruk": ruk,
            },
        )

    def Validate(self, ruk: str = None):
        return self._get("Validate", params={"ruk": ruk})

    def ValidateAll(self, ruk: str = None):
        return self._get("ValidateAll", params={"ruk": ruk})


class _Subscription(Billing):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/billing.Subscription
    """

    _endpoint = "subscription"

    def Cancel(
        self,
        id: int,
        immediately: bool = None,
        cancel_date: date = None,
        passphrase: str = None,
        expand_fields: str = None,
        ruk: str = None,
    ):
        """
        :param id: unique identifier of the target subscription.
        :param immediately: defines whether the current subscription should be cancelled immediately (true) or at the end of already purchased period (false).
        :param cancel_date: a specific date when the subscription should be canceled. UTC time in the ISO 8601 format, e.g. "2022-11-16T00:00:00".
        :param passphrase: unique code to confirm immediate subscription resources deletion.
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "Cancel",
            params={
                "id": id,
                "immediately": immediately,
                "cancelDate": cancel_date,
                "passphrase": passphrase,
                "expandFields": expand_fields,
                "ruk": ruk,
            },
            datetime_format="%Y-%m-%d",
        )

    def CloneProduct(
        self,
        subscription_id: int,
        item_resource: int,
        target_env_name: str,
        item_id: int = None,
        ruk: str = None,
    ):
        """
        :param subscription_id: unique identifier of the target subscription.
        :param item_resource: unique identifier of the target subscription item resource.
        :param target_env_name: domain prefix for the cloned environment.
        :param item_id: unique identifier of the target subscription item.
        """
        return self._get(
            "CloneProduct",
            params={
                "subscriptionId": subscription_id,
                "itemResource": item_resource,
                "targetEnvName": target_env_name,
                "itemId": item_id,
                "ruk": ruk,
            },
        )

    def DiscardUpdateSubscription(self, subscription_id: int, ruk: str = None):
        """
        :param subscription_id: unique identifier of the target subscription.
        """
        return self._get(
            "DiscardUpdateSubscription",
            params={"subscriptionId": subscription_id, "ruk": ruk},
        )

    def GetCategories(self, expand_fields: str = None, ruk: str = None):
        """
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "GetCategories", params={"expandFields": expand_fields, "ruk": ruk}
        )

    def GetProducts(
        self,
        id: int = None,
        category_id: int = None,
        expand_fields: str = None,
        start_row: int = None,
        result_count: int = None,
        order_field: str = None,
        order_direction: str = None,
        ruk: str = None,
    ):
        """
        :param id: unique identifier of the target subscription Product (for filtering).
        :param category_id: unique identifier of the target subscription Category (for filtering).
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        :param start_row: returns information starting from the specified row in the response (starts with 0, by default).
        :param result_count: returns the specified number of rows from the response (0 – unlimited – by default).
        :param order_field: sorts results by the specified field
        :param order_direction: sorts results in the ascending (ASC) or descending (DESC) order
        """
        return self._get(
            "GetProducts",
            params={
                "id": id,
                "categoryId": category_id,
                "expandFields": expand_fields,
                "startRow": start_row,
                "resultCount": result_count,
                "orderField": order_field,
                "orderDirection": order_direction,
                "ruk": ruk,
            },
        )

    def GetRestrictedHardNodeGroups(self, subscription_item_id: int, ruk: str = None):
        """
        :param subscription_item_id: unique identifier of the target subscription item.
        """
        return self._get(
            "GetHardNodeGroups",
            params={"subscriptionItemId": subscription_item_id, "ruk": ruk},
        )

    def GetServicePlans(
        self,
        id: int = None,
        product_id: int = None,
        expand_fields: str = None,
        ruk: str = None,
    ):
        """
        :param id: unique identifier of the target service plan (for filtering).
        :param product_id: unique identifier of the target subscription product (for filtering).
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "GetServicePlans",
            params={
                "id": id,
                "productId": product_id,
                "expandFields": expand_fields,
                "ruk": ruk,
            },
        )

    def GetSubscriptions(
        self,
        id: int = None,
        product_id: int = None,
        status: list[str] = None,
        expand_fields: str = None,
        start_row: int = None,
        result_count: int = None,
        order_field: str = None,
        order_direction: str = None,
        ruk: str = None,
    ):
        """
        :param id: unique identifier of the target subscription (for filtering).
        :param product_id: unique identifier of the target subscription product (for filtering).
        :param status: a comma-separated list of the subscription statuses.("INCOMPLETE", "INCOMPLETE_EXPIRED", "TRIAL", "ACTIVE", "PAST_DUE", "UNPAID", "SUSPENDED", "CANCELED", "ENDED").
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        :param start_row: returns information starting from the specified row in the response (starts with 0, by default).
        :param result_count: returns the specified number of rows from the response (0 – unlimited – by default).
        :param order_field: sorts results by the specified field
        :param order_direction: sorts results in the ascending (ASC) or descending (DESC) order
        """
        return self._get(
            "GetSubscriptions",
            params={
                "id": id,
                "productId": product_id,
                "status": status,
                "expandFields": expand_fields,
                "startRow": start_row,
                "resultCount": result_count,
                "orderField": order_field,
                "orderDirection": order_direction,
                "ruk": ruk,
            },
            delimiter=",",
        )

    def InstallProduct(
        self,
        subscription_id: int,
        item_id: int = None,
        settings: str = None,
        env_name: str = None,
        display_name: str = None,
        env_groups: str = None,
        region: str = None,
        lang: str = None,
        ruk: str = None,
    ):
        """
        :param subscription_id: unique identifier of the target subscription.
        :param item_id: unique identifier of the target subscription item.
        :param settings: JSON object with subscription configuration.
        :param env_name: target environment name
        :param display_name: target environment display name
        :param env_groups: target environment groups
        :param region: target environment region
        :param lang: target installation language
        """
        return self._get(
            "InstallProduct",
            params={
                "subscriptionId": subscription_id,
                "itemId": item_id,
                "settings": settings,
                "envName": env_name,
                "displayName": display_name,
                "envGroups": env_groups,
                "region": region,
                "lang": lang,
                "ruk": ruk,
            },
        )

    def MoveProduct(
        self,
        subscription_id: int,
        item_resource_id: int,
        target_subscription_id: int,
        target_item_id: int,
        passphrase: str,
        item_id: int = None,
        ruk: str = None,
    ):
        """
        :param subscription_id: unique identifier of the source subscription.
        :param item_resource_id: unique identifier of the source subscription item resource.
        :param target_subscription_id: unique identifier of the target subscription item resource.
        :param target_item_id: unique identifier of the target subscription item.
        :param passphrase: confirmation code for the operation (provide the “uniqueName” value from the “ItemResource” object).
        :param item_id: unique identifier of the source subscription item.
        """
        return self._get(
            "MoveProduct",
            params={
                "subscriptionId": subscription_id,
                "itemResourceId": item_resource_id,
                "targetSubscriptionId": target_subscription_id,
                "targetItemId": target_item_id,
                "passphrase": passphrase,
                "itemId": item_id,
                "ruk": ruk,
            },
        )

    def SetAutopay(
        self, id: int, enabled: bool, expand_fields: str = None, ruk: str = None
    ):
        """
        :param id: unique identifier of the target subscription.
        :param enabled: defines whether to enable (true) or disable (false) the auto pay option for the subscription.
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "SetAutopay",
            params={
                "id": id,
                "enabled": enabled,
                "expandFields": expand_fields,
                "ruk": ruk,
            },
        )

    def Subscribe(
        self,
        product_id: int,
        items: str,
        change_automatically: bool = None,
        expand_fields: str = None,
        ruk: str = None,
    ):
        """
        :param product_id: unique identifier of the subscription product.
        :param items: JSON object with subscription details. For example: [{"servicePlanId": 1, "tariffPlanId": 1, "quantity": 10}].
        :param change_automatically: defines whether the auto pay option for the subscription should be enabled (true) or disabled (false).
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "Subscribe",
            params={
                "productId": product_id,
                "items": items,
                "chargeAutomatically": change_automatically,
                "expandFields": expand_fields,
                "ruk": ruk,
            },
        )

    def UndoCancel(self, id: int, expand_fields: str = None, ruk: str = None):
        """
        :param id: unique identifier of the target subscription.
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "UndoCancel",
            params={"id": id, "expandFields": expand_fields, "ruk": ruk},
        )

    def UninstallProduct(
        self,
        subscription_id: int,
        item_id: int,
        item_resource_id: int,
        passphrase: str,
        ruk: str = None,
    ):
        """
        :param subscription_id: unique identifier of the target subscription.
        :param item_id: unique identifier of the target subscription item.
        :param item_resource_id: unique identifier of the target subscription item resource.
        :param passphrase: confirmation code for the operation (provide the “uniqueName” value from the “ItemResource” object).
        """
        return self._get(
            "UninstallProduct",
            params={
                "subscriptionId": subscription_id,
                "itemId": item_id,
                "itemResourceId": item_resource_id,
                "passphrase": passphrase,
                "ruk": ruk,
            },
        )

    def UpcomingInvoice(
        self, subscription_id: int, item_id: int, quantity: int, ruk: str = None
    ):
        """
        :param subscription_id: unique identifier of the target subscription.
        :param item_id: unique identifier of the target subscription item.
        :param quantity: a new installation quantity for the subscription.
        """
        return self._get(
            "UpcomingInvoice",
            params={
                "subscriptionId": subscription_id,
                "itemId": item_id,
                "quantity": quantity,
                "ruk": ruk,
            },
        )

    def UpdateSubscription(
        self,
        subscription_id: int,
        item_id: int,
        quantity: int,
        expand_fields: str = None,
        ruk: str = None,
    ):
        """
        :param subscription_id: unique identifier of the target subscription.
        :param item_id: unique identifier of the target subscription item
        :param quantity: a new installation quantity for the subscription.
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "UpdateSubscription",
            params={
                "subscriptionId": subscription_id,
                "itemId": item_id,
                "quantity": quantity,
                "expandFields": expand_fields,
                "ruk": ruk,
            },
        )
