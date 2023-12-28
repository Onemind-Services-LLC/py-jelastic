import pytest
from unittest.mock import patch, Mock
from jelastic.api import Security

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}
