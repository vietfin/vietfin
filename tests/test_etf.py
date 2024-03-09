"""Test all functions in ETF class."""

import pytest

from vietfin import vf
from .utils import assert_run_success as ars


def test_etf_search_with_default_params():
    """Test etf.search() command with default params."""

    result = vf.etf.search()
    ars(result)

@pytest.mark.parametrize(
    "symbol",
    [
        "ssi",
    ],
)
def test_etf_historical_with_default_params(symbol):
    """Test etf.historical() command with default params."""

    result = vf.etf.historical(symbol)
    ars(result, symbol)