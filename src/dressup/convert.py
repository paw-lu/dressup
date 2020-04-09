"""Convert unicode."""
from typing import Dict


def convert_characters(characters: str) -> Dict[str, str]:
    """Convert characters to different unicode types."""
    translator = {
        "Circled": dict(zip("abcdefghijklmnopqrstuvwxyz", "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ"))
    }
    converted_characters = {
        character_type: "".join(
            translator[character_type].get(character, character)
            for character in characters
        )
        for character_type in translator
    }
    return converted_characters
