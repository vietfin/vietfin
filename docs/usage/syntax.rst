Basic Syntax
============

The structure of command syntax is standardized across common fields. This ensures that a *date* is always a *date string (YYYY-MM-DD)* and the format remains consistent throughout. Standardized parameters include, but are not limited to:

provider
    This parameter is the way to select the specific source of the data from the endpoint. There's always a default provider, but it can be overridden by the user.

    Provider values are entered as a ``string`` in lower-case, with an underscore for multiple words.

symbol
    Symbols are not case-sensitive, and is entered as a ``string``.

start_date, end_date
    Dates are entered as a ``string``, formatted as, ``YYYY-MM-DD``.

    If not specified, the default value of *end_date* is the current date. And the default value of *start_date* is ``60 days`` before the *end_date*.

limit
    When a command needs *limit* parameter, it will return N results starting from the *end_date*.

    Limit values are entered as an ``integer``.