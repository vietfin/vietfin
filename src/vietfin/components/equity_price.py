"""VietFin Equity.Price class."""

from typing import Literal

from vietfin.abstract.vfobject import VfObject
from vietfin.abstract.factory import EquityPriceFactory
from vietfin.abstract.interface import IEquityPrice
from vietfin.utils.helpers import INTERVALS


class EquityPrice:
    """VietFin Equity.Price-related group of commands.

    This is the Client code in Factory Design Pattern.
    """

    # list of implemented providers
    PROVIDERS = Literal["tcbs", "dnse", "ssi"]

    @staticmethod
    def _get_provider(provider: PROVIDERS) -> IEquityPrice:
        provider_name = provider.lower()
        return EquityPriceFactory().get_provider(provider_name)

    def historical(
        self,
        symbol: str,
        start_date: str | None = None,
        end_date: str | None = None,
        interval: INTERVALS = "1d",
        provider: PROVIDERS = "tcbs",
    ) -> VfObject:
        """Equity Historical price. Load stock historical price data for a specific ticker."""

        provider_instance = self._get_provider(provider)
        return provider_instance.historical(
            symbol=symbol,
            start_date=start_date,  # type: ignore
            end_date=end_date,  # type: ignore
            interval=interval,
        )

    def quote(
        self, symbol: str, limit: int = 100, provider: PROVIDERS = "tcbs"
    ) -> VfObject:
        """Equity Quote. Load quote data for a specific ticker."""

        provider_instance = self._get_provider(provider)
        return provider_instance.quote(
            symbol=symbol,
            limit=limit,
        )
