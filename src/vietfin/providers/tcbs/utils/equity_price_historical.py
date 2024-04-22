"""TCBS Equity Price Historical command."""

from datetime import timedelta, datetime
from typing import Literal

import httpx as requests
from pydantic import field_validator

from vietfin.providers.tcbs.utils.helpers import tcbs_headers
from vietfin.providers.tcbs.models.equity_price_historical import (
    TcbsEquityHistoricalPriceData,
)
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    generate_extra_metadata,
    check_response_error,
    BaseDateParams,
    BaseOtherParams,
)
from vietfin.utils.errors import EmptyDataError


# UTLIS


class HistoricalParams(BaseOtherParams):
    """Class to validate params of historical() function.

    Extended validation rules:
    - interval string must be "D"
    """

    @field_validator("interval")
    @classmethod
    def validate_interval(cls, v: str) -> str:
        """Validate interval string."""

        allowed_intervals = ["D", "1D", "1d"]
        v = v.upper()
        if v not in allowed_intervals:
            raise ValueError(
                f"Invalid interval: {v}. TCBS only supports interval: 1d."
            )
        return "D"


QueryParams = Literal["stock", "index", "derivative"]
ApiEndpoint = Literal["stock", "futures"]


# MAIN


def historical(
    symbol: str,
    start_date: str,
    end_date: str,
    interval: str = "D",
    api_endpoint: ApiEndpoint = "stock",
    query_param: QueryParams = "stock",
) -> VfObject:
    """Retrieve Historical price data of a specific ticker.

    Data from TCBS tcbs.com.vn

    Parameters
    ----------
    symbol : str
        stock/etf/index/futures ticker
    interval : str
        time interval. Options: "D" (default)
    start_date : str
        start date string in YYYY-MM-DD format
    end_date : str
        end date string in YYYY-MM-DD format

    Returns
    -------
    VfObject
        results : list[TcbsEquityHistoricalPriceData]
            equity historical price data of the given ticker
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
    date_params = BaseDateParams(
        start_date=start_date,
        end_date=end_date,
    )
    start_date = date_params.start_date  # type: ignore
    end_date = date_params.end_date  # type: ignore
    params = HistoricalParams(
        symbol=symbol,
        interval=interval,  # type: ignore
    )
    symbol = params.symbol
    interval = params.interval

    # convert str to date object
    input_start_date = datetime.strptime(start_date, "%Y-%m-%d").date()  # type: ignore
    input_end_date = datetime.strptime(end_date, "%Y-%m-%d").date()  # type: ignore

    # API logic: returns n daily price data points (max 365, operating days) counting back from the end_date timestamp
    # convert str to datetime object
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")  # type: ignore
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")  # type: ignore

    # Loop until all data within the date range is fetched
    url_list = []
    data = []
    equity_price_historical: list[TcbsEquityHistoricalPriceData] = []

    while start_dt < end_dt:
        # Calculate the number of days for the current chunk (up to 365 days)
        delta_days = (end_dt - start_dt).days
        chunk_days = min(delta_days, 365)

        # Calculate end timestamp for the current chunk
        current_end_dt = start_dt + timedelta(days=chunk_days)
        current_end_timestamp = int(current_end_dt.timestamp())

        # API call
        url = f"https://apipubaws.tcbs.com.vn/{api_endpoint}-insight/v2/stock/bars-long-term?ticker={symbol}&type={query_param}&resolution={interval}&to={current_end_timestamp}&countBack={chunk_days}"
        response = requests.get(url, headers=tcbs_headers)
        check_response_error(response)
        data_chunk = response.json()  # data type : list-of-dicts
        rows = data_chunk.get("data", [])

        if not rows:
            break  # stop if no more data

        url_list.append(url)
        data.append(data_chunk)

        # Add each element of rows data to the output list
        equity_price_historical.extend(
            [TcbsEquityHistoricalPriceData(**r) for r in rows]
        )

        # Update start_dt to the next chunk's start date
        start_dt = current_end_dt

    if not equity_price_historical:
        raise EmptyDataError(f"No data found for this {symbol} ticker.")

    # Filter out the data that is not within the input date range
    equity_price_historical = [
        item
        for item in equity_price_historical
        if input_start_date <= item.date <= input_end_date
    ]

    # Generate extra metadata
    extra = generate_extra_metadata(
        symbol=symbol, result=equity_price_historical, api_url=url_list
    )

    print(
        f"Retrieved {extra.get('records_count',[])} historical price data point for symbol {symbol}."
    )

    return VfObject(
        results=equity_price_historical,
        provider="tcbs",
        extra=extra,
        raw_data=data,
    )
