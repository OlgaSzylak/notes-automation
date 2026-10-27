from http import HTTPStatus

from playwright.sync_api import Page
import allure
from data.config import URL_NOTES_REGISTER
from enums.registration_data_fields import Registration
from framework.soft_assert import SoftAssert
from project.models.user_model import UserModel
from project.pages.signup_page import SignupPage
from project.utils.api.user_api_util import UserAPIUtil
from project.utils.user_random import UserRandomUtil


class UserFactory:

    @staticmethod
    def generate_registration_data() -> dict[str, str]:
        return {
            Registration.EMAIL.value: UserRandomUtil.generate_unique_email(),
            Registration.PASSWORD.value: UserRandomUtil.generate_letters_only_password(),
            Registration.NAME.value: UserRandomUtil.generate_random_first_and_last_name()
        }

    @staticmethod
    @allure.step("Create user via API")
    def sign_up_user_via_api() -> UserModel:
        registration_data = UserFactory.generate_registration_data()

        response = UserAPIUtil.register_user(**registration_data)

        assert response.status_code == HTTPStatus.CREATED, (
            f"Registration failed: {response.status_code} - {response.text}"
        )

        return UserFactory._build_user_model(
            response,
            name=registration_data[Registration.NAME.value],
            email=registration_data[Registration.EMAIL.value],
            password=registration_data[Registration.PASSWORD.value],
        )

    @staticmethod
    def _build_user_model(response, name, email, password) -> UserModel:
        user_data = response.json()["data"]

        return UserModel(
            user_id=user_data["id"],
            name=name,
            email=email,
            password=password
        )

    @staticmethod
    def sign_up_user_via_ui(page: Page, soft_assert: SoftAssert):
        sign_up_page = SignupPage(page, soft_assert)
        sign_up_page.navigate_to_url(URL_NOTES_REGISTER)
        sign_up_page.verify_register_page_opened()

        email = UserRandomUtil.generate_unique_email()
        password = UserRandomUtil.generate_letters_only_password()
        name = UserRandomUtil.generate_random_first_and_last_name()
        sign_up_page.sign_up_user(email, password, name)
        sign_up_page.verify_successful_message()

    @staticmethod
    @allure.step("Create authenticated user via API")
    def create_authenticated_user_via_api() -> UserModel:
        user = UserFactory.sign_up_user_via_api()

        user.token = UserAPIUtil.get_user_token(
            user.email,
            user.password,
        )

        return user
