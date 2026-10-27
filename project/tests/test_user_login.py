import allure
import pytest
from playwright.sync_api import expect

from enums.messages import ErrorMessages
from project.utils.user_random import UserRandomUtil
from data.user_test_data import INVALID_EMAIL_CASES


@allure.parent_suite("User")
@allure.suite("Login")
class TestUserLogin:

    @allure.title("Log in with valid credentials")
    def test_login_successful(self, login_page, registered_user):
        login_page.submit_auth_form(
            email=registered_user.email,
            password=registered_user.password,
        )
        login_page.verify_logout_button_displayed()

    @allure.title("Sign in as a user with incorrect email")
    @pytest.mark.parametrize("invalid_email", INVALID_EMAIL_CASES)
    def test_sign_in_invalid_email(self, login_page, invalid_email):
        login_page.submit_auth_form(
            email=invalid_email,
            password=UserRandomUtil.generate_letters_only_password(),
        )

        login_page.verify_validation_message(
            ErrorMessages.INVALID_EMAIL_MSG
        )
