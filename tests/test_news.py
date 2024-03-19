"""Test all functions in News class."""

import pytest

from vietfin import vf
from .utils import assert_run_success as ars


@pytest.mark.parametrize(
    "symbol",
    [
        "stb",
    ],
)
def test_news_company_with_default_params(symbol):
    """Test news.company() command with default params."""

    result = vf.news.company(symbol)
    ars(result, symbol)