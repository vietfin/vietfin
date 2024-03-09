"""VietFin Equity.Fundamental class."""

from typing import Literal

from vietfin.abstract.vfobject import VfObject
from vietfin.abstract.factory import EquityFundamentalFactory
from vietfin.abstract.interface import IEquityFundamental
from vietfin.utils.helpers import PERIODS


class EquityFundamental:
    """VietFin Equity.Fundamental-related group of commands.

    This is the Client code in Factory Design Pattern.
    """

    # list of implemented providers
    PROVIDERS = Literal["tcbs", "ssi"]

    @staticmethod
    def _get_provider(provider: PROVIDERS) -> IEquityFundamental:
        provider_name = provider.lower()
        return EquityFundamentalFactory().get_provider(provider_name)

    def management(self, symbol: str, provider: PROVIDERS = "tcbs") -> VfObject:
        """Equity Fundamental Management. Load Key executives data for a specific ticker."""

        provider_instance = self._get_provider(provider)
        return provider_instance.management(symbol=symbol)

    def ratios(
        self,
        symbol: str,
        period: PERIODS = "annual",
        provider: PROVIDERS = "tcbs",
    ) -> VfObject:
        """Equity Fundamental Ratios. Load Financial ratios data for a specific ticker."""

        provider_instance = self._get_provider(provider)
        return provider_instance.ratios(symbol=symbol, period=period)

    def dividends(
        self, symbol: str, limit: int = 100, provider: PROVIDERS = "tcbs"
    ) -> VfObject:
        """Equity Fundamental Dividends. Load Historical dividends data for a specific ticker."""

        provider_instance = self._get_provider(provider)
        return provider_instance.dividends(symbol=symbol, limit=limit)

    def income(
        self,
        symbol: str,
        period: PERIODS = "annual",
        provider: PROVIDERS = "tcbs",
    ) -> VfObject:
        """Equity Fundamental Income. Load Historical income statement data for a specific ticker."""

        provider_instance = self._get_provider(provider)
        return provider_instance.income(symbol=symbol, period=period)

    def balance(
        self,
        symbol: str,
        period: PERIODS = "annual",
        provider: PROVIDERS = "tcbs",
    ) -> VfObject:
        """Equity Fundamental Balance. Load Historical balance sheet statement data for a specific ticker."""

        provider_instance = self._get_provider(provider)
        return provider_instance.balance(symbol=symbol, period=period)

    def cash(
        self,
        symbol: str,
        period: PERIODS = "annual",
        provider: PROVIDERS = "tcbs",
    ) -> VfObject:
        """Equity Fundamental Cash. Load Historical cash flow statement data for a specific ticker."""

        provider_instance = self._get_provider(provider)
        return provider_instance.cash(symbol=symbol, period=period)
