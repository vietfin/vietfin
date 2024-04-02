# Change Log

## v0.2.0 (TBD)

- Change default provider of command `derivatives.futures.quote()` from `vdsc` to `ssi`.
    - Reason: `ssi` does not require cookies, easier to crawl data.
    - Add function to fetch futures contract quotes from `ssi` provider.
- Add new group of commands `equity.discovery.*()`
- Add new command `derivatives.futures.search()`
- Update docs related to these two new features
- Add unit tests for this new features
- Replace `datetime.utcfromtimestamp` with `datetime.fromtimestamp` since the previous will be [deprecated since v3.12](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp)

## v0.1.0 (2024-03-08)

- Finish development of the first version of the VietFin package.
- Added unit tests to assert the functionality of all the user-facing functions with default parameters.
- Added a documentation website with examples and reference.