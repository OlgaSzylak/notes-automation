from playwright.sync_api import Page, expect

from framework.soft_assert import SoftAssert
from project.forms.login_form import LoginForm
from project.pages.base_page import BasePage


class LoginPage(BasePage):
    login_form = "//form[contains (@class, 'py-3')]"
    logout_btn = "//button[@data-testid='logout']"

    def __init__(self, page: Page, soft_assert: SoftAssert):
        super().__init__(page, soft_assert)
        self.auth_form = LoginForm(page)

    def verify_login_page_opened(self):
        self.verify_page_opened(self.login_form)

    def submit_auth_form(self, email, password):
        self.auth_form.submit_form(email, password)

    def verify_logout_button_displayed(self):
        expect(
            self.page.locator(self.logout_btn)
        ).to_be_visible()
