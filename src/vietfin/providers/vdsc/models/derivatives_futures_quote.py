"""VDSC Rong Viet Derivatives Futures Quote Model."""

from datetime import time

from vietfin.abstract.data import Data


class VdscDerivativesFuturesQuoteData(Data):
    """VDSC Rong Viet Derivatives Futures Quote Data."""

    __alias_dict__ = {
        "time": "TradeTime",
        "symbol": "Code",
        "exchange": "FloorCode",
        "ref_price": "RefPrice",
        "high_price": "HigPrice",
        "low_price": "LowPrice",
        "matched_vol": "MatchedVol",
        "matched_price": "MatchedPrice",
        "matched_change": "MatchedChange",
        "avg_price": "AvgPrice",
        "matched_total_vol": "MatchedTotalVol",
        "bid_price_1": "BidPrice1",
        "bid_vol_1": "BidVol1",
        "bid_price_2": "BidPrice2",
        "bid_vol_2": "BidVol2",
        "bid_price_3": "BidPrice3",
        "bid_vol_3": "BidVol3",
        "offer_price_1": "OfferPrice1",
        "offer_vol_1": "OfferVol1",
        "offer_price_2": "OfferPrice2",
        "offer_vol_2": "OfferVol2",
        "offer_price_3": "OfferPrice3",
        "offer_vol_3": "OfferVol3",
        "ceil_price": "CeiPrice",
        "floor_price": "FlrPrice",
        "am_pm": "AmPm",
    }

    time: time  # Time of the latest trade execution
    symbol: str  # Unique identifier representing the futures contract
    exchange: str  # Unique identifier representing the trading floor or exchange
    ref_price: float  # Reference or opening price for the trading session
    high_price: float  # Highest price reached during the current trading session
    low_price: float  # Lowest price reached during the current trading session
    matched_vol: int  # Volume of contracts traded in the last match
    matched_price: float  # Price at which the last trade occurred
    matched_change: float  # Change in price from the last matched trade
    avg_price: float  # Average price of the contracts traded
    matched_total_vol: int  # Total volume of contracts traded
    bid_price_1: float  # Best bid price
    bid_vol_1: int  # Best bid volume
    bid_price_2: float
    bid_vol_2: int
    bid_price_3: float
    bid_vol_3: int
    offer_price_1: float  # Best offer (ask) price
    offer_vol_1: int  # Best offer (ask) volume
    offer_price_2: float
    offer_vol_2: int
    offer_price_3: float
    offer_vol_3: int
    ceil_price: float  # Closing price of the previous trading day
    floor_price: float  # The lowest price level at which a futures contract or security is allowed to trade
    am_pm: str  # Indicates whether it is the morning (AM) or afternoon (PM) trading session
