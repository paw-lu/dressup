"""Test cases for the convert module."""
from unittest.mock import Mock

import pytest

from dressup import converter


def test_read_translator(mock_toml_loads: Mock) -> None:
    """It reads the toml file."""
    actual_translator = converter._read_translator()
    expected_translator = {
        "circled": {
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
            "D": "Ⓓ",
            "R": "Ⓡ",
            "E": "Ⓔ",
            "S": "Ⓢ",
            "U": "Ⓤ",
            "P": "Ⓟ",
        },
        "negative_circled": {
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
    assert actual_translator == expected_translator


@pytest.mark.parametrize(
    "name, expected_output",
    [("circled", "Circled"), ("negative_circled", "Negative circled")],
)
def test_format_names(name: str, expected_output: str) -> None:
    """It formats the name."""
    assert converter._format_names(name) == expected_output


@pytest.mark.parametrize(
    "name, expected_output",
    [
        ("Circled", "circled"),
        ("Negative circled", "negative_circled"),
        ("negative-circled", "negative_circled"),
    ],
)
def test_normalize_text(name: str, expected_output: str) -> None:
    """It normalizes the text."""
    assert converter.normalize_text(name) == expected_output


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
    assert converted_characters == expected_output


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
    assert converted_character == expected_output
