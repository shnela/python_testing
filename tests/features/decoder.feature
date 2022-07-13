@decoder @decoder-basic
Feature: Box channel changing
  As a user,
  I want to set channel,
  And make sure it's selected.

  Scenario: Basic turn on
    Given decoder is turned on
    Then decoder should be in state ON

  Scenario: Basic turn off
    Given decoder is turned off
    Then decoder should be in state STANDBY

  Scenario: Basic channel selection
    Given decoder is turned on
    When the user selects channel 18
    Then decoder should be tuned to chanel 18

  Scenario: Storing selected channel
    Given decoder is turned on
    When the user selects channel 18
    And decoder is turned off and on again
    Then decoder should be tuned to chanel 18

  Scenario: Checking channel down and up
    Scenario Outline: Outlined given, when, then
      Given decoder is turned on
      When the user selects channel <start>
      And the user turns channel down
      And the user turns channel up
      And the user turns channel up
      Then decoder should be tuned to chanel <end>
    Examples:
    | start | end |
    |  10   |  11 |
    |  20   |  21 |

  Scenario: Checking channel down below 0
    Given decoder is turned on
    When the user selects channel 1
    Then Can't perform action channel_down
