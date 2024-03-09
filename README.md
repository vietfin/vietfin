<p align="center">
  <img src="/docs/_static/logo.jpg" alt="VietFin" width="228" />
</p>

<h2 align="center">VietFin</h2>

<div align="center">A python library to fetch Vietnam stock market data.</div>

<p align="center">
    <a href="https://github.com/Multiwoven/multiwoven/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Multiwoven/multiwoven?style=for-the-badge" alt="License"></a>
    <br />
    <a href="https://docs.vietfin.com" target="_blank" rel="noopener noreferrer"><strong>» Explore the docs »</strong></a>
    <br />
</p>

<hr />

<!-- TABLE OF CONTENTS -->
<details closed="closed">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li><a href="#1-why-vietfin">Why VietFin?</a></li>
    <li><a href="#2-isntallation">Installation</a></li>
    <li><a href="#3-usage">Usage</a></li>
    <li><a href="#4-contributing">Contributing</a></li>
    <li><a href="#5-attributions">Attributions</a></li>
    <li><a href="#6-disclaimer">Disclaimer</a></li>
    <li><a href="#7-contacts">Contacts</a></li>
  </ol>
</details>

## 1. Why VietFin?

Heavily inspired by [OpenBB](https://github.com/OpenBB-finance/OpenBBTerminal), VietFin is a Python package which provides a wrapper around the publicly available APIs from multiple brokerage firms.

This package aims to reproduce the hierarchical structure of commands used in OpenBB, but for Vietnamese market data.

VietFin is intended for personal use, research and educational purposes.

## 2. Installation

VietFin is available on [PyPI](https://pypi.org/). To use the package:

1. Install VietFin in your project's virtual environment.

    ``` {.sourceCode .bash}
    $ pip install vietfin
    ```

    Or using [Poetry](https://python-poetry.org/):

    ``` {.sourceCode .bash}
    $ poetry add vietfin
    ```

2. Import the package then use the package

    ``` {.sourceCode .python}
    from vietfin import vf
    ```

Requirements:

- [Python](https://www.python.org) \>= 3.10
- [requests](https://requests.readthedocs.io/en/latest/) \>= 2.31
- [pandas](https://pandas.pydata.org/) \>= 2.1.4
- [Pydantic](https://github.com/pydantic/pydantic) \>= 2.5

## 3. Usage

```python
from vietfin import vf
# Get list of all stocks
vf.equity.search()
# Get general info of a stock
vf.equity.profile(symbol='vnm')
# Get historical price of a stock
vf.equity.historical(symbol='vnm')
# Get the historical dividends data of a company
vf.equity.fundamental.dividends(symbol='vnm')
# Get list of key executives of a company
vf.equity.fundamental.management(symbol='vnm')
# Get the key financial ratios of a company
vf.equity.fundamental.ratios(symbol='vnm')
# Get the report on the income statement of a company
vf.equity.fundamental.income(symbol='vnm')
# Get the historical events of a stock ticker
vf.equity.calendar.events(symbol='vnm')
# Get the list of available mutual funds
vf.funds.search()
# Get the list of available ETFs
vf.etf.search()
# Get the list of constituents of an index
vf.index.constituents(symbol='vn30')
```

## 4. Contributing

More information on our [Contributing Guidelines](/CONTRIBUTING.md) and [Code of Conduct](/CONDUCT.md).

`VietFin` relies on community to investigate bugs and contribute code.

Before creating a ticket, make sure the one you are creating doesn't exist already [here](https://github.com/OpenBB-finance/OpenBBTerminal/issues)
- [Report bug](https://github.com/OpenBB-finance/OpenBBTerminal/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBug%5D)
- [Suggest improvement](https://github.com/OpenBB-finance/OpenBBTerminal/issues/new?assignees=&labels=enhancement&template=enhancement.md&title=%5BIMPROVE%5D)
- [Request a feature](https://github.com/OpenBB-finance/OpenBBTerminal/issues/new?assignees=&labels=new+feature&template=feature_request.md&title=%5BFR%5D)

Feel free to reach out to us in GitHub Discussion for feedback.

## 5. Attributions

VietFin is built on top of the inspiration and work of the following projects:

- [Openbb](https://github.com/OpenBB-finance/OpenBBTerminal), its [Data Standardization Infrastructure](https://docs.openbb.co/platform/development/developer-guidelines/architectural_considerations) and the [hierarchical structure](https://docs.openbb.co/platform/reference) of user-facing commands.
- [vnstock](https://github.com/thinh-vu/vnstock) and its findinds on publicly available APIs from brokerage firms in Vietnam.

## 6. Disclaimer

VietFin is not affiliated, endorsed, or vetted by any of the brokerage firms or research entities which provide the data. It's an open-source tool that crawl data from the publicly available APIs of these firms. VietFin is intended for personal use, research and educational purposes.

You should refer to each of the data provider's terms of use for details on your rights to use the actual data downloaded.

The data retrieved by the VietFin package is not necessarily accurate.

VietFin and any provider of the data contained in this website will not accept liability for any loss or damage as a result of your trading, or your reliance on the information displayed.

## 7. Contacts

If you have any questions about `VietFin` or just to say hi, feel free to leave your message by opening a new discussion in GitHub.
