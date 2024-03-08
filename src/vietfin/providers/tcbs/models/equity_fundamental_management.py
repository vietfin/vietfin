"""TCBS Equity Fundamental Management Model."""

from vietfin.abstract.data import Data


class TcbsEquityFundamentalManagementData(Data):
    """TCBS Equity Fundamental Management Data."""

    __alias_dict__ = {
        "name": "name",
        "title": "position",
        "weight": "ownPercent",
        "symbol": "ticker",
    }

    name: str | None  # Name of the key executive.
    title: str | None  # Designation of the key executive.
    weight: float  # Weight of the stock ownership.
    symbol: str  # Symbol representing the entity requested in the data.
