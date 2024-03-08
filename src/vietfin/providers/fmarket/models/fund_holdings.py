"""Fmarket Mutual Fund Top Holdings Model."""

from vietfin.abstract.data import Data
from vietfin.utils.helpers import ValidatedDatetime


class FmarketFundHoldingsData(Data):
    """Fmarket Fund Top Holdings Data."""

    __alias_dict__ = {
        "stock_code": "stockCode",
        "industry": "industry",
        "weight": "netAssetPercent",
        "asset_category": "type",
        "update_at": "updateAt",
    }

    stock_code: str  # The code string of the holding.
    industry: str  # The industry category of the holding.
    weight: float  # The weight of the holding, as a normalized percent.
    asset_category: str  # The asset category of the holding.
    update_at: ValidatedDatetime | None  # The date when the data was updated.
