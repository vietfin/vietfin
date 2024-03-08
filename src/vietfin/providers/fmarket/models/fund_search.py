"""Fmarket Mutual Fund Info Model."""

from typing import TypeVar, Generic
from typing_extensions import TypedDict

from pydantic import field_validator

from vietfin.abstract.data import Data
from vietfin.utils.helpers import ValidatedDatetime

T = TypeVar("T")


class FmarketFundOwnerData(TypedDict):
    """Fmarket Fund Owner Data.

    Purpose: define the nested structure of the data returned by the API.
    """

    name: str | None


class FmarketFundTypesData(TypedDict):
    """Fmarket Fund Types Data.

    Purpose: define the nested structure of the data returned by the API.
    """

    name: str | None


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

    fund_id: int  # ID of a fund in Fmarket database.
    short_name: str  # Common name of a fund.
    name: str  # Legal official name of a fund.
    inception_date: ValidatedDatetime | None  # Date of inception of a fund.
    management_fee: float | None  # Annual management fee of a fund. Unit: percent per year.
    nav: float | None  # Current Net Asset Value of a fund.
    # add generic type variable T. So pydantic does not warn `type mismatch from expectation` at runtime
    fund_owner: FmarketFundOwnerData | T | None  # Name of the Organization issuing the fund.
    fund_type: FmarketFundTypesData | T | None  # Type of fund. E.g. "stock", "bond", "balanced"

    @field_validator("fund_owner")
    @classmethod
    def parse_fund_owner_name(cls, v: FmarketFundOwnerData) -> str:
        return v.get("name", "")  # type: ignore

    @field_validator("fund_type")
    @classmethod
    def parse_fund_type_name(cls, v: FmarketFundTypesData) -> str:
        return v.get("name", "")  # type: ignore
