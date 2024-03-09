"""TCBS Equity Price Quote Model."""

from datetime import time

from vietfin.abstract.data import Data


class TcbsEquityPriceQuoteData(Data):
    """TCBS Equity Price Quote Data."""

    __alias_dict__ = {
        "time": "t",
        "price": "p",
        "volume": "v",
        "average_price": "ap",
        "order_type": "a",
        "order_count": "n",
        "investor_type": "type",
        "prev_price_change": "pcp",
    }

    time: time
    price: float | None = None
    volume: int | None = None
    average_price: float | None = None
    order_type: str | None = None
    order_count: int | None = None
    investor_type: str | None = None
    prev_price_change: float | None = None
