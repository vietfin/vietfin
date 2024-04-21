"""SSI Derivatives Covered Warrant Search command."""

import httpx as requests

from vietfin.providers.ssi.utils.helpers import ssi_headers
from vietfin.providers.ssi.models.derivatives_coveredwarrant_search import (
    SsiDerivativesCoveredwarrantSearchData,
)
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import generate_extra_metadata, check_response_error
from vietfin.utils.errors import EmptyDataError


def search(symbol: str = "") -> VfObject:
    """Derivatives Covered Warrant Search. Search for a covered warrant from SSI provider.

    Parameters
    ----------
    symbol : str
        The symbol of the covered warrant to search for.
        An empty string (by default) returns the full list of covered warrants.

    Returns
    -------
    VfObject
        results : list[SsiDerivativesCoveredwarrantSearchData]
            Info of the covered warrants available on SSI.
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
    url = "https://iboard-query.ssi.com.vn/v2/stock/type/w/hose"
    response = requests.get(url, headers=ssi_headers)
    check_response_error(response)
    data = response.json()

    rows = data["data"]

    # Filter "rows" by comparing the provided symbol with the value of key "ss"
    if symbol:
        rows = [r for r in rows if r.get("ss", "").upper() == symbol.upper()]

        if not rows:
            raise EmptyDataError(f"No data found for covered warrant: {symbol}")

    # Unpack json to data model
    covered_warrant_info: list[SsiDerivativesCoveredwarrantSearchData] = [
        SsiDerivativesCoveredwarrantSearchData(**r) for r in rows
    ]

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol, result=covered_warrant_info, api_url=url
    )

    print(
        f"Retrieved {extra.get('records_count',[])} records for cw.search() from SSI."
    )

    return VfObject(
        results=covered_warrant_info, provider="ssi", extra=extra, raw_data=data
    )
