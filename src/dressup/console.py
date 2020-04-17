"""Command-line interface."""
import typer

from . import __version__
from . import converter

app = typer.Typer()


def version_callback(value: bool) -> None:
    """Return the package version.

    Args:
        value (bool): Whether to return the version.

    Raises:
        Exit: Exits the command line interface.
    """
    if value:
        typer.echo(f"Dress up version: {__version__}")
        raise typer.Exit()
    pass


# TODO: Add a command that lists all types
# TODO: Add autocompletion for options:
# https://typer.tiangolo.com/tutorial/options/autocompletion/
@app.command()
def main(
    characters: str = typer.Argument(None),
    unicode_type: str = typer.Option(
        None, "--type", "-t", help="The Unicode type to convert to."
    ),
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Return the package version.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """Convert characters to different Unicode types.

    If --type is specified, convert to a specific type.
    """
    if characters is None:
        typer.echo("No characters provided to convert.")
        pass
    elif unicode_type is None:
        converted_characters = converter.show_all(characters)
        for character_type, converted_character in converted_characters.items():
            typer.secho(f"\n{character_type}", fg=typer.colors.MAGENTA, bold=True)
            typer.secho(f"\n{converted_character}")
        pass
    else:
        converted_characters = converter.convert(characters, unicode_type=unicode_type)
        typer.echo(converted_characters)
        pass
