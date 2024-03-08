"""TCBS News Company Model."""

from datetime import datetime

from vietfin.abstract.data import Data


class TcbsNewsCompanyData(Data):
    """TCBS News Company Data."""

    __alias_dict__ = {
        "symbol": "ticker",
        "date_published": "publishDate",
        "source": "source",
        "title": "title",
        "price": "price",
        "price_change": "priceChange",
        "price_change_ratio": "priceChangeRatio",
    }

    date_published: datetime  # Date and time when the news article was published.
    title: str  # Title of the news article.
    source: str | None  # Source of the news article.
    price: float | None  # Price of the stock at that moment.
    price_change: float | None  # Price change of the stock.
    price_change_ratio: float | None  # Price change ratio of the stock.
    symbol: str  # Symbol representing the entity requested in the data.
