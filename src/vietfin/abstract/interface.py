"""VietFin abstract interface."""

from abc import ABC, abstractmethod
from typing import Any

from vietfin.abstract.vfobject import VfObject


class IFunds(ABC):
    """Abstract Interface for Funds component."""

    @abstractmethod
    def search(self, symbol: str) -> VfObject:
        """Funds Search. Search for a fund."""
        pass

    @abstractmethod
    def historical(
        self, symbol: str, start_date: Any, end_date: Any
    ) -> VfObject:
        """Funds Historical price. Load historical NAV for a specific fund."""
        pass

    @abstractmethod
    def holdings(self, symbol: str) -> VfObject:
        """Funds Holdings. Load the top 10 holdings for a specific fund."""
        pass


class IEquity(ABC):
    """Interface for Equity component."""

    @abstractmethod
    def search(self, symbol: str) -> VfObject:
        """Equity Search. Search for a stock ticker."""
        pass

    @abstractmethod
    def profile(self, symbol: str) -> VfObject:
        """Equity Profile. Get general info of a stock sticker."""
        pass


class IEquityPrice(ABC):
    """Interface for Equity Price component."""

    @abstractmethod
    def historical(
        self, symbol: str, start_date: Any, end_date: Any, interval: str
    ) -> VfObject:
        """Equity Price Historical. Load historical price data for a specific ticker."""
        pass

    @abstractmethod
    def quote(self, symbol: str, limit: int) -> VfObject:
        """Equity Price Quote. Load quote data for a specific ticker."""
        pass


class IEquityOwnership(ABC):
    """Interface for Equity Ownership component."""

    @abstractmethod
    def insider_trading(self, symbol: str, limit: int) -> VfObject:
        """Equity Ownership Insider Trading. Load insider trading data for a specific ticker."""
        pass

    @abstractmethod
    def major_holders(self, symbol: str) -> VfObject:
        """Equity Ownership Major Holders. Load major holders data for a specific ticker."""
        pass

    @abstractmethod
    def foreign_trading(self, symbol: str, start_date: Any, end_date: Any) -> VfObject:
        """Equity Ownership Foreign Trading. Load the trading data of foreign entities for a specific ticker."""
        pass

    @abstractmethod
    def prop_trading(self, symbol: str, start_date: Any, end_date: Any) -> VfObject:
        """Equity Ownership Proprietary trading. Load the trading data of proprietary trading firms for a specific ticker."""
        pass



class IEquityCalendar(ABC):
    """Interface for Equity Calendar component."""

    @abstractmethod
    def events(self, symbol: str, limit: int) -> VfObject:
        """Equity Calendar Events. Load Historical All-event-type Calendar data for a specific ticker."""
        pass


class IEquityFundamental(ABC):
    """Interface for Equity Fundamental component."""

    @abstractmethod
    def management(self, symbol: str) -> VfObject:
        """Equity Fundamental Management. Load Key executives data for a specific ticker."""
        pass

    @abstractmethod
    def ratios(self, symbol: str, period: Any) -> VfObject:
        """Equity Fundamental Ratios. Load Financial ratios data for a specific ticker."""
        pass

    @abstractmethod
    def dividends(self, symbol: str, limit: int) -> VfObject:
        """Equity Fundamental Dividends. Load Historical dividends data for a specific ticker."""
        pass

    @abstractmethod
    def income(self, symbol: str, period: Any) -> VfObject:
        """Equity Fundamental Income. Load Historical income statement data for a specific ticker."""
        pass
    
    @abstractmethod
    def balance(self, symbol: str, period: Any) -> VfObject:
        """Equity Fundamental Balance. Load Historical balance sheet statement data for a specific ticker."""
        pass
    
    @abstractmethod
    def cash(self, symbol: str, period: Any) -> VfObject:
        """Equity Fundamental Cash. Load Historical cash flow statement data for a specific ticker."""
        pass

    @abstractmethod
    def multiples(self, symbol: str, period: Any) -> VfObject:
        """Equity Fundamental Multiples. Load Historical valuation multiples data for a specific ticker."""
        pass

class IEquityDiscovery(ABC):
    """Interface for Equity Discovery component."""

    @abstractmethod
    def active(self, exchange: Any) -> VfObject:
        """Equity Discovery Active. Load the list of most active stocks based on trading value."""
        pass

    @abstractmethod
    def gainers(self, exchange: Any) -> VfObject:
        """Equity Discovery Gainers. Load the list of top gainer stocks."""

    @abstractmethod
    def losers(self, exchange: Any) -> VfObject:
        """Equity Discovery Losers. Load the list of top loser stocks."""
        pass


class IDerivativesFutures(ABC):
    """Interface for Derivatives Futures component."""

    @abstractmethod
    def historical(
        self, symbol: str, start_date: Any, end_date: Any
    ) -> VfObject:
        """Derivatives Futures Historical. Load historical price data for a specific futures contract."""
        pass

    @abstractmethod
    def quote(self, symbol: str, limit: int) -> VfObject:
        """Derivatives Futures Quote. Load quote data for a specific futures contract."""
        pass

    @abstractmethod
    def search(self, symbol: str) -> VfObject:
        """Derivatives Futures Search. Search for a specific futures contract."""
        pass


class IIndex(ABC):
    """Interface for Index component."""

    @abstractmethod
    def search(self, symbol: str) -> VfObject:
        """Index Search. Search for an index."""
        pass

    @abstractmethod
    def constituents(self, symbol: str) -> VfObject:
        """Index Constituents. Load the constituents for a specific index."""
        pass


class IIndexPrice(ABC):
    """Interface for Index Price component."""

    @abstractmethod
    def historical(self, symbol: str, start_date: Any, end_date: Any, interval: Any) -> VfObject:
        """Index Price Historical. Load historical price data for a specific index."""
        pass


class IEtf(ABC):
    """Interface for Etf component."""

    @abstractmethod
    def historical(
        self, symbol: str, start_date: Any, end_date: Any, interval: Any
    ) -> VfObject:
        """Etf Price Historical. Load historical price data for a specific ETF ticker."""
        pass

    @abstractmethod
    def search(self, symbol: str) -> VfObject:
        """Etf Search. Search for an ETF ticker."""
        pass

class INews(ABC):
    """Interface for News component."""

    @abstractmethod
    def company(self, symbol: str, limit: int) -> VfObject:
        """News Company. Load company news data for a specific ticker."""
        pass
