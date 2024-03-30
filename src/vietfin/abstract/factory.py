"""Components Providers Factory class."""

from vietfin.abstract.interface import (
    IFunds,
    IEquity,
    IEquityPrice,
    IEquityOwnership,
    IEquityCalendar,
    IEquityFundamental,
    IEquityDiscovery,
    IDerivativesFutures,
    IIndex,
    IIndexPrice,
    IEtf,
    INews,
)
from vietfin.providers.fmarket.provider import FundsFmarket
from vietfin.providers.ssi.provider import (
    EquitySsi,
    EquityPriceSsi,
    EquityFundamentalSsi,
    IndexSsi,
    EquityDiscoverySsi,
    EtfSsi,
)
from vietfin.providers.wifeed.provider import EquityWifeed
from vietfin.providers.dnse.provider import (
    EquityPriceDnse,
    EtfDnse,
    IndexPriceDnse,
)
from vietfin.providers.tcbs.provider import (
    EquityTcbs,
    EquityPriceTcbs,
    EquityOwnershipTcbs,
    EquityCalendarTcbs,
    EquityFundamentalTcbs,
    DerivativesFuturesTcbs,
    EtfTcbs,
    NewsTcbs,
    IndexPriceTcbs,
)
from vietfin.providers.vdsc.provider import DerivativesFuturesVdsc
from vietfin.providers.cafef.provider import EquityOwnershipCafef
from vietfin.providers.vndirect.provider import EquityDiscoveryVndirect
from vietfin.providers.ssi.provider import DerivativesFuturesSsi


class FundsFactory:
    """Factory class for Funds component.

    Factory represents a combination of the IFunds's concrete implementations based on provider_name.
    The factory doesn't maintain any of the instances which it creates.
    """

    providers_implementations = {
        "fmarket": FundsFmarket(),
    }

    def get_provider(self, provider: str) -> IFunds:
        """Returns a new concrete implementation of IFunds instance based on the provider name."""

        if provider in self.providers_implementations:
            return self.providers_implementations[provider]
        else:
            raise NotImplementedError(
                f"Provider {provider} is not implemented yet."
            )


class EquityFactory:
    """Factory class for Equity component.

    Factory represents a combination of the IEquity's concrete implementations based on provider_name.
    """

    providers_implementations = {
        "ssi": EquitySsi(),
        "wifeed": EquityWifeed(),
        "tcbs": EquityTcbs(),
    }

    def get_provider(self, provider: str) -> IEquity:
        """Returns a new concrete implementation of IEquity instance based on the provider name."""

        if provider in self.providers_implementations:
            return self.providers_implementations[provider]
        else:
            raise NotImplementedError(
                f"Provider {provider} is not implemented yet."
            )


class EquityPriceFactory:
    """Factory class for Equity.Price component.

    Factory represents a combination of the IEquityPrice's concrete implementations based on provider_name.
    """

    providers_implementations = {
        "dnse": EquityPriceDnse(),
        "tcbs": EquityPriceTcbs(),
        "ssi": EquityPriceSsi(),
    }

    def get_provider(self, provider: str) -> IEquityPrice:
        """Returns a new concrete implementation of IEquityPrice instance based on the provider name."""

        if provider in self.providers_implementations:
            return self.providers_implementations[provider]
        else:
            raise NotImplementedError(
                f"Provider {provider} is not implemented yet."
            )


class EquityOwnershipFactory:
    """Factory class for Equity.Ownership component.

    Factory represents a combination of the IEquityOwnership's concrete implementations based on provider_name.
    """

    providers_implementations = {
        "tcbs": EquityOwnershipTcbs(),
        "cafef": EquityOwnershipCafef(),
    }

    def get_provider(self, provider: str) -> IEquityOwnership:
        """Returns a new concrete implementation of IEquityOwnership instance based on the provider name."""

        if provider in self.providers_implementations:
            return self.providers_implementations[provider]
        else:
            raise NotImplementedError(
                f"Provider {provider} is not implemented yet."
            )


class EquityCalendarFactory:
    """Factory class for Equity.Calendar component.

    Factory represents a combination of the IEquityCalendar's concrete implementations based on provider_name.
    """

    providers_implementations = {
        "tcbs": EquityCalendarTcbs(),
    }

    def get_provider(self, provider: str) -> IEquityCalendar:
        """Returns a new concrete implementation of IEquityCalendar instance based on the provider name."""

        if provider in self.providers_implementations:
            return self.providers_implementations[provider]
        else:
            raise NotImplementedError(
                f"Provider {provider} is not implemented yet."
            )


class EquityFundamentalFactory:
    """Factory class for Equity.Fundamental component.

    Factory represents a combination of the IEquityFundamental's concrete implementations based on provider_name.
    """

    providers_implementations = {
        "tcbs": EquityFundamentalTcbs(),
        "ssi": EquityFundamentalSsi(),
    }

    def get_provider(self, provider: str) -> IEquityFundamental:
        """Returns a new concrete implementation of IEquityFundamental instance based on the provider name."""

        if provider in self.providers_implementations:
            return self.providers_implementations[provider]
        else:
            raise NotImplementedError(
                f"Provider {provider} is not implemented yet."
            )


class EquityDiscoveryFactory:
    """Factory class for Equity.Discovery component.

    Factory represents a combination of the IEquityDiscovery's concrete implementations based on provider_name.
    """

    providers_implementations = {
        "ssi": EquityDiscoverySsi(),
        "vndirect": EquityDiscoveryVndirect(),
    }

    def get_provider(self, provider: str) -> IEquityDiscovery:
        """Returns a new concrete implementation of IEquityFundamental instance based on the provider name."""

        if provider in self.providers_implementations:
            return self.providers_implementations[provider]
        else:
            raise NotImplementedError(
                f"Provider {provider} is not implemented yet."
            )


class DerivativesFuturesFactory:
    """Factory class for Derivatives.Futures component.

    Factory represents a combination of the IDerivativesFutures's concrete implementations based on provider_name.
    """

    providers_implementations = {
        "vdsc": DerivativesFuturesVdsc(),
        "tcbs": DerivativesFuturesTcbs(),
        "ssi": DerivativesFuturesSsi(),
    }

    def get_provider(self, provider: str) -> IDerivativesFutures:
        """Returns a new concrete implementation of IDerivativesFutures instance based on the provider name."""

        if provider in self.providers_implementations:
            return self.providers_implementations[provider]
        else:
            raise NotImplementedError(
                f"Provider {provider} is not implemented yet."
            )


class IndexFactory:
    """Factory class for Index component.

    Factory represents a combination of the IIndex's concrete implementations based on provider_name.
    """

    providers_implementations = {
        "ssi": IndexSsi(),
    }

    def get_provider(self, provider: str) -> IIndex:
        """Returns a new concrete implementation of IIndex instance based on the provider name."""

        if provider in self.providers_implementations:
            return self.providers_implementations[provider]
        else:
            raise NotImplementedError(
                f"Provider {provider} is not implemented yet."
            )


class IndexPriceFactory:
    """Factory class for Index.Price component.

    Factory represents a combination of the IIndexPrice's concrete implementations based on provider_name.
    """

    providers_implementations = {
        "tcbs": IndexPriceTcbs(),
        "dnse": IndexPriceDnse(),
    }

    def get_provider(self, provider: str) -> IIndexPrice:
        """Returns a new concrete implementation of IIndexPrice instance based on the provider name."""

        if provider in self.providers_implementations:
            return self.providers_implementations[provider]
        else:
            raise NotImplementedError(
                f"Provider {provider} is not implemented yet."
            )


class EtfFactory:
    """Factory class for Etf component.

    Factory represents a combination of the IEtf's concrete implementations based on provider_name.

    """

    providers_implementations = {
        "dnse": EtfDnse(),
        "tcbs": EtfTcbs(),
        "ssi": EtfSsi(),
    }

    def get_provider(self, provider: str) -> IEtf:
        """Returns a new concrete implementation of IEtf instance based on the provider name."""

        if provider in self.providers_implementations:
            return self.providers_implementations[provider]
        else:
            raise NotImplementedError(
                f"Provider {provider} is not implemented yet."
            )


class NewsFactory:
    """Factory class for News component.

    Factory represents a combination of the INews's concrete implementations based on provider_name.
    """

    providers_implementations = {
        "tcbs": NewsTcbs(),
    }

    def get_provider(self, provider: str) -> INews:
        """Returns a new concrete implementation of INews instance based on the provider name."""

        if provider in self.providers_implementations:
            return self.providers_implementations[provider]
        else:
            raise NotImplementedError(
                f"Provider {provider} is not implemented yet."
            )
