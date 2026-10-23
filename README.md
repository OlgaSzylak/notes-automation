# Notes Automation

A small QA automation project for the [ExpandTesting Notes application](https://practice.expandtesting.com/notes/app/), built with Python, Playwright, Pytest, Requests, and Allure.

The project combines API test-data setup with UI testing: create a user through the API, use their credentials in a browser test, and delete the account during fixture teardown.

## Scope

- User registration through the API and UI.
- UI login with an API-created account.
- API login and authentication-token extraction.
- Authenticated account deletion.
- Automatic cleanup of fixture-created users after tests.

This is a learning project that is being extended incrementally. Utility methods support test setup and teardown; they do not by themselves represent dedicated test coverage for every endpoint.

## Technology

| Tool | Purpose |
| --- | --- |
| Python | Test and framework code |
| Pytest | Test runner and fixtures |
| Playwright / pytest-playwright | Browser automation |
| Requests | HTTP API requests |
| Allure / allure-pytest | Test results and reporting |
| Faker | Random user names |

## Project layout

```text
data/                       Configuration and API URLs
enums/                      Shared values and messages
framework/
    api_util/base_api_util.py   Reusable HTTP helpers
project/
    entities/user_factory.py    User creation and authentication
    forms/                      Reusable UI form actions
    models/user_model.py        User details and credentials
    pages/                      Playwright page objects
    utils/                      Random-data and API utilities
    tests/                      Test scenarios
conftest.py                 Shared fixtures and reporting hooks
pytest.ini                  Pytest configuration
```

## Getting started

Clone the repository and open its directory:

```bash
git clone https://github.com/OlgaSzylak/notes-automation.git
cd notes-automation
```

Create and activate a virtual environment (macOS / Linux):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the core dependencies and Chromium:

```bash
python -m pip install pytest pytest-playwright requests allure-pytest Faker python-dotenv
python -m playwright install chromium
```

If the repository provides a maintained `requirements.txt`, use `python -m pip install -r requirements.txt` instead of the dependency-install command above.

## Configuration

Check `data/config.py` before running tests. If it loads settings from a local `.env` file, create that file using the exact environment-variable names read by the configuration module.

The resolved configuration should use these values:

| Setting | Value |
| --- | --- |
| UI base URL | `https://practice.expandtesting.com/notes/app/` |
| URL_API_BASE | `https://practice.expandtesting.com/notes/api/` |
| UI registration URL | `https://practice.expandtesting.com/notes/app/register` |
| UI login URL | `https://practice.expandtesting.com/notes/app/login` |

Keep the trailing slash on base URLs when constructing endpoints with string concatenation. UI routes and API endpoints use different base paths.

API endpoint constants are defined in `data/api_url.py`:

```python
URL_API_DASHBOARD_REGISTER = f"{URL_API_BASE}users/register"
URL_API_DASHBOARD_LOGIN = f"{URL_API_BASE}users/login"
URL_API_DASHBOARD_DELETE_USER = f"{URL_API_BASE}users/delete-account"
```

Keep `.env`, credentials, tokens, virtual environments, and generated reports out of version control.

## Running tests

Run the suite from the repository root:

```bash
python -m pytest
```

Run with a visible browser:

```bash
python -m pytest --headed
```

Display temporary setup and cleanup prints:

```bash
python -m pytest -s
```

Display prints while retaining captured output:

```bash
python -m pytest --capture=tee-sys
```

Select tests by name:

```bash
python -m pytest -k login
```

Tests access a public practice service, so internet access and service availability are required.

## User setup and cleanup

The `registered_user` fixture creates a new user through the API and yields a `UserModel` to the test.

After the test, its `finally` block:

1. Logs in through the API using that user's credentials.
2. Extracts the token from `response.json()["data"]["token"]`.
3. Sends `DELETE /users/delete-account` with the `x-auth-token` header.
4. Checks that the response status is HTTP 200.

Cleanup is attempted even when the test fails. A cleanup failure is reported as a teardown error. A forced process termination can prevent teardown from running.

Tests using this fixture should retain the account and its original credentials until teardown. Dedicated account-deletion tests should manage their own user lifecycle to avoid deleting the same account twice.

Temporary cleanup prints can show the email, deletion status, and deletion response. Do not print passwords or tokens.

## API utilities

| Method | Responsibility |
| --- | --- |
| `UserAPIUtil.register_user(name, email, password)` | Return the registration response |
| `UserAPIUtil.login_user(email, password)` | Return the login response |
| `UserAPIUtil.get_token(response)` | Extract the login token |
| `UserAPIUtil.get_user_token(email, password)` | Log in, check success, and return the token |
| `UserAPIUtil.delete_user(token)` | Return the account-deletion response |

Use raw response methods in API tests that need to inspect error responses. Use factory methods when a test needs an existing account as setup.

## Allure reports

Generate result files:

```bash
python -m pytest --alluredir=allure-results
```

The Allure command-line tool must be installed separately from `allure-pytest` to view HTML reports. Once available:

```bash
allure serve allure-results
```

Or build a report directory:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

Check `pytest.ini` and `conftest.py` for existing Allure options or automatic report-generation hooks. A hook that invokes the CLI also requires the Allure command-line tool to be installed.
