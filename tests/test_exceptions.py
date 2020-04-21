"""Test cases for exceptions module."""
from dressup import exceptions


def test_dressupexception_repr() -> None:
    """It returns a string representation."""
    assert repr(exceptions.DressUpException()) == "DressUpException()"


def test_invalidunicodetypeerror_repr() -> None:
    """It returns a string representation."""
    assert repr(exceptions.InvalidUnicodeTypeError()) == "InvalidUnicodeTypeError()"
