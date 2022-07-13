import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from decoder_tool.decoder import DecoderException

scenarios('../features/decoder.feature')


@given(parsers.parse('decoder is turned {state}'))
def decoder_turned_on(decoder, state):
    if state == 'on':
        decoder.turn_on()
    elif state == 'off':
        decoder.turn_off()
    else:
        raise ValueError(state)


@when('decoder is turned off and on again')
def turning_off_and_on_again(decoder):
    decoder.turn_off()
    decoder.turn_on()


@when(parsers.parse('the user selects channel {channel}'))
def set_channel(decoder, channel):
    channel = int(channel)
    decoder.set_channel(channel)


@when(parsers.parse('the user turns channel {direction}'))
def change_channel(decoder, direction):
    if direction == 'up':
        decoder.channel_up()
    elif direction == 'down':
        decoder.channel_down()
    else:
        raise ValueError(direction)


@then(parsers.parse('decoder should be in state {state}'))
def search_results(decoder, state):
    assert decoder.get_state().value == state


@then(parsers.parse('decoder should be tuned to chanel {channel}'))
def search_results(decoder, channel):
    channel = int(channel)
    assert decoder.get_current_channel() == channel


@then(parsers.parse("Can't perform action {action}"))
def search_results(decoder, action):
    with pytest.raises(DecoderException):
        if action == 'channel_up':
            decoder.channel_up()
        elif action == 'channel_down':
            decoder.channel_down()
        else:
            raise ValueError(action)
