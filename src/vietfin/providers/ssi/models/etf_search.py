"""SSI Etf Search Model."""

from vietfin.abstract.data import Data


class SsiEtfSearchData(Data):
    """SSI Etf Search Data."""

    __alias_dict__ = {
        "symbol": "ss",
        "short_name": "cv",
        "inav": "ina",
        "open": "o",
        "high": "h",
        "low": "l",
        "volume": "mtq",
        "exchange": "e",
    }

    symbol: str  # Symbol of the ETF.
    short_name: str  # Short name of the ETF.
    inav: float  # Intraday indicative value of an ETF, giá trị tài sản ròng tham chiếu trên một chứng chỉ quỹ ETF.
    open: float | None = None  # Today open price.
    high: float | None = None  # Today high price.
    low: float | None = None  # Today low price.
    volume: int | None = None  # Today trading volume.
    exchange: str  # Name of the exchange where the ETF is listed.
