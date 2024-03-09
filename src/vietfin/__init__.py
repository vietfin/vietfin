"""VietFin package directory."""

# read version from installed package
from importlib.metadata import version

__version__ = version("vietfin")

# Import and instantiate classes and expose them as part of the package namespace
from vietfin.components.funds import Funds
from vietfin.components.equity import Equity
from vietfin.components.derivatives import Derivatives
from vietfin.components.index import Index
from vietfin.components.etf import Etf
from vietfin.components.news import News


class VietFin:
    def __init__(self) -> None:
        self.__version__ = version("vietfin")
        self.funds = Funds()
        self.equity = Equity()
        self.derivatives = Derivatives()
        self.index = Index()
        self.etf = Etf()
        self.news = News()


vf = VietFin()



