"""TCBS Equity Historical Price Model."""

from datetime import date

from vietfin.abstract.data import Data


class TcbsEquityHistoricalPriceData(Data):
    """TCBS Equity Historical Price Data."""

    __alias_dict__ = {
        "date": "tradingDate",
        "open": "open",
        "high": "high",
        "low": "low",
        "close": "close",
        "volume": "volume",
    }

    date: date  # The date of the data.
    open: float  # The open price.
    high: float  # The high price.
    low: float  # The low price.
    close: float  # The close price.
    volume: int | float  # The trading volume.
