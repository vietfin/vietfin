"""VietFin Funds module directory."""

# Import the Funds class from the .funds submodule
from .funds import Funds
"""NOTE:

The reason you need to include `from .funds import Funds` in vietfin/funds/__init__.py is because of how Python handles imports.

When you do `from vietfin.funds import Funds` in vietfin/__init__.py, Python will look in the vietfin/funds directory for an __init__.py file, which signifies a Python package.

If vietfin/funds/__init__.py is empty or does not explicitly import and expose the Funds class, Python will not be able to find it when you try to import it from the parent vietfin package.

By adding `from .funds import Funds` in `vietfin/funds/__init__.py`, you are explicitly importing the Funds class from the .funds submodule and exposing it to any code that imports from the vietfin.funds package.

The .__init__.py serves as the interface between the parent package (vietfin) and subpackage (funds). It controls what gets imported into the parent when you use a syntax like from vietfin.funds import Funds.
"""

# Export only the Funds class when "from vietfin.funds import *"
__all__ = ["Funds"]
# NOTE: not necessary for the functionning of package, but nice to have
