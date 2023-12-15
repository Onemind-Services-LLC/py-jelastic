__all__ = [
    "JelasticApiError",
    "JelasticPermissionError",
    "JelasticResourceNotFound",
    "JelasticExternBillingError",
    "JelasticExternBillingRejected",
]


class JelasticApiError(Exception):
    """API errors"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class JelasticPermissionError(JelasticApiError):
    """Permission errors"""

    def __init__(self, *args: object) -> None:
        super(JelasticApiError, self).__init__(*args)


class JelasticResourceNotFound(JelasticApiError):
    """Resource not found errors"""

    def __init__(self, *args: object) -> None:
        super(JelasticApiError, self).__init__(*args)


class JelasticExternBillingError(JelasticApiError):
    """External billing errors"""

    def __init__(self, *args: object) -> None:
        super(JelasticApiError, self).__init__(*args)


class JelasticExternBillingRejected(JelasticApiError):
    """External billing errors"""

    def __init__(self, *args: object) -> None:
        super(JelasticApiError, self).__init__(*args)
