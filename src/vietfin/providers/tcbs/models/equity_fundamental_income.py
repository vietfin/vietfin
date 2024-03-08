"""TCBS Equity Fundamental Income Model."""

from pydantic import field_validator

from vietfin.abstract.data import Data


class TcbsEquityFundamentalIncomeData(Data):
    """TCBS Equity Fundamental Income statement Data."""

    __alias_dict__ = {
        "symbol": "ticker",
        "fiscal_year": "year",
        "fiscal_quarter": "quarter",
        "items": "ITEMS",
    }

    fiscal_year: int  # Fiscal year.
    fiscal_quarter: int  # Fiscal quarter.
    period: str  # Time period of the data to return.
    items: str  # Line item in the financial statement.
    values: float | None = None  # Value of the line item.
    symbol: str  # Symbol representing the entity requested in the data.

    @field_validator("items")
    @classmethod
    def parse_txt(cls, v: str) -> str:
        """Parse text from provided source into user-friendly format.
        
        Return the user-friendly string for the line item.
        Return as is if no mapping is found.
        This string mapping is based on my own experiences.
        """

        str_map = {
            # Income statement:
            "grossProfit": "gross profit",
            "operationIncome": "total operating income",
            "operationExpense": "total operating expenses",
            "interestExpense": "total interest expense",
            # Balance sheet:
            "cash": "cash and cash equivalents",
            "asset": "total assets",
            "equity": "total equity",
            "debt": "total debt",
            # Cashflow statement:
            "fromSale": "net cash from operating activities",
            "fromInvest": "net cash from investing activities",
            "fromFinancial": "net cash from financing activities",
            "freeCashFlow": "free cash flow",
        }

        return str_map.get(v, v)
