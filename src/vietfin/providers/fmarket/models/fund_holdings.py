"""Fmarket Mutual Fund Top Holdings Model."""

from vietfin.standard_models.data import Data
from vietfin.utils.helpers import ValidatedDatetime


class FmarketFundHoldingsData(Data):
    """Fmarket Fund Top Holdings Data."""

    __alias_dict__ = {
        "stock_code": "stockCode",
        "industry": "industry",
        "net_asset_percent": "netAssetPercent",
        "type_asset": "type",
        "update_at": "updateAt",
    }

    stock_code: str
    industry: str
    net_asset_percent: float
    type_asset: str
    update_at: ValidatedDatetime | None
