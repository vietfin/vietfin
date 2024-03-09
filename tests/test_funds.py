"""Test all functions in Funds class."""

import pandas as pd
import pytest

from vietfin import vf


def test_search_with_default_params():
    """Test search() method in Funds class with default params."""
    result = vf.funds.search()

    # Check results attribute
    assert result.results is not None
    assert len(result.results) > 0

    # Check provider attribute
    assert result.provider == "fmarket"

    # Check results as dataframe
    df = result.to_df()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


@pytest.mark.parametrize(
    "symbol, provider",
    [
        ("VESAF", "fmarket"),
        ("VIBF", "fmarket"),
    ],
)
def test_search_with_valid_params(symbol, provider):
    """Test search() method in Funds class with valid params."""

    result = vf.funds.search(symbol=symbol, provider=provider)
    
    # Assert correct provider name
    assert result.provider == provider
    
    # Assert correct symbol name retured from query
    assert result.extra.get("symbol") == symbol


@pytest.mark.parametrize(
    "symbol, provider",
    [
        ("VESAF", "fmarket"),
        ("VIBF", "fmarket"),
    ],
)
def test_historical_with_valid_params(symbol, provider):
    """Test historical() method in Funds class with valid params."""

    result = vf.funds.historical(symbol=symbol, provider=provider)
    assert result.provider == provider
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "symbol, provider",
    [
        ("VESAF", "fmarket"),
        ("VIBF", "fmarket"),
    ],
)
def test_holdings_with_valid_params(symbol, provider):
    """Test holdings() method in Funds class with valid params."""

    result = vf.funds.holdings(symbol=symbol, provider=provider)
    assert result.provider == provider
    assert len(result.results) > 0
