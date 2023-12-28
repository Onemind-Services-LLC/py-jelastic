import datetime
from unittest.mock import patch, Mock

import pytest

from jelastic.api import System

CURRENT_DATETIME = datetime.datetime.now()
success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}

__all__ = ("client", "success_response", "CURRENT_DATETIME")


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        jc = System(session=Mock(), token="token")
        jc._get = mock_get
        yield jc
