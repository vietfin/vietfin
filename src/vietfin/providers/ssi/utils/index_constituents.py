"""SSI Index Constituents function."""

import requests

from vietfin.providers.ssi.utils.helpers import ssi_headers
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import generate_extra_metadata, check_response_error
from vietfin.providers.ssi.models.index_constituents import (
    SsiIndexConstituentsData,
)
from vietfin.utils.errors import EmptyDataError


def constituents(symbol: str) -> VfObject:
    """Index Constituents. Load the constituents for a specific index from SSI provider.

    Parameters
    ----------
    symbol : str
        The symbol of the index to search for.

    Returns
    -------
    VfObject
        results : list[SsiIndexConstituentsData]
            List of the constituents of the given index provided by SSI.
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
    url = f"https://iboard-query.ssi.com.vn/v2/stock/group/{symbol}"
    response = requests.get(url, headers=ssi_headers)
    check_response_error(response)
    data = response.json()

    rows = data["data"]
    if not rows:
        raise EmptyDataError(f"No data found for index symbol: {symbol}")

    # Unpack json to data model
    index_constituents: list[SsiIndexConstituentsData] = [
        SsiIndexConstituentsData(**r) for r in rows
    ]

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol, result=index_constituents, api_url=url
    )

    print(f"Retrieved {extra.get('records_count',[])} records.")

    return VfObject(
        results=index_constituents, provider="ssi", extra=extra, raw_data=data
    )
