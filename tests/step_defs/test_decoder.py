from pytest_bdd import scenarios, given, when, then, parsers


scenarios('../features/decoder.feature')


@given('decoder is turned on')
def turn_decoder_on(decoder):
    decoder.turn_on()


@when(parsers.parse('the user selects channel {channel}'))
def set_channel(decoder, channel):
    channel = int(channel)
    decoder.set_channel(channel)


@then(parsers.parse('decoder should be tuned to chanel {channel}'))
def search_results(decoder, channel):
    channel = int(channel)
    assert decoder.get_current_channel() == channel
