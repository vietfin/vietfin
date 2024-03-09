"""SSI Equity Search function."""

import requests

from vietfin.providers.ssi.utils.helpers import ssi_headers
from vietfin.abstract.vfobject import VfObject
from vietfin.providers.ssi.models.equity_search import SsiEquitySearchData
from vietfin.utils.helpers import generate_extra_metadata, check_response_error
from vietfin.utils.errors import EmptyDataError


def search(symbol: str = "") -> VfObject:
    """Equity Search. Search for a company by its stock ticker from SSI provider.

    Parameters
    ----------
    symbol : str
        The stock ticker symbol of the company to search for.
        An empty string (by default) returns the full list of currently listed companies.

    Returns
    -------
    VfObject
        results : list[SsiEquitySearchData]
            Info of the company or companies listed on SSI.
        provider : str
            Provider name: "ssi"
        extra : dict
            Extra metadata about the command run.
        raw_data : dict
            raw data from the API call

    Raises
    ------
    HttpError
        if the API call failed
    EmptyDataError
        if the API response is empty
    """

    symbol = symbol.upper()

    # API call
    url = "https://fiin-core.ssi.com.vn/Master/GetListOrganization?language=vi"
    response = requests.get(url, headers=ssi_headers)
    check_response_error(response)
    data = response.json()

    rows = data["items"]
    if not rows:
        raise EmptyDataError(f"No data found for stock symbol: {symbol}")

    # Filter results based on the provided symbol if it's not an empty string
    if symbol:
        rows = [
            r for r in rows if r.get("ticker", "").upper() == symbol.upper()
        ]

        if not rows:
            raise ValueError(f"No data found for stock symbol: {symbol}")

    # Unpack json to data model
    ticker_info: list[SsiEquitySearchData] = [
        SsiEquitySearchData(**r) for r in rows
    ]

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol, result=ticker_info, api_url=url
    )

    print(f"Retrieved {extra.get('records_count',[])} records for equity.search() from SSI.")

    return VfObject(
        results=ticker_info, provider="ssi", extra=extra, raw_data=data
    )
