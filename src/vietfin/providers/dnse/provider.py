"""Dnse provider concrete class."""

from vietfin.abstract.interface import IEquityPrice, IEtf, IIndexPrice
from vietfin.abstract.vfobject import VfObject
from vietfin.providers.dnse.utils.equity_price_historical import historical


class EquityPriceDnse(IEquityPrice):
    """The concrete implementation of Equity.Price component with Dnse as provider."""

    def historical(
        self, symbol: str, start_date: str, end_date: str, interval: str
    ) -> VfObject:
        """Equity Historical price. Load stock historical price data for a specific ticker."""

        return historical(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            query_param="stock",
        )

    def quote(self, symbol: str, limit: int) -> VfObject:
        """Equity Quote. Load quote data for a specific ticker."""

        raise NotImplementedError(
            "equity.price.quote() command is not implemented for Dnse provider."
        )


class EtfDnse(IEtf):
    """The concrete implementation of Etf component with Dnse as provider."""

    def historical(
        self, symbol: str, start_date: str, end_date: str, interval: str
    ) -> VfObject:
        """ETF Historical price. Load historical price data of a specific ETF ticker.

        Use the same function equity_price_historical() as EquityPriceDnse.
        """

        return historical(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            query_param="stock",
        )

    def search(self, symbol: str) -> VfObject:
        raise NotImplementedError(
            "etf.search() command is not implemented for Dnse provider."
        )


class IndexPriceDnse(IIndexPrice):
    """The concrete implementation of Index.Price component with Dnse as provider."""

    def historical(
        self, symbol: str, start_date: str, end_date: str, interval: str
    ) -> VfObject:
        """Index Historical price. Load historical price data of a specific ticker.

        Use the same function equity_price_historical() as EquityPriceDnse.
        """
        return historical(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            query_param="index",
        )
