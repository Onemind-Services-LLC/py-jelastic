import json
from datetime import date

from ..abstract import ClientAbstract

__all__ = ["Automation"]


class Automation(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.automation

    Ref: https://docs.jelastic.com/api/private/#!/api/automation
    """

    _endpoint1 = "automation"

    @property
    def Utils(self) -> "_Utils":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.automation.Utils

        Ref: https://docs.jelastic.com/api/private/#!/api/automation.Utils
        """
        return _Utils(
            session=self._session,
            token=self._token,
            debug=self._debug,
            ruk=self._ruk,
        )


class _Utils(Automation):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://app.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.automation.Utils

    Ref: https://docs.jelastic.com/api/private/#!/api/automation.Utils
    """

    _endpoint2 = "utils"

    def ClearBillingHistory(
        self, uid: int, start_date: date, end_date: date, env_name: str = None
    ):
        return self._get(
            "ClearBillingHistory",
            params={
                "uid": uid,
                "startDate": start_date,
                "endDate": end_date,
                "envName": env_name,
            },
            datetime_format="%Y-%m-%d",
        )

    def ClearMonthTraffic(self, uid: int, month_start: str):
        return self._get(
            "ClearMonthTraffic",
            params={
                "uid": uid,
                "monthStart": month_start,
            },
        )

    def ClearResourceStatistics(
        self, uid: int, start_date_from: date, start_date_to: date
    ):
        return self._get(
            "ClearResourceStatistics",
            params={
                "uid": uid,
                "startDateFrom": start_date_from,
                "startDateTo": start_date_to,
            },
            datetime_format="%Y-%m-%d",
        )

    def GenerateBillableItemStatistics(
        self,
        start_date: date,
        duration_hour: int,
        node_id: int,
        item_id: int,
        env_name: str = None,
    ):
        return self._get(
            "GenerateBillableItemStatistics",
            params={
                "startDate": start_date,
                "durationHour": duration_hour,
                "nodeId": node_id,
                "itemId": item_id,
                "envName": env_name,
            },
            datetime_format="%Y-%m-%d",
        )

    def GenerateStatistics(
        self, start_date: date, duration_hour: int, node_id: int, stat_json: dict
    ):
        stat_json = json.dumps(stat_json)
        return self._get(
            "GenerateStatistics",
            params={
                "startDate": start_date,
                "durationHour": duration_hour,
                "nodeId": node_id,
                "statJson": stat_json,
            },
            datetime_format="%Y-%m-%d",
        )

    def GetUidUsageByPeriod(self, uid: int, start_date: date, end_date: date):
        return self._get(
            "GetUidUsageByPeriod",
            params={
                "uid": uid,
                "startDate": start_date,
                "endDate": end_date,
            },
            datetime_format="%Y-%m-%d",
        )

    def SetAccountDate(self, uid: int, date_type: str, date_value: str):
        return self._get(
            "SetAccountDate",
            params={"uid": uid, "dateType": date_type, "dateValue": date_value},
        )

    def SetAppNodeDate(self, env_name: str, date_type: str, date_value: str):
        return self._get(
            "SetAppNodeDate",
            params={
                "envName": env_name,
                "dateType": date_type,
                "dateValue": date_value,
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
            },
            datetime_format="%Y-%m-%d",
        )

    def SetMonthTraffic(self, uid: int, month_start: str, external_traffic: float):
        return self._get(
            "SetMonthTraffic",
            params={
                "uid": uid,
                "monthStart": month_start,
                "externalTraffic": external_traffic,
            },
        )

    def ShiftResourceCreatedOnDateToStartDate(
        self, uid: int, env_name: str, start_date_from: date, start_date_to: date
    ):
        return self._get(
            "ShiftResourceCreatedOnDateToStartDate",
            params={
                "uid": uid,
                "envName": env_name,
                "startDateFrom": start_date_from,
                "startDateTo": start_date_to,
            },
            datetime_format="%Y-%m-%d",
        )
