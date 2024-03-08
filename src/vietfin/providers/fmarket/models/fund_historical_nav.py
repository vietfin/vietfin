"""Fmarket Mutual Fund Historical NAV per Share Model."""

from datetime import date

from vietfin.abstract.data import Data


class FmarketFundHistoricalNavData(Data):
    """Fmarket Fund Historical NAV per Share Data."""

    __alias_dict__ = {
        "date_nav": "navDate",  # navDate is a date in string format 'YYYY-MM-DD'
        "nav_per_share": "nav",
        "fund_id": "productId",
    }

    date_nav: date
    nav_per_share: float
    fund_id: int
