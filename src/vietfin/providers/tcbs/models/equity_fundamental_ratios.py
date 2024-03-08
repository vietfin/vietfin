"""TCBS Equity Fundamental Ratios Model."""

from pydantic import ConfigDict

from vietfin.abstract.data import Data


class TcbsEquityFundamentalRatiosData(Data):
    """TCBS Equity Fundamental Ratios Data."""

    __alias_dict__ = {
        "symbol": "ticker",
        "fiscal_year": "year",
        "fiscal_quarter": "quarter",
    }

    model_config = ConfigDict(
        extra="allow",
    )

    symbol: str  # Symbol representing the entity requested in the data.
    period: str  # Time period of the data to return.
    fiscal_year: int  # Fiscal year.
    fiscal_quarter: int  # Fiscal quarter.
