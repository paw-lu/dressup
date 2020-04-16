"""Tools for generating new Unicode convertions."""
from typing import Tuple


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
            raise ValueError(
                "Each string must contain only unique characters."
                f" ``string{i}`` contains duplicate characters."
            )
    cleaned_string1 = ""
    cleaned_string2 = ""
    for character1, character2 in zip(string1, string2):
        if character1 != character2:
            cleaned_string1 += character1
            cleaned_string2 += character2
    return cleaned_string1, cleaned_string2
