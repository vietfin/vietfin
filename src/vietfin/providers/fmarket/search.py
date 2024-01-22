import requests
from pydantic import BaseModel, ConfigDict, field_validator

from .models.fund_info import FmarketFundInfoData
from .utils import fmarket_headers, DEFAULT_SYMBOL, DEFAULT_FUND_TYPE
from vietfin.standard_models.vfobject import VfObject

# UTILS


class ValidateSearchInput(BaseModel):
    """Class for Input validation for Search function."""

    symbol: str
    fund_type: str

    model_config = ConfigDict(
        extra="ignore",
        str_to_upper=True,
    )

    @field_validator("fund_type")
    @classmethod
    def validate_fund_type(cls, v: str) -> str:
        """Validate fund_type string."""
        valid_types = {"BALANCED", "BOND", "STOCK", ""}
        if v.upper() not in valid_types:
            raise ValueError(
                f"Invalid fund type: {v}. Allowed types are {valid_types}"
            )
        return v.upper()


# MAIN


def search(
    symbol: str = DEFAULT_SYMBOL,
    fund_type: str = DEFAULT_FUND_TYPE,
) -> VfObject:
    """Search for mutual funds from the provider Fmarket.

    An empty query (set by default) returns the full list of mutual funds from the provider Fmarket.

    Parameters
    ----------
    symbol
        available fund short name: "" (default)
    fund_type
        available fund types: "" (default), "BALANCED", "BOND", "STOCK"
    headers : dict
        headers of the request

    Returns
    -------
    VfObject
        Info of mutual fund listed on Fmarket.

    Raises
    ------
    ValidationError
        if the input param are invalid
    HTTPError
        if the API call failed
    ValueError
        if no fund found for the given symbol

    """
    # Validate input param
    search_input = ValidateSearchInput(symbol=symbol, fund_type=fund_type)
    symbol = search_input.symbol
    fund_type = search_input.fund_type

    # API call
    # Formatting fundAssetTypes or get default value as an empty list
    fundAssetTypes = {
        "": [],
        "BALANCED": ["BALANCED"],
        "BOND": ["BOND"],
        "STOCK": ["STOCK"],
    }.get(fund_type, [])

    payload = {
        "types": ["NEW_FUND", "TRADING_FUND"],
        "issuerIds": [],
        "sortOrder": "DESC",
        "sortField": "navTo6Months",
        "page": 1,
        "pageSize": 100,
        "isIpo": False,
        "fundAssetTypes": fundAssetTypes,
        "bondRemainPeriods": [],
        "searchField": symbol,
        "isBuyByReward": False,
        "thirdAppIds": [],
    }

    url = "https://api.fmarket.vn/res/products/filter"
    response = requests.post(url, json=payload, headers=fmarket_headers)

    if response.status_code != 200:
        raise requests.exceptions.HTTPError(
            f"Error in API response: {response.status_code} - {response.text}"
        )

    data = response.json()

    rows = data["data"]["rows"]

    if not rows:
        raise ValueError(f"No data found for fund symbol: {symbol}")

    # Unpack json data to FmarketFundInfoData model
    fund_details: list[FmarketFundInfoData] = [
        FmarketFundInfoData(**r) for r in rows
    ]

    return VfObject(results=fund_details, provider="fmarket")
