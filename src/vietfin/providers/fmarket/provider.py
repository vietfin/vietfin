"""Fmarket provider concrete class."""

from vietfin.abstract.interface import IFunds
from vietfin.abstract.vfobject import VfObject
from vietfin.providers.fmarket.utils.funds_search import search
from vietfin.providers.fmarket.utils.funds_historical import historical
from vietfin.providers.fmarket.utils.funds_holdings import holdings


class FundsFmarket(IFunds):
    """The concrete implementation of Funds component with Fmarket as provider."""

    def search(self, symbol: str) -> VfObject:
        """Funds Search. Search for a fund."""

        return search(symbol=symbol)

    def historical(
        self, symbol: str, start_date: str, end_date: str
    ) -> VfObject:
        """Funds Historical price. Load historical NAV for a specific fund."""

        return historical(
            symbol=symbol, start_date=start_date, end_date=end_date
        )

    def holdings(self, symbol: str) -> VfObject:
        """Funds Holdings. Load the top 10 holdings for a specific fund."""

        return holdings(symbol=symbol)
