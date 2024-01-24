"""Fmarket Mutual Fund Info Model."""

from typing import TypeVar, Generic

from pydantic import field_validator

from vietfin.standard_models.data import Data
from vietfin.utils.helpers import ValidatedDatetime

T = TypeVar("T")


class FmarketFundOwnerData(Data):
    """Fmarket Fund Owner Data."""

    __alias_dict__ = {
        "owner_name": "name",
    }

    owner_name: str | None


class FmarketFundTypesData(Data):
    """Fmarket Fund Types Data."""

    __alias_dict__ = {
        "fund_type_name": "name",
    }

    fund_type_name: str | None


class FmarketFundInfoData(Data, Generic[T]):
    """Fmarket Fund Info Data."""

    __alias_dict__ = {
        "fund_id": "id",
        "short_name": "shortName",
        "name": "name",
        "inception_date": "firstIssueAt",
        "management_fee": "managementFee",
        "nav": "nav",
        "fund_owner": "owner",
        "fund_type": "dataFundAssetType",
    }

    # add generic type variable T. So pydantic does not warn `type mismatch from expectation`

    fund_id: int
    short_name: str
    name: str
    inception_date: ValidatedDatetime | None
    management_fee: float | None
    nav: float | None
    fund_owner: FmarketFundOwnerData | T | None
    fund_type: FmarketFundTypesData | T | None

    @field_validator("fund_owner")
    @classmethod
    def parse_fund_owner_name(cls, v: FmarketFundOwnerData) -> str:
        if isinstance(v, FmarketFundOwnerData):
            return v.owner_name  # type: ignore
        return v

    @field_validator("fund_type")
    @classmethod
    def parse_fund_type_name(cls, v: FmarketFundTypesData) -> str:
        if isinstance(v, FmarketFundTypesData):
            return v.fund_type_name  # type: ignore
        return v
