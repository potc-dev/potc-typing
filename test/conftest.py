import pytest

from potc.testing import mock_potc_plugins


@pytest.fixture(autouse=True)
def potc_typing_installed():
    with mock_potc_plugins('potc_typing.plugin', clear=True):
        yield
