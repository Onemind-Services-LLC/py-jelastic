import json
from typing import Literal

from ..abstract import ClientAbstract

__all__ = ["Utils"]

TRIGGER_TYPE = Literal["cron", "rate", "date", "oninit", "once_delay"]


class Utils(ClientAbstract):
    """
    >>> from jelastic import Jelastic
    >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
    >>> jelastic.utils

    Ref: https://docs.jelastic.com/api/private/#!/api/utils
    """

    _endpoint1 = "utils"

    @property
    def Batch(self) -> "_Batch":
        """
        Used to perform several actions in one request to the server.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.utils.Batch

        Ref: https://docs.jelastic.com/api/private/#!/api/utils.Batch
        """
        return _Batch(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Scheduler(self) -> "_Scheduler":
        """
        This service manages custom operations on the platform (tasks) that are performed based on the configured
        triggers. A task can be associated with the account or specific environment (automatically removed alongside it)
        and executed based on the specific conditions - cron, date, after the platform start, etc.

        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.utils.Scheduler

        Ref: https://docs.jelastic.com/api/private/#!/api/utils.Scheduler
        """
        return _Scheduler(session=self._session, token=self._token, debug=self._debug)


class _Batch(Utils):
    """
    Used to perform several actions in one request to the server.

    Ref: https://docs.jelastic.com/api/private/#!/api/utils.Batch
    """

    _endpoint2 = "batch"

    def Call(self, request: dict, sync: bool = False):
        """
        Multiply call the functions of platforms in a single query.

        :param request - batch query format JSON
        :param sync - sync call
        """
        request = json.dumps(request)

        return self._get("Call", params={"request": request, "sync": sync})


class _Scheduler(Utils):
    """
    This service manages custom operations on the platform (tasks) that are performed based on the configured triggers.
    A task can be associated with the account or specific environment (automatically removed alongside it) and executed
    based on the specific conditions - cron, date, after the platform start, etc.

    Ref: https://docs.jelastic.com/api/private/#!/api/utils.Scheduler
    """

    _endpoint2 = "scheduler"

    def CreateAccountTask(
        self,
        script: str,
        trigger: dict[TRIGGER_TYPE, str | int],
        description: str = None,
        params: dict = None,
    ):
        """
        Creates a task that executes a specified script based on the configured trigger.

        :param script: custom script name to be executed by the task.
        :param trigger: condition or frequency of the script execution (in the format: "trigger_type:value", supported
        :param description: custom description for the task.
        :param params: JSON object with additional trigger parameters.
        """
        trigger = json.dumps(trigger)
        params = json.dumps(params)
        return self._get(
            "CreateAccountTask",
            params={
                "script": script,
                "trigger": trigger,
                "description": description,
                "params": params,
            },
        )

    def CreateEnvTask(
        self,
        script: str,
        trigger: dict[TRIGGER_TYPE, str | int],
        env_name: list[str] = None,
        description: str = None,
        params: dict = None,
    ):
        """
        Creates a task that executes a specified script based on the configured trigger. The task is automatically
        removed when the corresponding environment is deleted.

        :param script: custom script name to be executed by the task.
        :param trigger: condition or frequency of the script execution (in the format: "trigger_type:value", supported
        :param env_name: target environment name.
        :param description: custom description for the task.
        :param params: JSON object with additional trigger parameters.
        """
        trigger = json.dumps(trigger)
        params = json.dumps(params)

        return self._get(
            "CreateEnvTask",
            params={
                "script": script,
                "trigger": trigger,
                "envName": env_name,
                "description": description,
                "params": params,
            },
        )

    def DeleteTasks(self, ids: list[str]):
        """
        Deletes specified tasks.

        :param ids: list of task IDs to remove.
        """
        return self._get("DeleteTasks", params={"ids": ids}, delimiter=",")

    def EditTask(
        self,
        script: str,
        trigger: dict[TRIGGER_TYPE, str | int],
        id: int,
        description: str = None,
        params: dict = None,
    ):
        """
        Changes the existing task according to the provided new values.

        :param script: custom script name to be executed by the task.
        :param trigger: condition or frequency of the script execution (in the format: "trigger_type:value", supported
        :param id: unique identifier of the target task.
        :param description: custom description for the task.
        :param params: JSON object with additional trigger parameters.
        """
        trigger = json.dumps(trigger)
        params = json.dumps(params)

        return self._get(
            "EditTask",
            params={
                "script": script,
                "trigger": trigger,
                "id": id,
                "description": description,
                "params": params,
            },
        )

    def GetTasks(self, ids: list[str] = None):
        """
        Returns information on the specified tasks.

        :param ids: list of IDs to retrieve
        """
        return self._get("GetTasks", params={"ids": ids}, delimiter=",")

    def RescheduleTasks(self):
        return self._get("RescheduleTasks")

    def UnscheduleTasks(self):
        """
        Unschedules all the tasks assigned for regular execution.
        """
        return self._get("UnscheduleTasks")
