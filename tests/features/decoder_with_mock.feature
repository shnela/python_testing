@decoder @decoder-patch
Feature: Box server connection
  As background daemon,
  I want to connect to the server,
  And make sure proper action is taken.

  Scenario: Check performed once
    When turn decoder on
    And turn decoder on
    And turn decoder on
    Then decoder status was checked 1 times


  Scenario: Check performed once every day
    When turn decoder on at "2012-01-14 03:21:34"
    And turn decoder on at "2012-01-15 04:21:34"
    And turn decoder on at "2012-01-16 05:21:34"
    Then decoder status was checked 3 times
