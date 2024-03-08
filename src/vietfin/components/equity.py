"""VietFin Equity class."""

from typing import Literal

from vietfin.abstract.vfobject import VfObject
from vietfin.abstract.factory import EquityFactory
from vietfin.abstract.interface import IEquity
from vietfin.components.equity_price import EquityPrice
from vietfin.components.equity_ownership import EquityOwnership
from vietfin.components.equity_calendar import EquityCalendar
from vietfin.components.equity_fundamental import EquityFundamental
from vietfin.components.equity_discovery import EquityDiscovery


class Equity:
    """VietFin Equity-related group of commands.

    This is the Client code in Factory Design Pattern.
    """

    # list of implemented providers
    PROVIDERS_S = Literal["ssi", "wifeed"]
    PROVIDERS_P = Literal["tcbs"]

    def __init__(self) -> None:
        self.price = EquityPrice()
        self.ownership = EquityOwnership()
        self.calendar = EquityCalendar()
        self.fundamental = EquityFundamental()
        self.discovery = EquityDiscovery()

    @staticmethod
    def _get_provider(provider: PROVIDERS_S | PROVIDERS_P) -> IEquity:
        provider_name = provider.lower()
        return EquityFactory().get_provider(provider_name)

    def search(
        self, symbol: str = "", provider: PROVIDERS_S = "ssi"
    ) -> VfObject:
        """Equity Search. Search for a stock ticker.

        An empty query (by default) returns the full list of listed companies from selected provider.
        """

        provider_instance = self._get_provider(provider)
        return provider_instance.search(symbol=symbol)

    def profile(self, symbol: str, provider: PROVIDERS_P = "tcbs") -> VfObject:
        """Equity Profile. Get general info of a stock sticker."""

        provider_instance = self._get_provider(provider)
        return provider_instance.profile(symbol=symbol)
