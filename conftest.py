from http import HTTPStatus

import pytest
import subprocess
from pathlib import Path

from project.entities.user_factory import UserFactory
from project.utils.api.user_api_util import UserAPIUtil

ROOT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = ROOT_DIR / "allure-results"
REPORT_DIR = ROOT_DIR / "allure-report"


def pytest_configure(config):
    config.option.allure_report_dir = str(RESULTS_DIR)
    config.option.clean_alluredir = True


def pytest_sessionfinish(session, exitstatus):
    subprocess.run(
        [
            "allure",
            "generate",
            str(RESULTS_DIR),
            "-o",
            str(REPORT_DIR),
            "--clean",
        ],
        check=True,
    )


@pytest.fixture
def registered_user():
    user = UserFactory.sign_up_user_via_api()
    print(f"\n[SETUP] Created user: {user.email}")

    try:
        yield user
    finally:
        print(f"\n[CLEANUP] Deleting user: {user.email}")

        token = UserAPIUtil.get_user_token(
            user.email,
            user.password,
        )
        response = UserAPIUtil.delete_user(token)

        print(f"[CLEANUP] Status: {response.status_code}")
        print(f"[CLEANUP] Response: {response.text}")

        assert response.status_code == HTTPStatus.OK, (
            f"User cleanup failed: HTTP {response.status_code}"
        )

        print(f"[CLEANUP] Successfully deleted user: {user.email}")
