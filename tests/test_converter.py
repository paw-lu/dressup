"""Test cases for the convert module."""
from unittest.mock import Mock

import pytest

from dressup import converter


def test_read_translator(mock_toml_loads: Mock) -> None:
    """It reads the toml file."""
    actual_translator = converter._read_translator()
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
        "Negative circled": {
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


@pytest.mark.parametrize(
    "characters, expected_output",
    [
        ("hello", {"Circled": "ⓗⓔⓛⓛⓞ", "Negative circled": "🅗🅔🅛🅛🅞"}),
        ("he(lo", {"Circled": "ⓗⓔ(ⓛⓞ", "Negative circled": "🅗🅔(🅛🅞"}),
        ("💦a", {"Circled": "💦ⓐ", "Negative circled": "💦🅐"}),
    ],
)
def test_show_all(mock_toml_loads: Mock, characters: str, expected_output: str) -> None:
    """It converts characterse to all possible Unicode types."""
    converted_characters = converter.show_all(characters=characters)
    assert expected_output == converted_characters


@pytest.mark.parametrize(
    "characters, unicode_type, expected_output",
    [
        ("hello", "Circled", "ⓗⓔⓛⓛⓞ"),
        ("hello", "Negative circled", "🅗🅔🅛🅛🅞"),
        ("he(lo", "Circled", "ⓗⓔ(ⓛⓞ"),
        ("💦a", "Circled", "💦ⓐ"),
    ],
)
def test_convert(
    mock_toml_loads: Mock, characters: str, unicode_type: str, expected_output: str
) -> None:
    """It converts characters to the specified Unicode type."""
    converted_character = converter.convert(
        characters=characters, unicode_type=unicode_type
    )
    assert expected_output == converted_character
