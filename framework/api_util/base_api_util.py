import requests
import allure

from enums.content_types import ContentTypes


@allure.step("POST request to {url}")
def post(url, data):
    response = requests.post(
        url,
        data=data,
        headers={"Accept": ContentTypes.JSON.value},
        timeout=10
    )
    return response


@allure.step("GET request to {url}")
def get(url, token):
    return requests.get(
        url,
        headers={
            "Accept": ContentTypes.JSON.value,
            "x-auth-token": token,
        },
        timeout=10,
    )


@allure.step("DELETE request to {url}")
def delete(url, token):
    return requests.delete(
        url,
        headers={
            "Accept": ContentTypes.JSON.value,
            "x-auth-token": token,
        },
        timeout=10,
    )
