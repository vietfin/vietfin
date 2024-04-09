# """Cafef Equity Ownership Proprietary Trading command."""

import httpx as requests

from vietfin.providers.cafef.utils.helpers import cafef_headers
from vietfin.providers.cafef.models.equity_ownership_prop import (
    CafefEquityOwnershipPropTradingData,
)
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    generate_extra_metadata,
    check_response_error,
    BaseDateParams,
    BaseOtherParams,
)
from vietfin.utils.errors import EmptyDataError


def prop(
    symbol: str,
    start_date: str | None = None,
    end_date: str | None = None,
) -> VfObject:
    """Retrieve Equity Ownership Proprietary Trading data of a specific ticker from CafeF provider.

    Data from https://s.cafef.vn/lich-su-giao-dich-vnm-3.chn

    Paramaters
    ----------
    symbol : str
        stock/index ticker
    start_date : str
        start date string in YYYY-MM-DD format
    end_date : str
        end date string in YYYY-MM-DD format

    Returns
    -------
    VfObject
        results : list[CafefEquityOwnershipPropTradingData]
            equity ownership proprietary trading data
        provider : str
            provider name "cafef"
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
    params = BaseDateParams(
        start_date=start_date,
        end_date=end_date,
    )
    start_date = params.start_date  # type: ignore
    end_date = params.end_date  # type: ignore

    other_params = BaseOtherParams(symbol=symbol)
    symbol = other_params.symbol

    # API call
    page_index = 1
    page_size = 20
    trading_data = []
    url_list = []
    data = []

    while True:
        url = f"https://s.cafef.vn/Ajax/PageNew/DataHistory/GDTuDoanh.ashx?Symbol={symbol}&StartDate={start_date}&EndDate={end_date}&PageIndex={page_index}&PageSize={page_size}"
        response = requests.get(url, headers=cafef_headers)
        check_response_error(response)
        data_chunk = response.json()
        rows = data_chunk.get("Data", {}).get("Data", {}).get("ListDataTudoanh", [])

        if not rows:
            break  # stop if no more data

        url_list.append(url)
        data.append(data_chunk)

        # Unpack dictionary to data model and return the results
        trading_data.extend([CafefEquityOwnershipPropTradingData(**r) for r in rows])

        # increment page_index to continue fetching until no more data
        page_index += 1


    if not trading_data:
        raise EmptyDataError

    # Additional metadata about the command run
    extra = generate_extra_metadata(
        symbol=symbol,
        result=trading_data,
        api_url=url_list,
    )

    print(
        f"Retrieved {extra.get('records_count',[])} proprietary trading data point for symbol {symbol}."
    )

    return VfObject(
        results=trading_data,
        provider="cafef",
        extra=extra,
        raw_data=data,
    )
