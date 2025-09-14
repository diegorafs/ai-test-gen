Feature: Application requirements

  Scenario: User logs in with email and password
    Given the user is on the login page
    When the user enters a valid email and password
    And clicks the login button
    Then the user should be redirected to the dashboard

  Scenario: Admin creates a new user
    Given the admin is logged in
    And is on the user management page
    When the admin enters new user details
    And clicks the create button
    Then the new user should be added to the system
