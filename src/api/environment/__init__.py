from datetime import datetime

from ..api import API

__all__ = ["Environment"]


class Environment(API):
    _endpoint1 = "environment"
