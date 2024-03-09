"""TCBS Equity Calendar Events Model."""

from bs4 import BeautifulSoup as bs
from pydantic import field_validator

from vietfin.abstract.data import Data
from vietfin.utils.helpers import ValidatedDatetime


class TcbsEquityCalendarEventsData(Data):
    """TCBS Equity Calendar Events Data."""

    __alias_dict__ = {
        "symbol": "ticker",
        "event_name": "eventName",
        "event_code": "eventCode",
        "price": "price",
        "price_change": "priceChange",
        "price_change_ratio": "priceChangeRatio",
        "event_desc": "eventDesc",
        "date_notify": "notifyDate",
        "date_execute": "exerDate",
        "date_register": "regFinalDate",
        "date_ex_right": "exRigthDate",
    }

    event_code: str  # Code of the event.
    event_name: str  # Name of the event.
    event_desc: str  # Description of the event.
    price: float | None  # Price of the stock.
    price_change: float | None  # Price change of the stock.
    price_change_ratio: float | None  # Price change ratio of the stock.
    date_notify: ValidatedDatetime | None  # Date of the notification sent to the public.
    date_execute: ValidatedDatetime | None  # Execution date of the event.
    date_register: ValidatedDatetime | None  # Registration date of the event.
    date_ex_right: ValidatedDatetime | None  # Ex-right date of the event.
    symbol: str  # Symbol representing the entity requested in the data.

    @field_validator("event_desc")
    @classmethod
    def parse_html(cls, v: str) -> str:
        """Parse HTML to text."""
        soup = bs(v, "html.parser")
        v = soup.get_text(separator="\n", strip=True)
        return v
