import pytest
import requests

class TestHeader:
    headers = [
        ('Date'),
        ('Content-Type'),
        ('Content-Length'),
        ('Connection'),
        ('Keep-Alive'),
        ('Server'),
        ('x-secret-homework-header'),
        ('Cache-Control'),
        ('Expires')
    ]

    value_headers = [
        ('Sun, 25 Feb 2024 14:27:16 GMT'),
        ('application/json'),
        ('15'),
        ('keep-alive'),
        ('timeout=10'),
        ('Apache'),
        ('Some secret value'),
        ('max-age=0'),
        ('Sun, 25 Feb 2024 14:27:16 GMT')
    ]

    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    head = response.headers
    print(head)

    @pytest.mark.parametrize('header', headers)
    def test_header(self, header):

        assert header in self.head, f"There is no header {header} in the request"

        head_val = self.head[header]
        assert head_val in self.value_headers, "There is no header value in the request"

