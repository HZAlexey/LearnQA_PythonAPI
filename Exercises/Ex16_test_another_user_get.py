from datetime import datetime

import allure

from lib.my_requests import MyRequests
from lib.assertions import Assertions
from lib.base_case import BaseCase

class TestUserGet(BaseCase):
    # Для начала регистрируем двух пользователей
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_first(self):
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")

        data1 = self.prepare_registration_data()
        data2 = self.prepare_registration_data(f"{random_part}@yandex.ru")

        response1 = MyRequests.post("/user/", data=data1)
        response2 = MyRequests.post("/user/", data=data2)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email1 = data1["email"]
        email2 = data2["email"]

        password1 = data1["password"]
        password2 = data2["password"]

        val1 = {
            'email': email1,
            'password': password1
        }

        val2 = {
            'email': email2,
            'password': password2
        }

        response1 = MyRequests.post("/user/login", data=val1)  # Авторизуемся ПЕРВЫМ пользователем
        response2 = MyRequests.post("/user/login", data=val2)  # Авторизуемся ВТОРЫМ пользователем


        user_id_from_auth_method1 = self.get_json_value(response1, "user_id")

        auth_sid2 = self.get_cookie(response2, "auth_sid")
        token2 = self.get_header(response2, "x-csrf-token")


        response3 = MyRequests.get(
            f"/user/{user_id_from_auth_method1}", # указываем id ПЕРВОГО пользователя
            headers={"x-csrf-token": f"{token2}"}, # указываем token ВТОРОГО пользователя
            cookies={"auth_sid": f"{auth_sid2}"} # указываем auth_sid ВТОРОГО пользователя
        )

        Assertions.assert_json_has_not_key(response2, "username")
        print(response3.text)