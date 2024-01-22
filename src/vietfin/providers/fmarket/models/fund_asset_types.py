"""Fmarket Mutual Fund Holding Asset Standard Model."""

from vietfin.standard_models.data import Data


class FmarketFundAssetTypeNameData(Data):
    """Fmarket Fund Asset Type Name Data."""

    __alias_dict__ = {
        "asset_type_name": "name",
    }

    asset_type_name: str | None


class FmarketFundAssetTypesData(Data):
    """Fmarket Fund Holding Assets Data."""

    __alias_dict__ = {
        "asset_type": "assetType",
        "weight": "assetPercent",
    }

    asset_type: FmarketFundAssetTypeNameData
    weight: float | None