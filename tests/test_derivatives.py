"""Test all functions in Derivatives class."""

import pytest

from vietfin import vf


# Test methods of Derivatives.Futures class
@pytest.mark.parametrize(
    "symbol, start_date, end_date, provider",
    [
        ("VN30F1M", "2023-07-01", "2023-12-31", "tcbs"),
    ],
)
def test_derivatives_futures_historical(
    symbol, start_date, end_date, provider
):
    """Test derivatives.futures.historical() command. with valid params"""

    result = vf.derivatives.futures.historical(
        symbol, start_date, end_date, provider
    )

    # Assert correct provider name
    assert result.provider == provider

    # Assert correct symbol name retured from query
    assert result.extra.get("symbol") == symbol

    # Assert results attribute is not null
    assert result.extra.get("records_count") > 0