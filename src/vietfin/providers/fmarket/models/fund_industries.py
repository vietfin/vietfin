"""Fmarket Mutual Fund Industries Model."""

from vietfin.abstract.data import Data


class FmarketFundIndustriesData(Data):
    """Fmarket Fund Industries Data."""

    __alias_dict__ = {
        "industry": "industry",
        "weight": "assetPercent",
    }

    industry: str
    weight: float
