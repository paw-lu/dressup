"""Test cases for the convert module."""
import pathlib
from unittest.mock import Mock

import pytest
import toml

from dressup import converter, exceptions


def test_translator_repr() -> None:
    """Its string representation contains the init parameters."""
    translator = converter.Translator({letter: "b" for letter in "ab"}, False)
    assert str(translator) == "Translator({'a': 'b', 'b': 'b'}, False)"


def test_default_translatortor() -> None:
    """It returns an empty dictionary when provided to items."""
    translator = converter.Translator()
    assert translator == {}


def test_strict_case_translator() -> None:
    """It returns the key when no match is found."""
    values = {"a": "<3"}
    translator = converter.Translator(values, strict_case=True)
    assert translator["A"] == "A"


def test_missing_translator_upper() -> None:
    """It returns the upper case match when no match is found."""
    values = {"A": "<3"}
    translator = converter.Translator(values, strict_case=False)
    assert translator["a"] == "<3"


def test_missing_translator_lower() -> None:
    """It returns the lower case match when no match is found."""
    values = {"a": "<3"}
    translator = converter.Translator(values, strict_case=False)
    assert translator["A"] == "<3"


def test_valid_toml() -> None:
    """It is a valid TOML file."""
    file_text = pathlib.Path("src/dressup/translator.toml").read_text()
    assert toml.loads(file_text)


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
            "A": "🅐",
            "B": "🅑",
            "C": "🅒",
            "D": "🅓",
            "E": "🅔",
            "F": "🅕",
            "G": "🅖",
            "H": "🅗",
            "I": "🅘",
            "J": "🅙",
            "K": "🅚",
            "L": "🅛",
            "M": "🅜",
            "N": "🅝",
            "O": "🅞",
            "P": "🅟",
            "Q": "🅠",
            "R": "🅡",
            "S": "🅢",
            "T": "🅣",
            "U": "🅤",
            "V": "🅥",
            "W": "🅦",
            "X": "🅧",
            "Y": "🅨",
            "Z": "🅩",
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
    "characters, expected_output, strict_case, reverse",
    [
        ("hello", {"Circled": "ⓗⓔⓛⓛⓞ", "Negative circled": "🅗🅔🅛🅛🅞"}, False, False),
        ("he(lo", {"Circled": "ⓗⓔ(ⓛⓞ", "Negative circled": "🅗🅔(🅛🅞"}, False, False),
        ("💦a", {"Circled": "💦ⓐ", "Negative circled": "💦🅐"}, False, False),
    ],
)
def test_show_all(
    mock_toml_loads: Mock,
    characters: str,
    expected_output: str,
    strict_case: bool,
    reverse: bool,
) -> None:
    """It converts characterse to all possible Unicode types."""
    converted_characters = converter.show_all(
        characters=characters, strict_case=strict_case, reverse=reverse
    )
    assert converted_characters == expected_output


@pytest.mark.parametrize(
    "characters, expected_output, strict_case, reverse",
    [
        ("hello", {"Circled": "ⓗⓔⓛⓛⓞ", "Negative circled": "hello"}, True, False),
        ("he(lo", {"Circled": "ⓗⓔ(ⓛⓞ", "Negative circled": "he(lo"}, True, False),
        ("💦a", {"Circled": "💦ⓐ", "Negative circled": "💦a"}, True, False),
    ],
)
def test_strict_case_show_all(
    mock_toml_loads: Mock,
    characters: str,
    expected_output: str,
    strict_case: bool,
    reverse: bool,
) -> None:
    """It strictly converts characterse to all Unicode types."""
    converted_characters = converter.show_all(
        characters=characters, strict_case=strict_case, reverse=reverse
    )
    assert converted_characters == expected_output


@pytest.mark.parametrize(
    "characters, expected_output, strict_case, reverse",
    [
        ("hello", {"Circled": "ⓞⓛⓛⓔⓗ", "Negative circled": "🅞🅛🅛🅔🅗"}, False, True),
        ("he(lo", {"Circled": "ⓞⓛ(ⓔⓗ", "Negative circled": "🅞🅛(🅔🅗"}, False, True),
        ("💦a", {"Circled": "ⓐ💦", "Negative circled": "🅐💦"}, False, True),
    ],
)
def test_reverse_show_all(
    mock_toml_loads: Mock,
    characters: str,
    expected_output: str,
    strict_case: bool,
    reverse: bool,
) -> None:
    """It converts reversed characterse to all Unicode types."""
    converted_characters = converter.show_all(
        characters=characters, strict_case=strict_case, reverse=reverse
    )
    assert converted_characters == expected_output


@pytest.mark.parametrize(
    "characters, unicode_type, expected_output, strict_case, reverse",
    [
        ("hello", "Circled", "ⓗⓔⓛⓛⓞ", False, False),
        ("hello", "Negative circled", "🅗🅔🅛🅛🅞", False, False),
        ("he(lo", "Circled", "ⓗⓔ(ⓛⓞ", False, False),
        ("💦a", "Circled", "💦ⓐ", False, False),
    ],
)
def test_convert(
    mock_toml_loads: Mock,
    characters: str,
    unicode_type: str,
    expected_output: str,
    strict_case: bool,
    reverse: bool,
) -> None:
    """It converts characters to the specified Unicode type."""
    converted_character = converter.convert(
        characters=characters,
        unicode_type=unicode_type,
        strict_case=strict_case,
        reverse=reverse,
    )
    assert converted_character == expected_output


@pytest.mark.parametrize(
    "characters, unicode_type, expected_output, strict_case, reverse",
    [
        ("hello", "Circled", "ⓗⓔⓛⓛⓞ", True, False),
        ("hello", "Negative circled", "hello", True, False),
        ("he(lo", "Circled", "ⓗⓔ(ⓛⓞ", True, False),
        ("💦a", "Circled", "💦ⓐ", True, False),
    ],
)
def test_strict_case_convert(
    mock_toml_loads: Mock,
    characters: str,
    unicode_type: str,
    expected_output: str,
    strict_case: bool,
    reverse: bool,
) -> None:
    """It strictly converts characters to the specified Unicode type."""
    converted_character = converter.convert(
        characters=characters,
        unicode_type=unicode_type,
        strict_case=strict_case,
        reverse=reverse,
    )
    assert converted_character == expected_output


@pytest.mark.parametrize(
    "characters, unicode_type, expected_output, strict_case, reverse",
    [
        ("hello", "Circled", "ⓞⓛⓛⓔⓗ", False, True),
        ("hello", "Negative circled", "🅞🅛🅛🅔🅗", False, True),
        ("he(lo", "Circled", "ⓞⓛ(ⓔⓗ", False, True),
        ("💦a", "Circled", "ⓐ💦", False, True),
    ],
)
def test_reverse_convert(
    mock_toml_loads: Mock,
    characters: str,
    unicode_type: str,
    expected_output: str,
    strict_case: bool,
    reverse: bool,
) -> None:
    """It converts and reverses characters to the specified type."""
    converted_character = converter.convert(
        characters=characters,
        unicode_type=unicode_type,
        strict_case=strict_case,
        reverse=reverse,
    )
    assert converted_character == expected_output


def test_invalid_unicode_type_exception(mock_toml_loads: Mock) -> None:
    """It raises an InvalidUnicodeTypeError exception."""
    with pytest.raises(exceptions.InvalidUnicodeTypeError):
        converter.convert("hello", unicode_type="non-existant type")


def test_invalid_unicode_type_info(mock_toml_loads: Mock) -> None:
    """It lists accepted values upon raising exception."""
    with pytest.raises(exceptions.InvalidUnicodeTypeError) as execinfo:
        converter.convert("hello", unicode_type="non-existant type")
    exception_message = str(execinfo.value)
    expected_exception_message = (
        "'non_existant_type' is not a valid Unicode type."
        " Valid types are circled, negative_circled."
    )
    assert exception_message == expected_exception_message
