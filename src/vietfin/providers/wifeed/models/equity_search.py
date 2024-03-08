"""WiFeed Equity Search Model."""

from vietfin.abstract.data import Data


class WifeedEquitySearchData(Data):
    """WiFeed Equity Search Data."""

    __alias_dict__ = {
        "symbol": "code",
        "name": "fullname_vi",
        "exchange": "san",
    }

    symbol: str
    name: str
    exchange: str
