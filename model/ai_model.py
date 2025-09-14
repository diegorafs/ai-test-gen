def generate_gherkin_from_requirements(requirements_list):
    scenarios = []
    scenarios.append("Feature: Application requirements\n")
    for requirement in requirements_list:
        requirement = requirement.strip()
        if not requirement:
            continue

        if "log in" in requirement:
            scenarios.append("""
  Scenario: User logs in with email and password
    Given the user is on the login page
    When the user enters a valid email and password
    And clicks the login button
    Then the user should be redirected to the dashboard
""")        
        elif "create new users" in requirement:
            scenarios.append("""
  Scenario: Admin creates a new user
    Given the admin is logged in
    And is on the user management page
    When the admin enters new user details
    And clicks the create button
    Then the new user should be added to the system
""")        
        else:
            scenarios.append(f"""
  # Scenario for: {requirement}
  Scenario: {requirement}
    Given some initial state
    When some action occurs
    Then the expected outcome is observed
""")
    return "\n".join(scenarios)