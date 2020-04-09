"""Test cases for the convert module."""
from typing import Dict

import pytest

from dressup import convert


def test_converter() -> None:
    """It converts "hello" to ⓗⓔⓛⓛⓞ."""
    converted_characters = convert.convert_characters("hello")
    assert {"Circled": "ⓗⓔⓛⓛⓞ", "Negative circled": "🅗🅔🅛🅛🅞"} == converted_characters


@pytest.mark.parametrize(
    "char_types,expected_output", [("circled", {"Circled": "ⓗⓔⓛⓛⓞ"})]
)
def test_paramaterized_converter(
    char_types: str, expected_output: Dict[str, str]
) -> None:
    """It converts "hello" to the specified unicode type."""
    converted_characters = convert.convert_characters("hello", char_types=char_types)
    assert expected_output == converted_characters
