import pytest
from decoder_tool.decoder import Decoder


@pytest.fixture
def decoder():
    yield Decoder()
