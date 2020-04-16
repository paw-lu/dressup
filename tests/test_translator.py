"""Test cases for translator script."""
import pytest

import translator


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
