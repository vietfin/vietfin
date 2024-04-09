"""SSI Derivatives Futures Quote command."""

from datetime import datetime

import httpx as requests

from vietfin.providers.ssi.utils.helpers import ssi_headers
from vietfin.providers.ssi.models.derivatives_futures_quote import (
    SsiDerivativesFuturesQuoteData,
)
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    generate_extra_metadata,
    check_response_error,
    BaseOtherParams,
)
from vietfin.utils.errors import EmptyDataError


def quote(symbol: str, limit: int) -> VfObject:
    """Retrieve Derivatives Futures Quote data of a specific contract symbol.

    Data from SSI https://iboard.ssi.com.vn/

    Parameters
    ----------
    symbol : str
        Futures contract symbol
    limit : int
        limit of number of records to be retrieved.
        0 will return all records.

    Returns
    -------
    VfObject
        results : list[SsiDerivativesFuturesQuoteData]
            derivatives futures quote data of the given contract symbol on current date
        provider : str
            provider name 'ssi'
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
    params = BaseOtherParams(symbol=symbol, limit=limit)
    symbol = params.symbol
    limit = params.limit

    current_date = datetime.now()
    current_date_string = current_date.strftime("%Y-%m-%d")

    # API call
    rows = []
    count = 0
    if limit == 0:
        limit = 1_000_000  # arbitrary large number to retrieve all records
    url = f"https://iboard-query.ssi.com.vn/le-table?stockSymbol={symbol}&pageSize=50"

    while True:
        response = requests.get(url, headers=ssi_headers)
        check_response_error(response)
        data = response.json()
        data_chunk = data["data"]["items"]
        rows.extend(data_chunk)

        # Break loop if "count" exceeds "limit"
        count += len(data_chunk)
        if count >= limit:
            break

        # Break loop if less than 50 records returned, since there are no more records to retrieve
        if len(data_chunk) < 50:
            break

        # Update URL to retrieve the next batch of 50 records
        last_id = data_chunk[-1]["_id"]
        url = f"https://iboard-query.ssi.com.vn/le-table?stockSymbol={symbol}&pageSize=50&lastId={last_id}"

    if not rows:
        raise EmptyDataError(
            f"No data found for the given futures contract {symbol} on {current_date_string}."
        )

    # Return only the number of records specified by `limit`
    limited_rows = rows[:limit]

    # Unpack json data into data model
    derivatives_futures_quote: list[SsiDerivativesFuturesQuoteData] = [
        SsiDerivativesFuturesQuoteData(**r) for r in limited_rows
    ]

    # Generate extra metadata
    extra = generate_extra_metadata(
        symbol=symbol, result=derivatives_futures_quote, api_url=url
    )

    print(
        f"Retrieved {extra.get('records_count','')} intraday quotes for futures contract {symbol}."
    )

    return VfObject(
        results=derivatives_futures_quote,
        provider="ssi",
        extra=extra,
        raw_data=data,
    )
