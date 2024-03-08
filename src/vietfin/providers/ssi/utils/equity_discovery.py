"""SSI Equity Discovery group of functions."""

import requests
from typing import Literal

from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import generate_extra_metadata, check_response_error
from vietfin.providers.ssi.utils.helpers import ssi_headers
from vietfin.providers.ssi.models.equity_discovery import SsiEquityDiscoveryData
from vietfin.utils.errors import EmptyDataError


REPORT_NAMES = Literal["Gainers", "Losers", "Value"]
EXCHANGE_NAMES = Literal["HOSE", "HNX", "UPCOM", "ALL"]


def get_top_movers(name: REPORT_NAMES, exchange: EXCHANGE_NAMES) -> VfObject:
    """Equity Discovery. Retrieve a report from SSI provider.

    Parameters
    ----------
    name : str
        name of the report. Options: Literal["Gainers", "Losers", "Value"]
    exchange : srt
        name of the exchange. Options: Literal["HOSE", "HNX", "UPCOM", "ALL"]

    Returns
    -------
    VfObject
        results : list[SsiEquityDiscoveryData]
            list of stock tickers listed the specific report.
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

    # API call
    url = f"https://fiin-market.ssi.com.vn/TopMover/GetTop{name}?language=vi&ComGroupCode={exchange}"
    response = requests.get(url, headers=ssi_headers)
    check_response_error(response)
    data = response.json()
    rows = data.get("items", [])

    if not rows:
        raise EmptyDataError(
            f"No data found for the list of top {name}, at exchange {exchange}"
        )

    # Unpack json dict to data model
    report_results = [SsiEquityDiscoveryData(**r) for r in rows]

    # Additional metadata about the command run
    extra = generate_extra_metadata(result=report_results, api_url=url)

    return VfObject(
        results=report_results, provider="ssi", extra=extra, raw_data=data
    )
