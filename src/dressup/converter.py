"""Convert Unicode characters."""
import pathlib
import re
from typing import Any, Dict, MutableMapping, Optional

import toml

from . import exceptions


class Translator(dict):
    """Translator for converting text to Unicode.

    Attributes:
        items (Dict[str, str]): Keys and values to prepopulate Translator.
            Optional.
        strict_case (bool): Whether to forbid characters from being
            converted to an upper or lower case counterpart if an exact
            match is not found. By default set to False.
    """

    def __init__(
        self, items: Optional[Dict[str, str]] = None, strict_case: bool = False
    ) -> None:
        """Constructor."""
        if items is not None:
            self.update(items)
        self.strict_case = strict_case
        pass

    def __repr__(self) -> str:
        """Representation of Translator."""
        dict_repr = (
            "{"
            + ", ".join(
                ": ".join((f"'{item}'", f"'{key}'")) for item, key in self.items()
            )
            + "}"
        )
        return f"Translator({dict_repr}, {self.strict_case})"

    def __missing__(self, key: str) -> str:
        """Return value in the case of a missing key.

        If ``strict_case`` is True, will return the key itself. If
        False, will first try to return a value matching the upper or
        lowercase variant of the key.

        Args:
            key (str): The key missing from Translator.

        Returns:
            str: The returned value.
        """
        if self.strict_case:
            return key
        else:
            if key.upper() in self:
                return self[key.upper()]
            elif key.lower() in self:
                return self[key.lower()]
            else:
                return key


def _read_translator(strict_case: bool = False) -> MutableMapping[str, Any]:
    """Read translator from config file.

    Args:
        strict_case (bool): Whether to forbid characters from being
            converted to an upper or lower case counterpart if an exact
            match is not found. By default set to False.

    Returns:
        MutableMapping[str, Any]: A dictionary where the keys are the
        unicode type, and the values are nested dictionaries with the
        keys are typical characters and the values are their
        converted unicode.
    """
    toml_path = pathlib.Path(__file__).parent / pathlib.Path("translator.toml")
    toml_text = toml_path.read_text()
    unicode_mapping = toml.loads(toml_text)
    translator = {
        unicode_type: Translator(unicode_mapping[unicode_type], strict_case=strict_case)
        for unicode_type in unicode_mapping
    }
    return translator


def _format_names(name: str) -> str:
    """Format dictionary key names to be human friendly.

    Args:
        name (str): The Unicode type name.

    Returns:
        str: The formatted Unicode type name.
    """
    return name[0].upper() + name[1:].replace("_", " ")


def show_all(
    characters: str, strict_case: bool = False, reverse: bool = False
) -> Dict[str, str]:
    """Return all possible unicode conversions.

    Args:
        characters (str): The characters to convert.
        strict_case (bool): Whether to forbid a character from being
            converted to its lower or upper case counterpart if an exact
            mapping is not found. By default False.
        reverse (bool): Whether to reverse the returned characters. This
            can be useful when converting to ``unicode_type``
            "inverted" or "reverse". By default False.

    Returns:
        Dict(str, str): A dictionary with the converted characters.

        The dictionary keys are the names of character types and the
        values are the converted characters.

    Example:
        Show all possible conversions for the string "Hello".

        >>> import dressup
        >>> dressup.show_all("Hello")
        {'Circle': 'Ⓗⓔⓛⓛⓞ', 'Negative circle': '🅗🅔🅛🅛🅞',
        'Monospace': 'Ｈｅｌｌｏ', 'Math bold': '𝐇𝐞𝐥𝐥𝐨',
        'Math bold fraktur': '𝕳𝖊𝖑𝖑𝖔', 'Math bold italic': '𝑯𝒆𝒍𝒍𝒐',
        'Math bold script': '𝓗𝓮𝓵𝓵𝓸', 'Math double struck': 'ℍ𝕖𝕝𝕝𝕠',
        'Math monospace': '𝙷𝚎𝚕𝚕𝚘', 'Math sans': '𝖧𝖾𝗅𝗅𝗈', 'Math sans bold':
        '𝗛𝗲𝗹𝗹𝗼', 'Math sans bold italic': '𝙃𝙚𝙡𝙡𝙤', 'Math sans italic':
        '𝘏𝘦𝘭𝘭𝘰', 'Parenthesized': '⒣⒠⒧⒧⒪', 'Square': '🄷🄴🄻🄻🄾',
        'Negative square': '🅷🅴🅻🅻🅾', 'Cute': 'Héĺĺő', 'Math fraktur':
        'ℌ𝔢𝔩𝔩𝔬', 'Rock dots': 'Ḧëḷḷö', 'Small caps': 'ʜᴇʟʟᴏ', 'Stroked':
        'Ħɇłłø', 'Subscript': 'ₕₑₗₗₒ', 'Superscript': 'ᴴᵉˡˡᵒ',
        'Inverted': 'ɥǝןןo', 'Reversed': 'Hɘ⅃⅃o'}
    """
    translator = _read_translator(strict_case=strict_case)
    if reverse:
        characters = characters[::-1]
    converted_characters = {
        _format_names(character_type): "".join(
            translator[normalize_text(character_type)][character]
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
            convert to. Valid values are "circle", "negative circle",
            "monospace", "math bold", "math bold fraktur",
            "math bold italic", "math bold script",
            "math double struck", "math monospace",
            "math sans", "math sans bold", "math sans bold italic",
            "math sans italic", "parenthesized", "square",
            "negative square", "cute", "math fraktur", "rock dots",
            "small caps", "stroked", "subscript", "superscript",
            "inverted", and "reversed".
        strict_case (bool): Whether to forbid a character from being
            converted to its lower or upper case counterpart if an exact
            mapping is not found. By default False.
        reverse (bool): Whether to reverse the returned characters. This
            can be useful when converting to ``unicode_type``
            "inverted" or "reverse". By default False.

    Returns:
        str: The converted Unicode characters.

    Raises:
        InvalidUnicodeTypeError: Raised if value inputted in
            ``unicode_type`` is invalid.

    Examples:
        Convert the string "Hello" to negative circle characters.

        >>> import dressup
        >>> dressup.convert("Hello", unicode_type="negative circle")
        '🅗🅔🅛🅛🅞'

        Convert the string "Hello" to negative circle characters, but
        don't convert lowercase to uppercase if a perfect  match isn't
        found.

        >>> import dressup
        >>> dressup.convert(
        ...     "Hello",
        ...     unicode_type="negative circle",
        ...     strict_case=True,
        ... )
        '🅗ello'

        Concvert the string "Hello" to reversed characters, but

        >>> import dressup
        >>> import dressup
        >>> dressup.convert(
        ...     "Hello",
        ...     unicode_type="reversed",
        ...     reverse=True,
        ... )
        'o⅃⅃ɘH'
    """
    unicode_type = normalize_text(unicode_type)
    translator = _read_translator()
    if reverse:
        characters = characters[::-1]
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
        )
    else:
        converted_character = "".join(
            type_mapping.get(
                character,
                type_mapping.get(
                    character.upper(), type_mapping.get(character.lower(), character)
                ),
            )
            for character in characters
        )
    return converted_character
