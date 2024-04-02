"""Ssi provider concrete class."""

from typing import Any
from vietfin.abstract.interface import (
    IEquity,
    IIndex,
    IEquityDiscovery,
    IEquityFundamental,
    IEtf,
    IEquityPrice,
    IDerivativesFutures,
)
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import PERIODS, EXCHANGE_NAMES
from vietfin.providers.ssi.utils.equity_search import search as equity_search
from vietfin.providers.ssi.utils.index_search import search as index_search
from vietfin.providers.ssi.utils.equity_discovery import (
    get_top_movers,
)
from vietfin.providers.ssi.utils.etf_search import search as etf_search
from vietfin.providers.ssi.utils.etf_historical import historical
from vietfin.providers.ssi.utils.index_constituents import constituents
from vietfin.providers.ssi.utils.equity_fundamental_income import (
    get_financial_report,
)
from vietfin.providers.ssi.utils.derivatives_futures_search import (
    search as futures_search,
)
from vietfin.providers.ssi.utils.derivatives_futures_quote import (
    quote as futures_quote,
)


class EquitySsi(IEquity):
    """The concrete implementation of Equity component with Ssi as provider."""

    def search(self, symbol: str) -> VfObject:
        """Equity Search. Search for a stock ticker."""

        return equity_search(symbol=symbol)

    def profile(self, symbol: str) -> VfObject:
        """Equity Profile. Get general info of a stock sticker."""

        raise NotImplementedError(
            "equity.profile() command is not implemented for SSI provider."
        )


class EquityPriceSsi(IEquityPrice):
    """The concrete implementation of Equity.Price component with Ssi as provider."""

    def quote(self, symbol: str, limit: int) -> VfObject:
        raise NotImplementedError(
            "equity.price.quote() command is not implemented for SSI provider."
        )

    def historical(
        self, symbol: str, start_date: str, end_date: str, interval: Any
    ) -> VfObject:
        """Equity Historical price. Load stock historical price data for a specific ticker.

        Use the same historical() function from module etf_historical.
        """
        return historical(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
        )


class EquityDiscoverySsi(IEquityDiscovery):
    """The concrete implementation of Equity Discovery component with Ssi as provider."""

    def active(self, exchange: EXCHANGE_NAMES) -> VfObject:
        """Equity Discovery Active. Load the list of most active stocks based on trading value."""
        return get_top_movers(name="value", exchange=exchange)

    def gainers(self, exchange: EXCHANGE_NAMES) -> VfObject:
        """Equity Discovery Gainers. Load the list of top gainer stocks."""
        return get_top_movers(name="gainers", exchange=exchange)

    def losers(self, exchange: EXCHANGE_NAMES) -> VfObject:
        """Equity Discovery Losers. Load the list of top loser stocks."""
        return get_top_movers(name="losers", exchange=exchange)


class EquityFundamentalSsi(IEquityFundamental):
    """The concrete implementation of Equity.Fundamental component with Ssi as provider."""

    def management(self, symbol: str) -> VfObject:
        """Equity Fundamental Management. Load Key executives data for a specific ticker."""
        raise NotImplementedError(
            "equity.fundamental.management() command is not implemented for SSI provider."
        )

    def ratios(self, symbol: str, period: PERIODS) -> VfObject:
        """Equity Fundamental Ratios. Load Financial ratios data for a specific ticker."""
        raise NotImplementedError(
            "equity.fundamental.ratios() command is not implemented for SSI provider."
        )

    def dividends(self, symbol: str, limit: int) -> VfObject:
        """Equity Fundamental Dividends. Load Historical dividends data for a specific ticker."""
        raise NotImplementedError(
            "equity.fundamental.dividends() command is not implemented for SSI provider."
        )

    def income(self, symbol: str, period: PERIODS) -> VfObject:
        """Equity Fundamental Income. Load Historical income statement data for a specific ticker."""
        return get_financial_report(symbol=symbol, period=period, name="income")

    def balance(self, symbol: str, period: PERIODS) -> VfObject:
        """Equity Fundamental Balance. Load Historical balance sheet statement data for a specific ticker."""
        return get_financial_report(
            symbol=symbol, period=period, name="balance"
        )

    def cash(self, symbol: str, period: PERIODS) -> VfObject:
        """Equity Fundamental Cash. Load Historical cash flow statement data for a specific ticker."""
        return get_financial_report(symbol=symbol, period=period, name="cash")

    def multiples(self, symbol: str, period: PERIODS) -> VfObject:
        """Equity Fundamental Multiples. Load Historical valuation multiples data for a specific ticker."""
        raise NotImplementedError(
            "equity.fundamental.multiples() command is not implemented for SSI provider."
        )


class IndexSsi(IIndex):
    """The concrete implementation of Index component with Ssi as provider."""

    def search(self, symbol: str) -> VfObject:
        """Index Search. Search for an index."""

        return index_search(symbol=symbol)

    def constituents(self, symbol: str) -> VfObject:
        """Index Constituents. Load the constituents for a specific index."""

        return constituents(symbol=symbol)


class EtfSsi(IEtf):
    """The concrete implementation of Etf component with Ssi as provider."""

    def search(self, symbol: str) -> VfObject:
        return etf_search(symbol=symbol)

    def historical(
        self, symbol: str, start_date: str, end_date: str, interval: Any
    ) -> VfObject:
        return historical(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
        )


class DerivativesFuturesSsi(IDerivativesFutures):
    """The concrete implementation of Derivatives.Futures component with VietStock as provider."""

    def historical(
        self, symbol: str, start_date: str, end_date: str
    ) -> VfObject:
        """Derivatives Futures Historical. Load historical price data for a specific futures contract."""

        raise NotImplementedError(
            "derivatives.futures.historical() command is not implemented for SSI provider."
        )

    def quote(self, symbol: str, limit: int, cookie: str = "") -> VfObject:
        """Derivatives Futures Quote. Load quote data for a specific futures contract."""

        return futures_quote(symbol=symbol, limit=limit)

    def search(self, symbol: str) -> VfObject:
        """Derivatives Futures Search. Search for a specific futures contract."""

        return futures_search(symbol=symbol)
