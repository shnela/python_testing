from unittest.mock import MagicMock

import pytest
from pytest_bdd import parsers, given

from decoder_tool.decoder import Decoder


@pytest.fixture
def decoder():
    yield Decoder()
