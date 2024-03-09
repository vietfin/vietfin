"""VietFin Index class."""

from typing import Literal

from vietfin.abstract.vfobject import VfObject
from vietfin.abstract.factory import IndexFactory, IndexPriceFactory
from vietfin.abstract.interface import IIndex, IIndexPrice
from vietfin.utils.helpers import INTERVALS


class IndexPrice:
    """VietFin Index.Price-related group of commands."""

    # list of implemented providers
    PROVIDERS = Literal["tcbs", "dnse"]

    @staticmethod
    def _get_provider(provider: PROVIDERS) -> IIndexPrice:
        provider_name = provider.lower()
        return IndexPriceFactory().get_provider(provider_name)

    def historical(
        self,
        symbol: str,
        start_date: str | None = None,
        end_date: str | None = None,
        interval: INTERVALS = "1d",
        provider: PROVIDERS = "tcbs",
    ) -> VfObject:
        """Index Historical price. Load historical price data for a specific index."""

        provider_instance = self._get_provider(provider)
        return provider_instance.historical(
            symbol=symbol,
            start_date=start_date,  # type: ignore
            end_date=end_date,  # type: ignore
            interval=interval,
        )


class Index:
    """VietFin Index-related group of commands.

    This is the Client code in Factory Design Pattern.
    """

    # list of implemented providers
    PROVIDERS = Literal["ssi"]

    def __init__(self) -> None:
        self.price = IndexPrice()

    @staticmethod
    def _get_provider(provider: PROVIDERS) -> IIndex:
        provider_name = provider.lower()
        return IndexFactory().get_provider(provider_name)

    def search(self, symbol: str = "", provider: PROVIDERS = "ssi") -> VfObject:
        """Index Search. Search for an index.

        An empty query (by default) returns the list of all available indexes from selected provider.
        """

        provider_instance = self._get_provider(provider)
        return provider_instance.search(symbol=symbol)

    def constituents(
        self, symbol: str, provider: PROVIDERS = "ssi"
    ) -> VfObject:
        """Index Constituents. Load the constituents for a specific index."""

        provider_instance = self._get_provider(provider)
        return provider_instance.constituents(symbol=symbol)
