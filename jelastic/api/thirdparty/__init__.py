from ..abstract import ClientAbstract

__all__ = ["ThirdParty"]


class ThirdParty(ClientAbstract):
    _endpoint1 = "thirdparty"

    @property
    def GeoIp(self) -> "_GeoIp":
        return _GeoIp(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _GeoIp(ThirdParty):
    _endpoint2 = "geoip"

    def GeoIp(
        self,
        ruk: str = None,
    ):
        return self._get("GeoIp", params={"ruk": ruk})
