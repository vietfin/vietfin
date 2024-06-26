"""Test all functions in Index class."""

import pytest

from vietfin import vf
from .utils import assert_run_success as ars


def test_index_search_with_default_params():
    """Test index.search() command with default params."""

    result = vf.index.search()
    ars(result)


@pytest.mark.parametrize(
    "symbol",
    [
        "vn30",
    ],
)
class TestIndex:
    """Test index.*() commands with default params."""

    def test_index_constituents_with_default_params(self, symbol):
        """Test index.constituents() command with default params."""
        result = vf.index.constituents(symbol)
        ars(result, symbol)

    def test_index_price_historical_with_default_params(self, symbol):
        """Test index.price.historical() command with default params."""
        result = vf.index.price.historical(symbol)
        ars(result, symbol)
