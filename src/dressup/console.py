"""Command-line interface."""
import typer

from . import __version__
from . import convert

app = typer.Typer()


def version_callback(value: bool) -> None:
    """Return the package version."""
    if value:
        typer.echo(f"Dress up version: {__version__}")
        raise typer.Exit()
    pass


@app.command()
def main(
    characters: str,
    version: bool = typer.Option(
        None,
        "--version",
        help="Return the package version." "",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """Dress up your unicode!"""
    converted_characters = convert.convert_characters(characters)
    for character_type, converted_character in converted_characters.items():
        typer.secho(f"\n{character_type}", fg=typer.colors.MAGENTA, bold=True)
        typer.secho(f"\n{converted_character}")
    pass
