"""Command-line interface."""
import typer

from . import __version__

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
    if version:
        typer.echo(f"Dress up version: {__version__}")
