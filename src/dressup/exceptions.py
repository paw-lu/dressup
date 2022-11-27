"""Exceptions for library."""


class DressUpError(Exception):
    """Base exception for all exceptions raised by the library."""

    def __repr__(self) -> str:
        """Representation of DressUpError."""
        return "DressUpError()"


class InvalidUnicodeTypeError(DressUpError, ValueError):
    """The provided unicode type does not exist."""

    def __repr__(self) -> str:
        """Representation of InvalidUnicodeTypeError."""
        return "InvalidUnicodeTypeError()"
