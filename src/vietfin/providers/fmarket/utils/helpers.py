"""Fmarket utils."""

import json

import requests

from vietfin.utils.errors import VietFinError


# Requests headers

fmarket_headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "vi",
    "content-type": "application/json",
    "sec-ch-ua": '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "referrer": "https://fmarket.vn/",
}


# Helpers


def get_fund_id(symbol: str) -> int:
    """Lookup FundID based on Fund short name from Fmarket provider.

    Parameters
    ----------
    symbol : str
        Fund short name.

    Returns
    -------
    fund_id : int
        FundID matching the given symbol.
        
    """

    payload = {
        "searchField": symbol,
        "types": ["NEW_FUND", "TRADING_FUND"],
        "pageSize": 100,
    }
    payload = json.dumps(payload)  # type: ignore

    url = "https://api.fmarket.vn/res/products/filter"
    response = requests.post(url, headers=fmarket_headers, data=payload)

    if response.status_code != 200:
        raise requests.exceptions.HTTPError(
            f"Error in API response: {response.status_code} - {response.text}"
        )

    data = response.json()

    # This logic is handcrafted for the data structure of response from the API
    if data["data"]["total"] == 0:
        raise VietFinError(f"No fund found for symbol {symbol}. Please check the symbol.")
    elif data["data"]["total"] > 1:
        raise VietFinError(
            f"Multiple funds found for the given symbol {symbol}. Please check the symbol."
        )
    else:
        fund_id = int(data["data"]["rows"][0]["id"])

    return fund_id
