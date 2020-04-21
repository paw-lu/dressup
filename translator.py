"""Tools for generating new Unicode convertions."""
import argparse
import collections
import pathlib
from pathlib import Path
from typing import Dict, Tuple

import toml


def remove_common_characters(string1: str, string2: str) -> Tuple[str, str]:
    """Remove characters the two strings have in common.

    Both strings must be of the same length and only cointain unique
    characters. Characters in both ``string1`` and ``string2`` should
    have both characters in the same order.

    Args:
        string1 (str): The string that will be checked against
            ``string2``.
        string2 (str): The string that will be checked against
            ``string1``.

    Returns:
        Tuple[str, str]: The characters unique to ``string1`` and
            ``string2``, respectively.

    Raises:
        ValueError: If the length of ``string1`` does not equal that of
            ``string2``.
        ValueError: If either ``string1`` or ``string2`` contain
            duplicate characters.
    """
    if len(string1) != len(string2):
        raise ValueError(
            "Both strings must be the same length."
            f" ``string1`` is of length {len(string1)}"
            f" and ``string2`` is of length {len(string2)}"
        )
    for i, string in enumerate((string1, string2)):
        if len(string) != len(set(string)):
            character_counts = collections.Counter(string)
            duplicates = [
                character
                for character in character_counts
                if 1 < character_counts[character]
            ]
            duplicate_preview = ", ".join(duplicate for duplicate in duplicates[:5])
            raise ValueError(
                "Each string must contain only unique characters."
                f" ``string{i + 1}`` contains duplicates of the"
                f" following characters: {duplicate_preview},..."
            )
    cleaned_string1 = ""
    cleaned_string2 = ""
    for character1, character2 in zip(string1, string2):
        if character1 != character2:
            cleaned_string1 += character1
            cleaned_string2 += character2
    return cleaned_string1, cleaned_string2


def read_file(file_path: Path) -> Dict[str, Dict[str, str]]:
    """Read in a file of character transformations.

    Assumes top line of file is the characters to be transformed, and
    following lines are the transformation name followed by a whitespace
    seperator and the transformed characters. It is assumed that
    characters without a corresponding transformation will just contain
    the original character.

    Args:
        file_path (Path): The location of the file.

    Returns:
        Dict[str, Dict[str, str]]: A dictionary representation of the
            file. Keys are the transformation's name, and values are
            dictionaries who's keys are the characters to be transformed
            and their respective values are the transformed characters.
    """
    translator = {}
    with open(file_path) as file:
        for i, line in enumerate(file.readlines()):
            if i == 0:
                original_text = line.strip()
            else:
                unicode_name, converted_characters = line.split()
                base_characters, converted_characters = remove_common_characters(
                    original_text, converted_characters
                )
                translator[unicode_name] = dict(
                    zip(base_characters, converted_characters)
                )
    return translator


def write_config(translator: Dict[str, Dict[str, str]], write_path: Path) -> None:
    """Write dictionary to a TOML file.

    Args:
        translator (Dict[str, Dict[str, str]]): The dictionary to
            convert to TOML.
        write_path (Path): The path that will be written to. Should be a
            TOML file.
    """
    write_path.write_text(toml.dumps(translator))
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_filename")
    parser.add_argument("output_filename")
    args = parser.parse_args()
    converted_characters = pathlib.Path(args.input_filename)
    config_path = pathlib.Path("hey.toml")
    translator = read_file(converted_characters)
    write_config(translator, write_path=pathlib.Path(args.output_filename))
