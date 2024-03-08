"""TCBS Equity Fundamental Dividends Model."""

from datetime import datetime
from pydantic import field_validator

from vietfin.abstract.data import Data


class TcbsEquityFundamentalDividendsData(Data):
    """TCBS Equity Fundamental Dividends Data."""

    __alias_dict__ = {
        "symbol": "ticker",
        "dividend_type": "issueMethod",
        "payment_date": "exerciseDate",
        "cash_dividend_percentage": "cashDividendPercentage",
    }

    symbol: str # Symbol representing the entity requested in the data.
    dividend_type: str  # Type of the dividend, i.e. cash, stock.
    payment_date: str | datetime  # The payment date of the dividend.
    cash_dividend_percentage: float  # I have no idea what this is.

    @field_validator("payment_date")
    @classmethod
    def parse_payment_date(cls, v: str) -> datetime:
        """Parse date from string format 'dd/mm/yy' to datetime."""
        return datetime.strptime(v, "%d/%m/%y")