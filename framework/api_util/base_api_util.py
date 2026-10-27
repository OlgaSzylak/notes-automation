import requests
import allure

from enums.content_types import ContentTypes


def post(url, data):
    with allure.step(f"POST request to {url}"):
        return requests.post(
            url,
            data=data,
            headers={"Accept": ContentTypes.JSON.value},
            timeout=30,
        )


def get(url, token):
    with allure.step(f"GET request to {url}"):
        return requests.get(
            url,
            headers={
                "Accept": ContentTypes.JSON.value,
                "x-auth-token": token,
            },
            timeout=10,
        )


def delete(url, token):
    with allure.step(f"DELETE request to {url}"):
        return requests.delete(
            url,
            headers={
                "Accept": ContentTypes.JSON.value,
                "x-auth-token": token,
            },
            timeout=10,
        )
