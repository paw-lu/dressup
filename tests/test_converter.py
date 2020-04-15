"""Test cases for the convert module."""
from unittest.mock import Mock

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


def test_show_all(mock_toml_loads: Mock) -> None:
    """It converts "hello" to all possible Unicode types."""
    converted_characters = converter.show_all("hello")
    assert {"Circled": "ⓗⓔⓛⓛⓞ", "Negative circled": "🅗🅔🅛🅛🅞"} == converted_characters


def test_convert(mock_toml_loads: Mock) -> None:
    """It converts "hello" to the specified Unicode type."""
    converted_character = converter.convert("hello", "Circled")
    assert "ⓗⓔⓛⓛⓞ" == converted_character
