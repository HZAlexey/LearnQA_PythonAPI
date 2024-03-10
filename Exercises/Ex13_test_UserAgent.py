import allure
import pytest
import requests

@allure.epic("Test User Agent")
class TestUserAgent:
    value = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]
    @allure.link(name="Документация", url="https://gist.github.com/KotovVitaliy/138894aa5b6fa442163561b5db6e2e26")
    @pytest.mark.parametrize("value_user_agent", value)
    def test_user_agent(self, value_user_agent):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        headers = {'User-Agent':value_user_agent}

        response = requests.get(
            url,
            headers=headers
        )

        response_dict = response.json()

        if value_user_agent == "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30":
            value_user_agent = "User Agent № 1"
            expected_platform = "Mobile"
            expected_browser = "No"
            expected_device = "Android"
        elif value_user_agent == "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1":
            value_user_agent = "User Agent № 2"
            expected_platform = "Mobile"
            expected_browser = "Chrome"
            expected_device = "iOS"
        elif value_user_agent == "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)":
            value_user_agent = "User Agent № 3"
            expected_platform = "Googlebot"
            expected_browser = "Unknown"
            expected_device = "Unknown"
        elif value_user_agent == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0":
            value_user_agent = "User Agent № 4"
            expected_platform = "Web"
            expected_browser = "Chrome"
            expected_device = "No"
        elif value_user_agent == "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1":
            value_user_agent = "User Agent № 5"
            expected_platform = "Mobile"
            expected_browser = "No"
            expected_device = "iPhone"

        actual_platform = response_dict["platform"]
        actual_browser = response_dict["browser"]
        actual_device = response_dict["device"]

        assert actual_platform == expected_platform, f"platform для User-Agent {value_user_agent} не верная. !!! ОЖИДАЛОСЬ platform: {expected_platform} ФКТИЧЕСКИЙ platform:{actual_platform}"
        assert actual_browser == expected_browser, f"browswe для User-Agent {value_user_agent} не верная. !!! ОЖИДАЛОСЬ browswe: {expected_browser} ФКТИЧЕСКИЙ browswe:{actual_browser}"
        assert actual_device == expected_device, f"device для User-Agent {value_user_agent} не верная. !!! ОЖИДАЛОСЬ device: {expected_device} ФКТИЧЕСКИЙ device:{actual_device}"