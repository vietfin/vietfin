"""TCBS Equity Fundamental Dividends command."""

import requests

from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    check_response_error,
    generate_extra_metadata,
    BaseOtherParams,
)
from vietfin.providers.tcbs.utils.helpers import tcbs_headers
from vietfin.providers.tcbs.models.equity_fundamental_dividends import (
    TcbsEquityFundamentalDividendsData,
)
from vietfin.utils.errors import EmptyDataError


def dividends(symbol: str, limit: int = 100) -> VfObject:
    """Retrieve Equity Fundamental Dividends, historical dividends data of the given ticker.

    Data from TCBS tcbs.com.vn

    Parameters
    ----------
    symbol : str
        stock ticker
    limit: int
        number of records to retrieve. Default: 100
        0 will return all records.

    Returns
    -------
    VfObject
        results : list[TcbsEquityFundamentalDividendsData]
            historical dividends data of the given ticker
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
    params = BaseOtherParams(symbol=symbol, limit=limit)
    symbol = params.symbol
    limit = params.limit

    # API logic: paginated returns up to 100 records per page per single API call
    page_size = 100 if (limit == 0 or limit > 100) else limit
    page = 0  # start from the 1st page
    dividends_history = []
    url_list = []
    data = []

    # API call
    while True:
        url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/company/{symbol}/dividend-payment-histories?page={page}&size={page_size}"
        response = requests.get(url, headers=tcbs_headers)
        check_response_error(response)
        data_chunk = response.json()
        rows = data_chunk.get("listDividendPaymentHis", [])

        if not rows:
            break  # stop if no more data

        url_list.append(url)
        data.append(data_chunk)

        # Unpack json to data model and append to the results output
        dividends_history.extend(
            [TcbsEquityFundamentalDividendsData(**r) for r in rows]
        )

        if 0 < limit <= len(dividends_history):
            dividends_history = dividends_history[:limit]
            break  # stop if limit reached

        # increment page number to continue fetching until no more data
        page += 1

    if not dividends_history:
        raise EmptyDataError(f"No data found for the symbol {symbol}.")

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol, result=dividends_history, api_url=url_list
    )

    print(
        f"Retrieved {extra.get('records_count',[])} historical dividends data point for stock ticker {symbol}."
    )

    return VfObject(
        results=dividends_history, provider="tcbs", extra=extra, raw_data=data
    )
