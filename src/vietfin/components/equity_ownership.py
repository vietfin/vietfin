"""VietFin Equity.Ownership class."""

from typing import Literal

from vietfin.abstract.vfobject import VfObject
from vietfin.abstract.factory import EquityOwnershipFactory
from vietfin.abstract.interface import IEquityOwnership


class EquityOwnership:
    """VietFin Equity.Ownership-related group of commands.

    This is the Client code in Factory Design Pattern.
    """

    # list of implemented providers
    PROVIDERS = Literal["tcbs", "cafef"]

    @staticmethod
    def _get_provider(provider: PROVIDERS) -> IEquityOwnership:
        provider_name = provider.lower()
        return EquityOwnershipFactory().get_provider(provider_name)

    def insider_trading(
        self, symbol: str, limit: int = 100, provider: PROVIDERS = "tcbs"
    ) -> VfObject:
        """Equity Insider Trading. Load insider trading data for a specific ticker."""
        provider_instance = self._get_provider(provider)
        return provider_instance.insider_trading(symbol=symbol, limit=limit)

    def major_holders(
        self, symbol: str, provider: PROVIDERS = "tcbs"
    ) -> VfObject:
        """Equity Major Holders. Load major holders data for a specific ticker."""
        provider_instance = self._get_provider(provider)
        return provider_instance.major_holders(symbol=symbol)

    def foreign_trading(
        self,
        symbol: str,
        start_date: str | None = None,
        end_date: str | None = None,
        provider: PROVIDERS = "cafef",
    ) -> VfObject:
        """Equity Ownership Foreign Trading. Load the trading data of foreign entities for a specific ticker."""
        provider_instance = self._get_provider(provider)
        return provider_instance.foreign_trading(
            symbol=symbol, start_date=start_date, end_date=end_date
        )

    def prop_trading(
        self,
        symbol: str,
        start_date: str | None = None,
        end_date: str | None = None,
        provider: PROVIDERS = "cafef",
    ) -> VfObject:
        """Equity Ownership Foreign Trading. Load the trading data of proprietary trading firms for a specific ticker."""
        provider_instance = self._get_provider(provider)
        return provider_instance.prop_trading(
            symbol=symbol, start_date=start_date, end_date=end_date
        )
