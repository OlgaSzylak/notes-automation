import allure
from playwright.sync_api import Page

from enums.messages import Messages, ErrorMessages
from framework.soft_assert import SoftAssert
from project.pages.base_page import BasePage


class SignupPage(BasePage):
    register_form = "//form[@data-testid='login-form']"
    email_inp = "//input[@data-testid='register-email']"
    password_inp = "//input[@data-testid='register-password']"
    confirm_password_inp = "//input[@data-testid='register-confirm-password']"
    register_name = "//input[@data-testid='register-name']"
    register_btn = "//button[@data-testid='register-submit']"
    success_alert = ".alert-success b"
    alert_message = ".toast-body"

    def __init__(self, page: Page, soft_assert: SoftAssert):
        super().__init__(page, soft_assert)

    def sign_up_user(self, email, password, name, confirm_password=None):
        self.fill_email(email)
        self.fill_password(password)
        self.reconfirm_password(
            password if confirm_password is None else confirm_password
        )
        self.fill_name(name)
        self.click_register()

    def fill_email(self, email):
        with allure.step(f"Fill '{email}' email"):
            self.page.fill(self.email_inp, email)

    def fill_password(self, password):
        with allure.step("Fill password"):
            self.page.fill(self.password_inp, password)

    def reconfirm_password(self, password):
        with allure.step("Confirm password"):
            self.page.fill(self.confirm_password_inp, password)

    def fill_name(self, name):
        with allure.step(f"Fill '{name}'"):
            self.page.fill(self.register_name, name)

    @allure.step("Click on 'register' button")
    def click_register(self):
        self.page.click(self.register_btn)

    def verify_register_page_opened(self):
        self.verify_page_opened(self.register_form)

    def verify_successful_message(self):
        with allure.step("Verify successful registration message"):
            self.verify_element_text(
                self.success_alert,
                Messages.REGISTRATION_SUCCESS.value
            )

    def verify_duplicate_email_message(self):
        with allure.step("Verify duplicated email message"):
            self.verify_element_text(
                self.alert_message,
                ErrorMessages.EMAIL_TAKEN_MSG.value
            )
