@decoder @decoder-patch
Feature: Box server connection
  As background daemon,
  I want to connect to the server,
  And make sure proper action is taken.

  Scenario: Check status ok
    Given decoder is turned on
    When check payment OK
    Then decoder is not blocked

  Scenario: Check status not ok
    Given decoder is turned on
    When check payment NOT OK
    Then decoder is blocked
