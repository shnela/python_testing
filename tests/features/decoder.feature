@decoder
Feature: Box channel changing
  As a user,
  I want to set channel,
  And make sure it's selected.

  Scenario: Basic channel selection
    Given decoder is turned on
    When the user selects channel 18
    Then decoder should be tuned to chanel 18
