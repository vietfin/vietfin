"""TCBS Equity Fundamental Ratios command."""

import httpx as requests

from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    check_response_error,
    generate_extra_metadata,
    BaseOtherParams,
    PERIODS,
)
from vietfin.providers.tcbs.utils.helpers import tcbs_headers
from vietfin.providers.tcbs.models.equity_fundamental_ratios import (
    TcbsEquityFundamentalRatiosData,
)
from vietfin.utils.errors import EmptyDataError


def ratios(symbol: str, period: PERIODS = "annual") -> VfObject:
    """Retrieve Equity Fundamental Ratios, Financial ratios data of the given ticker.

    Data from TCBS tcbs.com.vn

    Parameters
    ----------
    symbol : str
        stock ticker
    period : PERIODS
        period of the financial ratios. Options: Literal['annual', 'quarter']

    Returns
    -------
    VfObject
        results : list[TcbsEquityFundamentalRatiosData]
            financial ratios data of the given ticker
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
    params = BaseOtherParams(
        symbol=symbol,
        period=period,
    )
    symbol = params.symbol
    period = params.period

    period_mapping = {
        "annual": 1,
        "quarter": 0,
    }
    is_annual = period_mapping.get(period)

    # API call
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/finance/{symbol}/financialratio?yearly={is_annual}&isAll=true"
    response = requests.get(url, headers=tcbs_headers)
    check_response_error(response)
    data = response.json()
    rows = data

    if not rows:
        raise EmptyDataError(f"No data found for the symbol {symbol}.")

    # Add 'period' column
    for r in rows:
        r["period"] = period

    # Unpack json dict to data model
    fundamental_ratios = [TcbsEquityFundamentalRatiosData(**r) for r in rows]

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol, result=fundamental_ratios, api_url=url
    )

    print(
        f"Retrieved {extra.get('records_count',[])} financial ratios data point for stock ticker {symbol}."
    )

    return VfObject(
        results=fundamental_ratios, provider="tcbs", extra=extra, raw_data=data
    )
