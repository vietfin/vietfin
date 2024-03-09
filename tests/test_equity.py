"""Test all functions in Equity class."""

import pytest

from vietfin import vf
from .utils import assert_run_success as ars


# Test methods of Equity.Price class
@pytest.mark.parametrize(
    "symbol, start_date, end_date, interval, provider",
    [
        ("SSI", "2023-12-01", "2023-12-10", "1m", "dnse"),
        ("FPT", "2023-12-01", "2023-12-10", "15m", "dnse"),
        ("MSN", "2023-12-01", "2023-12-10", "30m", "dnse"),
        ("VPB", "2023-12-01", "2023-12-10", "1h", "dnse"),
        ("VNM", "2023-12-01", "2023-12-10", "1d", "dnse"),
        ("VNM", "2023-12-01", "2023-12-10", "1d", "tcbs"),
    ],
)
def test_equity_price_historical(
    symbol, start_date, end_date, interval, provider
):
    """Test equity.price.historical() command with valid params."""

    result = vf.equity.price.historical(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        interval=interval,
        provider=provider,
    )
    ars(result, symbol, provider)


@pytest.mark.parametrize(
    "symbol, limit, provider",
    [
        ("SSI", 1, "tcbs"),
        ("VNM", 10, "tcbs"),
    ],
)
def test_equity_price_quote(symbol, limit, provider):
    """Test equity.price.quote() command with valid params."""

    result = vf.equity.price.quote(symbol, limit, provider)
    ars(result, symbol, provider)


# Test methods in Equity class
def test_equity_search_with_default_params():
    """Test equity.search() command with default params."""

    result = vf.equity.search()
    assert (
        result.extra.get("records_count") > 1000
    )  # expected at least 1600 companies


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
    ars(result, symbol, provider)

    # Assert only one result returned from query
    assert result.extra.get("records_count") == 1


@pytest.mark.parametrize(
    "symbol",
    [
        "ssi",
    ],
)
def test_equity_profile_with_default_params(symbol):
    """Test equity.profile() command with default params."""

    result = vf.equity.search(symbol)
    ars(result, symbol)


# Test methods in Equity.Calendar class
@pytest.mark.parametrize(
    "symbol",
    [
        "ssi",
    ],
)
def test_equity_calendar_events_with_default_params(symbol):
    """Test equity.profile() command with default params."""

    result = vf.equity.calendar.events(symbol)
    ars(result, symbol)


# Test methods in Equity.Fundamental class
@pytest.mark.parametrize(
    "symbol",
    [
        "ssi",
    ],
)
def test_equity_fundamental_management_with_default_params(symbol):
    """Test equity.fundamental.management() command with default params."""

    result = vf.equity.fundamental.management(symbol)
    ars(result, symbol)


@pytest.mark.parametrize(
    "symbol",
    [
        "acb",
    ],
)
def test_equity_fundamental_ratios_with_default_params(symbol):
    """Test equity.fundamental.ratios() command with default params."""

    result = vf.equity.fundamental.ratios(symbol)
    ars(result, symbol)


@pytest.mark.parametrize(
    "symbol",
    [
        "acb",
    ],
)
def test_equity_fundamental_dividends_with_default_params(symbol):
    """Test equity.fundamental.dividends() command with default params."""

    result = vf.equity.fundamental.dividends(symbol)
    ars(result, symbol)


@pytest.mark.parametrize(
    "symbol",
    [
        "acb",
    ],
)
def test_equity_fundamental_income_with_default_params(symbol):
    """Test equity.fundamental.income() command with default params."""

    result = vf.equity.fundamental.income(symbol)
    ars(result, symbol)


@pytest.mark.parametrize(
    "symbol",
    [
        "acb",
    ],
)
def test_equity_fundamental_balance_with_default_params(symbol):
    """Test equity.fundamental.balance() command with default params."""

    result = vf.equity.fundamental.balance(symbol)
    ars(result, symbol)


@pytest.mark.parametrize(
    "symbol",
    [
        "acb",
    ],
)
def test_equity_fundamental_cash_with_default_params(symbol):
    """Test equity.fundamental.cash() command with default params."""

    result = vf.equity.fundamental.cash(symbol)
    ars(result, symbol)


# Test methods in Equity.Ownership class
@pytest.mark.parametrize(
    "symbol",
    [
        "fpt",
    ],
)
def test_equity_ownership_insider_trading_with_default_params(symbol):
    """Test equity.ownership.insider_trading() command with default params."""

    result = vf.equity.ownership.insider_trading(symbol)
    ars(result, symbol)


@pytest.mark.parametrize(
    "symbol",
    [
        "fpt",
    ],
)
def test_equity_ownership_major_holders_with_default_params(symbol):
    """Test equity.ownership.major_holders() command with default params."""

    result = vf.equity.ownership.major_holders(symbol)
    ars(result, symbol)


@pytest.mark.parametrize(
    "symbol",
    [
        "fpt",
    ],
)
def test_equity_ownership_foreign_trading_with_default_params(symbol):
    """Test equity.ownership.foreign_trading() command with default params."""

    result = vf.equity.ownership.foreign_trading(symbol)
    ars(result, symbol)


@pytest.mark.parametrize(
    "symbol",
    [
        "fpt",
    ],
)
def test_equity_ownership_prop_trading_with_default_params(symbol):
    """Test equity.ownership.prop_trading() command with default params."""

    result = vf.equity.ownership.prop_trading(symbol)
    ars(result, symbol)