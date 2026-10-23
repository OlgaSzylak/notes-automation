import allure

from data.api_url import URL_API_DASHBOARD_REGISTER
from framework.api_util.base_api_util import post


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
