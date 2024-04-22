"""Utility functions for testing."""

from typing import Any


def assert_run_success(
    result: Any,
    symbol: str | None = None,
    provider: str | None = None,
) -> None:
    """Checks whether the command in VietFin can be executed successfully.

    This simple assertion validates the result obtained from a command:
    - assert correct symbol name returned from command
    - assert correct provider name returned from command
    - assert results attribute of VfObject is not Null
    """
    if symbol is not None:
        # Assert correct symbol name returned from query
        symbol = symbol.upper()  # type: ignore
        assert result.extra.get("symbol") == symbol

    if provider is not None:
        # Assert correct provider name returned from query
        provider = provider.lower()
        assert result.provider == provider

    # Assert results attribute is not null
    assert result.extra.get("records_count") > 0
