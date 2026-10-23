import subprocess
import pytest
import subprocess
from pathlib import Path

from project.entities.user_factory import UserFactory

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
    return UserFactory.sign_up_user_via_api()
