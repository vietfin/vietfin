"""SSI Etf Historical Model."""

from datetime import date, datetime, timezone
from typing import Any

from pydantic import field_validator, model_validator

from vietfin.abstract.data import Data


class SsiEtfHistoricalData(Data):
    """SSI Etf Historical Data."""

    __alias_dict__ = {
        "date": "t",
        "open": "o",
        "high": "h",
        "low": "l",
        "close": "c",
        "volume": "v",
    }

    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int

    @model_validator(mode="before")
    @classmethod
    def parse_unix_timestamp(cls, data: Any) -> Any:
        """Before model validators are applied, parse the raw input, convert the value of `t` key from unix timestamp to date."""
        if isinstance(data, dict):
            data["t"] = datetime.fromtimestamp(data["t"], tz=timezone.utc).date()
        return data

    @field_validator("open", "high", "low", "close")
    @classmethod
    def multiply_1k(cls, value: float) -> float:
        """Multiply the price value by 1000."""
        return value * 1000
    