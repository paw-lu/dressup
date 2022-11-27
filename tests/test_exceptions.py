"""Test cases for exceptions module."""
from dressup import exceptions


def test_dressupexception_repr() -> None:
    """It returns a string representation."""
    assert repr(exceptions.DressUpError()) == "DressUpError()"


def test_invalidunicodetypeerror_repr() -> None:
    """It returns a string representation."""
    assert repr(exceptions.InvalidUnicodeTypeError()) == "InvalidUnicodeTypeError()"
