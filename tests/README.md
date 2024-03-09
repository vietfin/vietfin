# 1. VietFin Testing GUidelines

This document is an annex of the VietFin [Contributing Guidelines](/CONTRIBUTING.md).

It provides the necessary information to build, run and maintain Unit Tests for VietFin.

## 2. Run `unit tests`

In this section we will explain everything you need to run the `unit tests` on the VietFin project.

## 2.1. How to install tests dependencies?

To run the tests you will need first to install the [`pytest` package](https://docs.pytest.org/en/7.1.x/index.html). For example, we use `poetry` to manage our python dependencies.

```bash
poetry add pytest
```

### 2.2. How to run `tests`:

#### By `module`

You can run tests on a specific module by specifying the path of this module, as follows:

```bash
pytest tests/test_some_module.py
```

#### By test `name`

You can run tests by their name with the argument `-k`. Read more about this argument [here](https://docs.pytest.org/en/7.1.x/example/markers.html#using-k-expr-to-select-tests-based-on-their-name)

```bash
pytest tests/test_some_module.py -k test_function_name
```

## 3. How to build `unit tests`

When you contribute a new feature to the VietFin project, it's important that `tests` are added for this particular feature.

All the `unit tests` should be insides the `tests` folder. There should be at most one `test module` for each `module`/`package` of the VietFin project.

Each `test module` should follow the same naming pattern of the `module`/`package` that it is `testing`. For instance,

- in order to test the following module `src/vietfin/funds/funds.py`
- a `test module` should be added here: `tests/test_funds.py`

## 4. Example of test results

With the current simple unit tests, I got the following results:

```bash
❯ pytest -v tests/
====================================================================== test session starts =======================================================================
platform win32 -- Python 3.10.13, pytest-7.4.4, pluggy-1.4.0 -- C:\Users\h7b\miniconda3\envs\vietfin-dev\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\h7b\my_workspace\h7b\vietfin
plugins: cov-4.1.0
collected 37 items

tests/test_derivatives.py::test_derivatives_futures_historical[VN30F1M-2023-07-01-2023-12-31-tcbs] PASSED                                                   [  2%]
tests/test_equity.py::test_equity_price_historical[SSI-2023-12-01-2023-12-10-1m-dnse] PASSED                                                                [  5%]
tests/test_equity.py::test_equity_price_historical[FPT-2023-12-01-2023-12-10-15m-dnse] PASSED                                                               [  8%]
tests/test_equity.py::test_equity_price_historical[MSN-2023-12-01-2023-12-10-30m-dnse] PASSED                                                               [ 10%]
tests/test_equity.py::test_equity_price_historical[VPB-2023-12-01-2023-12-10-1h-dnse] PASSED                                                                [ 13%]
tests/test_equity.py::test_equity_price_historical[VNM-2023-12-01-2023-12-10-1d-dnse] PASSED                                                                [ 16%]
tests/test_equity.py::test_equity_price_historical[VNM-2023-12-01-2023-12-10-1d-tcbs] PASSED                                                                [ 18%]
tests/test_equity.py::test_equity_price_quote[SSI-1-tcbs] PASSED                                                                                            [ 21%]
tests/test_equity.py::test_equity_price_quote[VNM-10-tcbs] PASSED                                                                                           [ 24%]
tests/test_equity.py::test_equity_search_with_default_params PASSED                                                                                         [ 27%]
tests/test_equity.py::test_equity_search_with_valid_params[VNM-ssi] PASSED                                                                                  [ 29%]
tests/test_equity.py::test_equity_search_with_valid_params[SSI-wifeed] PASSED                                                                               [ 32%]
tests/test_equity.py::test_equity_profile_with_default_params[ssi] PASSED                                                                                   [ 35%]
tests/test_equity.py::test_equity_calendar_events_with_default_params[ssi] PASSED                                                                           [ 37%]
tests/test_equity.py::test_equity_fundamental_management_with_default_params[ssi] PASSED                                                                    [ 40%]
tests/test_equity.py::test_equity_fundamental_ratios_with_default_params[acb] PASSED                                                                        [ 43%]
tests/test_equity.py::test_equity_fundamental_dividends_with_default_params[acb] PASSED                                                                     [ 45%]
tests/test_equity.py::test_equity_fundamental_income_with_default_params[acb] PASSED                                                                        [ 48%]
tests/test_equity.py::test_equity_fundamental_balance_with_default_params[acb] PASSED                                                                       [ 51%]
tests/test_equity.py::test_equity_fundamental_cash_with_default_params[acb] PASSED                                                                          [ 54%]
tests/test_equity.py::test_equity_ownership_insider_trading_with_default_params[fpt] PASSED                                                                 [ 56%]
tests/test_equity.py::test_equity_ownership_major_holders_with_default_params[fpt] PASSED                                                                   [ 59%]
tests/test_equity.py::test_equity_ownership_foreign_trading_with_default_params[fpt] PASSED                                                                 [ 62%]
tests/test_equity.py::test_equity_ownership_prop_trading_with_default_params[fpt] PASSED                                                                    [ 64%]
tests/test_etf.py::test_etf_search_with_default_params PASSED                                                                                               [ 67%]
tests/test_etf.py::test_etf_historical_with_default_params[ssi] PASSED                                                                                      [ 70%]
tests/test_funds.py::test_search_with_default_params PASSED                                                                                                 [ 72%]
tests/test_funds.py::test_search_with_valid_params[VESAF-fmarket] PASSED                                                                                    [ 75%]
tests/test_funds.py::test_search_with_valid_params[VIBF-fmarket] PASSED                                                                                     [ 78%]
tests/test_funds.py::test_historical_with_valid_params[VESAF-fmarket] PASSED                                                                                [ 81%]
tests/test_funds.py::test_historical_with_valid_params[VIBF-fmarket] PASSED                                                                                 [ 83%]
tests/test_funds.py::test_holdings_with_valid_params[VESAF-fmarket] PASSED                                                                                  [ 86%]
tests/test_funds.py::test_holdings_with_valid_params[VIBF-fmarket] PASSED                                                                                   [ 89%]
tests/test_index.py::test_index_search_with_default_params PASSED                                                                                           [ 91%]
tests/test_index.py::test_index_constituents_with_default_params[vn30] PASSED                                                                               [ 94%]
tests/test_index.py::test_index_price_historical_with_default_params[vn30] PASSED                                                                           [ 97%]
tests/test_news.py::test_news_company_with_default_params[stb] PASSED                                                                                       [100%]

================================================================= 37 passed in 61.03s (0:01:01) ================================================================== 

vietfin on  dev [!?] is 󰏗 v0.1.0  via  v3.10.13 via  vietfin-dev took 1m1s
```