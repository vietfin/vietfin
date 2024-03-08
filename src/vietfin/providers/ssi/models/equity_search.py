"""SSI Equity Search Model."""

from vietfin.abstract.data import Data


class SsiEquitySearchData(Data):
    """SSI Equity Search Data."""

    __alias_dict__ = {
        "symbol": "ticker",
        "name": "organName",
        "short_name": "organShortName",
        "organ_code": "organCode",
    }

    symbol: str  # Symbol of the stock ticker
    name: str  # Legal name of the company
    short_name: str  # Short name of the company
    organ_code: str  # Organization code of the company in SSI database