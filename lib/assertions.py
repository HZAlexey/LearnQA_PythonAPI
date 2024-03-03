from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message): # Проверяем, что ответ в JSON-формате
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not on JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name): # Проверяем, что какое-то значение в JSON есть
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not on JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list): # Проверяем, что конкретные значения (ключи) присутствуют в JSON
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not on JSON format. Response text is '{response.text}'"

        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_not_key(response: Response, name): # Проверяем, что какого-то значения в JSON нет
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not on JSON format. Response text is '{response.text}'"

        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. But it's present"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code): # Проверяем, что статус код соответстует фактическому
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected {expected_status_code}. Actual: {response.status_code}"
