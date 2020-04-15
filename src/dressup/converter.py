"""Convert unicode."""
import pathlib
from typing import Any, Dict, MutableMapping

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


def _format_names(name: str) -> str:
    """Format dictionary key names to be human friendly.

    Args:
        name (str): The Unicode type name.

    Returns:
        str: The formatted Unicode type name.
    """
    return name[0].upper() + name[1:].replace("_", " ")


def show_all(characters: str) -> Dict[str, str]:
    """Return all possible unicode conversions.

    Args:
        characters (str): The characters to convert.

    Returns:
        A dictionary where the keys are unicode character types and the
        values are the converted.
    """
    translator = _read_translator()
    converted_characters = {
        character_type: "".join(
            translator[character_type].get(character, character)
            for character in characters
        )
        for character_type in translator
    }
    return converted_characters


def convert(characters: str, unicode_type: str) -> str:
    """Convert characters to a Unicode character type.

    Args:
        characters (str): The characters to convert.
        unicode_type (str): The type of Unicode character types to
            convert to.

    Returns:
        The converted Unicode characters.
    """
    # TODO: Make this case-insensitive
    translator = _read_translator()[unicode_type]
    converted_character = "".join(
        translator.get(character, character) for character in characters
    )
    return converted_character
