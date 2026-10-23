import allure
from playwright.sync_api import Page

from data import config
from project.pages.login_page import LoginPage


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
class TestAddTasks:

    @allure.title("Register new user via UI")
    def test_login(self, registered_user, page: Page):
        login(page, registered_user)
