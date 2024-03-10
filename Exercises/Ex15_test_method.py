import random
import string

import allure
import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

@allure.epic("Test create user")
class TestUserRegister(BaseCase):
    exclude_params = [
        ("no_username"),
        ("no_password"),
        ("no_firstName"),
        ("no_lastName"),
        ("no_email")
    ]

    # Создание пользователя с некорректным email - без символа @
    @allure.feature("Negative tests")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_email_no_at(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format"

    # Создание пользователя без указания одного из полей

    @pytest.mark.parametrize('condition', exclude_params)
    @allure.feature("Negative tests")
    @allure.story("Создание пользователя без указания одного из полей")
    def test_create_user_without_field(self,condition):
        email = 'vinkotov@example.com'

        #  Если нет userName
        if condition == "no_username":
            data = {
                'password': '123',
                'firstName': 'learnqa',
                'lastName': 'learnqa',
                'email': email
            }
            response = MyRequests.post(
                "/user/",
                data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == "The following required params are missed: username"

        #  Если нет password
        elif condition == "no_password":
            data = {
                'username': 'learnqa',
                'firstName': 'learnqa',
                'lastName': 'learnqa',
                'email': email
            }
            response = MyRequests.post(
                "/user/",
                data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == "The following required params are missed: password"

        #  Если нет firstName
        elif condition == "no_firstName":
            data = {
                'username': 'learnqa',
                'password': '123',
                'lastName': 'learnqa',
                'email': email
            }
            response = MyRequests.post(
                "/user/",
                data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == "The following required params are missed: firstName"

        #  Если нет lastName
        elif condition == "no_lastName":
            data = {
                'username': 'learnqa',
                'password': '123',
                'firstName': 'learnqa',
                'email': email
            }
            response = MyRequests.post(
                "/user/",
                data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == "The following required params are missed: lastName"

        #  Если нет email
        elif condition == "no_email":
            data = {
                'username': 'learnqa',
                'password': '123',
                'firstName': 'learnqa',
                'lastName': 'learnqa'
            }
            response = MyRequests.post(
                "/user/",
                data=data)

            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == "The following required params are missed: email"

    # Создание пользователя с очень коротким именем в один символ
    @allure.feature("Negative tests")
    def test_create_user_with_to_short_name(self):
        email = 'vinkotov@example.com'
        data = {
            'username': 'l',
            'password': '123',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
        response = MyRequests.post(
            "/user/",
            data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'username' field is too short"


    # Создание пользователя с очень длинным именем - длиннее 250 символов
    @allure.feature("Negative tests")
    def test_create_user_with_to_long_name(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(255)) # генерим имя длянной 255 символов

        email = 'vinkotov2sasd@example.com'

        data = {
            'username': rand_string,
            'password': '123',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
                }
        response = MyRequests.post(
             "/user/",
             data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'username' field is too long"