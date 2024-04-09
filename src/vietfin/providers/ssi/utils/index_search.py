"""SSI Index Search function."""

import httpx as requests

from vietfin.providers.ssi.utils.helpers import ssi_headers
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import generate_extra_metadata, check_response_error
from vietfin.providers.ssi.models.index_search import SsiIndexSearchData
from vietfin.utils.errors import EmptyDataError


def search(symbol: str = "") -> VfObject:
    """Index Search. Search for an index by its symbol from SSI provider.

    An empty string (by default) returns the full list of currently listed indexes.

    Parameters
    ----------
    symbol : str, optional
        The symbol of the index to search for.

    Returns
    -------
    VfObject
        results : list[SsiIndexSearchData]
            Info of the index provided by SSI.
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
    url = "https://fiin-core.ssi.com.vn/Master/GetAllCompanyGroup?language=vi"
    response = requests.get(url, headers=ssi_headers)
    check_response_error(response)
    data = response.json()

    rows = data["items"]
    if not rows:
        raise EmptyDataError(f"No data found for index symbol: {symbol}")

    # Filter results based on the provided symbol if it's not an empty string
    if symbol:
        rows = [
            r
            for r in rows
            if r.get("comGroupCode", "").upper() == symbol.upper()
        ]

        if not rows:
            raise EmptyDataError(f"No data found for index symbol: {symbol}")

    # Unpack json to data model
    index_info: list[SsiIndexSearchData] = [
        SsiIndexSearchData(**r) for r in rows
    ]

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol, result=index_info, api_url=url
    )

    print(f"Retrieved {extra.get('records_count',[])} records.")

    return VfObject(
        results=index_info, provider="ssi", extra=extra, raw_data=data
    )
