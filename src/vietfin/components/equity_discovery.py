"""VietFin Equity.Discovery class."""

from typing import Literal

from vietfin.abstract.vfobject import VfObject
from vietfin.abstract.factory import EquityDiscoveryFactory
from vietfin.abstract.interface import IEquityDiscovery
from vietfin.utils.helpers import EXCHANGE_NAMES


class EquityDiscovery:
    """VietFin Equity.Discovery-related group of commands."""

    # list of implemented providers
    PROVIDERS = Literal["vndirect"]

    @staticmethod
    def _get_provider(provider: PROVIDERS) -> IEquityDiscovery:
        provider_name = provider.lower()
        return EquityDiscoveryFactory().get_provider(provider_name)

    def active(
        self, exchange: EXCHANGE_NAMES = "hose", provider: PROVIDERS = "vndirect"
    ) -> VfObject:
        """Equity Discovery Active. Load the list of most active stocks based on trading value."""

        provider_instance = self._get_provider(provider)
        return provider_instance.active(exchange=exchange)

    def gainers(
        self, exchange: EXCHANGE_NAMES = "hose", provider: PROVIDERS = "vndirect"
    ) -> VfObject:
        """Equity Discovery Gainers. Load the list of top gainer stocks."""

        provider_instance = self._get_provider(provider)
        return provider_instance.gainers(exchange=exchange)

    def losers(
        self, exchange: EXCHANGE_NAMES = "hose", provider: PROVIDERS = "vndirect"
    ) -> VfObject:
        """Equity Discovery Losers. Load the list of top loser stocks."""

        provider_instance = self._get_provider(provider)
        return provider_instance.losers(exchange=exchange)
