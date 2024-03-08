"""Test all functions in Equity class."""

import pytest

from vietfin import vf


# Test methods of Equity.Price class
@pytest.mark.parametrize(
    "symbol, start_date, end_date, interval, provider",
    [
        ("SSI", "2023-12-01", "2023-12-20", "1m", "dnse"),
        ("FPT", "2023-12-01", "2023-12-20", "15m", "dnse"),
        ("MSN", "2023-12-01", "2023-12-20", "30m", "dnse"),
        ("VPB", "2023-12-01", "2023-12-20", "1h", "dnse"),
        ("VNM", "2023-12-01", "2023-12-20", "1d", "dnse"),
        ("VNM", "2023-12-01", "2023-12-20", "1d", "tcbs"),
    ],
)
def test_equity_price_historical(
    symbol, start_date, end_date, interval, provider
):
    """Test equity.price.historical() command with valid params."""

    result = vf.equity.price.historical(
        symbol, start_date, end_date, interval, provider
    )

    # Assert correct provider name
    assert result.provider == provider

    # Assert correct symbol name retured from query
    assert result.extra.get("symbol") == symbol

    # Assert results attribute is not null
    assert result.extra.get("records_count") > 0


@pytest.mark.parametrize(
    "symbol, limit, provider",
    [
        ("SSI", 1, "tcbs"),
        ("VNM", 10, "tcbs"),
        ("FPT", 0, "tcbs"),
    ],
)
def test_equity_price_quote(symbol, limit, provider):
    """Test equity.price.quote() command with valid params."""

    result = vf.equity.price.quote(symbol, limit, provider)

    # Assert correct provider name
    assert result.provider == provider

    # Assert correct symbol name retured from query
    assert result.extra.get("symbol") == symbol

    # Assert results attribute is not null
    assert result.extra.get("records_count") > 0


# Test search() method in Equity class
def test_equity_search_with_default_params():
    """Test equity.search() command with default params."""

    result = vf.equity.search()
    assert result.extra.get("records_count") > 1000  # expected at least 1600 companies


@pytest.mark.parametrize(
    "symbol, provider",
    [
        ("VNM", "ssi"),
        ("SSI", "wifeed"),
    ],
)
def test_equity_search_with_valid_params(symbol, provider):
    """Test equity.search() command with valid params."""

    result = vf.equity.search(symbol, provider)

    # Assert correct provider name
    assert result.provider == provider

    # Assert only one result returned from query
    assert result.extra.get("records_count") == 1

    # Assert correct symbol returned from query
    assert result.extra.get("symbol") == symbol
