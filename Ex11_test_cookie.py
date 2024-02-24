import requests
class TestCookijes:
    def test_cookies(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

        print(dict(response.cookies))

        assert "HomeWork" in response.cookies, "There is no this cookie"

        cookie_value = response.cookies.get("HomeWork")

        assert cookie_value == "hw_value", "Cookie value is incorrect"