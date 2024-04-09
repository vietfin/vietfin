"""DNSE Equity Price Historical command."""

from datetime import datetime, timedelta
from typing import Literal

import httpx as requests
from pydantic import field_validator, model_validator

from vietfin.providers.dnse.utils.helpers import dnse_headers
from vietfin.providers.dnse.models.equity_price_historical import (
    DnseEquityHistoricalPriceData,
)
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    generate_extra_metadata,
    check_response_error,
    BaseDateParams,
    BaseOtherParams,
    convert_dictlists_to_listdicts,
)
from vietfin.utils.errors import EmptyDataError


# UTILS


class HistoricalParams(BaseDateParams):
    """Class to validate params of historical() function.

    Extended validation rules:
    - interval string must be one of the following: 1m, 15m, 30m, 1h, 1d
    - start_date and end_date must be in the range of 90-day limit of DNSE API
    """

    interval: str

    @field_validator("interval")
    def validate_interval(cls, v: str) -> str:
        """Validate interval string."""

        # Mapping from the user-friendly strings to the API's expected values
        interval_map = {
            "1m": "1",
            "15m": "15",
            "30m": "30",
            "1h": "1H",
            "1d": "1D",
        }

        v = v.lower()
        if v not in interval_map:
            allowed_intervals = ", ".join(interval_map.keys())
            raise ValueError(
                f"Invalid interval: {v}. Allowed intervals for provider DNSE are [{allowed_intervals}]."
            )

        return interval_map[v]

    @model_validator(mode="after")
    def validate_date_range(self) -> "HistoricalParams":
        """Enforce valid date range for short intervals.

        The DNSE API allows a maximum range of 90 days of data (counting back from the current date)
            to be retrieved for short intervals [1m, 15m, 30m, 1h].
        If the user requests for a date range greater than this max number of days,
            adjust the date range to the closest available date.

        Parameters
        ----------
        start_date
            start date string in YYYY-MM-DD format
        end_date
            end date string in YYYY-MM-DD format
        interval
            time interval. Options: ["1", "15", "30", "1H"]

        Returns
        -------
        HistoricalParams
            the adjusted (if necessary) attributes of the HistoricalParams object
                start_date
                end_date
        """
        interval = self.interval
        start_date = self.start_date
        end_date = self.end_date

        if interval not in ("1", "15", "30", "1H"):
            return self

        # Mapping from the the API's expected values to user-friendly strings
        interval_map = {
            "1": "1m",
            "15": "15m",
            "30": "30m",
            "1H": "1h",
        }

        max_range = timedelta(days=90)

        # If end_date is older than 90 days from today adjust it to current date
        end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")  # type: ignore
        if datetime.now() - end_date_dt > max_range:
            end_date_dt = datetime.now()
            self.end_date = end_date_dt.strftime("%Y-%m-%d")
            print(
                f"Adjusting end_date to {self.end_date} due to DNSE API limit of 90 days of data for interval {interval_map[interval]}."
            )

        # Adjust the start_date to the closest available date if end - start > 90 days
        start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")  # type: ignore
        end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")  # type: ignore
        if end_date_dt - start_date_dt > max_range:
            start_date_dt = end_date_dt - max_range
            self.start_date = start_date_dt.strftime("%Y-%m-%d")
            print(
                f"Adjusting start_date to {self.start_date} due to DNSE API limit of 90 days of data for interval {interval_map[interval]}."
            )

        return self


QueryParams = Literal["stock", "index"]


# MAIN


def historical(
    symbol: str,
    start_date: str,
    end_date: str,
    interval: str = "1D",
    query_param: QueryParams = "stock",
) -> VfObject:
    """Retrieve Equity Historical price of a specific ticker from DNSE provider.

    Data from DNSE entrade.com.vn

    Paramaters
    ----------
    symbol : str
        stock/index ticker
    interval : str
        time interval. Options: 1m, 15m, 30m, 1h, 1d (default)
        A limit of 90 days is applied to short intervals [1m, 15m, 30m, 1h]
    start_date : str
        start date string in YYYY-MM-DD format
    end_date : str
        end date string in YYYY-MM-DD format
    query_param : QueryParams
        type of query params of API url. Options: "stock" (default) or "index"

    Returns
    -------
    VfObject
        results : list[DnseEquityHistoricalPriceData]
            equity historical price data
        provider : str
            provider name "dnse"
        extra : dict
            extra metadata about the command run
        raw_data : dict
            raw data from the API call

    Raises
    ------
    HttpError
        if the API call failed
    EmptyDataError
        if the API response is empty
    ValidationError
        if the input param are invalid
    """
    # Validate input param
    params = HistoricalParams(
        start_date=start_date,
        end_date=end_date,
        interval=interval,
    )
    interval = params.interval
    start_date = params.start_date  # type: ignore
    end_date = params.end_date  # type: ignore

    other_params = BaseOtherParams(symbol=symbol)
    symbol = other_params.symbol

    start_timestamp = int(datetime.strptime(start_date, "%Y-%m-%d").timestamp())
    end_timestamp = int(datetime.strptime(end_date, "%Y-%m-%d").timestamp())

    # API call
    url = f"https://services.entrade.com.vn/chart-api/v2/ohlcs/{query_param}?from={start_timestamp}&to={end_timestamp}&symbol={symbol}&resolution={interval}"
    response = requests.get(url, headers=dnse_headers)

    check_response_error(response)

    # The structure of this json `data` is a dict-of-lists where the values are lists of equal length
    data = response.json()

    # Transpose the dict-of-lists structure into a list-of-dicts structure
    rows = convert_dictlists_to_listdicts(data)

    if not rows:
        raise EmptyDataError

    # Unpack json to data model
    equity_price_historical = [DnseEquityHistoricalPriceData(**r) for r in rows]

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol,
        result=equity_price_historical,
        api_url=url,
    )

    print(
        f"Retrieved {extra.get('records_count',[])} historical price data point for symbol {symbol}."
    )

    return VfObject(
        results=equity_price_historical,
        provider="dnse",
        extra=extra,
        raw_data=data,
    )
