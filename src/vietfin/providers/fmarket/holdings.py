import requests

from vietfin.standard_models.vfobject import VfObject
from vietfin.utils.errors import VietFinError
from .utils import fmarket_headers, get_fund_id
from .models.fund_holdings import FmarketFundHoldingsData


def holdings(symbol: str) -> VfObject:
    """
    Retrieve a list of top 10 holdings in the specified fund from the Fmarket API.

    Parameters
    ----------
    symbol : str
        Fund short name.

    Returns
    -------
    VfObject
        The current top 10 holdings of the selected fund.

    """

    # Retrieve fund_id matching the given symbol
    fund_id = get_fund_id(symbol)

    # API call
    url = f"https://api.fmarket.vn/res/products/{fund_id}"
    response = requests.get(url, headers=fmarket_headers, cookies=None)

    if response.status_code != 200:
        raise requests.exceptions.HTTPError(
            f"Error in API response: {response.status_code} - {response.text}"
        )

    data = response.json()
    list_of_holdings = []

    # NOTE: there are funds which allocate to either equities or fixed income securities, or both
    # We need to parse the data from two separated nodes and merge into one output

    # Extract top holdings in equity
    rows = data["data"]["productTopHoldingList"]
    fund_top_holdings_stock = [FmarketFundHoldingsData(**r) for r in rows]

    # Extract top holdings in fixed income securities
    rows = data["data"]["productTopHoldingBondList"]
    fund_top_holdings_bond = [FmarketFundHoldingsData(**r) for r in rows]

    # Output the merged list
    list_of_holdings = fund_top_holdings_stock + fund_top_holdings_bond

    if len(list_of_holdings) == 0:
        raise VietFinError(f"No holdings found for given fund {symbol}.")
    else:
        return VfObject(results=list_of_holdings, provider="fmarket")
