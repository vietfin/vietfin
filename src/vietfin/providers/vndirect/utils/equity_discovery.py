"""VNDIRECT Equity Discovery group of functions."""

import httpx as requests

from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    generate_extra_metadata,
    check_response_error,
    TOP_MOVERS_REPORT_NAMES,
    EXCHANGE_NAMES,
    BaseOtherParams,
)
from vietfin.utils.errors import EmptyDataError
from vietfin.providers.vndirect.models.equity_discovery import (
    VndirectEquityDiscoveryData,
)
from vietfin.providers.vndirect.utils.helpers import vndirect_headers


def get_top_movers(
    name: TOP_MOVERS_REPORT_NAMES, exchange: EXCHANGE_NAMES
) -> VfObject:
    """Equity Discovery. Retrieve a report from VNDIRECT provider.

    Parameters
    ----------
    name : Literal
        name of the report.
    exchange : Literal
        name of the exchange.

    Returns
    -------
    VfObject
        results : list[VndirectEquityDiscoveryData]
            list of stock tickers listed the specific report.
        provider : str
            Provider name: "vndirect"
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
    exchange_mapping = {
        "hose": "VNIndex",
        "hnx": "HNX",
    }
    exchange_api = exchange_mapping.get(exchange, "")
    if not exchange_api:
        raise ValueError(f"Exchange {exchange} is not supported by this provider VNDIRECT.")

    # API call
    url_mapping = {
        "gainers": f"https://finfo-api.vndirect.com.vn/v4/top_stocks?q=index:{exchange_api}~nmVolumeAvgCr20D:gte:10000~priceChgPctCr1D:gt:0&size=10&sort=priceChgPctCr1D",
        "losers": f"https://finfo-api.vndirect.com.vn/v4/top_stocks?q=index:{exchange_api}~nmVolumeAvgCr20D:gte:10000~priceChgPctCr1D:lt:0&size=10&sort=priceChgPctCr1D:asc",
        "value": f"https://finfo-api.vndirect.com.vn/v4/top_stocks?q=index:{exchange_api}~accumulatedVal:gt:0&size=10&sort=accumulatedVal",
    }
    url = url_mapping.get(name)
    response = requests.get(url, headers=vndirect_headers)  # type: ignore
    check_response_error(response)
    data = response.json()
    rows = data.get("data", [])

    if not rows:
        raise EmptyDataError(
            f"No data found for the list of top {name}, at exchange {exchange}"
        )

    # Unpack json dict to data model
    report_results = [VndirectEquityDiscoveryData(**r) for r in rows]

    # Additional metadata about the command run
    extra = generate_extra_metadata(result=report_results, api_url=url)

    return VfObject(
        results=report_results, provider="vndirect", extra=extra, raw_data=data
    )
