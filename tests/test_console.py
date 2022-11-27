"""Test cases for the console module."""
import textwrap
from typing import List
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture
import typer
import typer.testing
from typer.testing import CliRunner

import dressup
from dressup import console


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return typer.testing.CliRunner()


@pytest.fixture
def mock_typer_context_no_argument(mocker: MockFixture) -> Mock:
    """Fixture for mocking typer.Context without arguments."""
    mock = mocker.patch("typer.Context")
    mock.args = []
    mock.params = {
        "version": None,
        "characters": None,
        "strict_case": None,
        "unicode_type": None,
        "reverse": None,
    }
    return mock


@pytest.fixture
def mock_typer_context_with_argument(mocker: MockFixture) -> Mock:
    """Fixture for mocking typer.Context with arguments."""
    mock = mocker.patch("typer.Context")
    mock.args = ["SAmPlE"]
    mock.params = {
        "version": None,
        "characters": None,
        "strict_case": None,
        "unicode_type": None,
        "reverse": None,
    }
    return mock


@pytest.fixture
def mock_typer_context_with_argument_strict(mocker: MockFixture) -> Mock:
    """Fixture for mocking typer.Context with args and strict-case."""
    mock = mocker.patch("typer.Context")
    mock.args = ["SAmPlE"]
    mock.params = {
        "version": None,
        "characters": None,
        "strict_case": True,
        "unicode_type": None,
        "reverse": None,
    }
    return mock


@pytest.fixture
def mock_typer_context_with_argument_reverse(mocker: MockFixture) -> Mock:
    """Fixture for mocking typer.Context with args and strict-case."""
    mock = mocker.patch("typer.Context")
    mock.args = ["SAmPlE"]
    mock.params = {
        "version": None,
        "characters": None,
        "strict_case": None,
        "unicode_type": None,
        "reverse": True,
    }
    return mock


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of 0."""
    result = runner.invoke(console.app)
    exit_code = result.exit_code
    assert exit_code == 0


@pytest.mark.parametrize(
    "arguments", [["--type", "circle"], ["--strict-case"], ["--reverse"]]
)
def test_main_fails(runner: CliRunner, arguments: List[str]) -> None:
    """It exits with code 1 if option but no argument provided."""
    result = runner.invoke(console.app, arguments)
    exit_code = result.exit_code
    assert exit_code == 1


def test_no_argument_message(runner: CliRunner) -> None:
    """It prints a message when no argument is provided."""
    result = runner.invoke(console.app)
    message = result.stdout
    assert "No characters provided to convert.\n" == message


@pytest.mark.parametrize(
    "arguments",
    [
        ["--type", "circle"],
        ["--strict-case"],
        ["--strict-case", "--type", "circle"],
        ["--reverse"],
    ],
)
def test_option_no_argument_message(runner: CliRunner, arguments: List[str]) -> None:
    """It prints a message when option but no argument is provided."""
    result = runner.invoke(console.app, arguments)
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
    help_message = result.stdout
    expected_messages = (
        "Convert characters to different Unicode types.",
        "If --type is specified, convert to a specific type."
    )
    assert all(expected_message in help_message for expected_message in expected_messages)


def test_help_parameter_descriptions(runner: CliRunner) -> None:
    """It describes the parameters when "--help" is called."""
    result = runner.invoke(console.app, ["--help"])
    output = result.stdout
    expected_parameters = (
        "--strict-case",
        "--reverse",
        "--type",
        "--version",
    )
    assert all(parameter in output for parameter in expected_parameters)


def test_complete_type(
    mock_typer_context_no_argument: Mock, mock_toml_loads: Mock
) -> None:
    """It generates an autocompletion list."""
    completion_list = console.complete_type(typer.Context, "cir")
    for completion in completion_list:
        assert completion == ("circled", "Ⓓⓡⓔⓢⓢ Ⓤⓟ!")


def test_arg_complete_type(
    mock_typer_context_with_argument: Mock, mock_toml_loads: Mock
) -> None:
    """It generates an autocompletion list using argument."""
    completion_list = console.complete_type(typer.Context, "cir")
    for completion in completion_list:
        assert completion == ("circled", "ⓈⓐⓜⓅⓛⒺ")


def test_arg_strict_complete_type(
    mock_typer_context_with_argument_strict: Mock, mock_toml_loads: Mock
) -> None:
    """It generates an autocompletion list using argument and strict."""
    completion_list = console.complete_type(typer.Context, "cir")
    for completion in completion_list:
        assert completion == ("circled", "ⓈAⓜⓅⓛⒺ")


def test_arg_reverse_complete_type(
    mock_typer_context_with_argument_reverse: Mock, mock_toml_loads: Mock
) -> None:
    """It generates an autocompletion list using argument and reverse."""
    completion_list = console.complete_type(typer.Context, "cir")
    for completion in completion_list:
        assert completion == ("circled", "ⒺⓛⓅⓜⓐⓈ")


def test_cli_conversion_succeeds(runner: CliRunner, mock_toml_loads: Mock) -> None:
    """It exits with a code of zero when an argument is provided."""
    result = runner.invoke(console.app, ["hello"])
    exit_code = result.exit_code
    assert exit_code == 0


def test_cli_conversion_output(runner: CliRunner, mock_toml_loads: Mock) -> None:
    """It converts the characters."""
    result = runner.invoke(console.app, ["hello"])
    actual_output = result.stdout
    expected_output = f"""\
                Dress up{" ":^13}
    ╭──────────────────┬────────────╮
    │ Style            │ Conversion │
    ├──────────────────┼────────────┤
    │ Circled          │ ⓗⓔⓛⓛⓞ      │
    │ Negative circled │ 🅗🅔🅛🅛🅞      │
    ╰──────────────────┴────────────╯
    """
    expected_output = textwrap.dedent(expected_output)
    assert actual_output == expected_output


def test_cli_conversion_output_strict(runner: CliRunner, mock_toml_loads: Mock) -> None:
    """It strictly converts the characters."""
    result = runner.invoke(console.app, ["hello", "--strict-case"])
    actual_output = result.stdout
    expected_output = f"""\
                Dress up{" ":^13}
    ╭──────────────────┬────────────╮
    │ Style            │ Conversion │
    ├──────────────────┼────────────┤
    │ Circled          │ ⓗⓔⓛⓛⓞ      │
    │ Negative circled │ hello      │
    ╰──────────────────┴────────────╯
    """
    expected_output = textwrap.dedent(expected_output)
    assert actual_output == expected_output


def test_cli_conversion_output_reverse(
    runner: CliRunner, mock_toml_loads: Mock
) -> None:
    """It converts reversed characters."""
    result = runner.invoke(console.app, ["hello", "--reverse"])
    actual_output = result.stdout
    expected_output = f"""\
                Dress up{" ":^13}
    ╭──────────────────┬────────────╮
    │ Style            │ Conversion │
    ├──────────────────┼────────────┤
    │ Circled          │ ⓞⓛⓛⓔⓗ      │
    │ Negative circled │ 🅞🅛🅛🅔🅗      │
    ╰──────────────────┴────────────╯
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
    result = runner.invoke(console.app, [characters, "--type", unicode_type])
    actual_output = result.stdout
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "characters, unicode_type, expected_output",
    [
        ("hello", "Circled", "ⓗⓔⓛⓛⓞ\n"),
        ("hello", "Negative circled", "hello\n"),
        ("he(lo", "Circled", "ⓗⓔ(ⓛⓞ\n"),
        ("💦a", "Circled", "💦ⓐ\n"),
    ],
)
def test_cli_option_strict(
    runner: CliRunner,
    mock_toml_loads: Mock,
    characters: str,
    unicode_type: str,
    expected_output: str,
) -> None:
    """It converts the characters to the specified type."""
    result = runner.invoke(
        console.app, [characters, "--type", unicode_type, "--strict-case"]
    )
    actual_output = result.stdout
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "characters, unicode_type, expected_output",
    [
        ("hello", "Circled", "ⓞⓛⓛⓔⓗ\n"),
        ("hello", "Negative circled", "🅞🅛🅛🅔🅗\n"),
        ("he(lo", "Circled", "ⓞⓛ(ⓔⓗ\n"),
        ("💦a", "Circled", "ⓐ💦\n"),
    ],
)
def test_cli_option_reverse(
    runner: CliRunner,
    mock_toml_loads: Mock,
    characters: str,
    unicode_type: str,
    expected_output: str,
) -> None:
    """It converts the characters to the specified type."""
    result = runner.invoke(
        console.app, [characters, "--type", unicode_type, "--reverse"]
    )
    actual_output = result.stdout
    assert actual_output == expected_output


def test_invalid_unicode_type_fails(runner: CliRunner, mock_toml_loads: Mock) -> None:
    """It exits with code 1 with invalid unicode_type."""
    result = runner.invoke(console.app, ["characters", "--type", "invalid_type"])
    exit_code = result.exit_code
    assert exit_code == 1


def test_invalid_unicode_type_message(runner: CliRunner, mock_toml_loads: Mock) -> None:
    """It returns a message with an invalid unicode_type."""
    result = runner.invoke(console.app, ["characters", "--type", "invalid_type"])
    message = result.stdout
    expected_message = (
        "'invalid-type' is not a valid Unicode type."
        " Valid types are circled, negative-circled.\n"
    )
    assert message == expected_message
