"""Exceptions for library."""


class DressUpException(Exception):
    """Base exception for all exceptions raised by the library."""

    def __repr__(self) -> str:
        """Representation of DressUpException."""
        return "DressUpException()"


class InvalidUnicodeTypeError(DressUpException, ValueError):
    """The provided unicode type does not exist."""

    def __repr__(self) -> str:
        """Representation of InvalidUnicodeTypeError."""
        return "InvalidUnicodeTypeError()"
