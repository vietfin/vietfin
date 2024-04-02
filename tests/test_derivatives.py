"""Test all functions in Derivatives class."""

import pytest

from vietfin import vf
from .utils import assert_run_success as ars


# Test methods of Derivatives.Futures class
@pytest.mark.parametrize(
    "symbol, start_date, end_date, provider",
    [
        ("VN30F1M", "2023-07-01", "2023-12-31", "tcbs"),
    ],
)
def test_derivatives_futures_historical(symbol, start_date, end_date, provider):
    """Test derivatives.futures.historical() command. with valid params"""

    result = vf.derivatives.futures.historical(
        symbol, start_date, end_date, provider
    )
    ars(result, symbol, provider)

@pytest.mark.parametrize(
    "symbol",
    [
        "",
        "VN30F2409",
    ],
)
def test_derivatives_futures_search(symbol):
    """Test derivatives.futures.search() command."""

    result = vf.derivatives.futures.search(symbol)
    ars(result, symbol)

@pytest.mark.parametrize(
    "symbol",
    [
        "VN30F2409",
    ],
)
def test_derivatives_futures_quote(symbol):
    """Test derivatives.futures.quote() command."""

    result = vf.derivatives.futures.quote(symbol)
    ars(result, symbol)