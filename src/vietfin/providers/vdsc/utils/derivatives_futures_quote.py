"""VDSC Rong Viet Derivatives Futures Quote command."""

from datetime import datetime

import httpx as requests

from vietfin.providers.vdsc.utils.helpers import rv_headers
from vietfin.providers.vdsc.models.derivatives_futures_quote import (
    VdscDerivativesFuturesQuoteData,
)
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    generate_extra_metadata,
    check_response_error,
    BaseOtherParams,
)
from vietfin.utils.errors import EmptyDataError


def get_cookies_selenium():
    """Retrieve cookies from VDSC Rong Viet website using Selenium."""
    try:
        from selenium import webdriver  # type: ignore # pylint: disable=import-outside-toplevel
    except ImportError as exc:
        raise ImportError(
            "Please install selenium to use this function. e.g. `poetry add selenium`."
        ) from exc

    driver = webdriver.Chrome()
    driver.get("https://livedragon.vdsc.com.vn/general/intradayBoard.rv")
    cookies = driver.get_cookies()
    requests_cookies = {}
    for c in cookies:
        requests_cookies[c["name"]] = c["value"]

    return requests_cookies


def quote(symbol: str, limit: int) -> VfObject:
    """Retrieve Derivatives Futures intraday quote data of a specific contract symbol.

    Data from VDSC Rong Viet https://livedragon.vdsc.com.vn/
    As of 2024-02-08, this API is not stable, long runtime and requires cookies.

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
        results : list[VdscEquityHistoricalPriceData]
            derivatives futures historical price data of the given contract symbol on current date
        provider : str
            provider name 'vdsc'
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
    current_date_string_api = current_date.strftime("%d/%m/%Y")
    current_date_string_iso = current_date.strftime("%Y-%m-%d")

    # API call
    requests_cookies = get_cookies_selenium()

    payload = {"stockCode": symbol, "boardDate": current_date_string_api}
    url = "https://livedragon.vdsc.com.vn/general/intradaySearch.rv"
    response = requests.post(
        url, headers=rv_headers, data=payload, cookies=requests_cookies
    )
    check_response_error(response)

    data = response.json()
    rows = data.get("list", [])

    if not rows:
        raise EmptyDataError(
            f"No data found for the given symbol {symbol} on {current_date_string_iso}"
        )

    # Return only the number of records specified by `limit`
    if limit == 0:
        limit = len(rows)  # return all available data points
    limited_rows = rows[:limit]

    # Unpack json data into data model
    derivatives_futures_quote: list[VdscDerivativesFuturesQuoteData] = [
        VdscDerivativesFuturesQuoteData(**r) for r in limited_rows
    ]

    # Generate extra metadata
    extra = generate_extra_metadata(
        symbol=symbol, result=derivatives_futures_quote, api_url=url
    )

    print(
        f"Retrieved {extra.get('records_count',[])} intraday quotes for futures contract {symbol} traded on {current_date_string_iso}."
    )

    return VfObject(
        results=derivatives_futures_quote,
        provider="vdsc",
        extra=extra,
        raw_data=data,
    )
