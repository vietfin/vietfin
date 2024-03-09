"""SSI Equity Fundamental Income command."""

from datetime import datetime
from io import BytesIO
import re

import requests
import pandas as pd

from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    check_response_error,
    generate_extra_metadata,
    PERIODS,
    FINANCIAL_STATEMENTS,
)
from vietfin.providers.ssi.utils.helpers import ssi_headers
from vietfin.providers.ssi.models.equity_fundamental_income import (
    SsiEquityFundamentalIncomeData,
)
from vietfin.providers.ssi.utils.equity_search import search
from vietfin.utils.errors import EmptyDataError


def get_financial_report(
    symbol: str, name: FINANCIAL_STATEMENTS = "income", period: PERIODS = "annual"
) -> VfObject:
    """Retrieve Equity Fundamental financial statement data of the given ticker.

    Data from SSI provider

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
        results : list[SsiEquityFundamentalIncomeData]
            historical income/balance/cashflow data of the given ticker
        provider : str
            provider name 'ssi'
        extra : dict
            Extra metadata about the command run.
        raw_data : dict[list]
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
    symbol = symbol.upper()

    # Map user friendly string to API value
    period_mapping = {
        "annual": "Yearly",
        "quarter": "Quarterly",
    }
    period_api = period_mapping.get(period)

    name_mapping = {
        "income": "IncomeStatement",
        "balance": "BalanceSheet",
        "cash": "CashFlow",
    }
    name_api = name_mapping.get(name)  # type: ignore

    # Lookup organ_code matching ticker symbol
    # if symbol not valid, "search" function will raise error
    lookup_dict = search(symbol).to_dict()
    organ_code = lookup_dict.get("organ_code")[0]  # type: ignore

    # API call
    number_periods = 100  # i.e. retrieve 100 years or 100 quarters of data
    current_year = str(datetime.now().year)

    url = f"https://fiin-fundamental.ssi.com.vn/FinancialStatement/Download{name_api}?language=en&OrganCode={organ_code}&Skip=0&Frequency={period_api}&numberOfPeriod={number_periods}&latestYear={current_year}"
    response = requests.get(url, headers=ssi_headers)
    check_response_error(response)

    # Parse API response then remove the first 7 rows and last 3 rows
    df = pd.read_excel(BytesIO(response.content), skiprows=7)
    df = df.iloc[:-3]

    if df.empty:
        raise EmptyDataError(f"No data found for the symbol {symbol}.")

    # Make column labels of cashflow statement similar to other two statements
    if name == "cash":
        df = df.rename(columns={"Unnamed: 0": "ITEMS"})

    # Prepare raw_data for VfObject
    raw = df.to_dict(orient="list")

    # Add 'period' column
    df["period"] = period

    # Unpivot the DataFrame
    # This regex match any string that starts with 'Q' followed by 1 or 2 digits and a space,
    # then ends with 4 digits (for quarters) or just 4 digits (for years)
    year_quarter_regex = re.compile(r"^(Q\d{1,2}\s)?\d{4}$")
    # Identify column labels that represent years or quarters
    period_columns = [
        col for col in df.columns if year_quarter_regex.match(col)
    ]

    df = pd.melt(
        df,
        id_vars=["ITEMS", "period"],
        value_vars=period_columns,
        var_name="fiscal_period",
        value_name="values",
    )

    # Convert df to a list of dicts where each dict represents a row in the DataFrame
    # This format is convenient to process the data row-wise, i.e. unpacking the dict to a pydantic model
    rows = df.to_dict(orient="records")
    output = [SsiEquityFundamentalIncomeData(**r) for r in rows]  # type: ignore

    # Additional metadata about the command run
    extra = generate_extra_metadata(symbol=symbol, result=output, api_url=url)

    print(
        f"Retrieved {extra.get('records_count',[])} data point for {name_mapping.get(name)}, of stock ticker {symbol}."
    )

    return VfObject(results=output, provider="ssi", extra=extra, raw_data=raw)
