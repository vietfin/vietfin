"""Custom exceptions for the query from providers in VietFin."""


class EmptyDataError(Exception):
    """Raised if the API response is empty."""

    def __init__(
        self,
        message: str = "API response is empty. Try adjusting the query parameters.",
    ):
        """Initialize the exception."""
        self.message = message
        super().__init__(self.message)


class VietFinError(Exception):
    """Raised for Uncategorized Error."""

    def __init__(self, original: str | Exception | None = None):
        self.original = original
        super().__init__(str(original))
