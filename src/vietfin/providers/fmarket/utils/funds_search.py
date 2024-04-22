"""Fmarket Funds Search function."""

import httpx as requests
from pydantic import BaseModel, ConfigDict, field_validator

from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import generate_extra_metadata, check_response_error
from vietfin.providers.fmarket.models.fund_search import FmarketFundInfoData
from vietfin.providers.fmarket.utils.helpers import fmarket_headers
from vietfin.utils.errors import EmptyDataError


class SearchParams(BaseModel):
    """Class for Input validation for search() function."""

    symbol: str | None = ""
    fund_type: str | None = ""

    model_config = ConfigDict(
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


def search(
    symbol: str | None = "",
    fund_type: str | None = "",
) -> VfObject:
    """Search for mutual funds from Fmarket provider.

    An empty query (by default) returns the full list of available mutual funds.

    Parameters
    ----------
    symbol : str, Optional
        fund short name. Options: "" (default)
    fund_type : str, Optional
        available fund types. Options: "" (default), "BALANCED", "BOND", "STOCK"

    Returns
    -------
    VfObject
        results : list[FmarketFundInfoData]
            Info of mutual fund listed on Fmarket.
        provider : str
            Provider name: "fmarket"
        extra : dict
            Extra metadata about the command run, including the timestamp, the symbol.
        raw_data : dict
            raw data from the API call

    Raises
    ------
    ValidationError
        if the input param are invalid
    HttpError
        if the API call failed
    EmptyDataError
        if the API response is empty
    """

    # Validate input param
    params = SearchParams(symbol=symbol, fund_type=fund_type)
    symbol = params.symbol
    fund_type = params.fund_type

    # API call
    # Formatting fundAssetTypes or return default value as an empty list
    fundAssetTypes = {
        None: [],
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
    check_response_error(response)
    data = response.json()

    rows = data["data"]["rows"]
    if not rows:
        raise EmptyDataError(f"No data found for fund symbol: {symbol}")

    # Unpack json to data model
    fund_details: list[FmarketFundInfoData] = [
        FmarketFundInfoData(**r) for r in rows
    ]

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol, result=fund_details, api_url=url
    )

    print(f"Retrieved {extra.get('records_count',[])} record(s) from Fmarket.")

    return VfObject(
        results=fund_details, provider="fmarket", extra=extra, raw_data=data
    )
