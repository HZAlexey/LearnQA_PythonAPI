from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from datetime import datetime
import allure

@allure.epic("Delete user cases")
class TestUserDelete(BaseCase):
    def setup_method(self):
        self.random_part = datetime.now().strftime("%m%d%Y%H%M%S")

        self.data = self.prepare_registration_data()
        self.data2 = self.prepare_registration_data(f"{self.random_part}@yandex.ru")

        self.val = {
            'email': self.data["email"],
            'password': self.data["password"]
        }

        self.val2 = {
            'email': self.data2["email"],
            'password': self.data2["password"]
        }
    # Попытка удалить пользователя ID 2
    @allure.feature("Негативные тесты")
    @allure.description("This negative test of delete user by id = 2")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_delete_user_negative(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id = self.get_json_value(response, "user_id")

        response2 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token":token},
            cookies={"auth_sid":auth_sid}
        )

        Assertions.assert_code_status(response2,400)
        Assertions.assert_json_value_by_name(
            response2,
            "error",
            "Please, do not delete test users with ID 1, 2, 3, 4 or 5.",\
            "Wrong after delete user"
        )

    # Позитивный тест на удаление пользователя
    @allure.feature("Позитивные тесты")
    @allure.description("This test checks delete user successful")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_delete_user_successful(self):

        self.data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=self.data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")


        data = {
            "email": self.data["email"],
            "password": self.data["password"]
        }


        response2 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id = self.get_json_value(response2, "user_id")

        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 200)

        response4 = MyRequests.get(f"/user/{user_id}")

        Assertions.assert_code_status(response4, 404)
        assert response4.text == "User not found", "Wrong after delete user"

    # Пробуем удалить пользователя, будучи авторизованными другим пользователем.
    @allure.feature("Негативные тесты")
    @allure.description("This test checks delete another user is impossible")
    @allure.severity(allure.severity_level.NORMAL)
    def test_negative_delete_user(self):
        response1 = MyRequests.post("/user/", data=self.data)  # зарегали первого пользователя
        response2 = MyRequests.post("/user/", data=self.data2)  # зарегали второго пользователя

        response3 = MyRequests.post("/user/login", data=self.val)  # Авторизуемся ПЕРВЫМ пользователем

        auth_sid1 = self.get_cookie(response3, "auth_sid")
        token1 = self.get_header(response3, "x-csrf-token")
        user_id1 = self.get_json_value(response3, "user_id")

        response4 = MyRequests.post("/user/login", data=self.val2)  # Авторизуемся ВТОРЫМ пользователем

        auth_sid2 = self.get_cookie(response4, "auth_sid")
        token2 = self.get_header(response4, "x-csrf-token")
        user_id2 = self.get_json_value(response4, "user_id")


        response5 = MyRequests.delete(
            f"/user/{user_id1}", # указываем id ПЕРВОГО пользователя
            headers={"x-csrf-token": token2}, # указываем token ВТОРОГО пользователя
            cookies={"auth_sid": auth_sid2} # указываем cookies ВТОРОГО пользователя
        )

        response6 = MyRequests.get(
            f"/user/{user_id1}",
            headers={"x-csrf-token": token1},
            cookies={"auth_sid": auth_sid1}
        )

        expected_fields = ["id", "username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response6, expected_fields)

