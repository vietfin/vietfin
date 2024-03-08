"""SSI Index Constituents Model."""

from vietfin.abstract.data import Data


class SsiIndexConstituentsData(Data):
    """SSI Index Constituents Data."""

    __alias_dict__ = {
        "symbol": "ss",
        "name": "cv",
        "open": "o",
        "high": "h",
        "low": "l",
        "volume": "mtq",
        "prev_close": "pcp",
        "exchange": "e",
    }

    symbol: str  # Symbol representing the stock ticker.
    name: str  # Name of the constituent company in the index.
    open: float | None = None  # The open price.
    high: float | None = None  # The high price.
    low: float | None = None  # The low price.
    volume: int | None = None  # The trading volume.
    prev_close: float | None = None  # The previous close price.
    exchange: str  # The exchange where the stock is listed.
