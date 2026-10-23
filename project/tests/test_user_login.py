import allure
import pytest
from playwright.sync_api import Page

from data import config
from project.pages.login_page import LoginPage
from project.utils.user_random import UserRandomUtil


def login(page, registered_user):
    login_page = LoginPage(page)
    login_page.navigate_to_url(config.URL_NOTES_LOGIN)
    login_page.verify_login_page_opened()
    login_page.submit_auth_form(
        registered_user.email,
        registered_user.password)
    login_page.verify_logout_button_displayed()


@allure.parent_suite("User")
@allure.suite("Login")
class TestUserLogin:

    @allure.title("Register new user via UI")
    def test_login_successful(self, registered_user, page: Page):
        login(page, registered_user)

    @allure.title("Sign in as a user with incorrect email")
    @pytest.mark.parametrize(
        "incorrect_email",
        [
            UserRandomUtil.generate_invalid_email(),
            UserRandomUtil.generate_email_without_domain(),
            UserRandomUtil.generate_email_without_domain_extension(),
        ],
    )
    def test_sign_in_invalid_email(
        self, page: Page, incorrect_email
    ):
        login_page = LoginPage(page)
        login_page.navigate_to_url(config.URL_NOTES_LOGIN)
        login_page.verify_login_page_opened()

        login_page.submit_auth_form(
            email=incorrect_email,
            password=UserRandomUtil.generate_letters_only_password(),
        )
        login_page.verify_invalid_email_message()
        login_page.soft_assert.verify()
