"""SSI Equity Fundamental Income Model."""

from vietfin.abstract.data import Data


class SsiEquityFundamentalIncomeData(Data):
    """SSI Equity Fundamental Income Data."""

    __alias_dict__ = {
        "items": "ITEMS",
    }

    fiscal_period: str | None = None
    period: str  # Time period of the data to return.
    items: str  # Line item in the financial statement.
    values: float | None = None  # Value of the line item.
