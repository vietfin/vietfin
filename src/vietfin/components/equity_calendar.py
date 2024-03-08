"""VietFin Equity.Calendar class."""

from typing import Literal

from vietfin.abstract.vfobject import VfObject
from vietfin.abstract.factory import EquityCalendarFactory


class EquityCalendar:
    """VietFin Equity.Calendar-related group of commands."""

    # list of implemented providers
    PROVIDERS = Literal["tcbs"]

    @staticmethod
    def events(
        symbol: str, limit: int = 100, provider: PROVIDERS = "tcbs"
    ) -> VfObject:
        """Equity Calendar Events. Load Historical All-event-type Calendar data for a specific ticker."""
        provider_name = provider.lower()
        provider_instance = EquityCalendarFactory().get_provider(provider_name)
        return provider_instance.events(symbol=symbol, limit=limit)
