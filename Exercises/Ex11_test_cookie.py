import requests

class TestCookijes():
    def test_cookies(self):

        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

        print(dict(response.cookies))  #{'HomeWork': 'hw_value'}

        assert "HomeWork" in response.cookies, f"There is no such cookie in the  response"

        cookie_value = response.cookies.get("HomeWork")
        assert "hw_value" == cookie_value, "Cookie value is incorrect"