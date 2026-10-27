import allure
import pytest

from data.user_test_data import InvalidEmails, INVALID_EMAIL_CASES
from enums.messages import ErrorMessages
from enums.registration_data_fields import Registration


@allure.parent_suite("User")
@allure.suite("Registration")
class TestUserRegistration:

    def test_register_successfully(self, signup_page, ui_registration_user):
        signup_page.sign_up_user(**ui_registration_user)
        signup_page.verify_successful_message()

    def test_register_duplicate_email(
            self, signup_page, registration_data, registered_user
    ):
        registration_data[Registration.EMAIL.value] = registered_user.email
        signup_page.sign_up_user(**registration_data)
        signup_page.verify_duplicate_email_message()

    @allure.title("Reject registration with an invalid email")
    @pytest.mark.parametrize("invalid_email", INVALID_EMAIL_CASES)
    def test_register_invalid_email(self, signup_page, registration_data, invalid_email):
        registration_data[Registration.EMAIL.value] = invalid_email

        signup_page.sign_up_user(**registration_data)
        signup_page.verify_validation_message(
            ErrorMessages.INVALID_EMAIL_MSG
        )

    def test_register_missing_email(self, signup_page, registration_data):
        registration_data[Registration.EMAIL.value] = InvalidEmails.EMPTY
        signup_page.sign_up_user(**registration_data)
        signup_page.verify_validation_message(ErrorMessages.MISSING_EMAIL_MSG)
