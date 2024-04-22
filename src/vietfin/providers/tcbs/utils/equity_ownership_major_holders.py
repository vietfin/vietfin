"""TCBS Equity Ownership major_holders() command."""

import httpx as requests

from vietfin.providers.tcbs.utils.helpers import tcbs_headers
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    generate_extra_metadata,
    check_response_error,
    BaseOtherParams,
)
from vietfin.providers.tcbs.models.equity_ownership_major_holders import (
    TcbsEquityOwnershipMajorHoldersData,
)
from vietfin.utils.errors import EmptyDataError


def major_holders(symbol: str) -> VfObject:
    """Retrieve Equity Ownership Major Holders data of a specific ticker.

    Data from TCBS tcbs.com.vn

    Parameters
    ----------
    symbol : str
        stock ticker

    Returns
    -------
    VfObject
        results : list[TcbsEquityOwnershipMajorHoldersData]
            equity ownership major holders data of the given ticker
        provider : str
            provider name 'tcbs'
        extra : dict
            Extra metadata about the command run.
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
    params = BaseOtherParams(symbol=symbol)
    symbol = params.symbol

    # API call
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/company/{symbol}/large-share-holders"
    response = requests.get(url, headers=tcbs_headers)
    check_response_error(response)
    data = response.json()
    rows = data.get("listShareHolder", [])

    if not rows:
        raise EmptyDataError(f"No data found for stock ticker {symbol}.")

    # Unpack json to data model and append to the results output
    major_holders = [TcbsEquityOwnershipMajorHoldersData(**r) for r in rows]

    # Additional metadata about the command run
    extra = generate_extra_metadata(symbol=symbol, result=major_holders, api_url=url)

    print(
        f"Retrieved {extra.get('records_count',[])} major holders data point for stock ticker {symbol}."
    )

    return VfObject(results=major_holders, provider="tcbs", extra=extra, raw_data=data)
