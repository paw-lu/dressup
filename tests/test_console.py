"""Test cases for the console module."""
import textwrap
from unittest.mock import Mock

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
    """It exits with a status code of 0."""
    result = runner.invoke(console.app)
    exit_code = result.exit_code
    assert exit_code == 0


def test_no_argument_message(runner: CliRunner) -> None:
    """It prints a message when no argument is provided."""
    result = runner.invoke(console.app)
    message = result.stdout
    assert "No characters provided to convert.\n" == message


def test_version_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero when "--version" is called."""
    result = runner.invoke(console.app, ["--version"])
    exit_code = result.exit_code
    assert exit_code == 0


def test_version_output(runner: CliRunner) -> None:
    """It returns a version."""
    result = runner.invoke(console.app, ["--version"])
    output = result.stdout
    assert output == f"Dress up version: {dressup.__version__}\n"


def test_help_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero when "--help" is called."""
    result = runner.invoke(console.app, ["--help"])
    exit_code = result.exit_code
    assert exit_code == 0


def test_help_message(runner: CliRunner) -> None:
    """It gives a message when "--help" is called."""
    result = runner.invoke(console.app, ["--help"])
    output = result.stdout
    help_message = "\n\n".join(output.split("\n\n")[1:3])
    expected_message = (
        "  Convert characters to different Unicode types.\n\n"
        "  If --type is specified, convert to a specific type."
    )
    assert expected_message == help_message


def test_help_parameter_descriptions(runner: CliRunner) -> None:
    """It describes the parameters when "--help" is called."""
    result = runner.invoke(console.app, ["--help"])
    output = result.stdout
    parameter_help = output.split("\n\n")[3]
    expected_message = (
        "Options:\n  -t, "
        "--type TEXT                 The Unicode type to convert to.\n  "
        "-v, --version                   Return the package version."
    )
    assert parameter_help.startswith(expected_message)


def test_complete_type(mock_toml_loads: Mock) -> None:
    """It generates an autompletion list."""
    completion_list = console.complete_type("cir")
    for completion in completion_list:
        assert ("circled", "ⒹⓇⒺⓈⓈ ⓊⓅ") == completion


def test_cli_conversion_succeeds(runner: CliRunner, mock_toml_loads: Mock) -> None:
    """It exits with a code of zero when an argument is provided."""
    result = runner.invoke(console.app, ["hello"])
    exit_code = result.exit_code
    assert exit_code == 0


def test_cli_conversion_output(runner: CliRunner, mock_toml_loads: Mock) -> None:
    """It converts the characters."""
    result = runner.invoke(console.app, ["hello"])
    actual_output = result.stdout
    expected_output = """
    Circled

    ⓗⓔⓛⓛⓞ

    Negative circled

    🅗🅔🅛🅛🅞
    """
    expected_output = textwrap.dedent(expected_output)
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "characters, unicode_type, expected_output",
    [
        ("hello", "Circled", "ⓗⓔⓛⓛⓞ\n"),
        ("hello", "Negative circled", "🅗🅔🅛🅛🅞\n"),
        ("he(lo", "Circled", "ⓗⓔ(ⓛⓞ\n"),
        ("💦a", "Circled", "💦ⓐ\n"),
    ],
)
def test_cli_option(
    runner: CliRunner,
    mock_toml_loads: Mock,
    characters: str,
    unicode_type: str,
    expected_output: str,
) -> None:
    """It converts the characters to the specified type."""
    result = runner.invoke(console.app, [characters, f"--type={unicode_type}"])
    actual_output = result.stdout
    assert actual_output == expected_output
