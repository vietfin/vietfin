import pandas as pd

from vietfin import vf

def test_search():
    """Test search() method in Funds class."""
    result = vf.funds.search()
    
    # Check results attribute
    assert result.results is not None  
    assert len(result.results) > 0

    # Check provider attribute
    assert result.provider == "fmarket"

    # Can also access results as dataframe
    df = result.to_df()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0

    # Test with specific query parameters:
    result = vf.funds.search(symbol="VESAF")
    assert len(result.results) == 1

    result = vf.funds.search(fund_type="STOCK")
    assert len(result.results) > 0