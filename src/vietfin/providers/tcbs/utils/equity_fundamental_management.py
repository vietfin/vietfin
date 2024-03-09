"""TCBS Equity Fundamental Management command."""

import requests

from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    check_response_error,
    generate_extra_metadata,
    BaseOtherParams,
)
from vietfin.providers.tcbs.utils.helpers import tcbs_headers
from vietfin.providers.tcbs.models.equity_fundamental_management import (
    TcbsEquityFundamentalManagementData,
)
from vietfin.utils.errors import EmptyDataError


def management(symbol: str) -> VfObject:
    """Retrieve Equity Fundamental Management, key executives data of the given ticker.

    Data from TCBS tcbs.com.vn

    Parameters
    ----------
    symbol : str
        stock ticker

    Returns
    -------
    VfObject
        results : list[TcbsEquityFundamentalManagementData]
            key executives data of the given ticker
        provider : str
            provider name 'tcbs'
        extra : dict
            Extra metadata about the command run.
        raw_data : list[dict]
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

    # API logic: paginated returns up to 100 records per page per single API call
    page_size = 100
    page = 0  # start from the 1st page
    fundamental_management = []
    url_list = []
    data = []

    # API call
    while True:
        url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/company/{symbol}/key-officers?page={page}&size={page_size}"
        response = requests.get(url, headers=tcbs_headers)
        check_response_error(response)
        data_chunk = response.json()
        rows = data_chunk.get("listKeyOfficer",[])

        if not rows:
            break  # stop if no more data

        url_list.append(url)
        data.append(data_chunk)

        # Unpack json to data model and append to the results output
        fundamental_management.extend(
            [TcbsEquityFundamentalManagementData(**r) for r in rows]
        )

        # increment page number to continue fetching until no more data
        page += 1

    if not fundamental_management:
        raise EmptyDataError(f"No data found for the ticker {symbol}.")

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol, result=fundamental_management, api_url=url_list
    )

    print(
        f"Retrieved {extra.get('records_count',[])} key executives for stock ticker {symbol}."
    )

    return VfObject(
        results=fundamental_management,
        provider="tcbs",
        extra=extra,
        raw_data=data,
    )
