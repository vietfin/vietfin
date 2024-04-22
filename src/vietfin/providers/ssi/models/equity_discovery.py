"""Ssi Equity Discovery group of Models."""

from vietfin.abstract.data import Data


class SsiEquityDiscoveryData(Data):
    """Ssi Equity Discovery Data. Most top mover stocks based on certain criteria."""

    __alias_dict__ = {
        "symbol": "ticker",
        "price": "price",
        "change": "priceChange",
        "percent_change": "percentPriceChange",
        "volume": "volume",
        "trading_value": "value",
        "industry": "sectorName",
    }

    symbol: str  # Symbol representing the stock satisfying the criteria.
    price: float  # Last price of the stock.
    change: float  # Change in price value.
    percent_change: float  # Percent change in price value.
    volume: int  # Trading volume.
    trading_value: float  # Trading value, i.e. price * volume
    industry: str  # Operating industry of the company.
