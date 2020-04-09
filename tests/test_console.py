"""Test cases for the console module."""
import pytest
import typer.testing
from typer.testing import CliRunner

import dressup
from dressup import console


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return typer.testing.CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of two."""
    result = runner.invoke(console.app)
    assert result.exit_code == 2


def test_version(runner: CliRunner) -> None:
    """It returns a version."""
    result = runner.invoke(console.app, ["--version"])
    output = result.stdout
    assert output == f"Dress up version: {dressup.__version__}\n"
