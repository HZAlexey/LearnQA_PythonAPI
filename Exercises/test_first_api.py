import pytest
import requests

class TestFirstAPI:
    names = [
        ("Vitalii"), # картеж, который содержит имя
        ("Arseniy"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)

    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name':name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is not field 'answer' in the response"

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}" # Тут мы приводим то что ожидаем увидить, что бы сравнить с фактическим результатом

        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Actual text in the response is not correct"

