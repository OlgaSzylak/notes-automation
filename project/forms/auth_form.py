import allure


class AuthForm:
    email_inp = "//input[@data-testid='login-email']"
    password_inp = "//input[@data-testid='login-password']"
    login_btn = "//button[@data-testid='login-submit']"
    success_alert = ".alert-success b"

    def __init__(self, page):
        self.page = page

    def fill_email(self, email):
        with allure.step(f"Fill email {email}"):
            self.page.fill(self.email_inp, email)

    def fill_password(self, password):
        with allure.step(f"Fill password {password}"):
            self.page.fill(self.password_inp, password)

    def click_login(self):
        with allure.step("Click on 'Login' button"):
            self.page.locator(self.login_btn).click()

    def submit_form(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login()
