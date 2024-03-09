"""Cafef provider concrete class."""

from vietfin.abstract.interface import (
    IEquityOwnership,
)
from vietfin.abstract.vfobject import VfObject
from vietfin.providers.cafef.utils.equity_ownership_foreign import foreign
from vietfin.providers.cafef.utils.equity_ownership_prop import prop


class EquityOwnershipCafef(IEquityOwnership):
    """The concrete implementation of Equity.Ownership component with Cafef as provider."""

    def insider_trading(self, symbol: str, limit: int) -> VfObject:
        """Equity Insider Trading. Load insider trading data of a specific ticker."""
        raise NotImplementedError(
            "equity.ownership.insider_trading() command is not implemented for CafeF provider."
        )

    def major_holders(self, symbol: str) -> VfObject:
        """Equity Major Holders. Load major holders data of a specific ticker."""
        raise NotImplementedError(
            "equity.ownership.major_holders() command is not implemented for CafeF provider."
        )

    def foreign_trading(
        self, symbol: str, start_date: str, end_date: str
    ) -> VfObject:
        """Equity Ownership Foreign Trading. Load the trading data of foreign entities for a specific ticker."""
        return foreign(symbol=symbol, start_date=start_date, end_date=end_date)

    def prop_trading(
        self, symbol: str, start_date: str, end_date: str
    ) -> VfObject:
        """Equity Ownership Proprietary trading. Load the trading data of proprietary trading firms for a specific ticker."""
        return prop(symbol=symbol, start_date=start_date, end_date=end_date)
