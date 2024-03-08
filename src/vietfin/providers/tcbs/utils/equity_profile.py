"""TCBS Equity Profile command."""

import requests

from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    check_response_error,
    generate_extra_metadata,
    BaseOtherParams,
)
from vietfin.providers.tcbs.utils.helpers import tcbs_headers
from vietfin.providers.tcbs.models.equity_profile import TcbsEquityProfileData
from vietfin.utils.errors import EmptyDataError


def profile(symbol: str) -> VfObject:
    """Retrieve Equity Profile general info of the given equity symbol.

    Data from TCBS tcbs.com.vn

    Parameters
    ----------
    symbol : str
        stock ticker

    Returns
    -------
    VfObject
        results : list[TcbsEquityProfileData]
            equity profile general info of the given ticker
        provider : str
            provider name 'tcbs'
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
    url_1 = (
        f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/company/{symbol}/overview"
    )

    url_2 = (
        f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{symbol}/overview"
    )
    response_1 = requests.get(url_1, headers=tcbs_headers)
    response_2 = requests.get(url_2, headers=tcbs_headers)

    check_response_error(response_1)
    check_response_error(response_2)

    response_dict_1 = response_1.json()
    response_dict_2 = response_2.json()

    data = {}
    data.update(response_dict_1)
    data.update(response_dict_2)

    if not data:
        raise EmptyDataError("Error in API response. No data found.")

    # Unpack dict to data model
    ticker_profile: list[TcbsEquityProfileData] = [
        TcbsEquityProfileData(**data)
    ]

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol, result=ticker_profile, api_url=[url_1, url_2]
    )

    return VfObject(
        results=ticker_profile, provider="tcbs", extra=extra, raw_data=data
    )
