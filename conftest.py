import pytest
import subprocess
from pathlib import Path

from data import config
from enums.registration_data_fields import Registration
from framework.soft_assert import SoftAssert
from project.entities.user_factory import UserFactory
from project.pages.login_page import LoginPage
from project.pages.signup_page import SignupPage
from project.utils.api.user_api_util import UserAPIUtil

ROOT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = ROOT_DIR / "allure-results"
REPORT_DIR = ROOT_DIR / "allure-report"


def pytest_configure(config):
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
def soft_assert():
    soft_assert = SoftAssert()
    yield soft_assert
    soft_assert.verify()


@pytest.fixture
def signup_page(page, soft_assert):
    signup_page = SignupPage(page, soft_assert)
    signup_page.navigate_to_url(config.URL_NOTES_REGISTER)
    signup_page.verify_register_page_opened()
    return signup_page


@pytest.fixture
def login_page(page, soft_assert):
    login_page = LoginPage(page, soft_assert)
    login_page.navigate_to_url(config.URL_NOTES_LOGIN)
    login_page.verify_login_page_opened()
    return login_page


@pytest.fixture
def ui_registration_user(registration_data):
    yield registration_data

    UserAPIUtil.delete_user_by_credentials(
        email=registration_data[Registration.EMAIL.value],
        password=registration_data[Registration.PASSWORD.value],
        allow_missing=True,
    )


@pytest.fixture
def registration_data():
    return UserFactory.generate_registration_data()


@pytest.fixture
def registered_user():
    user = UserFactory.sign_up_user_via_api()

    yield user

    UserAPIUtil.delete_user_by_credentials(
        user.email,
        user.password,
    )
