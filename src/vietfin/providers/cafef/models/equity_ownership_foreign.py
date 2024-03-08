"""CafeF Equity Ownership Foreign Trading Model."""

from datetime import date, datetime
from typing import Any
import re

from pydantic import model_validator

from vietfin.abstract.data import Data


class CafefEquityOwnershipForeignTradingData(Data):
    """CafeF Equity Ownership Foreign Trading Data."""

    __alias_dict__ = {
        "date": "Ngay",
        "net_trading_volume": "KLGDRong",
        "net_trading_value": "GTDGRong",
        "bid_volume": "KLMua",
        "bid_value": "GtMua",
        "ask_volume": "KLBan",
        "ask_value": "GtBan",
        "remaining_room": "RoomConLai",
        "weight": "DangSoHuu",
    }

    date: date  # The date of the data.
    net_trading_volume: int | None = None  # Net trading volume. Khối lượng giao dịch ròng.
    net_trading_value: int | None = None  # Net trading value. Giá trị giao dịch ròng.
    bid_volume: int | None = None  # Bid volume. Khối lượng mua bởi nhà đầu tư nước ngoài.
    bid_value: int | None = None  # Bid value. Giá trị mua bởi nhà đầu tư nước ngoài.
    ask_volume: int | None = None  # Ask volume. Khối lượng bán bởi nhà đầu tư nước ngoài.
    ask_value: int | None = None  # Ask value. Giá trị bán bởi nhà đầu tư nước ngoài.
    remaining_room: int | None = None  # Remaining room. Khối lượng còn lại mà nhà đầu tư nước ngoài có thể sở hữu.
    weight: float | None = None  # Current Ownership Percent. Tỷ lệ % sở hữu hiện tại của nhà đầu tư nước ngoài.
    close_price: float | None = None  # Current daily close price of the stock ticker.
    percent_change: float | None = None  # Percent change of the stock ticker compared to previous session.
    
    @model_validator(mode="before")
    @classmethod
    def parse_string(cls, data: Any) -> Any:
        """Before model validators are applied, parse the raw input.

        - convert the value of `Ngay` key from date string DD/MM/YYYY to date object.
        - parse the value of `ThayDoi` key from string (e.g. "76.1(-2.65 %)") into two separate keys: close_price and percent_change.
        """

        if isinstance(data, dict):
            data["Ngay"] = datetime.strptime(data["Ngay"], "%d/%m/%Y").date()

            # Use regular expressions to extract close_price, percent_change and add them as two new keys to the data dict.
            match = re.match(r'([\d.]+)\(([-\d.]+) %\)', data["ThayDoi"])
            if match:
                data["close_price"] = float(match.group(1))
                data["percent_change"] = float(match.group(2))
            else:
                data["close_price"] = None
                data["percent_change"] = None
        return data
