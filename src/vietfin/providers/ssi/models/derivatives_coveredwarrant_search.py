"""SSI Derivatives Covered Warrant Search Model."""

from datetime import date, datetime
from typing import Any

from pydantic import model_validator

from vietfin.abstract.data import Data


class SsiDerivativesCoveredwarrantSearchData(Data):
    """SSI Derivatives Covered Warrant Search Data."""

    __alias_dict__ = {
        "symbol": "ss",
        "expiration_date": "md",
        "last_trading_date": "ltd",
        "issuer": "isn",
        "underlying_asset": "us",
        "strike_price": "ep",
        "close_price": "mp",
        "price_change": "pc",
        "price_change_pct": "cp",
        "volume": "mtq",
        "conversion_ratio": "er",
    }

    symbol: str  # Symbol of the covered warrant. Mã chứng quyền có đảm bảo.
    expiration_date: date  # The expiry (a.k.a maturity) date of the covered warrant. Ngày đáo hạn.
    last_trading_date: date  # The last trading day of the covered warrant. Ngày giao dịch cuối cùng.
    issuer: str  # Identification code of the issuer (financial institution). Tổ chức phát hành.
    underlying_asset: str  # Underlying asset of the covered warrant. Chứng khoán cơ sở.
    strike_price: float  # Strike price. Giá thực hiện.
    close_price: float  # Close price. Giá chứng quyền.
    price_change: float  # Price change compared to the previous trading day. Giá thay đổi.
    price_change_pct: float  # Price change percentage. Giá thay đổi theo phần trăm.
    volume: int | None = None  # Matched volume. Khối lượng khớp lệnh.
    conversion_ratio: str  # Conversion ratio of the covered warrant. Tỷ lệ chuyển đổi.

    @model_validator(mode="before")
    @classmethod
    def parse_string(cls, data: Any) -> Any:
        """Before model validators are applied, parse the raw input.

        - convert the value of `md` and `ltd` key from date string YYYYMMDD to date object.
        """

        if isinstance(data, dict):
            data["md"] = datetime.strptime(data["md"], "%Y%m%d").date()
            data["ltd"] = datetime.strptime(data["ltd"], "%Y%m%d").date()

        return data
