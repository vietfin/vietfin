"""VNDIRECT Equity Discovery group of Models."""

from datetime import datetime

from vietfin.abstract.data import Data


class VndirectEquityDiscoveryData(Data):
    """VNDIRECT Equity Discovery Data. Most top mover stocks based on certain criteria."""

    __alias_dict__ = {
        "symbol": "code",
        "price": "lastPrice",
        "change": "priceChgCr1D",
        "percent_change": "priceChgPctCr1D",
        "volume": "totalVolumeAvgCr20D",
        "trading_value": "accumulatedVal",
        "updated_at": "lastUpdated",
    }

    symbol: str  # Symbol representing the stock satisfying the criteria.
    price: float  # Last price of the stock.
    change: float  # Change in price value.
    percent_change: float  # Percent change in price value.
    volume: float  # Trading volume averaged over 20 days.
    trading_value: float  # Trading value, i.e. price * volume, unit VND.
    updated_at: datetime  # Date and time of the last data update.
