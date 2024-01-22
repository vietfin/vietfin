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

# Constants

DEFAULT_SYMBOL = ""
DEFAULT_FUND_TYPE = ""

# Helpers

def get_fund_id(symbol: str) -> int:
    """Lookup FundID based on Fund short name.

    Empty query by default returns a list of all available funds short name and their FundID

    Parameters
    ----------
    symbol : str
        Fund short name.

    Returns
    -------
    fund_id : int
        DataFrame of filtered funds
    """

    symbol = symbol.upper()

    payload = {
        "searchField": symbol,
        "types": ["NEW_FUND", "TRADING_FUND"],
        "pageSize": 100,
    }

    url = "https://api.fmarket.vn/res/products/filter"
    payload = json.dumps(payload)
    response = requests.post(url, headers=fmarket_headers, data=payload)

    if response.status_code != 200:
        raise requests.exceptions.HTTPError(
            f"Error in API response: {response.status_code} - {response.text}"
        )

    data = response.json()
    
    # This logic is handcrafted for the data structure returned by the API
    if data["data"]["total"] == 0:
        raise VietFinError(f"No fund found for symbol {symbol}")
    elif data["data"]["total"] > 1:
        raise VietFinError(f"Multiple funds found for the given symbol {symbol}")
    else:
        fund_id = int(data["data"]["rows"][0]["id"])
    
    return fund_id
