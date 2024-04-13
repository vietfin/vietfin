# Change Log

## v0.2.0 (TBD)

- Change default provider of command `derivatives.futures.quote()` from `vdsc` to `ssi`.
    - Reason: `ssi` does not require cookies, easier to crawl data.
    - Add function to fetch futures contract quotes from `ssi` provider.
- Add new group of commands `equity.discovery.*()`
- Add new command `derivatives.futures.search()`
- Update docs related to these two new features
- Add unit tests for this new features
- Replace `datetime.utcfromtimestamp` with `datetime.fromtimestamp` since the previous will be [deprecated since python v3.12](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp)
- Replace package [bs4](https://pypi.org/project/beautifulsoup4/) with [selectolax](https://github.com/rushter/selectolax) for better performance.
- Replace package [requests](https://github.com/psf/requests) with [httpx](https://www.python-httpx.org/) for better performance.
- Remove `vdsc` from list of available data provider of function `derivatives.futures.quote()`. Reason: `vdsc` requires cookies, currently did not find an automated solutions to handle this. Update docs accordingly.


## v0.1.0 (2024-03-08)

- Finish development of the first version of the VietFin package.
- Added unit tests to assert the functionality of all the user-facing functions with default parameters.
- Added a documentation website with examples and reference.