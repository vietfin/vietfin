from vietfin.standard_models.vfobject import VfObject
from vietfin.providers.fmarket.search import search as fmarket_search
from vietfin.providers.fmarket.historical import historical as fmarket_historical
from vietfin.providers.fmarket.holdings import holdings as fmarket_holdings


class Funds:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def search(symbol: str = "", fund_type: str = "", provider: str = "fmarket") -> VfObject:
        """Search for mutual funds.
        
        An empty query (set by default) returns the full list of mutual funds from the selected provider.

        """

        if provider == "fmarket":
            return fmarket_search(symbol, fund_type)
        else:
            raise NotImplementedError(f"Provider {provider} is not implemented yet.")
        
    @staticmethod
    def historical(symbol: str, provider: str = "fmarket") -> VfObject:
        """Retrieve historical NAV of selected fund.

        """

        if provider == "fmarket":
            return fmarket_historical(symbol)
        else:
            raise NotImplementedError(f"Provider {provider} is not implemented yet.")
        
    @staticmethod
    def holdings(symbol: str, provider: str = "fmarket") -> VfObject:
        """Retrieve a list of top 10 holdings in the specified fund.

        """

        if provider == "fmarket":
            return fmarket_holdings(symbol)
        else:
            raise NotImplementedError(f"Provider {provider} is not implemented yet.")
