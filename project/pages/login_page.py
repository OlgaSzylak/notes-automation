import allure
from playwright.sync_api import Page

from framework.soft_assert import SoftAssert
from project.forms.auth_form import AuthForm
from project.pages.base_page import BasePage


class LoginPage(BasePage):
    login_form = "//form[contains (@class, 'py-3')]"
    logout_btn = "//button[@data-testid='logout']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.auth_form = AuthForm(page)
        self.soft_assert = SoftAssert.instance()

    def verify_login_page_opened(self):
        self.verify_page_opened(self.login_form)

    def submit_auth_form(self, email, password):
        self.auth_form.submit_form(email, password)

    def verify_logout_button_displayed(self):
        self.soft_assert.assert_visible(self.page.locator(self.logout_btn),
                                        "'Logout' button is not displayed")
