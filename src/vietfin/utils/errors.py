"""Custom exceptions for the query from providers in VietFin."""


class EmptyDataError(Exception):
    """Exception raised for empty data."""

    def __init__(
        self,
        message: str = "No results found. Try adjusting the query parameters.",
    ):
        """Initialize the exception."""
        self.message = message
        super().__init__(self.message)


class VietFinError(Exception):
    """VietFin Error."""

    def __init__(self, original: str | Exception | None = None):
        self.original = original
        super().__init__(str(original))
