"""WiFeed provider concrete class."""

from vietfin.abstract.interface import IEquity
from vietfin.abstract.vfobject import VfObject
from vietfin.providers.wifeed.utils.equity_search import search


class EquityWifeed(IEquity):
    """The concrete implementation of Equity component with WiFeed as provider."""

    def search(self, symbol: str) -> VfObject:
        """Equity Search. Search for a stock ticker."""

        return search(symbol=symbol)
    
    def profile(self, symbol: str) -> VfObject:
        """Equity Profile. Get general info of a stock sticker."""

        raise NotImplementedError("equity.profile() command is not implemented for WiFeed provider.")