"""Test cases for the convert module."""
from dressup import convert


def test_converter() -> None:
    """It converts "hello" to ⓗⓔⓛⓛⓞ."""
    converted_characters = convert.convert_characters("hello")
    assert {"Circled": "ⓗⓔⓛⓛⓞ", "Negative circled": "🅗🅔🅛🅛🅞"} == converted_characters
