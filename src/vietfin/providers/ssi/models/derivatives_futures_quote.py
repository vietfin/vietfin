"""SSI Derivatives Futures Quote Model."""

from datetime import time, datetime, timezone, date
from typing import Any

from pydantic import model_validator, field_validator

from vietfin.abstract.data import Data


class SsiDerivativesFuturesQuoteData(Data):
    """SSI Derivatives Futures Quote Data."""

    __alias_dict__ = {
        "time": "time",
        "volume": "vol",
        "price": "price",
        "price_change": "priceChange",
        "price_change_percent": "priceChangePercent",
        "ref_price": "ref",
        "status": "side",
        "symbol": "stockSymbol",
        "id": "_id",
    }

    date_session: date  # Date of the session of the quote.
    time: time  # Time of the quote execution.
    symbol: str  # Unique identifier representing the futures contract.
    volume: int  # Volume of contracts in the quote.
    price: float  # Price of the quote.
    status: str  # Buy or Sell or Unfilled. Convey the idea that the order has been fulfilled (executed) or not.
    price_change: float  # Change in price from the session's reference price, in absolute value.
    price_change_percent: float  # Change in price from the current reference price, in percent.
    ref_price: float  # Reference or opening price for the trading session.
    id: str  # Unique identifier representing the quote.

    @model_validator(mode="before")
    @classmethod
    def parse_string(cls, data: Any) -> Any:
        """Before model validators are applied, parse the value of `_id` key.

        The value of `_id` key is in the format of `HHmmssxxxxxxxxx` where
        - HH is the hour of the quote execution.
        - mm is the minute
        - ss is the second
        - xxxxxxxx is the Unix timestamp in milliseconds of the quote execution.
        """
        if isinstance(data, dict):
            # ignore the first six characters of the value of `_id` key
            id_substring = data["_id"][6:]
            try:
                # Convert the extracted substring into a date object
                timestamp_milliseconds = int(id_substring)
                data["date_session"] = datetime.fromtimestamp(
                    timestamp_milliseconds / 1000, tz=timezone.utc
                ).date()
            except ValueError:
                print("Error: Unable to convert substring to timestamp.")

        return data

    @field_validator("status")
    def parse_status_string(cls, v: str) -> str:
        """Parse the value of `status` key.

        The value of `status` key is in the list of ["bu", "sd", "unknown"]
        - "bu" (may be abbreviated as "buy up") means that the quote is a Buy order and is fulfilled.
        - "sd" (may be abbreviated as "sell down") means that the quote is a Sell order and is fulfilled.
        - "unknown" means that the quote is not fulfilled.
        """

        # Mapping from the API's values to the user-friendly strings
        status_mappings = {
            "bu": "Buy",
            "sd": "Sell",
            "unknown": "Unfilled",
        }

        v = v.lower()
        if v not in status_mappings:
            defined_status = ", ".join(status_mappings.keys())
            raise ValueError(
                f"Unknown status: {v}. Predefined values are [{defined_status}]."
            )

        return status_mappings[v]
