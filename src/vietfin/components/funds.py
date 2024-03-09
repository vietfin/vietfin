"""VietFin Funds class."""

from typing import Literal

from vietfin.abstract.vfobject import VfObject
from vietfin.abstract.factory import FundsFactory
from vietfin.abstract.interface import IFunds


class Funds:
    """VietFin Funds-related group of commands.

    This is the Client code in Factory Design Pattern.
    """

    # list of implemented providers
    PROVIDERS = Literal["fmarket"]

    @staticmethod
    def _get_provider(provider: PROVIDERS) -> IFunds:
        provider_name = provider.lower()
        return FundsFactory().get_provider(provider_name)

    def search(
        self, symbol: str = "", provider: PROVIDERS = "fmarket"
    ) -> VfObject:
        """Funds Search. Search for a fund.

        An empty query (by default) returns the list of all funds from selected provider.
        """

        provider_instance = self._get_provider(provider)
        return provider_instance.search(symbol=symbol)

    def historical(
        self,
        symbol: str,
        start_date: str | None = None,
        end_date: str | None = None,
        provider: PROVIDERS = "fmarket",
    ) -> VfObject:
        """Funds Historical price. Load historical NAV for a specific fund."""

        provider_instance = self._get_provider(provider)
        return provider_instance.historical(
            symbol=symbol,
            start_date=start_date,  # type: ignore
            end_date=end_date,  # type: ignore
        )

    def holdings(
        self, symbol: str, provider: PROVIDERS = "fmarket"
    ) -> VfObject:
        """Funds Holdings. Load the top 10 holdings for a specific fund."""

        provider_instance = self._get_provider(provider)
        return provider_instance.holdings(symbol=symbol)
