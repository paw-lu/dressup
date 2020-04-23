"""Convert Unicode characters."""
import pathlib
import re
from typing import Any, Dict, MutableMapping

import toml

from . import exceptions


def _read_translator() -> MutableMapping[str, Any]:
    """Read translator from config file.

    Returns:
        MutableMapping[str, Any]: A dictionary where the keys are the
            unicode type, and the values are nested dictionaries with
            the keys are typical characters and the values are their
            converted unicode.
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


def show_all(characters: str, strict_case: bool = False) -> Dict[str, str]:
    """Return all possible unicode conversions.

    Args:
        characters (str): The characters to convert.
        strict_case (bool): Whether to forbid a character from being
            converted to its lower or upper case counterpart if an exact
            mapping is not found. By default False.

    Returns:
        Dict(str, str): A dictionary where the keys are unicode
            character types and the values are the converted.
    """
    translator = _read_translator()
    if strict_case:
        converted_characters = {
            _format_names(character_type): "".join(
                translator[normalize_text(character_type)].get(character, character)
                for character in characters
            )
            for character_type in translator
        }
    else:
        converted_characters = {
            _format_names(character_type): "".join(
                translator[normalize_text(character_type)].get(
                    character,
                    translator[normalize_text(character_type)].get(
                        character.upper(),
                        translator[normalize_text(character_type)].get(
                            character.lower(), character
                        ),
                    ),
                )
                for character in characters
            )
            for character_type in translator
        }
    return converted_characters


def normalize_text(text_input: str) -> str:
    """Normalize inputted text for easy dictionary matching.

    Strips surrounding whitespace, changes all characters to lowercase,
    and replaces inner whitespace with "_".

    Args:
        text_input (str): An inputted name.

    Returns:
        str: A normalized version of the name.
    """
    return re.sub(r"\s+", "_", text_input.strip().lower().replace("-", "_"))


def convert(
    characters: str, unicode_type: str, strict_case: bool = False, reverse: bool = False
) -> str:
    """Convert characters to a Unicode character type.

    Args:
        characters (str): The characters to convert.
        unicode_type (str): The type of Unicode character types to
            convert to.
        strict_case (bool): Whether to forbid a character from being
            converted to its lower or upper case counterpart if an exact
            mapping is not found. By default False.
        reverse (bool): Whether to reverse the returned characters. This
            can be useful when converting to ``unicode_type``
            "inverted" or "reverse".

    Returns:
        str: The converted Unicode characters.

    Raises:
        InvalidUnicodeTypeError: Raised if value inputted in
            ``unicode_type`` is invalid.
    """
    unicode_type = normalize_text(unicode_type)
    translator = _read_translator()
    if reverse:
        step = -1
    else:
        step = 1
    try:
        type_mapping = translator[unicode_type]
    except KeyError:
        valid_types = ", ".join(translator.keys())
        raise exceptions.InvalidUnicodeTypeError(
            f"'{unicode_type}' is not a valid Unicode type."
            f" Valid types are {valid_types}."
        )
    if strict_case:
        converted_character = "".join(
            type_mapping.get(character, character) for character in characters
        )[::step]
    else:
        converted_character = "".join(
            type_mapping.get(
                character,
                type_mapping.get(
                    character.upper(), type_mapping.get(character.lower(), character)
                ),
            )
            for character in characters
        )[::step]
    return converted_character
