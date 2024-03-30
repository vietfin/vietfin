"""SSI Etf Search function."""

import requests

from vietfin.providers.ssi.utils.helpers import ssi_headers
from vietfin.abstract.vfobject import VfObject
from vietfin.providers.ssi.models.etf_search import SsiEtfSearchData
from vietfin.utils.helpers import generate_extra_metadata, check_response_error
from vietfin.utils.errors import EmptyDataError


def search(symbol: str = "") -> VfObject:
    """Etf Search. Search for an Etf by its ticker from SSI provider.

    Parameters
    ----------
    symbol : str
        The ticker symbol of the Etf to search for.
        An empty string (by default) returns the full list of currently listed companies.

    Returns
    -------
    VfObject
        results : list[SsiEtfSearchData]
            Info of the Etf(s) listed on SSI.
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
    url = "https://iboard-query.ssi.com.vn/v2/stock/type/e/hose"
    response = requests.get(url, headers=ssi_headers)
    check_response_error(response)
    data = response.json()
    rows = data["data"]

    if not rows:
        raise EmptyDataError

    # Filter results by comparing the provided symbol to the value of key "ss"
    if symbol:
        rows = [r for r in rows if r.get("ss", "").upper() == symbol.upper()]

        if not rows:
            raise EmptyDataError(f"No data found for Etf symbol: {symbol}")

    # Unpack json dict to data model
    etf_list: list[SsiEtfSearchData] = [SsiEtfSearchData(**r) for r in rows]

    # Additional metadata about the command run
    extra = generate_extra_metadata(symbol=symbol, result=etf_list, api_url=url)

    print(f"Retrieved {extra.get('records_count',[])} ETFs records.")

    return VfObject(
        results=etf_list, provider="ssi", extra=extra, raw_data=data
    )
