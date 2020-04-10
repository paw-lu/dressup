"""Test cases for the convert module."""
from typing import Dict
from unittest.mock import Mock

import pytest

from dressup import convert


def test_read_translator(mock_toml_loads: Mock) -> None:
    """It reads the toml file."""
    actual_translator = convert._read_translator()
    expected_translator = {
        "Circled": {
            "a": "ⓐ",
            "b": "ⓑ",
            "c": "ⓒ",
            "d": "ⓓ",
            "e": "ⓔ",
            "f": "ⓕ",
            "g": "ⓖ",
            "h": "ⓗ",
            "i": "ⓘ",
            "j": "ⓙ",
            "k": "ⓚ",
            "l": "ⓛ",
            "m": "ⓜ",
            "n": "ⓝ",
            "o": "ⓞ",
            "p": "ⓟ",
            "q": "ⓠ",
            "r": "ⓡ",
            "s": "ⓢ",
            "t": "ⓣ",
            "u": "ⓤ",
            "v": "ⓥ",
            "w": "ⓦ",
            "x": "ⓧ",
            "y": "ⓨ",
            "z": "ⓩ",
        },
        "Circled (neg)": {
            "a": "🅐",
            "b": "🅑",
            "c": "🅒",
            "d": "🅓",
            "e": "🅔",
            "f": "🅕",
            "g": "🅖",
            "h": "🅗",
            "i": "🅘",
            "j": "🅙",
            "k": "🅚",
            "l": "🅛",
            "m": "🅜",
            "n": "🅝",
            "o": "🅞",
            "p": "🅟",
            "q": "🅠",
            "r": "🅡",
            "s": "🅢",
            "t": "🅣",
            "u": "🅤",
            "v": "🅥",
            "w": "🅦",
            "x": "🅧",
            "y": "🅨",
            "z": "🅩",
        },
    }
    assert expected_translator == actual_translator


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
