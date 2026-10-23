import allure
from project.entities.user_factory import UserFactory


@allure.parent_suite("User")
@allure.suite("Registration")
class TestAddTasks:

    @allure.title("Register new user via UI")
    def test_sign_up(self, page):
        UserFactory.sign_up_user_via_ui(page)
