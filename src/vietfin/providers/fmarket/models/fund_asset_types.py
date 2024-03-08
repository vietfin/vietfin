"""Fmarket Mutual Fund Holding Asset Standard Model."""

from typing_extensions import TypedDict

from vietfin.abstract.data import Data


class FmarketFundAssetTypeNameData(TypedDict):
    """Fmarket Fund Asset Type Name Data.
    
    Purpose: define the nested structure of the data returned by the API.
    """

    name: str | None


class FmarketFundAssetTypesData(Data):
    """Fmarket Fund Holding Assets Data."""

    __alias_dict__ = {
        "asset_type": "assetType",
        "weight": "assetPercent",
    }

    asset_type: FmarketFundAssetTypeNameData
    weight: float | None
