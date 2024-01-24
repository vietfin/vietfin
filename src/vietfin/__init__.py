"""VietFin package directory."""

# read version from installed package
from importlib.metadata import version

__version__ = version("vietfin")

# Import and instantiate classes and expose them as part of the package namespace
from vietfin.funds import Funds


class VietFinCommandMenu:
    def __init__(self) -> None:
        self.funds = Funds()
        # self.equity = Equity()
        # self.index = Index()
        # self.etf = Etf()
        # self.derivatives = Derivatives()


vf = VietFinCommandMenu()
