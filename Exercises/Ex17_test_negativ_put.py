from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime


class TestUserEditNegative(BaseCase):

    def setup_method(self):
        self.random_part = datetime.now().strftime("%m%d%Y%H%M%S")

        self.data = self.prepare_registration_data()
        self.data2 = self.prepare_registration_data(f"{self.random_part}@yandex.ru")

        email = self.data["email"]
        password = self.data["password"]

        email2 = self.data2["email"]
        password2 = self.data2["password"]

        self.val = {
            'email': email,
            'password': password
        }

        self.val2 = {
            'email': email2,
            'password': password2
        }

    # 1 Попытаемся изменить данные пользователя, будучи неавторизованными
    def test_edit_user_wo_login(self):
        response1 = MyRequests.post("/user/", data=self.data)
        response2 = MyRequests.post("/user/", data=self.data2)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        id_user = response1.json()["id"]

        new_name = "Changed name"

        response3 = MyRequests.put(
            f"/user/{id_user}",
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 400)
        assert "Auth token not supplied" in response3.text, "Что-то пошло не так, тыж не авторизован"

    # 2 Попытаемся изменить данные пользователя, будучи авторизованными другим пользователем
    def test_edit_another_user(self):
        response1 = MyRequests.post("/user/", data=self.data) # зарегали первого пользователя
        response2 = MyRequests.post("/user/", data=self.data2) # зарегали второго пользователя

        response3 = MyRequests.post("/user/login", data=self.val)  # Авторизуемся ПЕРВЫМ пользователем

        auth_sid1 = self.get_cookie(response3, "auth_sid")
        token1 = self.get_header(response3, "x-csrf-token")
        user_id1 = self.get_json_value(response3, "user_id")

        response4 = MyRequests.post("/user/login", data=self.val2)  # Авторизуемся ВТОРЫМ пользователем

        auth_sid2 = self.get_cookie(response4, "auth_sid")
        token2 = self.get_header(response4, "x-csrf-token")
        user_id2 = self.get_json_value(response4, "user_id")

        # Пытаемся изменить Имя пользователя №2 будучи авторизованным пользователем №1
        new_email = f"change{self.random_part}@yandex.ru"

        response5 = MyRequests.put(
            f"/user/{user_id2}",  # id второго пользователя
            data={"email": new_email},
            headers={"x-csrf-token": token1},  # token от первого пользователя
            cookies={"auth_sid": auth_sid1}  # auth_sid1 от первого пользоввателя
        )

        # Проверяем изменилось ли Имя у второго пользователя

        response6 = MyRequests.get(
            f"/user/{user_id2}",
            headers={"x-csrf-token": token2},
            cookies={"auth_sid": auth_sid2}
        )

        Assertions.assert_json_value_by_name(
            response6,
            "email",
            self.data2["email"],
            "Wrong email of the user after edit"
        )

    # 3 Попытаемся изменить email пользователя, будучи авторизованными тем же пользователем, на новый email без символа @
    def test_edit_with_incorrect_email(self):

        response = MyRequests.post("/user/", data=self.data) # Регистрируем пользователя

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        response2 = MyRequests.post("/user/login", data=self.val) # Авторизовываемся этим пользователем

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id = self.get_json_value(response2, "user_id")

        new_email = f"change{self.random_part}yandex.ru" # некорректный email, без символа @

        response3 = MyRequests.put(
            f"/user/{user_id}",
            data={"email": new_email},
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        # Првоерка того, что заменить некорркктным значением email невозможно
        Assertions.assert_code_status(response3,400)
        Assertions.assert_json_value_by_name(
            response3,
            "error",
            "Invalid email format",
            "Wrong email of the user after edit"
        )

    # 4 Попытаемся изменить firstName пользователя, будучи авторизованными тем же пользователем, на очень короткое значение в один символ
    def test_edit_name_with_too_short_name(self):
        response = MyRequests.post("/user/", data=self.data)  # Регистрируем пользователя

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        response2 = MyRequests.post("/user/login", data=self.val)  # Авторизовываемся этим пользователем

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id = self.get_json_value(response2, "user_id")

        new_short_name = 'L'

        response3 = MyRequests.put(
            f"/user/{user_id}",
            data={"firstName": new_short_name},
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response3,
            "error",
            "The value for field `firstName` is too short",
            "Wrong firstName of the user after edit"
        )
























