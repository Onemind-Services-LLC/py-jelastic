import datetime
from unittest.mock import patch, Mock
import pytest

from jelastic.api import System, system

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}

CURRENT_DATETIME = datetime.datetime.now()
