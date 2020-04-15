"""Package-wide test fixtures."""
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture


@pytest.fixture
def mock_toml_loads(mocker: MockFixture) -> Mock:
    """Fixture for mocking toml.loads."""
    mock = mocker.patch("toml.loads")
    mock.return_value = {
        "circled": dict(
            zip("abcdefghijklmnopqrstuvwxyz", "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ")
        ),
        "negative_circled": dict(
            zip("abcdefghijklmnopqrstuvwxyz", "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩")
        ),
    }
    return mock
