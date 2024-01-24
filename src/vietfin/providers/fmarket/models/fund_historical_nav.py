"""Fmarket Mutual Fund Historical NAV per Share Model."""

from vietfin.standard_models.data import Data


class FmarketFundHistoricalNavData(Data):
    """Fmarket Fund Historical NAV per Share Data."""

    __alias_dict__ = {
        "date": "navDate",
        "nav_per_share": "nav",
        "fund_id": "productId",
    }

    date: str
    nav_per_share: float
    fund_id: int
