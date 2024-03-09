"""VietFin Etf class."""

from typing import Literal

from vietfin.abstract.vfobject import VfObject
from vietfin.abstract.factory import EtfFactory
from vietfin.abstract.interface import IEtf
from vietfin.utils.helpers import INTERVALS


class Etf:
    """VietFin ETF-related group of commands."""

    # list of implemented providers
    PROVIDERS = Literal["tcbs", "dnse", "ssi"]

    @staticmethod
    def _get_provider(provider: PROVIDERS) -> IEtf:
        provider_name = provider.lower()
        return EtfFactory().get_provider(provider_name)

    def historical(
        self,
        symbol: str,
        start_date: str | None = None,
        end_date: str | None = None,
        interval: INTERVALS = "1d",
        provider: PROVIDERS = "ssi",
    ) -> VfObject:
        """ETF Historical price. Load historical price data of a specific ETF ticker."""

        provider_instance = self._get_provider(provider)
        return provider_instance.historical(
            symbol=symbol,
            start_date=start_date,  # type: ignore
            end_date=end_date,  # type: ignore
            interval=interval,
        )

    def search(
        self,
        symbol: str = "",
        provider: PROVIDERS = "ssi",
    ) -> VfObject:
        """Etf Search. Search for an ETF ticker.

        An empty string (by default) returns the full list of currently listed ETFs.
        """

        provider_instance = self._get_provider(provider)
        return provider_instance.search(symbol=symbol)
