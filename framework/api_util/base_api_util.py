import requests
import allure


@allure.step("POST request to {url}")
def post(url, data):
    response = requests.post(
        url,
        data=data,
        headers={"Accept": "application/json"},
        timeout=10
    )
    return response
