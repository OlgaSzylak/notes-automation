from http import HTTPStatus

import allure

from data.api_url import URL_API_DASHBOARD_REGISTER, URL_API_DASHBOARD_LOGIN, URL_API_DASHBOARD_DELETE_USER
from enums.messages import ErrorMessages
from framework.api_util.base_api_util import post, delete


class UserAPIUtil:

    @staticmethod
    def register_user(name, email, password):
        with allure.step("Register new user via API"):
            payload = {
                "name": name,
                "email": email,
                "password": password,
            }
            return post(URL_API_DASHBOARD_REGISTER, payload)

    @staticmethod
    def login_user(email, password):
        with allure.step("Log in user via API"):
            payload = {
                "email": email,
                "password": password,
            }
            return post(URL_API_DASHBOARD_LOGIN, payload)

    @staticmethod
    def get_token(response) -> str:
        token = response.json()["data"]["token"]
        assert isinstance(token, str) and token, "Missing valid login token"
        return token

    @staticmethod
    def get_user_token(email, password) -> str:
        with allure.step("Get user token"):
            response = UserAPIUtil.login_user(email, password)

            assert response.status_code == HTTPStatus.OK, (
                f"Login failed: HTTP {response.status_code}"
            )

            return UserAPIUtil.get_token(response)

    @staticmethod
    def delete_user(token):
        with allure.step("Delete user via API"):
            return delete(URL_API_DASHBOARD_DELETE_USER, token)

    @staticmethod
    def delete_user_by_credentials(email: str, password: str, *, allow_missing: bool = False) -> None:
        with allure.step("Delete user using credentials"):
            login_response = UserAPIUtil.login_user(email, password)

            if (
                    allow_missing
                    and login_response.status_code == HTTPStatus.UNAUTHORIZED
                    and login_response.json().get("message")
                    == ErrorMessages.INVALID_CREDENTIALS_MSG.value
            ):
                return

            assert login_response.status_code == HTTPStatus.OK, (
                f"Cleanup login failed: HTTP {login_response.status_code}. "
                f"Response: {login_response.text}"
            )
            token = UserAPIUtil.get_token(login_response)
            response = UserAPIUtil.delete_user(token)

            assert response.status_code == HTTPStatus.OK, (
                f"User cleanup failed: HTTP {response.status_code}. "
                f"Response: {response.text}"
            )
