"""Command-line interface."""
import typer

from . import __version__

app = typer.Typer()


@app.command()
def main(
    version: bool = typer.Option(False, help="Return the package version.")
) -> None:
    """Dress up your unicode!"""
    if version:
        typer.echo(f"Dress up version: {__version__}")
