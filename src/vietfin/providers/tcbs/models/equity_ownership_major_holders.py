"""TCBS Equity Ownership Major Holders Model."""

from vietfin.abstract.data import Data


class TcbsEquityOwnershipMajorHoldersData(Data):
    """TCBS Equity Ownership Major Holders Data."""

    __alias_dict__ = {
        "investor_name": "name",
        "weight": "ownPercent",
    }

    investor_name: str  # Investor name of the stock ownership.
    weight: float  # Weight of the stock ownership.
