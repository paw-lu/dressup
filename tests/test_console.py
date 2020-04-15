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


def test_cli_conversion_succeeds(runner: CliRunner, mock_toml_loads: Mock) -> None:
    """It exits with a code of zero when an argument is provided."""
    result = runner.invoke(console.app, ["hello"])
    exit_code = result.exit_code
    assert exit_code == 0


# TODO: Add parameterized version of this test for different options
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


# TODO: Paramaterize
def test_cli_option(runner: CliRunner, mock_toml_loads: Mock) -> None:
    """It converts the characters to the specified type."""
    result = runner.invoke(console.app, ["hello", "--type=Circled"])
    actual_output = result.stdout
    expected_output = """ⓗⓔⓛⓛⓞ\n"""
    assert expected_output == actual_output
