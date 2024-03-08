"""Fmarket Funds Top Holdings function."""

import requests

from vietfin.abstract.vfobject import VfObject
from vietfin.providers.fmarket.utils.helpers import fmarket_headers, get_fund_id
from vietfin.providers.fmarket.models.fund_holdings import (
    FmarketFundHoldingsData,
)
from vietfin.utils.helpers import generate_extra_metadata, check_response_error, BaseOtherParams
from vietfin.utils.errors import EmptyDataError


def holdings(symbol: str) -> VfObject:
    """Retrieve a list of the current top 10 holdings of the specified fund from the Fmarket provider.

    Parameters
    ----------
    symbol : str
        Fund short name.

    Returns
    -------
    VfObject
        results : list[FmarketFundHoldingsData]
           The current top 10 holdings of the selected fund.
        provider : str
            provider name "fmarket"
        extra : dict
            extra metadata about the command run
        raw_data : dict
            raw data from the API call

    Raises
    ------
    HttpError
        if the API call failed
    EmptyDataError
        if the API response is empty
    """

    # Validate input params
    params = BaseOtherParams(symbol=symbol)
    symbol = params.symbol

    # Retrieve fund_id matching the given symbol
    fund_id = get_fund_id(symbol)

    # API call
    url = f"https://api.fmarket.vn/res/products/{fund_id}"
    response = requests.get(url, headers=fmarket_headers, cookies=None)
    check_response_error(response)
    data = response.json()

    # NOTE: API logic. Funds can allocate to either equities or fixed income securities, or both
    list_of_holdings = []

    # Extract top holdings in equity
    rows = data["data"]["productTopHoldingList"]
    fund_top_holdings_stock = [FmarketFundHoldingsData(**r) for r in rows]

    # Extract top holdings in fixed income securities
    rows = data["data"]["productTopHoldingBondList"]
    fund_top_holdings_bond = [FmarketFundHoldingsData(**r) for r in rows]

    # Output the merged list
    list_of_holdings = fund_top_holdings_stock + fund_top_holdings_bond

    if len(list_of_holdings) == 0:
        raise EmptyDataError

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol, result=list_of_holdings, api_url=url
    )

    return VfObject(
        results=list_of_holdings, provider="fmarket", extra=extra, raw_data=data
    )
