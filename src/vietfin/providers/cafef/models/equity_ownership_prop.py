"""CafeF Equity Ownership Proprietary Trading Model."""

from datetime import date, datetime
from typing import Any

from pydantic import model_validator

from vietfin.abstract.data import Data


class CafefEquityOwnershipPropTradingData(Data):
    """CafeF Equity Ownership Proprietary Trading Data."""

    __alias_dict__ = {
        "date": "Date",
        "bid_volume": "KLcpMua",
        "bid_value": "GtMua",
        "ask_volume": "KlcpBan",
        "ask_value": "GtBan",
        "symbol": "Symbol",
    }

    date: date  # The date of the data
    bid_volume: int | None = None  # Bid volume. Khối lượng mua bởi khối tự doanh của các cty chứng khoán
    bid_value: int | None = None  # Bid value. Giá trị mua bởi khối tự doanh của các cty chứng khoán
    ask_volume: int | None = None  # Ask volume. Khối lượng bán bởi khối tự doanh của các cty chứng khoán
    ask_value: int | None = None  # Ask value. Giá trị bán bởi khối tự doanh của các cty chứng khoán
    symbol: str  # The stock ticker
    
    @model_validator(mode="before")
    @classmethod
    def parse_string(cls, data: Any) -> Any:
        """Before model validators are applied, parse the raw input.

        - convert the value of `Date` key from date string DD/MM/YYYY to date object.
        """

        if isinstance(data, dict):
            data["Date"] = datetime.strptime(data["Date"], "%d/%m/%Y").date()

        return data
