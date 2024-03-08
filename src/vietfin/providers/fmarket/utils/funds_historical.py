"""Fmarket Funds Historical function."""

from datetime import datetime
import requests
from pydantic import model_validator

from vietfin.providers.fmarket.utils.helpers import fmarket_headers, get_fund_id
from vietfin.providers.fmarket.models.fund_historical_nav import (
    FmarketFundHistoricalNavData,
)
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    generate_extra_metadata,
    check_response_error,
    BaseDateParams,
    BaseOtherParams,
)
from vietfin.utils.errors import EmptyDataError


class HistoricalParams(BaseDateParams):
    """Class to validate params of historical() function.

    Extended validation rules:
    - enforce date string format as 'yyyyMMdd' used by the Fmarket API
    """

    @model_validator(mode="after")
    def validate_date_format(self) -> "HistoricalParams":
        """Enforce date string format as 'yyyyMMdd'."""

        start = self.start_date
        end = self.end_date
        current_date = datetime.now()

        # Enforce start_date string format
        self.start_date = datetime.strptime(start, "%Y-%m-%d").strftime(  # type: ignore
            "%Y%m%d"
        )

        # Enforce end_date string format
        if datetime.strptime(end, "%Y-%m-%d") > current_date:  # type: ignore
            self.end_date = current_date.strftime("%Y%m%d")

        self.end_date = datetime.strptime(end, "%Y-%m-%d").strftime(  # type: ignore
            "%Y%m%d"
        )

        return self


def historical(
    symbol: str, start_date: str | None = None, end_date: str | None = None
) -> VfObject:
    """Retrieve historical NAV of selected fund from Fmarket provider.

    Parameters
    ----------
    symbol : str
        Fund short name.
    start_date : str, optional
        start date string in YYYY-MM-DD format
        default is None, which means the earliest available NAV data point
    end_date : str, optional
        end date string in YYYY-MM-DD format
        default is None, which means the current date, the latest available NAV data point

    Returns
    -------
    VfObject
        results : list[FmarketFundHistoricalNavData]
            avalaible daily NAV data points of the selected fund
        provider : str
            provider name "fmarket"
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

    # Validate input
    params = HistoricalParams(
        start_date=start_date, end_date=end_date
    )
    start_date = params.start_date
    end_date = params.end_date

    other_params = BaseOtherParams(symbol=symbol)
    symbol = other_params.symbol

    # Retrieve fund_id matching given symbol
    fund_id = get_fund_id(symbol)

    # API call
    url = "https://api.fmarket.vn/res/product/get-nav-history"
    payload = {
        "isAllData": 1,
        "productId": fund_id,
        "fromDate": start_date,
        "toDate": end_date,
    }
    response = requests.post(url, json=payload, headers=fmarket_headers)
    check_response_error(response)
    data = response.json()

    rows = data["data"]
    if not rows:
        raise EmptyDataError

    # Unpack json to data model
    fund_nav = [FmarketFundHistoricalNavData(**r) for r in rows]

    # NOTE: Fmarket API does not accept an arbitrary start_date.
    # It takes only the [3mo, 6mo, 12mo, 36mo] counting back from the current date.
    # Any start_date other than these dynamically pre-defined values will be ignored by Fmarket,
    #     and considered as None.

    # A workaround to filter out the data that is not within the input date range
    start = datetime.strptime(params.start_date, "%Y%m%d").date()  # type: ignore
    end = datetime.strptime(params.end_date, "%Y%m%d").date()  # type: ignore

    fund_nav = [
        item
        for item in fund_nav
        if start <= item.date_nav <= end
    ]

    # Additional metadata about the command run
    extra = generate_extra_metadata(symbol=symbol, result=fund_nav, api_url=url)

    print(
        f"Retrieved {extra.get('records_count',[])} daily NAV data point for fund {symbol}."
    )

    return VfObject(
        results=fund_nav,
        provider="fmarket",
        extra=extra,
        raw_data=data,
    )
