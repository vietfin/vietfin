"""TCBS Equity Ownership Insider Trading Model."""

from datetime import datetime, date
from typing import Any

from pydantic import field_validator

from vietfin.abstract.data import Data

class TcbsEquityOwnershipInsiderTradingData(Data):
    """TCBS Equity Ownership Insider Trading Data."""

    __alias_dict__ = {
        "symbol": "ticker",
        "transaction_price": "price",
        "securities_transacted": "quantity",
        "filing_date": "anDate",
        "acquisition_or_disposition": "dealingAction",
        "owner_type": "dealingMethod",
    }

    filing_date: str | date  # Filing date of the trade.
    acquisition_or_disposition: str  # Acquisition or disposition of the shares. e.g. Mua, Bán
    transaction_price: float | Any  # Price at which the transaction was executed.
    securities_transacted: float | Any  # Number of securities transacted by the reporting individual.
    owner_type: int | str  # Type of the owner. e.g. Cổ đông lớn, Cổ đông sáng lập, Cổ đông nội bộ
    symbol: str  # Ticker of the company.
    
    @field_validator("filing_date")
    @classmethod
    def parse_date(cls, v: str) -> date:
        """Parse date from string format 'dd/mm/yy' to date."""
        return datetime.strptime(v, "%d/%m/%y").date()
    
    @field_validator("acquisition_or_disposition")
    @classmethod
    def parse_acquisition_or_disposition(cls, v: str) -> str:
        """Parse acquisition_or_disposition."""
        v = v.lower()
        v_map = {
            "0": "Mua",
            "1": "Bán",
        }
        return v_map.get(v, f"Invalid value for acquisition_or_disposition: {v}")
    
    @field_validator("owner_type")
    @classmethod
    def parse_owner_type(cls, v: int) -> str:
        """Parse owner_type."""
        v_map = {
            0: "Cổ đông nội bộ",
            1: "Cổ đông lớn",
            2: "Cổ đông sáng lập",
        }
        return v_map.get(v, f"Invalid value for owner_type: {v}")