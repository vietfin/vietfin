# vietFin

VietFin - a python library to fetch Vietnam stock market data.

VietFin is an open-source tool that provides a Python interface for publicly available APIs from brokerage firms. It is intended for research and educational purposes.

## Usage

<!-- TODO: Add usage examples -->

## Reference

<!-- TODO: Edit reference examples, currently marked as ref to OpenBB -->

Possible hierarchical structure of user-facing commands:

- Equity
    - search() [ref](https://docs.openbb.co/platform/reference/equity/search)
    - Price
        - historical() [ref](https://docs.openbb.co/platform/reference/equity/price/historical)
    - Discovery
        - gainers() [ref](https://docs.openbb.co/platform/reference/equity/discovery/gainers)
        - losers() [ref](https://docs.openbb.co/platform/reference/equity/discovery/losers)
- Derivatives
    - Futures
        - historical() [ref](https://docs.openbb.co/platform/reference/derivatives/futures/historical) 
- Mutual Funds [ref](https://docs.openbb.co/terminal/menus/mutualfunds)
    - search()
    - historical()
    - holdings()
- ETF
    - historical() [ref](https://docs.openbb.co/platform/reference/etf/historical)
    - search() [ref](https://docs.openbb.co/platform/reference/etf/search)
- Index
    - historical() [ref](https://docs.openbb.co/platform/reference/index/market)
    - search() [ref](https://docs.openbb.co/platform/reference/index/search)

## Installation

<!-- TODO: Add install instructions -->

<!-- 
Install `vietfin` using `poetry`:

``` {.sourceCode .bash}
$ poetry add vietfin
```
-->

## Requirements

<!-- TODO: Add requirements -->

- [Python](https://www.python.org) \>= 3.10
- [requests](https://requests.readthedocs.io/en/latest/) \>= 2.31
- [pandas](https://pandas.pydata.org/) \>= 2.1.4
- [Pydantic](https://github.com/pydantic/pydantic) \>= 2.5

## Attributions

VietFin is built on top of the inspiration and work of the following projects:

- [Openbb](https://github.com/OpenBB-finance/OpenBBTerminal), its [Data Standardization Infrastructure](https://docs.openbb.co/platform/development/developer-guidelines/architectural_considerations) and [hierarchical structure](https://docs.openbb.co/platform/reference) of commands menu
- [yfinance](https://github.com/ranaroussi/yfinance)