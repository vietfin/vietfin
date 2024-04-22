"""SSI Etf Historical function."""

from datetime import datetime, timedelta

import httpx as requests
from pydantic import field_validator, model_validator

from vietfin.providers.ssi.utils.helpers import ssi_headers
from vietfin.abstract.vfobject import VfObject
from vietfin.providers.ssi.models.etf_historical import SsiEtfHistoricalData
from vietfin.utils.helpers import (
    generate_extra_metadata,
    check_response_error,
    BaseDateParams,
    convert_dictlists_to_listdicts,
    BaseOtherParams,
)
from vietfin.utils.errors import EmptyDataError


class HistoricalParams(BaseDateParams):
    """Class to validate params of historical() function.

    Extended validation rules:
    - interval string must be converted to "1" or "1D"
    - for short interval "1", start_date and end_date must be within 30 days from current date
    """

    interval: str = "1d"

    @field_validator("interval")
    @classmethod
    def validate_interval(cls, v: str) -> str:
        """Validate interval string."""

        # Mapping from the user-friendly strings to the API's expected values
        interval_map = {
            "1d": "1D",
            "1h": "1",
        }

        v = v.lower()
        if v not in interval_map:
            allowed_intervals = ", ".join(interval_map.keys())
            raise ValueError(
                f"Invalid interval: {v}. Allowed intervals for provider SSI are [{allowed_intervals}]."
            )

        return interval_map[v]

    @model_validator(mode="after")
    def validate_date_range(self) -> "HistoricalParams":
        """Enforce valid date range for short intervals.

        The SSI API allows a maximum range of 30 days of data (counting back from the current date)
            to be retrieved for short intervals [1h].
        If the user requests for a date range greater than this max number of days,
            adjust the start_date to the closest available date.

        Parameters
        ----------
        start_date
            start date string in YYYY-MM-DD format
        end_date
            end date string in YYYY-MM-DD format
        interval
            time interval. Options: ["1"]

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

        if interval not in ("1"):
            return self

        # Mapping from the the API's expected values to user-friendly strings
        interval_map = {
            "1": "1h",
        }

        max_range = timedelta(days=30)

        # Adjust end_date to current date if it is older than 30 days from today
        end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")  # type: ignore
        if datetime.now() - end_date_dt > max_range:
            end_date_dt = datetime.now()
            self.end_date = end_date_dt.strftime("%Y-%m-%d")
            print(
                f"Adjusting end_date to {self.end_date} due to SSI API limit of 30 days of data for interval {interval_map[interval]}."
            )

        # Adjust the start_date to the closest available date if end - start > 30 days
        start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")  # type: ignore
        end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")  # type: ignore
        if end_date_dt - start_date_dt > max_range:
            start_date_dt = end_date_dt - max_range
            self.start_date = start_date_dt.strftime("%Y-%m-%d")
            print(
                f"Adjusting start_date to {self.start_date} due to SSI API limit of 30 days of data for interval {interval_map[interval]}."
            )

        return self


def historical(
    symbol: str, start_date: str, end_date: str, interval: str
) -> VfObject:
    """Etf Historical. Retrieve historical price data of an ETF from SSI provider.

    Parameters
    ----------
    symbol : str
        The ticker symbol of the Etf/stock to search for.

    Returns
    -------
    VfObject
        results : list[SsiEtfHistoricalData]
            historical price of an ETF/stock provided by SSI.
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

    # Validate params
    other_params = BaseOtherParams(symbol=symbol)
    symbol = other_params.symbol
    
    params = HistoricalParams(
        start_date=start_date,
        end_date=end_date,
        interval=interval,
    )
    interval = params.interval
    start_date = params.start_date  # type: ignore
    end_date = params.end_date  # type: ignore

    # convert date string into timestamp
    start = int(datetime.strptime(start_date, "%Y-%m-%d").timestamp())
    end = int(datetime.strptime(end_date, "%Y-%m-%d").timestamp())

    # API call
    url = f"https://iboard.ssi.com.vn/dchart/api/history?resolution={interval}&symbol={symbol}&from={start}&to={end}"
    response = requests.get(url, headers=ssi_headers)
    check_response_error(response)
    data = response.json()

    rows = convert_dictlists_to_listdicts(data)
    if not rows:
        raise EmptyDataError

    # Unpack json dict to data model
    etf_list: list[SsiEtfHistoricalData] = [
        SsiEtfHistoricalData(**r) for r in rows
    ]

    # Additional metadata about the command run
    extra = generate_extra_metadata(symbol=symbol, result=etf_list, api_url=url)

    print(
        f"Retrieved {extra.get('records_count',[])} historical price data for symbol {symbol}."
    )

    return VfObject(
        results=etf_list,
        provider="ssi",
        extra=extra,
        raw_data=data,
    )
