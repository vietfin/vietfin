"""TCBS Equity Fundamental Income command."""

import httpx as requests
import pandas as pd

from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    check_response_error,
    generate_extra_metadata,
    FINANCIAL_STATEMENTS,
    BaseOtherParams,
    PERIODS,
)
from vietfin.providers.tcbs.utils.helpers import tcbs_headers
from vietfin.providers.tcbs.models.equity_fundamental_income import (
    TcbsEquityFundamentalIncomeData,
)
from vietfin.utils.errors import EmptyDataError


def get_financial_report(
    symbol: str, name: FINANCIAL_STATEMENTS, period: PERIODS = "annual"
) -> VfObject:
    """Retrieve Equity Fundamental financial statement data of the given ticker.

    Data from TCBS tcbs.com.vn

    Parameters
    ----------
    symbol : str
        stock ticker
    name : str
        financial statement name
    period : str
        time period of the data to return

    Returns
    -------
    VfObject
        results : list[TcbsEquityFundamentalIncomeData]
            historical income/balance/cashflow data of the given ticker
        provider : str
            provider name 'tcbs'
        extra : dict
            Extra metadata about the command run.
        raw_data : list[dict]
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
        symbol=symbol, financial_statement=name, period=period
    )
    symbol = params.symbol
    name = params.financial_statement
    period = params.period

    # Map user friendly string to API value
    period_mapping = {
        "annual": 1,
        "quarter": 0,
    }
    is_annual = period_mapping.get(period)

    name_mapping = {
        "income": "incomestatement",
        "balance": "balancesheet",
        "cash": "cashflow",
    }
    name_api = name_mapping.get(name)  # type: ignore

    # API call
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/finance/{symbol}/{name_api}"
    query_params = {"yearly": is_annual, "isAll": True}
    response = requests.get(url, params=query_params, headers=tcbs_headers)
    check_response_error(response)
    data = response.json()
    rows = data

    if not rows:
        raise EmptyDataError(f"No data found for the symbol {symbol}.")

    # Add 'period' column
    for r in rows:
        r["period"] = period

    # Unpivot the rows dict
    df = pd.DataFrame(rows)
    df = pd.melt(
        df,
        id_vars=["ticker", "period", "year", "quarter"],
        var_name="ITEMS",
        value_name="values",
    )

    # Convert df to a list of dicts where each dictionary represents a row in the DataFrame
    # This format is convenient to process the data row-wise, i.e. unpacking the dict to a pydantic model
    rows = df.to_dict(orient="records")
    output = [TcbsEquityFundamentalIncomeData(**r) for r in rows]

    # Additional metadata about the command run
    extra = generate_extra_metadata(symbol=symbol, result=output, api_url=url)

    print(
        f"Retrieved {extra.get('records_count',[])} data point for {name_mapping.get(name)}, of stock ticker {symbol}."
    )

    return VfObject(results=output, provider="tcbs", extra=extra, raw_data=data)
