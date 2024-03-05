from lib.my_requests import MyRequests
from lib.assertions import Assertions
from lib.base_case import BaseCase

class TestUserGet(BaseCase):
    # Для начала регистрируем нового пользователя
    def test_create_user_first(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = data["email"]
        password = data["password"]

        data = {
            'email': email,
            'password': password
        }
        response1 = MyRequests.post("/user/login", data=data) # Авторизуемся данным пользователем

        self.user_id_from_auth_method1 = self.get_json_value(response1, "user_id") # получаем его id

    # Регистрируем второго пользователя
    def test_create_user_second(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = data["email"]
        password = data["password"]

        data = {
            'email': email,
            'password': password
        }
        response1 = MyRequests.post("/user/login", data=data) # Авторизуемся данным пользователем

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method2 = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(                               # Запрашиваем данные с другим ID
            f"/user/{self.user_id_from_auth_method1}",
            headers={"x-csrf-token": f"{token}"},
            cookies={"auth_sid": f"{auth_sid}"}
        )


        print(response2.content)


