"""Test cases for the convert module."""
from typing import Dict
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture

from dressup import convert


@pytest.fixture
def mock_toml_loads(mocker: MockFixture) -> Mock:
    """Fixture for mocking toml.loads."""
    mock = mocker.patch("toml.loads")
    mock.return_value = {
        "Circled": dict(
            zip("abcdefghijklmnopqrstuvwxyz", "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ")
        ),
        "Circled (neg)": dict(
            zip("abcdefghijklmnopqrstuvwxyz", "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩")
        ),
    }
    return mock


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
