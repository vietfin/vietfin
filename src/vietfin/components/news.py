"""VietFin News class."""

from typing import Literal

from vietfin.abstract.vfobject import VfObject
from vietfin.abstract.factory import NewsFactory
from vietfin.abstract.interface import INews


class News:
    """VietFin News-related group of commands.

    This is the Client code in Factory Design Pattern.
    """

    # list of implemented providers
    PROVIDERS = Literal["tcbs"]

    @staticmethod
    def _get_provider(provider: PROVIDERS) -> INews:
        provider_name = provider.lower()
        return NewsFactory().get_provider(provider_name)

    def company(
        self, symbol: str, limit: int = 100, provider: PROVIDERS = "tcbs"
    ) -> VfObject:
        """News Company. Load news data for a specific ticker."""

        provider_instance = self._get_provider(provider)
        return provider_instance.company(symbol=symbol, limit=limit)
