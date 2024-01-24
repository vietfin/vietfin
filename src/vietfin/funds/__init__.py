"""VietFin Funds module directory."""

# Import the Funds class from the .funds submodule
from .funds import Funds

# Export only the Funds class when "from vietfin.funds import *"
# NOTE: not necessary for the functionning of package, but nice to have
__all__ = ["Funds"]
