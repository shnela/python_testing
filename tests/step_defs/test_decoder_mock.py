from unittest.mock import MagicMock

from freezegun import freeze_time
from pytest_bdd import scenarios, when, then, parsers

scenarios('../features/decoder_with_mock.feature')


class MockResponse:
    def __init__(self, status):
        self.status = status

    def json(self):
        return {"status": self.status}


@when('turn decoder on')
def when_turn_decoder_on(decoder):
    decoder.turn_on()


@when(parsers.parse('turn decoder on at "{date}"'))
def when_turn_decoder_on(decoder, date):
    with freeze_time(date):
        decoder.turn_on()


@then(parsers.parse('decoder status was checked {times} times'))
def status_checked(decoder, times):
    times = int(times)
    assert decoder._server.check_payment.called
    assert decoder._server.check_payment.call_count == times
