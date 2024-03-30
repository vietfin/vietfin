"""SSI Derivatives Futures Search Model."""

from datetime import date, datetime
from typing import Any

from pydantic import model_validator

from vietfin.abstract.data import Data


class SsiDerivativesFuturesSearchData(Data):
    """SSI Derivatives Futures Search Data."""

    __alias_dict__ = {
        "symbol": "ss",
        "expiration_date": "md",
        "initial_date": "ltd",
        "price": "mp",
        "volume": "mv",
        "asset": "us",
    }

    symbol: str  # Symbol of the futures contract.
    expiration_date: date  # Expiration (a.k.a maturity or expiry date) refers to the last trading day of the futures contract. Ngày đáo hạn hợp đồng.
    initial_date: date  # Refers to the first trading day of the futures contract. Ngày giao dịch đầu tiên.
    price: float  # Matched price. Giá khớp lệnh.
    volume: int  # Matched volume. Khối lượng khớp lệnh.
    asset: str  # Underlying asset. Tài sản cơ sở của hợp đồng tương lai.

    @model_validator(mode="before")
    @classmethod
    def parse_string(cls, data: Any) -> Any:
        """Before model validators are applied, parse the raw input.

        - convert the value of `md` and `ltd` key from date string DD/MM/YYYY to date object.
        """

        if isinstance(data, dict):
            data["md"] = datetime.strptime(data["md"], "%d/%m/%Y").date()
            data["ltd"] = datetime.strptime(data["ltd"], "%d/%m/%Y").date()

        return data
