"""WiFeed Equity Search function."""

import requests

from vietfin.abstract.vfobject import VfObject
from vietfin.providers.wifeed.models.equity_search import WifeedEquitySearchData
from vietfin.utils.helpers import (
    generate_extra_metadata,
    check_response_error,
    BaseOtherParams,
)
from vietfin.utils.errors import EmptyDataError


def search(symbol: str = "") -> VfObject:
    """Equity Search. Search for a company by its stock ticker from WiFeed provider.

    An empty string (by default) returns the full list of currently listed companies.

    Parameters
    ----------
    symbol : str, optional
        The stock ticker symbol of the company to search for.

    Returns
    -------
    VfObject
        results : list[WifeedEquitySearchData]
            Info of the company or companies listed on WiFeed.
        provider : str
            Provider name: "wifeed"
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
    url = "https://wifeed.vn/api/thong-tin-co-phieu/danh-sach-ma-chung-khoan"
    response = requests.get(url)
    check_response_error(response)
    data = response.json()
    rows = data["data"]

    if not rows:
        raise EmptyDataError

    # Filter results based on the provided symbol if it's not an empty string
    if symbol:
        rows = [r for r in rows if r.get("code", "").upper() == symbol.upper()]

        if not rows:
            raise EmptyDataError(f"No data found for stock symbol: {symbol}")

    # Unpack json to data model
    ticker_info: list[WifeedEquitySearchData] = [
        WifeedEquitySearchData(**r) for r in rows
    ]

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol, result=ticker_info, api_url=url
    )

    print(f"Retrieved {extra.get('records_count',[])} records from WiFeed.")

    return VfObject(
        results=ticker_info, provider="wifeed", extra=extra, raw_data=data
    )
