"""Command-line interface."""
from typing import Generator, Tuple

import typer
from typer import Context

from . import __version__, converter, exceptions

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


def complete_type(
    ctx: Context, incomplete: str
) -> Generator[Tuple[str, str], None, None]:
    """Autocomplete options for --type option.

    Args:
        ctx (Context): Current command line arguments.
        incomplete (str): The incomplete argument.

    Yields:
        (Generator): Arguments that match ``incomplete`` along
            with a preview of the conversion.
    """
    # TODO: Respect options in preview as you add them in cli
    if ctx.args:
        sample_text = ctx.args[0]
    else:
        sample_text = "Dress Up!"
    incomplete = converter.normalize_text(incomplete)
    converted_incomplete = converter.show_all(sample_text)
    for unicode_type, converted_characters in converted_incomplete.items():
        unicode_type = converter.normalize_text(unicode_type)
        if unicode_type.startswith(incomplete):
            yield (unicode_type.replace("_", "-"), converted_characters)


# TODO: Add a command that lists all types
# TODO: Add autocompletion for options:
# https://typer.tiangolo.com/tutorial/options/autocompletion/
@app.command()
def main(
    characters: str = typer.Argument(None),
    strict_case: bool = typer.Option(
        False, "--strict-case", "-s", help="Do not fallback to different cases.",
    ),
    unicode_type: str = typer.Option(
        None,
        "--type",
        "-t",
        help="The Unicode type to convert to.",
        autocompletion=complete_type,
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
        # TODO As I add more options in make sure to check for their
        # invocation here and add accompanying test
        if unicode_type is not None:
            raise typer.Exit(code=1)
        else:
            raise typer.Exit(code=0)
    elif unicode_type is None:
        converted_characters = converter.show_all(characters)
        for character_type, converted_character in converted_characters.items():
            typer.secho(f"\n{character_type}", fg=typer.colors.MAGENTA, bold=True)
            typer.secho(f"\n{converted_character}")
        pass
    else:
        try:
            converted_characters = converter.convert(
                characters, unicode_type=unicode_type
            )
        except exceptions.InvalidUnicodeTypeError as error:
            exception_message = str(error).replace("_", "-")
            typer.secho(
                exception_message, fg=typer.colors.BRIGHT_RED,
            )
            raise typer.Exit(code=1)
        typer.echo(converted_characters)
        pass
