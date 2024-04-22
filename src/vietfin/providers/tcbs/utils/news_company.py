"""TCBS News Company command."""

import httpx as requests

from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import (
    check_response_error,
    generate_extra_metadata,
    BaseOtherParams,
)
from vietfin.providers.tcbs.utils.helpers import tcbs_headers
from vietfin.providers.tcbs.models.news_company import (
    TcbsNewsCompanyData,
)
from vietfin.utils.errors import EmptyDataError


def company(symbol: str, limit: int = 100) -> VfObject:
    """Retrieve News Company data of the given ticker.

    Data from TCBS tcbs.com.vn

    Parameters
    ----------
    symbol : str
        stock ticker
    limit : int
        limit of number of records to be retrieved
        0 will return all records
        Default 100

    Returns
    -------
    VfObject
        results : list[TcbsNewsCompanyData]
            news company data of the given ticker
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
        symbol=symbol,
        limit=limit,
    )
    symbol = params.symbol
    limit = params.limit

    # API logic: paginated returns up to 100 records per page per single API call
    page_size = 100 if (limit == 0 or limit > 100) else limit
    page = 0  # start from the 1st page
    news_company = []
    data = []
    url_list = []

    # API call
    while True:
        url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{symbol}/activity-news?page={page}&size={page_size}"
        response = requests.get(url, headers=tcbs_headers)
        check_response_error(response)
        data_chunk = response.json()
        rows = data_chunk.get("listActivityNews", [])

        if not rows:
            break  # stop if no more data

        url_list.append(url)
        data.append(data_chunk)

        # Add each element of rows into the output list
        news_company.extend([TcbsNewsCompanyData(**r) for r in rows])

        if 0 < limit <= len(news_company):
            news_company = news_company[:limit]
            break  # stop if limit reached

        # increment page number to continue fetching until no more data
        page += 1

    if not news_company:
        raise EmptyDataError(f"No data found for the symbol {symbol}.")

    # Additional metadata about the command run
    extra = generate_extra_metadata(symbol=symbol, result=news_company, api_url=url_list)

    print(
        f"Retrieved {extra.get('records_count',[])} news titles for stock ticker {symbol}."
    )

    return VfObject(results=news_company, provider="tcbs", extra=extra, raw_data=data)
