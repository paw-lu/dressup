"""Package-wide test fixtures."""
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture


@pytest.fixture
def mock_toml_loads(mocker: MockFixture) -> Mock:
    """Fixture for mocking toml.loads."""
    mock = mocker.patch("toml.loads")
    mock.return_value = {
        "Circled": dict(
            zip("abcdefghijklmnopqrstuvwxyz", "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ")
        ),
        "Circled (neg)": dict(
            zip("abcdefghijklmnopqrstuvwxyz", "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩")
        ),
    }
    return mock
