from datetime import datetime
import requests

from .utils import fmarket_headers, get_fund_id
from .models.fund_historical_nav import FmarketFundHistoricalNavData
from vietfin.standard_models.vfobject import VfObject


def historical(symbol: str) -> VfObject:
    """Retrieve historical NAV of selected fund.

    Parameters
    ----------
    symbol : str
        Fund short name.
    start_date
    end_date

    Returns
    -------
    VfObject
        all avalaible daily NAV data points of the selected fund

    """

    # Retrieve fund_id matching given symbol
    fund_id = get_fund_id(symbol)

    # API call
    # Get the current date and format it as 'yyyyMMdd'
    current_date = datetime.now().strftime("%Y%m%d")
    url = "https://api.fmarket.vn/res/product/get-nav-history"
    payload = {
        "isAllData": 1,
        "productId": fund_id,
        "fromDate": None,
        "toDate": current_date,
    }
    response = requests.post(url, json=payload, headers=fmarket_headers)

    if response.status_code != 200:
        raise requests.exceptions.HTTPError(
            f"Error in API response: {response.status_code} - {response.text}"
        )

    data = response.json()
    rows = data["data"]
    fund_historical_nav = [FmarketFundHistoricalNavData(**r) for r in rows]

    return VfObject(results=fund_historical_nav, provider="fmarket")
