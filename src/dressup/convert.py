"""Convert unicode."""
import pathlib
from typing import Any, Dict, Iterable, MutableMapping, Optional, Union

import toml


def _read_translator() -> MutableMapping[str, Any]:
    """Read translator from config file.

    Returns:
        A dictionary where the keys are the unicode type, and the values
        are nested dictionaries with the keys are typical characters and
        the values are their converted unicode.
    """
    toml_path = pathlib.Path(__file__).parent / pathlib.Path("translator.toml")
    toml_text = toml_path.read_text()
    translator = toml.loads(toml_text)
    return translator


def convert_characters(
    characters: str, char_types: Optional[Union[str, Iterable[str]]] = None
) -> Dict[str, str]:
    """Convert characters to different unicode types.

    Args:
        characters (str): The characters to convert.
        char_types (str or iterable of strings): The type of unicode character
            to convert to. Options are "circled" and "negative circled".
            If left as None will return all types.

    Returns:
        A dictionary where the keys are unicode character types and the
        values are the converted
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    translator = {
        "Circled": dict(zip(alphabet, "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ")),
        "Negative circled": dict(zip(alphabet, "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩")),
    }
    if isinstance(char_types, str):
        char_types = [char_types]
    if char_types is not None:
        char_types = [
            f"{char_type[0].upper()}{char_type[1:].lower()}" for char_type in char_types
        ]
    else:
        char_types = ["Circled", "Negative circled"]

    converted_characters = {
        character_type: "".join(
            translator[character_type].get(character, character)
            for character in characters
        )
        for character_type in char_types
    }
    # TODO: Add exception here for missing key
    return converted_characters
