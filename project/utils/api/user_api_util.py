from http import HTTPStatus

import allure

from data.api_url import URL_API_DASHBOARD_REGISTER, URL_API_DASHBOARD_LOGIN, URL_API_DASHBOARD_DELETE_USER
from framework.api_util.base_api_util import post, delete


class UserAPIUtil:

    @staticmethod
    @allure.step("Register new user via API")
    def register_user(name, email, password):
        payload = {
            "name": name,
            "email": email,
            "password": password
        }

        return post(URL_API_DASHBOARD_REGISTER, payload)

    @staticmethod
    @allure.step("Log in user via API")
    def login_user(email, password):
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
    @allure.step("Get user token")
    def get_user_token(email, password) -> str:
        response = UserAPIUtil.login_user(email, password)

        assert response.status_code == HTTPStatus.OK, (
            f"Login failed: HTTP {response.status_code}"
        )

        return UserAPIUtil.get_token(response)

    @staticmethod
    @allure.step("Delete user via API")
    def delete_user(token):
        return delete(URL_API_DASHBOARD_DELETE_USER, token)