"""Test cases for translator script."""
import pathlib
import textwrap
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture

import translator


@pytest.fixture
def mock_open_file(mocker: MockFixture) -> Mock:
    """Fixture for open file."""
    mock_file_text = """\
        qwer
        mock_unicode asef
        mock_numbers 1234
    """
    mock_file_text = textwrap.dedent(mock_file_text)
    mock = mocker.patch("builtins.open", mocker.mock_open(read_data=mock_file_text))
    return mock


def test_read_file(mock_open_file: Mock) -> None:
    """It converts a text file into character mappings."""
    character_mapping = translator.read_file(pathlib.Path("translator.txt"))
    expected_character_mapping = {
        "mock_numbers": {"e": "3", "q": "1", "r": "4", "w": "2"},
        "mock_unicode": {"q": "a", "r": "f", "w": "s"},
    }
    assert expected_character_mapping == character_mapping


def test_remove_common_characters() -> None:
    """It removes common characters between two strings."""
    base_characters = "`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./~!@"
    circled_characters = "`①②③④⑤⑥⑦⑧⑨0⊖⊜ⓠⓦⓔⓡⓣⓨⓤⓘⓞⓟ[]ⓐⓢⓓⓕⓖⓗⓙⓚⓛ;'ⓩⓧⓒⓥⓑⓝⓜ,⨀⊘~!@"
    actual_characters = translator.remove_common_characters(
        base_characters, circled_characters
    )
    expected_characters = (
        "123456789-=qwertyuiopasdfghjklzxcvbnm./",
        "①②③④⑤⑥⑦⑧⑨⊖⊜ⓠⓦⓔⓡⓣⓨⓤⓘⓞⓟⓐⓢⓓⓕⓖⓗⓙⓚⓛⓩⓧⓒⓥⓑⓝⓜ⨀⊘",
    )
    assert expected_characters == actual_characters


def test_unequal_length() -> None:
    """It raises a ValueError when string lengths are unequal."""
    base_characters = "`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./~!@"
    circled_characters = "`①②③④⑤⑥⑦⑧⑨0⊖⊜ⓠⓦⓔⓡⓣ"
    with pytest.raises(ValueError):
        translator.remove_common_characters(base_characters, circled_characters)
        pass


@pytest.mark.parametrize(
    "string1, string2", [("1234567890", "①②③④⑤⑥⑦⑨⑨0"), ("1234567990", "①②③④⑤⑥⑦⑧⑨0")]
)
def test_duplicates(string1: str, string2: str) -> None:
    """It raises a ValueError when either input had duplicate values."""
    base_characters = "`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./~!@"
    circled_characters = "`①②③④⑤⑥⑦⑧⑨0⊖⊜ⓠⓦⓔⓡⓣ"
    with pytest.raises(ValueError):
        translator.remove_common_characters(base_characters, circled_characters)
        pass
