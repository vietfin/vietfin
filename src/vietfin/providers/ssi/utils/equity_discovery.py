"""SSI Equity Discovery group of functions."""

import httpx as requests

from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    generate_extra_metadata,
    check_response_error,
    TOP_MOVERS_REPORT_NAMES,
    EXCHANGE_NAMES,
    BaseOtherParams,
)
from vietfin.providers.ssi.utils.helpers import ssi_headers
from vietfin.providers.ssi.models.equity_discovery import SsiEquityDiscoveryData
from vietfin.utils.errors import EmptyDataError


def get_top_movers(
    name: TOP_MOVERS_REPORT_NAMES, exchange: EXCHANGE_NAMES
) -> VfObject:
    """Equity Discovery. Retrieve a report from SSI provider.

    Parameters
    ----------
    name : str
        name of the report.
    exchange : srt
        name of the exchange.

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
    # Validate input
    params = BaseOtherParams(top_movers_report=name, exchange=exchange)
    name = params.top_movers_report
    exchange = params.exchange

    # Map user friendly string to API value
    name_mapping = {
        "gainers": "Gainers",
        "losers": "Losers",
        "value": "Value",
    }
    name_api = name_mapping.get(name)

    exchange_mapping = {
        "hose": "HOSE",
        "hnx": "HNX",
        "upcom": "UPCOM",
        "all": "ALL",
    }
    exchange_api = exchange_mapping.get(exchange)
    if not exchange_api:
        raise ValueError(f"Exchange {exchange} is not supported by this provider SSI.")

    # API call
    url = f"https://fiin-market.ssi.com.vn/TopMover/GetTop{name_api}?language=vi&ComGroupCode={exchange_api}"
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
