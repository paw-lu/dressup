"""Command-line interface."""
from typing import Generator, Tuple

import rich.box
import rich.console
import rich.style
import rich.table
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
    if ctx.args:
        sample_text = ctx.args[0]
    else:
        sample_text = "Dress Up!"
    incomplete = converter.normalize_text(incomplete)
    converted_incomplete = converter.show_all(
        sample_text,
        strict_case=ctx.params.get("strict_case", False),
        reverse=ctx.params.get("reverse", False),
    )
    for unicode_type, converted_characters in converted_incomplete.items():
        unicode_type = converter.normalize_text(unicode_type)
        if unicode_type.startswith(incomplete):
            yield (unicode_type.replace("_", "-"), converted_characters)


# TODO: Add a command that lists all types
@app.command()
def main(
    characters: str = typer.Argument(None),
    strict_case: bool = typer.Option(
        False, "--strict-case", "-s", help="Do not fallback to different cases.",
    ),
    reverse: bool = typer.Option(False, "--reverse", "-r", help="Reverse the output."),
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
        help="Display the version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """Convert characters to different Unicode types.

    If --type is specified, convert to a specific type.
    """
    if characters is None:
        typer.echo("No characters provided to convert.")
        if unicode_type is not None or strict_case or reverse:
            raise typer.Exit(code=1)
        else:
            raise typer.Exit(code=0)
    elif unicode_type is None:
        console = rich.console.Console()
        converted_characters = converter.show_all(
            characters, strict_case=strict_case, reverse=reverse
        )
        title_style = rich.style.Style(color="magenta", bold=True)
        header_style = rich.style.Style(color="magenta")
        border_style = rich.style.Style(color="magenta")
        table = rich.table.Table(
            title="Dress up",
            title_style=title_style,
            header_style=header_style,
            border_style=border_style,
            box=rich.box.ROUNDED,
        )
        for column_name in ("Style", "Conversion"):
            table.add_column(column_name, justify="left")
        for character_type, converted_character in converted_characters.items():
            table.add_row(character_type, converted_character)
        console.print(table)
        pass
    else:
        try:
            converted_characters = converter.convert(
                characters,
                unicode_type=unicode_type,
                strict_case=strict_case,
                reverse=reverse,
            )
        except exceptions.InvalidUnicodeTypeError as error:
            exception_message = str(error).replace("_", "-")
            typer.secho(
                exception_message, fg=typer.colors.BRIGHT_RED,
            )
            raise typer.Exit(code=1)
        typer.echo(converted_characters)
        pass
