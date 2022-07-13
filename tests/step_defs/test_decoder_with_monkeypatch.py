import requests
from pytest_bdd import scenarios, when, then, parsers

scenarios('../features/decoder_with_patching.feature')


class MockResponse:
    def __init__(self, status):
        self.status = status

    def json(self):
        return {"status": self.status}


@when(parsers.parse('check payment {status}'))
def check_payment(decoder, monkeypatch, status):
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: MockResponse(status))
    decoder.check_payment()


@then('decoder is blocked')
def is_blocked(decoder):
    assert decoder.is_blocked()


@then('decoder is not blocked')
def is_not_blocked(decoder):
    assert not decoder.is_blocked()
