import requests
class TestCookijes:
    def test_cookies(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

        cookie = dict(response.cookies)
        print(cookie)

        cookie_value = cookie["HomeWork"]

        assert "HomeWork" in cookie, "There is no this cookie"
        assert "hw_value" == cookie_value, "Cookie value is incorrect"