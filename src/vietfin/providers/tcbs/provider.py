"""Tcbs provider concrete class."""

from vietfin.abstract.interface import (
    IEquity,
    IEquityPrice,
    IEquityOwnership,
    IEquityCalendar,
    IEquityFundamental,
    IDerivativesFutures,
    IEtf,
    INews,
    IIndexPrice,
)
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import PERIODS
from vietfin.providers.tcbs.utils.equity_price_historical import historical
from vietfin.providers.tcbs.utils.equity_price_quote import quote
from vietfin.providers.tcbs.utils.equity_profile import profile
from vietfin.providers.tcbs.utils.equity_ownership_insider_trading import (
    insider_trading,
)
from vietfin.providers.tcbs.utils.equity_ownership_major_holders import (
    major_holders,
)
from vietfin.providers.tcbs.utils.equity_calendar_events import events
from vietfin.providers.tcbs.utils.news_company import company
from vietfin.providers.tcbs.utils.equity_fundamental_management import (
    management,
)
from vietfin.providers.tcbs.utils.equity_fundamental_ratios import ratios
from vietfin.providers.tcbs.utils.equity_fundamental_dividends import dividends
from vietfin.providers.tcbs.utils.equity_fundamental_income import (
    get_financial_report,
)


class EquityTcbs(IEquity):
    """The concrete implementation of Equity component with Tcbs as provider."""

    def search(self, symbol: str) -> VfObject:
        """Equity Search. Search for a stock ticker."""
        raise NotImplementedError(
            "equity.search() command is not implemented for TCBS provider."
        )

    def profile(self, symbol: str) -> VfObject:
        """Equity Profile. Get general info of a stock sticker."""
        return profile(symbol=symbol)


class EquityPriceTcbs(IEquityPrice):
    """The concrete implementation of Equity.Price component with Tcbs as provider."""

    def historical(
        self, symbol: str, start_date: str, end_date: str, interval: str
    ) -> VfObject:
        """Equity Historical price. Load stock historical price data of a specific ticker."""
        return historical(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            api_endpoint="stock",
            query_param="stock",
        )

    def quote(self, symbol: str, limit: int) -> VfObject:
        """Equity Quote. Load quote data of a specific ticker."""
        return quote(symbol=symbol, limit=limit)


class EquityOwnershipTcbs(IEquityOwnership):
    """The concrete implementation of Equity.Ownership component with Tcbs as provider."""

    def insider_trading(self, symbol: str, limit: int) -> VfObject:
        """Equity Insider Trading. Load insider trading data of a specific ticker."""
        return insider_trading(symbol=symbol, limit=limit)

    def major_holders(self, symbol: str) -> VfObject:
        """Equity Major Holders. Load major holders data of a specific ticker."""
        return major_holders(symbol=symbol)

    def foreign_trading(self, symbol: str) -> VfObject:
        """Equity Ownership Foreign Trading. Load the trading data of foreign entities for a specific ticker."""
        raise NotImplementedError(
            "equity.ownership.foreign_trading() command is not implemented for Tcbs provider."
        )
    
    def prop_trading(self, symbol: str) -> VfObject:
        """Equity Ownership Proprietary trading. Load the trading data of proprietary trading firms for a specific ticker."""
        raise NotImplementedError(
            "equity.ownership.prop_trading() command is not implemented for Tcbs provider."
        )


class EquityCalendarTcbs(IEquityCalendar):
    """The concrete implementation of Equity.Calendar component with Tcbs as provider."""

    def events(sefl, symbol: str, limit: int) -> VfObject:
        """Equity Calendar Events. Load Historical All-event-type Calendar data for a specific ticker."""
        return events(symbol=symbol, limit=limit)


class EquityFundamentalTcbs(IEquityFundamental):
    """The concrete implementation of Equity.Fundamental component with Tcbs as provider."""

    def management(self, symbol: str) -> VfObject:
        """Equity Fundamental Management. Load Key executives data for a specific ticker."""
        return management(symbol=symbol)

    def ratios(self, symbol: str, period: PERIODS) -> VfObject:
        """Equity Fundamental Ratios. Load Financial ratios data for a specific ticker."""
        return ratios(symbol=symbol, period=period)

    def dividends(self, symbol: str, limit: int) -> VfObject:
        """Equity Fundamental Dividends. Load Historical dividends data for a specific ticker."""
        return dividends(symbol=symbol, limit=limit)

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
            "equity.fundamental.multiples() command is not implemented for TCBS provider."
        )


class DerivativesFuturesTcbs(IDerivativesFutures):
    """The concrete implementation of Derivatives.Futures component with Tcbs as provider."""

    def historical(
        self, symbol: str, start_date: str, end_date: str
    ) -> VfObject:
        """Derivatives Futures Historical. Load historical price of a specific contract symbol.

        Use the logic of function historical() of EquityPriceTcbs.
        """
        return historical(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            interval="1d",
            api_endpoint="futures",
            query_param="derivative",
        )

    def quote(self, symbol: str, limit: int, cookie: str) -> VfObject:
        """Equity Quote. Load quote data of a specific ticker."""
        raise NotImplementedError(
            "equity.price.quote() command is not implemented for Tcbs provider."
        )


class EtfTcbs(IEtf):
    """The concrete implementation of ETF component with Tcbs as provider."""

    def historical(
        self, symbol: str, start_date: str, end_date: str, interval: str
    ) -> VfObject:
        """ETF Historical price. Load historical price data of a specific ticker.

        Use the logic of function historical() of EquityPriceTcbs.
        """
        return historical(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            api_endpoint="stock",
            query_param="stock",
        )

    def search(self, symbol: str) -> VfObject:
        raise NotImplementedError(
            "etf.search() command is not implemented for TCBS provider."
        )


class NewsTcbs(INews):
    """The concrete implementation of News component with Tcbs as provider."""

    def company(self, symbol: str, limit: int) -> VfObject:
        """News Company. Load company news data of a specific ticker."""
        return company(symbol=symbol, limit=limit)


class IndexPriceTcbs(IIndexPrice):
    """The concrete implementation of Index.Price component with Tcbs as provider."""

    def historical(
        self, symbol: str, start_date: str, end_date: str, interval: str
    ) -> VfObject:
        """Index Historical price. Load historical price data of a specific ticker.

        Use the logic of function historical() of EquityPriceTcbs.
        """
        return historical(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            api_endpoint="stock",
            query_param="index",
        )
