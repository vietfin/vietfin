"""VNDIRECT provider concrete class."""

from vietfin.abstract.interface import (
    IEquityDiscovery,
)
from vietfin.abstract.vfobject import VfObject
from vietfin.utils.helpers import EXCHANGE_NAMES
from vietfin.providers.vndirect.utils.equity_discovery import get_top_movers


class EquityDiscoveryVndirect(IEquityDiscovery):
    """The concrete implementation of Equity Discovery component with Ssi as provider."""

    def active(self, exchange: EXCHANGE_NAMES) -> VfObject:
        """Equity Discovery Active. Load the list of most active stocks based on trading value."""
        return get_top_movers(name="value", exchange=exchange)

    def gainers(self, exchange: EXCHANGE_NAMES) -> VfObject:
        """Equity Discovery Gainers. Load the list of top gainer stocks."""
        return get_top_movers(name="gainers", exchange=exchange)

    def losers(self, exchange: EXCHANGE_NAMES) -> VfObject:
        """Equity Discovery Losers. Load the list of top loser stocks."""
        return get_top_movers(name="losers", exchange=exchange)
